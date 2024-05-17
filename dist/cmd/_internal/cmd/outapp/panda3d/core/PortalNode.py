# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class PortalNode(PandaNode):
    """
    /**
     * A node in the scene graph that can hold a Portal Polygon, which is a
     * rectangle.  Other types of polygons are not supported for now.  It also
     * holds a PT(PandaNode) Cell that this portal is connected to
     */
    """
    def addVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_vertex(const PortalNode self, const LPoint3f vertex)
        
        /**
         * Adds a new vertex to the portal polygon.  The vertices should be defined in
         * a counterclockwise orientation when viewing through the portal.
         */
        """
        pass

    def add_vertex(self, const_PortalNode_self, const_LPoint3f_vertex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_vertex(const PortalNode self, const LPoint3f vertex)
        
        /**
         * Adds a new vertex to the portal polygon.  The vertices should be defined in
         * a counterclockwise orientation when viewing through the portal.
         */
        """
        pass

    def clearVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_vertices(const PortalNode self)
        
        /**
         * Resets the vertices of the portal to the empty list.
         */
        """
        pass

    def clear_vertices(self, const_PortalNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_vertices(const PortalNode self)
        
        /**
         * Resets the vertices of the portal to the empty list.
         */
        """
        pass

    def getCellIn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cell_in(PortalNode self)
        
        /**
         * Sets the cell that this portal belongs to
         */
        """
        pass

    def getCellOut(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cell_out(PortalNode self)
        
        /**
         * Sets the cell that this portal leads out to
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFromPortalMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_from_portal_mask(PortalNode self)
        
        /**
         * Returns the current "from" PortalMask.  In order for a portal to be
         * detected from this object into another object, the intersection of this
         * object's "from" mask and the other object's "into" mask must be nonzero.
         */
        """
        pass

    def getIntoPortalMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_into_portal_mask(PortalNode self)
        
        /**
         * Returns the current "into" PortalMask.  In order for a portal to be
         * detected from another object into this object, the intersection of the
         * other object's "from" mask and this object's "into" mask must be nonzero.
         */
        """
        pass

    def getMaxDepth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_depth(const PortalNode self)
        
        /**
         * Returns the maximum depth this portal will be visible at
         */
        """
        pass

    def getNumVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_vertices(PortalNode self)
        
        /**
         * Returns the number of vertices in the portal polygon.
         */
        """
        pass

    def getPortalGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_portal_geom(PortalNode self)
        
        /**
         * Returns the current state of the portal_geom flag.  See set_portal_geom().
         */
        """
        pass

    def getVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex(PortalNode self, int n)
        
        /**
         * Returns the nth vertex of the portal polygon.
         */
        """
        pass

    def getVertices(self, *args, **kwargs): # real signature unknown
        pass

    def get_cell_in(self, PortalNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cell_in(PortalNode self)
        
        /**
         * Sets the cell that this portal belongs to
         */
        """
        pass

    def get_cell_out(self, PortalNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cell_out(PortalNode self)
        
        /**
         * Sets the cell that this portal leads out to
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_from_portal_mask(self, PortalNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_from_portal_mask(PortalNode self)
        
        /**
         * Returns the current "from" PortalMask.  In order for a portal to be
         * detected from this object into another object, the intersection of this
         * object's "from" mask and the other object's "into" mask must be nonzero.
         */
        """
        pass

    def get_into_portal_mask(self, PortalNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_into_portal_mask(PortalNode self)
        
        /**
         * Returns the current "into" PortalMask.  In order for a portal to be
         * detected from another object into this object, the intersection of the
         * other object's "from" mask and this object's "into" mask must be nonzero.
         */
        """
        pass

    def get_max_depth(self, const_PortalNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_depth(const PortalNode self)
        
        /**
         * Returns the maximum depth this portal will be visible at
         */
        """
        pass

    def get_num_vertices(self, PortalNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_vertices(PortalNode self)
        
        /**
         * Returns the number of vertices in the portal polygon.
         */
        """
        pass

    def get_portal_geom(self, PortalNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_portal_geom(PortalNode self)
        
        /**
         * Returns the current state of the portal_geom flag.  See set_portal_geom().
         */
        """
        pass

    def get_vertex(self, PortalNode_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex(PortalNode self, int n)
        
        /**
         * Returns the nth vertex of the portal polygon.
         */
        """
        pass

    def get_vertices(self, *args, **kwargs): # real signature unknown
        pass

    def isClipPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_clip_plane(const PortalNode self)
        
        /**
         * Is this portal clipping against its left-right planes
         */
        """
        pass

    def isOpen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_open(const PortalNode self)
        
        /**
         * Is this portal open from current camera zone
         */
        """
        pass

    def isVisible(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_visible(const PortalNode self)
        
        /**
         * Is this portal facing the camera
         */
        """
        pass

    def is_clip_plane(self, const_PortalNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_clip_plane(const PortalNode self)
        
        /**
         * Is this portal clipping against its left-right planes
         */
        """
        pass

    def is_open(self, const_PortalNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_open(const PortalNode self)
        
        /**
         * Is this portal open from current camera zone
         */
        """
        pass

    def is_visible(self, const_PortalNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_visible(const PortalNode self)
        
        /**
         * Is this portal facing the camera
         */
        """
        pass

    def setCellIn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cell_in(const PortalNode self, const NodePath cell)
        
        /**
         * Sets the cell that this portal belongs to
         */
        """
        pass

    def setCellOut(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cell_out(const PortalNode self, const NodePath cell)
        
        /**
         * Sets the cell that this portal leads out to
         */
        """
        pass

    def setClipPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_clip_plane(const PortalNode self, bool value)
        
        /**
         * this is set if the portal will clip against its left and right planes
         */
        """
        pass

    def setFromPortalMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_from_portal_mask(const PortalNode self, BitMask mask)
        
        /**
         * Sets the "from" PortalMask.  In order for a portal to be detected from this
         * object into another object, the intersection of this object's "from" mask
         * and the other object's "into" mask must be nonzero.
         */
        """
        pass

    def setIntoPortalMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_into_portal_mask(const PortalNode self, BitMask mask)
        
        /**
         * Sets the "into" PortalMask.  In order for a portal to be detected from
         * another object into this object, the intersection of the other object's
         * "from" mask and this object's "into" mask must be nonzero.
         */
        """
        pass

    def setMaxDepth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_depth(const PortalNode self, int value)
        
        /**
         * Set the maximum depth this portal will be visible at
         */
        """
        pass

    def setOpen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_open(const PortalNode self, bool value)
        
        /**
         * Python sets this based on curent camera zone
         */
        """
        pass

    def setPortalGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_portal_geom(const PortalNode self, bool flag)
        
        /**
         * Sets the state of the "portal geom" flag for this PortalNode.  Normally,
         * this is false; when this is set true, the PortalSolids in this node will
         * test for portals with actual renderable geometry, in addition to whatever
         * PortalSolids may be indicated by the from_portal_mask.
         *
         * Setting this to true causes this to test *all* GeomNodes for portals.  It
         * is an all-or-none thing; there is no way to portal with only some
         * GeomNodes, as GeomNodes have no into_portal_mask.
         */
        """
        pass

    def setPortalMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_portal_mask(const PortalNode self, BitMask mask)
        
        /**
         * Simultaneously sets both the "from" and "into" PortalMask values to the
         * same thing.
         */
        """
        pass

    def setVisible(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_visible(const PortalNode self, bool value)
        
        /**
         * this is set if the portal is facing camera
         */
        """
        pass

    def set_cell_in(self, const_PortalNode_self, const_NodePath_cell): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cell_in(const PortalNode self, const NodePath cell)
        
        /**
         * Sets the cell that this portal belongs to
         */
        """
        pass

    def set_cell_out(self, const_PortalNode_self, const_NodePath_cell): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cell_out(const PortalNode self, const NodePath cell)
        
        /**
         * Sets the cell that this portal leads out to
         */
        """
        pass

    def set_clip_plane(self, const_PortalNode_self, bool_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_clip_plane(const PortalNode self, bool value)
        
        /**
         * this is set if the portal will clip against its left and right planes
         */
        """
        pass

    def set_from_portal_mask(self, const_PortalNode_self, BitMask_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_from_portal_mask(const PortalNode self, BitMask mask)
        
        /**
         * Sets the "from" PortalMask.  In order for a portal to be detected from this
         * object into another object, the intersection of this object's "from" mask
         * and the other object's "into" mask must be nonzero.
         */
        """
        pass

    def set_into_portal_mask(self, const_PortalNode_self, BitMask_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_into_portal_mask(const PortalNode self, BitMask mask)
        
        /**
         * Sets the "into" PortalMask.  In order for a portal to be detected from
         * another object into this object, the intersection of the other object's
         * "from" mask and this object's "into" mask must be nonzero.
         */
        """
        pass

    def set_max_depth(self, const_PortalNode_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_depth(const PortalNode self, int value)
        
        /**
         * Set the maximum depth this portal will be visible at
         */
        """
        pass

    def set_open(self, const_PortalNode_self, bool_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_open(const PortalNode self, bool value)
        
        /**
         * Python sets this based on curent camera zone
         */
        """
        pass

    def set_portal_geom(self, const_PortalNode_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_portal_geom(const PortalNode self, bool flag)
        
        /**
         * Sets the state of the "portal geom" flag for this PortalNode.  Normally,
         * this is false; when this is set true, the PortalSolids in this node will
         * test for portals with actual renderable geometry, in addition to whatever
         * PortalSolids may be indicated by the from_portal_mask.
         *
         * Setting this to true causes this to test *all* GeomNodes for portals.  It
         * is an all-or-none thing; there is no way to portal with only some
         * GeomNodes, as GeomNodes have no into_portal_mask.
         */
        """
        pass

    def set_portal_mask(self, const_PortalNode_self, BitMask_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_portal_mask(const PortalNode self, BitMask mask)
        
        /**
         * Simultaneously sets both the "from" and "into" PortalMask values to the
         * same thing.
         */
        """
        pass

    def set_visible(self, const_PortalNode_self, bool_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_visible(const PortalNode self, bool value)
        
        /**
         * this is set if the portal is facing camera
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    cell_in = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cell_out = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clip_plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    from_portal_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    into_portal_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    portal_geom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A node in the scene graph that can hold a Portal Polygon, which is a\n * rectangle.  Other types of polygons are not supported for now.  It also\n * holds a PT(PandaNode) Cell that this portal is connected to\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PortalNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE29ACA0>'
        'addVertex': None, # (!) real value is "<method 'addVertex' of 'panda3d.core.PortalNode' objects>"
        'add_vertex': None, # (!) real value is "<method 'add_vertex' of 'panda3d.core.PortalNode' objects>"
        'cell_in': None, # (!) real value is "<attribute 'cell_in' of 'panda3d.core.PortalNode' objects>"
        'cell_out': None, # (!) real value is "<attribute 'cell_out' of 'panda3d.core.PortalNode' objects>"
        'clearVertices': None, # (!) real value is "<method 'clearVertices' of 'panda3d.core.PortalNode' objects>"
        'clear_vertices': None, # (!) real value is "<method 'clear_vertices' of 'panda3d.core.PortalNode' objects>"
        'clip_plane': None, # (!) real value is "<attribute 'clip_plane' of 'panda3d.core.PortalNode' objects>"
        'from_portal_mask': None, # (!) real value is "<attribute 'from_portal_mask' of 'panda3d.core.PortalNode' objects>"
        'getCellIn': None, # (!) real value is "<method 'getCellIn' of 'panda3d.core.PortalNode' objects>"
        'getCellOut': None, # (!) real value is "<method 'getCellOut' of 'panda3d.core.PortalNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE29ACA0>)>'
        'getFromPortalMask': None, # (!) real value is "<method 'getFromPortalMask' of 'panda3d.core.PortalNode' objects>"
        'getIntoPortalMask': None, # (!) real value is "<method 'getIntoPortalMask' of 'panda3d.core.PortalNode' objects>"
        'getMaxDepth': None, # (!) real value is "<method 'getMaxDepth' of 'panda3d.core.PortalNode' objects>"
        'getNumVertices': None, # (!) real value is "<method 'getNumVertices' of 'panda3d.core.PortalNode' objects>"
        'getPortalGeom': None, # (!) real value is "<method 'getPortalGeom' of 'panda3d.core.PortalNode' objects>"
        'getVertex': None, # (!) real value is "<method 'getVertex' of 'panda3d.core.PortalNode' objects>"
        'getVertices': None, # (!) real value is "<method 'getVertices' of 'panda3d.core.PortalNode' objects>"
        'get_cell_in': None, # (!) real value is "<method 'get_cell_in' of 'panda3d.core.PortalNode' objects>"
        'get_cell_out': None, # (!) real value is "<method 'get_cell_out' of 'panda3d.core.PortalNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE29ACA0>)>'
        'get_from_portal_mask': None, # (!) real value is "<method 'get_from_portal_mask' of 'panda3d.core.PortalNode' objects>"
        'get_into_portal_mask': None, # (!) real value is "<method 'get_into_portal_mask' of 'panda3d.core.PortalNode' objects>"
        'get_max_depth': None, # (!) real value is "<method 'get_max_depth' of 'panda3d.core.PortalNode' objects>"
        'get_num_vertices': None, # (!) real value is "<method 'get_num_vertices' of 'panda3d.core.PortalNode' objects>"
        'get_portal_geom': None, # (!) real value is "<method 'get_portal_geom' of 'panda3d.core.PortalNode' objects>"
        'get_vertex': None, # (!) real value is "<method 'get_vertex' of 'panda3d.core.PortalNode' objects>"
        'get_vertices': None, # (!) real value is "<method 'get_vertices' of 'panda3d.core.PortalNode' objects>"
        'into_portal_mask': None, # (!) real value is "<attribute 'into_portal_mask' of 'panda3d.core.PortalNode' objects>"
        'isClipPlane': None, # (!) real value is "<method 'isClipPlane' of 'panda3d.core.PortalNode' objects>"
        'isOpen': None, # (!) real value is "<method 'isOpen' of 'panda3d.core.PortalNode' objects>"
        'isVisible': None, # (!) real value is "<method 'isVisible' of 'panda3d.core.PortalNode' objects>"
        'is_clip_plane': None, # (!) real value is "<method 'is_clip_plane' of 'panda3d.core.PortalNode' objects>"
        'is_open': None, # (!) real value is "<method 'is_open' of 'panda3d.core.PortalNode' objects>"
        'is_visible': None, # (!) real value is "<method 'is_visible' of 'panda3d.core.PortalNode' objects>"
        'max_depth': None, # (!) real value is "<attribute 'max_depth' of 'panda3d.core.PortalNode' objects>"
        'open': None, # (!) real value is "<attribute 'open' of 'panda3d.core.PortalNode' objects>"
        'portal_geom': None, # (!) real value is "<attribute 'portal_geom' of 'panda3d.core.PortalNode' objects>"
        'setCellIn': None, # (!) real value is "<method 'setCellIn' of 'panda3d.core.PortalNode' objects>"
        'setCellOut': None, # (!) real value is "<method 'setCellOut' of 'panda3d.core.PortalNode' objects>"
        'setClipPlane': None, # (!) real value is "<method 'setClipPlane' of 'panda3d.core.PortalNode' objects>"
        'setFromPortalMask': None, # (!) real value is "<method 'setFromPortalMask' of 'panda3d.core.PortalNode' objects>"
        'setIntoPortalMask': None, # (!) real value is "<method 'setIntoPortalMask' of 'panda3d.core.PortalNode' objects>"
        'setMaxDepth': None, # (!) real value is "<method 'setMaxDepth' of 'panda3d.core.PortalNode' objects>"
        'setOpen': None, # (!) real value is "<method 'setOpen' of 'panda3d.core.PortalNode' objects>"
        'setPortalGeom': None, # (!) real value is "<method 'setPortalGeom' of 'panda3d.core.PortalNode' objects>"
        'setPortalMask': None, # (!) real value is "<method 'setPortalMask' of 'panda3d.core.PortalNode' objects>"
        'setVisible': None, # (!) real value is "<method 'setVisible' of 'panda3d.core.PortalNode' objects>"
        'set_cell_in': None, # (!) real value is "<method 'set_cell_in' of 'panda3d.core.PortalNode' objects>"
        'set_cell_out': None, # (!) real value is "<method 'set_cell_out' of 'panda3d.core.PortalNode' objects>"
        'set_clip_plane': None, # (!) real value is "<method 'set_clip_plane' of 'panda3d.core.PortalNode' objects>"
        'set_from_portal_mask': None, # (!) real value is "<method 'set_from_portal_mask' of 'panda3d.core.PortalNode' objects>"
        'set_into_portal_mask': None, # (!) real value is "<method 'set_into_portal_mask' of 'panda3d.core.PortalNode' objects>"
        'set_max_depth': None, # (!) real value is "<method 'set_max_depth' of 'panda3d.core.PortalNode' objects>"
        'set_open': None, # (!) real value is "<method 'set_open' of 'panda3d.core.PortalNode' objects>"
        'set_portal_geom': None, # (!) real value is "<method 'set_portal_geom' of 'panda3d.core.PortalNode' objects>"
        'set_portal_mask': None, # (!) real value is "<method 'set_portal_mask' of 'panda3d.core.PortalNode' objects>"
        'set_visible': None, # (!) real value is "<method 'set_visible' of 'panda3d.core.PortalNode' objects>"
        'vertices': None, # (!) real value is "<attribute 'vertices' of 'panda3d.core.PortalNode' objects>"
        'visible': None, # (!) real value is "<attribute 'visible' of 'panda3d.core.PortalNode' objects>"
    }


