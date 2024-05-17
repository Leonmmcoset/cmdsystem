# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class RenderAttribRegistry(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class is used to associate each RenderAttrib with a different slot
     * index at runtime, so we can store a list of RenderAttribs in the
     * RenderState object, and very quickly look them up by type.
     */
    """
    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         *
         */
        """
        pass

    def getMaxSlots(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_slots()
        """
        pass

    def getNumSlots(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_slots(RenderAttribRegistry self)
        
        /**
         * Returns the number of RenderAttrib slots that have been allocated.  This is
         * one more than the highest slot number in use.
         */
        """
        pass

    def getNumSortedSlots(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_sorted_slots(RenderAttribRegistry self)
        
        /**
         * Returns the number of entries in the sorted_slots list.
         */
        """
        pass

    def getSlot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_slot(RenderAttribRegistry self, TypeHandle type_handle)
        
        /**
         * Returns the slot number assigned to the indicated TypeHandle, or 0 if no
         * slot number has been assigned.
         */
        """
        pass

    def getSlotDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_slot_default(RenderAttribRegistry self, int slot)
        
        /**
         * Returns the default RenderAttrib object associated with slot n.  This is
         * the attrib that should be applied in the absence of any other attrib of
         * this type.
         */
        """
        pass

    def getSlotSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_slot_sort(RenderAttribRegistry self, int slot)
        
        /**
         * Returns the sort number associated with slot n.
         */
        """
        pass

    def getSlotType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_slot_type(RenderAttribRegistry self, int slot)
        
        /**
         * Returns the TypeHandle associated with slot n.
         */
        """
        pass

    def getSortedSlot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sorted_slot(RenderAttribRegistry self, int n)
        
        /**
         * Returns the nth slot in sorted order.  By traversing this list, you will
         * retrieve all the slot numbers in order according to their registered sort
         * value.
         */
        """
        pass

    def get_global_ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         *
         */
        """
        pass

    def get_max_slots(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_slots()
        """
        pass

    def get_num_slots(self, RenderAttribRegistry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_slots(RenderAttribRegistry self)
        
        /**
         * Returns the number of RenderAttrib slots that have been allocated.  This is
         * one more than the highest slot number in use.
         */
        """
        pass

    def get_num_sorted_slots(self, RenderAttribRegistry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_sorted_slots(RenderAttribRegistry self)
        
        /**
         * Returns the number of entries in the sorted_slots list.
         */
        """
        pass

    def get_slot(self, RenderAttribRegistry_self, TypeHandle_type_handle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_slot(RenderAttribRegistry self, TypeHandle type_handle)
        
        /**
         * Returns the slot number assigned to the indicated TypeHandle, or 0 if no
         * slot number has been assigned.
         */
        """
        pass

    def get_slot_default(self, RenderAttribRegistry_self, int_slot): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_slot_default(RenderAttribRegistry self, int slot)
        
        /**
         * Returns the default RenderAttrib object associated with slot n.  This is
         * the attrib that should be applied in the absence of any other attrib of
         * this type.
         */
        """
        pass

    def get_slot_sort(self, RenderAttribRegistry_self, int_slot): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_slot_sort(RenderAttribRegistry self, int slot)
        
        /**
         * Returns the sort number associated with slot n.
         */
        """
        pass

    def get_slot_type(self, RenderAttribRegistry_self, int_slot): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_slot_type(RenderAttribRegistry self, int slot)
        
        /**
         * Returns the TypeHandle associated with slot n.
         */
        """
        pass

    def get_sorted_slot(self, RenderAttribRegistry_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sorted_slot(RenderAttribRegistry self, int n)
        
        /**
         * Returns the nth slot in sorted order.  By traversing this list, you will
         * retrieve all the slot numbers in order according to their registered sort
         * value.
         */
        """
        pass

    def setSlotSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_slot_sort(const RenderAttribRegistry self, int slot, int sort)
        
        /**
         * Changes the sort number associated with slot n.
         */
        """
        pass

    def set_slot_sort(self, const_RenderAttribRegistry_self, int_slot, int_sort): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_slot_sort(const RenderAttribRegistry self, int slot, int sort)
        
        /**
         * Changes the sort number associated with slot n.
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
        '__doc__': '/**\n * This class is used to associate each RenderAttrib with a different slot\n * index at runtime, so we can store a list of RenderAttribs in the\n * RenderState object, and very quickly look them up by type.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.RenderAttribRegistry' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE291800>'
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFCFE291800>)>'
        'getMaxSlots': None, # (!) real value is '<staticmethod(<built-in method getMaxSlots of type object at 0x00007FFCFE291800>)>'
        'getNumSlots': None, # (!) real value is "<method 'getNumSlots' of 'panda3d.core.RenderAttribRegistry' objects>"
        'getNumSortedSlots': None, # (!) real value is "<method 'getNumSortedSlots' of 'panda3d.core.RenderAttribRegistry' objects>"
        'getSlot': None, # (!) real value is "<method 'getSlot' of 'panda3d.core.RenderAttribRegistry' objects>"
        'getSlotDefault': None, # (!) real value is "<method 'getSlotDefault' of 'panda3d.core.RenderAttribRegistry' objects>"
        'getSlotSort': None, # (!) real value is "<method 'getSlotSort' of 'panda3d.core.RenderAttribRegistry' objects>"
        'getSlotType': None, # (!) real value is "<method 'getSlotType' of 'panda3d.core.RenderAttribRegistry' objects>"
        'getSortedSlot': None, # (!) real value is "<method 'getSortedSlot' of 'panda3d.core.RenderAttribRegistry' objects>"
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFCFE291800>)>'
        'get_max_slots': None, # (!) real value is '<staticmethod(<built-in method get_max_slots of type object at 0x00007FFCFE291800>)>'
        'get_num_slots': None, # (!) real value is "<method 'get_num_slots' of 'panda3d.core.RenderAttribRegistry' objects>"
        'get_num_sorted_slots': None, # (!) real value is "<method 'get_num_sorted_slots' of 'panda3d.core.RenderAttribRegistry' objects>"
        'get_slot': None, # (!) real value is "<method 'get_slot' of 'panda3d.core.RenderAttribRegistry' objects>"
        'get_slot_default': None, # (!) real value is "<method 'get_slot_default' of 'panda3d.core.RenderAttribRegistry' objects>"
        'get_slot_sort': None, # (!) real value is "<method 'get_slot_sort' of 'panda3d.core.RenderAttribRegistry' objects>"
        'get_slot_type': None, # (!) real value is "<method 'get_slot_type' of 'panda3d.core.RenderAttribRegistry' objects>"
        'get_sorted_slot': None, # (!) real value is "<method 'get_sorted_slot' of 'panda3d.core.RenderAttribRegistry' objects>"
        'setSlotSort': None, # (!) real value is "<method 'setSlotSort' of 'panda3d.core.RenderAttribRegistry' objects>"
        'set_slot_sort': None, # (!) real value is "<method 'set_slot_sort' of 'panda3d.core.RenderAttribRegistry' objects>"
    }


