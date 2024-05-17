# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class MouseWatcherBase(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This represents a collection of MouseWatcherRegions that may be managed as
     * a group.  This is the base class for both MouseWatcherGroup and
     * MouseWatcher, and exists so that we don't have to make MouseWatcher inherit
     * from ReferenceCount more than once.
     */
    """
    def addRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_region(const MouseWatcherBase self, MouseWatcherRegion region)
        
        /**
         * Adds the indicated region to the set of regions in the group.  It is no
         * longer an error to call this for the same region more than once.
         */
        """
        pass

    def add_region(self, const_MouseWatcherBase_self, MouseWatcherRegion_region): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_region(const MouseWatcherBase self, MouseWatcherRegion region)
        
        /**
         * Adds the indicated region to the set of regions in the group.  It is no
         * longer an error to call this for the same region more than once.
         */
        """
        pass

    def clearRegions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_regions(const MouseWatcherBase self)
        
        /**
         * Removes all the regions from the group.
         */
        """
        pass

    def clear_regions(self, const_MouseWatcherBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_regions(const MouseWatcherBase self)
        
        /**
         * Removes all the regions from the group.
         */
        """
        pass

    def findRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_region(MouseWatcherBase self, str name)
        
        /**
         * Returns a pointer to the first region found with the indicated name.  If
         * multiple regions share the same name, the one that is returned is
         * indeterminate.
         */
        """
        pass

    def find_region(self, MouseWatcherBase_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_region(MouseWatcherBase self, str name)
        
        /**
         * Returns a pointer to the first region found with the indicated name.  If
         * multiple regions share the same name, the one that is returned is
         * indeterminate.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNumRegions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_regions(MouseWatcherBase self)
        
        /**
         * Returns the number of regions in the group.
         */
        """
        pass

    def getRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_region(MouseWatcherBase self, int n)
        
        /**
         * Returns the nth region of the group; returns NULL if there is no nth
         * region.  Note that this is not thread-safe; another thread might have
         * removed the nth region before you called this method.
         */
        """
        pass

    def getRegions(self, *args, **kwargs): # real signature unknown
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_regions(self, MouseWatcherBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_regions(MouseWatcherBase self)
        
        /**
         * Returns the number of regions in the group.
         */
        """
        pass

    def get_region(self, MouseWatcherBase_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_region(MouseWatcherBase self, int n)
        
        /**
         * Returns the nth region of the group; returns NULL if there is no nth
         * region.  Note that this is not thread-safe; another thread might have
         * removed the nth region before you called this method.
         */
        """
        pass

    def get_regions(self, *args, **kwargs): # real signature unknown
        pass

    def hasRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_region(MouseWatcherBase self, MouseWatcherRegion region)
        
        /**
         * Returns true if the indicated region has already been added to the
         * MouseWatcherBase, false otherwise.
         */
        """
        pass

    def has_region(self, MouseWatcherBase_self, MouseWatcherRegion_region): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_region(MouseWatcherBase self, MouseWatcherRegion region)
        
        /**
         * Returns true if the indicated region has already been added to the
         * MouseWatcherBase, false otherwise.
         */
        """
        pass

    def hideRegions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        hide_regions(const MouseWatcherBase self)
        
        /**
         * Stops the visualization created by a previous call to show_regions().
         */
        """
        pass

    def hide_regions(self, const_MouseWatcherBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        hide_regions(const MouseWatcherBase self)
        
        /**
         * Stops the visualization created by a previous call to show_regions().
         */
        """
        pass

    def isSorted(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_sorted(MouseWatcherBase self)
        
        /**
         * Returns true if the group has already been sorted, false otherwise.
         */
        """
        pass

    def is_sorted(self, MouseWatcherBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_sorted(MouseWatcherBase self)
        
        /**
         * Returns true if the group has already been sorted, false otherwise.
         */
        """
        pass

    def output(self, MouseWatcherBase_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(MouseWatcherBase self, ostream out)
        
        /**
         *
         */
        """
        pass

    def removeRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_region(const MouseWatcherBase self, MouseWatcherRegion region)
        
        /**
         * Removes the indicated region from the group.  Returns true if it was
         * successfully removed, or false if it wasn't there in the first place.
         */
        """
        pass

    def remove_region(self, const_MouseWatcherBase_self, MouseWatcherRegion_region): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_region(const MouseWatcherBase self, MouseWatcherRegion region)
        
        /**
         * Removes the indicated region from the group.  Returns true if it was
         * successfully removed, or false if it wasn't there in the first place.
         */
        """
        pass

    def setColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color(const MouseWatcherBase self, const LVecBase4f color)
        
        /**
         * Specifies the color used to draw the region rectangles for the regions
         * visualized by show_regions().
         */
        """
        pass

    def set_color(self, const_MouseWatcherBase_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color(const MouseWatcherBase self, const LVecBase4f color)
        
        /**
         * Specifies the color used to draw the region rectangles for the regions
         * visualized by show_regions().
         */
        """
        pass

    def showRegions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        show_regions(const MouseWatcherBase self, const NodePath render2d, str bin_name, int draw_order)
        
        /**
         * Enables the visualization of all of the regions handled by this
         * MouseWatcherBase.  The supplied NodePath should be the root of the 2-d
         * scene graph for the window.
         */
        """
        pass

    def show_regions(self, const_MouseWatcherBase_self, const_NodePath_render2d, str_bin_name, int_draw_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        show_regions(const MouseWatcherBase self, const NodePath render2d, str bin_name, int draw_order)
        
        /**
         * Enables the visualization of all of the regions handled by this
         * MouseWatcherBase.  The supplied NodePath should be the root of the 2-d
         * scene graph for the window.
         */
        """
        pass

    def sortRegions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        sort_regions(const MouseWatcherBase self)
        
        /**
         * Sorts all the regions in this group into pointer order.
         */
        """
        pass

    def sort_regions(self, const_MouseWatcherBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sort_regions(const MouseWatcherBase self)
        
        /**
         * Sorts all the regions in this group into pointer order.
         */
        """
        pass

    def updateRegions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        update_regions(const MouseWatcherBase self)
        
        /**
         * Refreshes the visualization created by show_regions().
         */
        """
        pass

    def update_regions(self, const_MouseWatcherBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update_regions(const MouseWatcherBase self)
        
        /**
         * Refreshes the visualization created by show_regions().
         */
        """
        pass

    def write(self, MouseWatcherBase_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(MouseWatcherBase self, ostream out, int indent_level)
        
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    regions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sorted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * This represents a collection of MouseWatcherRegions that may be managed as\n * a group.  This is the base class for both MouseWatcherGroup and\n * MouseWatcher, and exists so that we don't have to make MouseWatcher inherit\n * from ReferenceCount more than once.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MouseWatcherBase' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE366810>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.MouseWatcherBase' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.MouseWatcherBase' objects>"
        'addRegion': None, # (!) real value is "<method 'addRegion' of 'panda3d.core.MouseWatcherBase' objects>"
        'add_region': None, # (!) real value is "<method 'add_region' of 'panda3d.core.MouseWatcherBase' objects>"
        'clearRegions': None, # (!) real value is "<method 'clearRegions' of 'panda3d.core.MouseWatcherBase' objects>"
        'clear_regions': None, # (!) real value is "<method 'clear_regions' of 'panda3d.core.MouseWatcherBase' objects>"
        'findRegion': None, # (!) real value is "<method 'findRegion' of 'panda3d.core.MouseWatcherBase' objects>"
        'find_region': None, # (!) real value is "<method 'find_region' of 'panda3d.core.MouseWatcherBase' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE366810>)>'
        'getNumRegions': None, # (!) real value is "<method 'getNumRegions' of 'panda3d.core.MouseWatcherBase' objects>"
        'getRegion': None, # (!) real value is "<method 'getRegion' of 'panda3d.core.MouseWatcherBase' objects>"
        'getRegions': None, # (!) real value is "<method 'getRegions' of 'panda3d.core.MouseWatcherBase' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE366810>)>'
        'get_num_regions': None, # (!) real value is "<method 'get_num_regions' of 'panda3d.core.MouseWatcherBase' objects>"
        'get_region': None, # (!) real value is "<method 'get_region' of 'panda3d.core.MouseWatcherBase' objects>"
        'get_regions': None, # (!) real value is "<method 'get_regions' of 'panda3d.core.MouseWatcherBase' objects>"
        'hasRegion': None, # (!) real value is "<method 'hasRegion' of 'panda3d.core.MouseWatcherBase' objects>"
        'has_region': None, # (!) real value is "<method 'has_region' of 'panda3d.core.MouseWatcherBase' objects>"
        'hideRegions': None, # (!) real value is "<method 'hideRegions' of 'panda3d.core.MouseWatcherBase' objects>"
        'hide_regions': None, # (!) real value is "<method 'hide_regions' of 'panda3d.core.MouseWatcherBase' objects>"
        'isSorted': None, # (!) real value is "<method 'isSorted' of 'panda3d.core.MouseWatcherBase' objects>"
        'is_sorted': None, # (!) real value is "<method 'is_sorted' of 'panda3d.core.MouseWatcherBase' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.MouseWatcherBase' objects>"
        'regions': None, # (!) real value is "<attribute 'regions' of 'panda3d.core.MouseWatcherBase' objects>"
        'removeRegion': None, # (!) real value is "<method 'removeRegion' of 'panda3d.core.MouseWatcherBase' objects>"
        'remove_region': None, # (!) real value is "<method 'remove_region' of 'panda3d.core.MouseWatcherBase' objects>"
        'setColor': None, # (!) real value is "<method 'setColor' of 'panda3d.core.MouseWatcherBase' objects>"
        'set_color': None, # (!) real value is "<method 'set_color' of 'panda3d.core.MouseWatcherBase' objects>"
        'showRegions': None, # (!) real value is "<method 'showRegions' of 'panda3d.core.MouseWatcherBase' objects>"
        'show_regions': None, # (!) real value is "<method 'show_regions' of 'panda3d.core.MouseWatcherBase' objects>"
        'sortRegions': None, # (!) real value is "<method 'sortRegions' of 'panda3d.core.MouseWatcherBase' objects>"
        'sort_regions': None, # (!) real value is "<method 'sort_regions' of 'panda3d.core.MouseWatcherBase' objects>"
        'sorted': None, # (!) real value is "<attribute 'sorted' of 'panda3d.core.MouseWatcherBase' objects>"
        'updateRegions': None, # (!) real value is "<method 'updateRegions' of 'panda3d.core.MouseWatcherBase' objects>"
        'update_regions': None, # (!) real value is "<method 'update_regions' of 'panda3d.core.MouseWatcherBase' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.MouseWatcherBase' objects>"
    }


