# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class LODNode(PandaNode):
    """
    /**
     * A Level-of-Detail node.  This selects only one of its children for
     * rendering, according to the distance from the camera and the table
     * indicated in the associated LOD object.
     */
    """
    def addSwitch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_switch(const LODNode self, float in, float out)
        
        /**
         * Adds a switch range to the LODNode.  This implies that the corresponding
         * child node has been parented to the node.
         *
         * The sense of in vs.  out distances is as if the object were coming towards
         * you from far away: it switches "in" at the far distance, and switches "out"
         * at the close distance.  Thus, "in" should be larger than "out".
         */
        """
        pass

    def add_switch(self, const_LODNode_self, float_in, float_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_switch(const LODNode self, float in, float out)
        
        /**
         * Adds a switch range to the LODNode.  This implies that the corresponding
         * child node has been parented to the node.
         *
         * The sense of in vs.  out distances is as if the object were coming towards
         * you from far away: it switches "in" at the far distance, and switches "out"
         * at the close distance.  Thus, "in" should be larger than "out".
         */
        """
        pass

    def clearForceSwitch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_force_switch(const LODNode self)
        
        /**
         * Undoes the effect of a previous call to force_switch() and releases the
         * LODNode to once again display the normal level.
         */
        """
        pass

    def clearSwitches(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_switches(const LODNode self)
        
        /**
         * Removes the set of switching ranges for the LODNode, presumably in
         * conjunction with removing all of its children.  See add_switch().
         */
        """
        pass

    def clear_force_switch(self, const_LODNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_force_switch(const LODNode self)
        
        /**
         * Undoes the effect of a previous call to force_switch() and releases the
         * LODNode to once again display the normal level.
         */
        """
        pass

    def clear_switches(self, const_LODNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_switches(const LODNode self)
        
        /**
         * Removes the set of switching ranges for the LODNode, presumably in
         * conjunction with removing all of its children.  See add_switch().
         */
        """
        pass

    def forceSwitch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        force_switch(const LODNode self, int index)
        
        /**
         * Forces the LODNode to show the indicated level instead of the level that
         * would normally be shown based on the distance from the camera.
         */
        """
        pass

    def force_switch(self, const_LODNode_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        force_switch(const LODNode self, int index)
        
        /**
         * Forces the LODNode to show the indicated level instead of the level that
         * would normally be shown based on the distance from the camera.
         */
        """
        pass

    def getCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_center(LODNode self)
        
        /**
         * Returns the center of the LOD.  This is the point that is compared to the
         * camera (in camera space) to determine the particular LOD that should be
         * chosen.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getHighestSwitch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_highest_switch(LODNode self)
        
        /**
         * Returns the index number of the child with the highest level of detail;
         * that is, the one that is designed to be seen from the closest to the
         * camera.  This is usually the last child, but it is not necessarily so.
         */
        """
        pass

    def getIn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_in(LODNode self, int index)
        
        /**
         * Returns the "in" distance of the indicated switch range.  This should be
         * larger than the "out" distance of the same range.
         */
        """
        pass

    def getIns(self, *args, **kwargs): # real signature unknown
        pass

    def getLodScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lod_scale(LODNode self)
        
        /**
         * Returns the multiplier for lod distances
         */
        """
        pass

    def getLowestSwitch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lowest_switch(LODNode self)
        
        /**
         * Returns the index number of the child with the lowest level of detail; that
         * is, the one that is designed to be seen from the farthest away.  This is
         * usually the first child, but it is not necessarily so.
         */
        """
        pass

    def getNumSwitches(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_switches(LODNode self)
        
        /**
         * Returns the number of switch ranges added to the LODNode.  This should
         * correspond to the number of children of the node in order for the LODNode
         * to function correctly.
         */
        """
        pass

    def getOut(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_out(LODNode self, int index)
        
        /**
         * Returns the "out" distance of the indicated switch range.  This should be
         * smaller than the "in" distance of the same range.
         */
        """
        pass

    def getOuts(self, *args, **kwargs): # real signature unknown
        pass

    def get_center(self, LODNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_center(LODNode self)
        
        /**
         * Returns the center of the LOD.  This is the point that is compared to the
         * camera (in camera space) to determine the particular LOD that should be
         * chosen.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_highest_switch(self, LODNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_highest_switch(LODNode self)
        
        /**
         * Returns the index number of the child with the highest level of detail;
         * that is, the one that is designed to be seen from the closest to the
         * camera.  This is usually the last child, but it is not necessarily so.
         */
        """
        pass

    def get_in(self, LODNode_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_in(LODNode self, int index)
        
        /**
         * Returns the "in" distance of the indicated switch range.  This should be
         * larger than the "out" distance of the same range.
         */
        """
        pass

    def get_ins(self, *args, **kwargs): # real signature unknown
        pass

    def get_lod_scale(self, LODNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lod_scale(LODNode self)
        
        /**
         * Returns the multiplier for lod distances
         */
        """
        pass

    def get_lowest_switch(self, LODNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lowest_switch(LODNode self)
        
        /**
         * Returns the index number of the child with the lowest level of detail; that
         * is, the one that is designed to be seen from the farthest away.  This is
         * usually the first child, but it is not necessarily so.
         */
        """
        pass

    def get_num_switches(self, LODNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_switches(LODNode self)
        
        /**
         * Returns the number of switch ranges added to the LODNode.  This should
         * correspond to the number of children of the node in order for the LODNode
         * to function correctly.
         */
        """
        pass

    def get_out(self, LODNode_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_out(LODNode self, int index)
        
        /**
         * Returns the "out" distance of the indicated switch range.  This should be
         * smaller than the "in" distance of the same range.
         */
        """
        pass

    def get_outs(self, *args, **kwargs): # real signature unknown
        pass

    def hideAllSwitches(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        hide_all_switches(const LODNode self)
        
        /**
         * Hides all levels, restoring the LODNode to normal operation.
         */
        """
        pass

    def hideSwitch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        hide_switch(const LODNode self, int index)
        
        /**
         * Disables a previous call to show_switch().
         */
        """
        pass

    def hide_all_switches(self, const_LODNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        hide_all_switches(const LODNode self)
        
        /**
         * Hides all levels, restoring the LODNode to normal operation.
         */
        """
        pass

    def hide_switch(self, const_LODNode_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        hide_switch(const LODNode self, int index)
        
        /**
         * Disables a previous call to show_switch().
         */
        """
        pass

    def isAnyShown(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_any_shown(LODNode self)
        
        /**
         * Returns true if any switch has been shown with show_switch(), indicating
         * the LODNode is in debug show mode; or false if it is in the normal mode.
         */
        """
        pass

    def is_any_shown(self, LODNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_any_shown(LODNode self)
        
        /**
         * Returns true if any switch has been shown with show_switch(), indicating
         * the LODNode is in debug show mode; or false if it is in the normal mode.
         */
        """
        pass

    def makeDefaultLod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_default_lod(str name)
        
        /**
         * Creates a new LODNode of the type specified by the default-lod-type config
         * variable.
         */
        """
        pass

    def make_default_lod(self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_default_lod(str name)
        
        /**
         * Creates a new LODNode of the type specified by the default-lod-type config
         * variable.
         */
        """
        pass

    def setCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_center(const LODNode self, const LPoint3f center)
        
        /**
         * Specifies the center of the LOD.  This is the point that is compared to the
         * camera (in camera space) to determine the particular LOD that should be
         * chosen.
         */
        """
        pass

    def setLodScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_lod_scale(const LODNode self, float value)
        
        // for performance tuning, increasing this value should improve performance
        // at the cost of model quality
        
        // for performance tuning, increasing this value should improve performance
        // at the cost of model quality
        
        /**
         * Sets the multiplier for lod distances.  A higher value means you'll see
         * farther switchs than normal
         */
        """
        pass

    def setSwitch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_switch(const LODNode self, int index, float in, float out)
        
        /**
         * Changes the switching range of a particular child of the LODNode.  See
         * add_switch().
         */
        """
        pass

    def set_center(self, const_LODNode_self, const_LPoint3f_center): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_center(const LODNode self, const LPoint3f center)
        
        /**
         * Specifies the center of the LOD.  This is the point that is compared to the
         * camera (in camera space) to determine the particular LOD that should be
         * chosen.
         */
        """
        pass

    def set_lod_scale(self, const_LODNode_self, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_lod_scale(const LODNode self, float value)
        
        // for performance tuning, increasing this value should improve performance
        // at the cost of model quality
        
        // for performance tuning, increasing this value should improve performance
        // at the cost of model quality
        
        /**
         * Sets the multiplier for lod distances.  A higher value means you'll see
         * farther switchs than normal
         */
        """
        pass

    def set_switch(self, const_LODNode_self, int_index, float_in, float_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_switch(const LODNode self, int index, float in, float out)
        
        /**
         * Changes the switching range of a particular child of the LODNode.  See
         * add_switch().
         */
        """
        pass

    def showAllSwitches(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        show_all_switches(const LODNode self)
        
        /**
         * Shows all levels in their default colors.
         */
        """
        pass

    def showSwitch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        show_switch(const LODNode self, int index)
        show_switch(const LODNode self, int index, const LVecBase4f color)
        
        /**
         * This is provided as a debugging aid.  show_switch() will put the LODNode
         * into a special mode where rather than computing and drawing the appropriate
         * level of the LOD, a ring is drawn around the LODNode center indicating the
         * switch distances from the camera for the indicated level, and the geometry
         * of the indicated level is drawn in wireframe.
         *
         * Multiple different levels can be visualized this way at once.  Call
         * hide_switch() or hide_all_switches() to undo this mode and restore the
         * LODNode to its normal behavior.
         */
        
        /**
         * This is provided as a debugging aid.  show_switch() will put the LODNode
         * into a special mode where rather than computing and drawing the appropriate
         * level of the LOD, a ring is drawn around the LODNode center indicating the
         * switch distances from the camera for the indicated level, and the geometry
         * of the indicated level is drawn in wireframe.
         *
         * Multiple different levels can be visualized this way at once.  Call
         * hide_switch() or hide_all_switches() to undo this mode and restore the
         * LODNode to its normal behavior.
         */
        """
        pass

    def show_all_switches(self, const_LODNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        show_all_switches(const LODNode self)
        
        /**
         * Shows all levels in their default colors.
         */
        """
        pass

    def show_switch(self, const_LODNode_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        show_switch(const LODNode self, int index)
        show_switch(const LODNode self, int index, const LVecBase4f color)
        
        /**
         * This is provided as a debugging aid.  show_switch() will put the LODNode
         * into a special mode where rather than computing and drawing the appropriate
         * level of the LOD, a ring is drawn around the LODNode center indicating the
         * switch distances from the camera for the indicated level, and the geometry
         * of the indicated level is drawn in wireframe.
         *
         * Multiple different levels can be visualized this way at once.  Call
         * hide_switch() or hide_all_switches() to undo this mode and restore the
         * LODNode to its normal behavior.
         */
        
        /**
         * This is provided as a debugging aid.  show_switch() will put the LODNode
         * into a special mode where rather than computing and drawing the appropriate
         * level of the LOD, a ring is drawn around the LODNode center indicating the
         * switch distances from the camera for the indicated level, and the geometry
         * of the indicated level is drawn in wireframe.
         *
         * Multiple different levels can be visualized this way at once.  Call
         * hide_switch() or hide_all_switches() to undo this mode and restore the
         * LODNode to its normal behavior.
         */
        """
        pass

    def verifyChildBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        verify_child_bounds(LODNode self)
        
        /**
         * Returns true if the bounding volumes for the geometry of each fhild node
         * entirely fits within the switch_in radius for that child, or false
         * otherwise.  It is almost always a mistake for the geometry of an LOD level
         * to be larger than its switch_in radius.
         */
        """
        pass

    def verify_child_bounds(self, LODNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        verify_child_bounds(LODNode self)
        
        /**
         * Returns true if the bounding volumes for the geometry of each fhild node
         * entirely fits within the switch_in radius for that child, or false
         * otherwise.  It is almost always a mistake for the geometry of an LOD level
         * to be larger than its switch_in radius.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    highest_switch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lod_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lowest_switch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    outs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A Level-of-Detail node.  This selects only one of its children for\n * rendering, according to the distance from the camera and the table\n * indicated in the associated LOD object.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LODNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2878D0>'
        'addSwitch': None, # (!) real value is "<method 'addSwitch' of 'panda3d.core.LODNode' objects>"
        'add_switch': None, # (!) real value is "<method 'add_switch' of 'panda3d.core.LODNode' objects>"
        'center': None, # (!) real value is "<attribute 'center' of 'panda3d.core.LODNode' objects>"
        'clearForceSwitch': None, # (!) real value is "<method 'clearForceSwitch' of 'panda3d.core.LODNode' objects>"
        'clearSwitches': None, # (!) real value is "<method 'clearSwitches' of 'panda3d.core.LODNode' objects>"
        'clear_force_switch': None, # (!) real value is "<method 'clear_force_switch' of 'panda3d.core.LODNode' objects>"
        'clear_switches': None, # (!) real value is "<method 'clear_switches' of 'panda3d.core.LODNode' objects>"
        'forceSwitch': None, # (!) real value is "<method 'forceSwitch' of 'panda3d.core.LODNode' objects>"
        'force_switch': None, # (!) real value is "<method 'force_switch' of 'panda3d.core.LODNode' objects>"
        'getCenter': None, # (!) real value is "<method 'getCenter' of 'panda3d.core.LODNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2878D0>)>'
        'getHighestSwitch': None, # (!) real value is "<method 'getHighestSwitch' of 'panda3d.core.LODNode' objects>"
        'getIn': None, # (!) real value is "<method 'getIn' of 'panda3d.core.LODNode' objects>"
        'getIns': None, # (!) real value is "<method 'getIns' of 'panda3d.core.LODNode' objects>"
        'getLodScale': None, # (!) real value is "<method 'getLodScale' of 'panda3d.core.LODNode' objects>"
        'getLowestSwitch': None, # (!) real value is "<method 'getLowestSwitch' of 'panda3d.core.LODNode' objects>"
        'getNumSwitches': None, # (!) real value is "<method 'getNumSwitches' of 'panda3d.core.LODNode' objects>"
        'getOut': None, # (!) real value is "<method 'getOut' of 'panda3d.core.LODNode' objects>"
        'getOuts': None, # (!) real value is "<method 'getOuts' of 'panda3d.core.LODNode' objects>"
        'get_center': None, # (!) real value is "<method 'get_center' of 'panda3d.core.LODNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2878D0>)>'
        'get_highest_switch': None, # (!) real value is "<method 'get_highest_switch' of 'panda3d.core.LODNode' objects>"
        'get_in': None, # (!) real value is "<method 'get_in' of 'panda3d.core.LODNode' objects>"
        'get_ins': None, # (!) real value is "<method 'get_ins' of 'panda3d.core.LODNode' objects>"
        'get_lod_scale': None, # (!) real value is "<method 'get_lod_scale' of 'panda3d.core.LODNode' objects>"
        'get_lowest_switch': None, # (!) real value is "<method 'get_lowest_switch' of 'panda3d.core.LODNode' objects>"
        'get_num_switches': None, # (!) real value is "<method 'get_num_switches' of 'panda3d.core.LODNode' objects>"
        'get_out': None, # (!) real value is "<method 'get_out' of 'panda3d.core.LODNode' objects>"
        'get_outs': None, # (!) real value is "<method 'get_outs' of 'panda3d.core.LODNode' objects>"
        'hideAllSwitches': None, # (!) real value is "<method 'hideAllSwitches' of 'panda3d.core.LODNode' objects>"
        'hideSwitch': None, # (!) real value is "<method 'hideSwitch' of 'panda3d.core.LODNode' objects>"
        'hide_all_switches': None, # (!) real value is "<method 'hide_all_switches' of 'panda3d.core.LODNode' objects>"
        'hide_switch': None, # (!) real value is "<method 'hide_switch' of 'panda3d.core.LODNode' objects>"
        'highest_switch': None, # (!) real value is "<attribute 'highest_switch' of 'panda3d.core.LODNode' objects>"
        'ins': None, # (!) real value is "<attribute 'ins' of 'panda3d.core.LODNode' objects>"
        'isAnyShown': None, # (!) real value is "<method 'isAnyShown' of 'panda3d.core.LODNode' objects>"
        'is_any_shown': None, # (!) real value is "<method 'is_any_shown' of 'panda3d.core.LODNode' objects>"
        'lod_scale': None, # (!) real value is "<attribute 'lod_scale' of 'panda3d.core.LODNode' objects>"
        'lowest_switch': None, # (!) real value is "<attribute 'lowest_switch' of 'panda3d.core.LODNode' objects>"
        'makeDefaultLod': None, # (!) real value is '<staticmethod(<built-in method makeDefaultLod of type object at 0x00007FFCFE2878D0>)>'
        'make_default_lod': None, # (!) real value is '<staticmethod(<built-in method make_default_lod of type object at 0x00007FFCFE2878D0>)>'
        'outs': None, # (!) real value is "<attribute 'outs' of 'panda3d.core.LODNode' objects>"
        'setCenter': None, # (!) real value is "<method 'setCenter' of 'panda3d.core.LODNode' objects>"
        'setLodScale': None, # (!) real value is "<method 'setLodScale' of 'panda3d.core.LODNode' objects>"
        'setSwitch': None, # (!) real value is "<method 'setSwitch' of 'panda3d.core.LODNode' objects>"
        'set_center': None, # (!) real value is "<method 'set_center' of 'panda3d.core.LODNode' objects>"
        'set_lod_scale': None, # (!) real value is "<method 'set_lod_scale' of 'panda3d.core.LODNode' objects>"
        'set_switch': None, # (!) real value is "<method 'set_switch' of 'panda3d.core.LODNode' objects>"
        'showAllSwitches': None, # (!) real value is "<method 'showAllSwitches' of 'panda3d.core.LODNode' objects>"
        'showSwitch': None, # (!) real value is "<method 'showSwitch' of 'panda3d.core.LODNode' objects>"
        'show_all_switches': None, # (!) real value is "<method 'show_all_switches' of 'panda3d.core.LODNode' objects>"
        'show_switch': None, # (!) real value is "<method 'show_switch' of 'panda3d.core.LODNode' objects>"
        'verifyChildBounds': None, # (!) real value is "<method 'verifyChildBounds' of 'panda3d.core.LODNode' objects>"
        'verify_child_bounds': None, # (!) real value is "<method 'verify_child_bounds' of 'panda3d.core.LODNode' objects>"
    }


