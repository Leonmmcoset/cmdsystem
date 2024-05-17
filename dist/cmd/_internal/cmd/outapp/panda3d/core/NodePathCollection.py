# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class NodePathCollection(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is a set of zero or more NodePaths.  It's handy for returning from
     * functions that need to return multiple NodePaths (for instance,
     * NodePaths::get_children).
     */
    """
    def addPath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_path(const NodePathCollection self, const NodePath node_path)
        
        /**
         * Adds a new NodePath to the collection.
         */
        """
        pass

    def addPathsFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_paths_from(const NodePathCollection self, const NodePathCollection other)
        
        /**
         * Adds all the NodePaths indicated in the other collection to this path.  The
         * other paths are simply appended to the end of the paths in this list;
         * duplicates are not automatically removed.
         */
        """
        pass

    def add_path(self, const_NodePathCollection_self, const_NodePath_node_path): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_path(const NodePathCollection self, const NodePath node_path)
        
        /**
         * Adds a new NodePath to the collection.
         */
        """
        pass

    def add_paths_from(self, const_NodePathCollection_self, const_NodePathCollection_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_paths_from(const NodePathCollection self, const NodePathCollection other)
        
        /**
         * Adds all the NodePaths indicated in the other collection to this path.  The
         * other paths are simply appended to the end of the paths in this list;
         * duplicates are not automatically removed.
         */
        """
        pass

    def append(self, const_NodePathCollection_self, const_NodePath_node_path): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        append(const NodePathCollection self, const NodePath node_path)
        
        // Method names to satisfy Python's conventions.
        
        /**
         * Adds a new NodePath to the collection.  This method duplicates the
         * add_path() method; it is provided to satisfy Python's naming convention.
         */
        """
        pass

    def calcTightBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        calc_tight_bounds(NodePathCollection self, LPoint3f min_point, LPoint3f max_point)
        
        /**
         * Calculates the minimum and maximum vertices of all Geoms at these
         * NodePath's bottom nodes and below This is a tight bounding box; it will
         * generally be tighter than the bounding volume returned by get_bounds() (but
         * it is more expensive to compute).
         *
         * The return value is true if any points are within the bounding volume, or
         * false if none are.
         */
        """
        pass

    def calc_tight_bounds(self, NodePathCollection_self, LPoint3f_min_point, LPoint3f_max_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        calc_tight_bounds(NodePathCollection self, LPoint3f min_point, LPoint3f max_point)
        
        /**
         * Calculates the minimum and maximum vertices of all Geoms at these
         * NodePath's bottom nodes and below This is a tight bounding box; it will
         * generally be tighter than the bounding volume returned by get_bounds() (but
         * it is more expensive to compute).
         *
         * The return value is true if any points are within the bounding volume, or
         * false if none are.
         */
        """
        pass

    def clear(self, const_NodePathCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const NodePathCollection self)
        
        /**
         * Removes all NodePaths from the collection.
         */
        """
        pass

    def composeColorScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compose_color_scale(const NodePathCollection self, const LVecBase4f scale)
        compose_color_scale(const NodePathCollection self, const LVecBase4f scale, int priority)
        compose_color_scale(const NodePathCollection self, float r, float g, float b, float a, int priority)
        
        /**
         * Applies color scales to all NodePaths in the collection.  The existing
         * color scale, if any, is multiplied by the specified color scale.
         */
        
        /**
         * Applies color scales to all NodePaths in the collection.  The existing
         * color scale, if any, is multiplied by the specified color scale.
         */
        """
        pass

    def compose_color_scale(self, const_NodePathCollection_self, const_LVecBase4f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compose_color_scale(const NodePathCollection self, const LVecBase4f scale)
        compose_color_scale(const NodePathCollection self, const LVecBase4f scale, int priority)
        compose_color_scale(const NodePathCollection self, float r, float g, float b, float a, int priority)
        
        /**
         * Applies color scales to all NodePaths in the collection.  The existing
         * color scale, if any, is multiplied by the specified color scale.
         */
        
        /**
         * Applies color scales to all NodePaths in the collection.  The existing
         * color scale, if any, is multiplied by the specified color scale.
         */
        """
        pass

    def detach(self, const_NodePathCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        detach(const NodePathCollection self)
        
        /**
         * Detaches all NodePaths in the collection.
         */
        """
        pass

    def extend(self, const_NodePathCollection_self, const_NodePathCollection_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        extend(const NodePathCollection self, const NodePathCollection other)
        
        /**
         * Appends the other list onto the end of this one.  This method duplicates
         * the += operator; it is provided to satisfy Python's naming convention.
         */
        """
        pass

    def findAllMatches(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_all_matches(NodePathCollection self, str path)
        
        /**
         * Returns the complete set of all NodePaths that begin with any NodePath in
         * this collection and can be extended by path.  The shortest paths will be
         * listed first.
         */
        """
        pass

    def find_all_matches(self, NodePathCollection_self, str_path): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_all_matches(NodePathCollection self, str path)
        
        /**
         * Returns the complete set of all NodePaths that begin with any NodePath in
         * this collection and can be extended by path.  The shortest paths will be
         * listed first.
         */
        """
        pass

    def getCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collide_mask(NodePathCollection self)
        
        /**
         * Returns the union of all of the into_collide_masks for nodes at this level
         * and below.  This is the same thing as node()->get_net_collide_mask().
         *
         * If you want to return what the into_collide_mask of this node itself is,
         * without regard to its children, use node()->get_into_collide_mask().
         */
        """
        pass

    def getNumPaths(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_paths(NodePathCollection self)
        
        /**
         * Returns the number of NodePaths in the collection.
         */
        """
        pass

    def getPath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_path(NodePathCollection self, int index)
        
        /**
         * Returns the nth NodePath in the collection.
         */
        """
        pass

    def getPaths(self, *args, **kwargs): # real signature unknown
        pass

    def getTightBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tight_bounds(NodePathCollection self)
        """
        pass

    def get_collide_mask(self, NodePathCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collide_mask(NodePathCollection self)
        
        /**
         * Returns the union of all of the into_collide_masks for nodes at this level
         * and below.  This is the same thing as node()->get_net_collide_mask().
         *
         * If you want to return what the into_collide_mask of this node itself is,
         * without regard to its children, use node()->get_into_collide_mask().
         */
        """
        pass

    def get_num_paths(self, NodePathCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_paths(NodePathCollection self)
        
        /**
         * Returns the number of NodePaths in the collection.
         */
        """
        pass

    def get_path(self, NodePathCollection_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_path(NodePathCollection self, int index)
        
        /**
         * Returns the nth NodePath in the collection.
         */
        """
        pass

    def get_paths(self, *args, **kwargs): # real signature unknown
        pass

    def get_tight_bounds(self, NodePathCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tight_bounds(NodePathCollection self)
        """
        pass

    def hasPath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_path(NodePathCollection self, const NodePath path)
        
        /**
         * Returns true if the indicated NodePath appears in this collection, false
         * otherwise.
         */
        """
        pass

    def has_path(self, NodePathCollection_self, const_NodePath_path): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_path(NodePathCollection self, const NodePath path)
        
        /**
         * Returns true if the indicated NodePath appears in this collection, false
         * otherwise.
         */
        """
        pass

    def hide(self, const_NodePathCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        hide(const NodePathCollection self)
        
        /**
         * Hides all NodePaths in the collection.
         */
        """
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(NodePathCollection self)
        
        /**
         * Returns true if there are no NodePaths in the collection, false otherwise.
         */
        """
        pass

    def is_empty(self, NodePathCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(NodePathCollection self)
        
        /**
         * Returns true if there are no NodePaths in the collection, false otherwise.
         */
        """
        pass

    def ls(self, NodePathCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ls(NodePathCollection self)
        ls(NodePathCollection self, ostream out, int indent_level)
        
        // Handy operations on many NodePaths at once.
        
        /**
         * Lists all the nodes at and below each node in the collection
         * hierarchically.
         */
        
        /**
         * Lists all the nodes at and below each node in the collection
         * hierarchically.
         */
        """
        pass

    def output(self, NodePathCollection_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(NodePathCollection self, ostream out)
        
        /**
         * Writes a brief one-line description of the NodePathCollection to the
         * indicated output stream.
         */
        """
        pass

    def removeDuplicatePaths(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_duplicate_paths(const NodePathCollection self)
        
        /**
         * Removes any duplicate entries of the same NodePaths on this collection.  If
         * a NodePath appears multiple times, the first appearance is retained;
         * subsequent appearances are removed.
         */
        """
        pass

    def removePath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_path(const NodePathCollection self, const NodePath node_path)
        
        /**
         * Removes the indicated NodePath from the collection.  Returns true if the
         * path was removed, false if it was not a member of the collection.
         */
        """
        pass

    def removePathsFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_paths_from(const NodePathCollection self, const NodePathCollection other)
        
        /**
         * Removes from this collection all of the NodePaths listed in the other
         * collection.
         */
        """
        pass

    def remove_duplicate_paths(self, const_NodePathCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_duplicate_paths(const NodePathCollection self)
        
        /**
         * Removes any duplicate entries of the same NodePaths on this collection.  If
         * a NodePath appears multiple times, the first appearance is retained;
         * subsequent appearances are removed.
         */
        """
        pass

    def remove_path(self, const_NodePathCollection_self, const_NodePath_node_path): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_path(const NodePathCollection self, const NodePath node_path)
        
        /**
         * Removes the indicated NodePath from the collection.  Returns true if the
         * path was removed, false if it was not a member of the collection.
         */
        """
        pass

    def remove_paths_from(self, const_NodePathCollection_self, const_NodePathCollection_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_paths_from(const NodePathCollection self, const NodePathCollection other)
        
        /**
         * Removes from this collection all of the NodePaths listed in the other
         * collection.
         */
        """
        pass

    def reparentTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reparent_to(const NodePathCollection self, const NodePath other)
        
        /**
         * Reparents all the NodePaths in the collection to the indicated node.
         */
        """
        pass

    def reparent_to(self, const_NodePathCollection_self, const_NodePath_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reparent_to(const NodePathCollection self, const NodePath other)
        
        /**
         * Reparents all the NodePaths in the collection to the indicated node.
         */
        """
        pass

    def reserve(self, const_NodePathCollection_self, int_num): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reserve(const NodePathCollection self, int num)
        
        /**
         * This is a hint to Panda to allocate enough memory to hold the given number
         * of NodePaths, if you know ahead of time how many you will be adding.
         */
        """
        pass

    def setAttrib(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_attrib(const NodePathCollection self, const RenderAttrib attrib, int priority)
        
        /**
         * Applies the indicated RenderAttrib to all NodePaths in the collection.  An
         * effort is made to apply the attrib to many NodePaths as quickly as
         * possible; redundant RenderState compositions are not duplicated.
         */
        """
        pass

    def setCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_collide_mask(const NodePathCollection self, BitMask new_mask, BitMask bits_to_change, TypeHandle node_type)
        
        /**
         * Recursively applies the indicated CollideMask to the into_collide_masks for
         * all nodes at this level and below.
         *
         * The default is to change all bits, but if bits_to_change is not all bits
         * on, then only the bits that are set in bits_to_change are modified,
         * allowing this call to change only a subset of the bits in the subgraph.
         */
        """
        pass

    def setColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color(const NodePathCollection self, const LVecBase4f color)
        set_color(const NodePathCollection self, const LVecBase4f color, int priority)
        set_color(const NodePathCollection self, float r, float g, float b, float a, int priority)
        
        /**
         * Colors all NodePaths in the collection
         */
        
        /**
         * Colors all NodePaths in the collection
         */
        """
        pass

    def setColorScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color_scale(const NodePathCollection self, const LVecBase4f scale)
        set_color_scale(const NodePathCollection self, const LVecBase4f scale, int priority)
        set_color_scale(const NodePathCollection self, float r, float g, float b, float a, int priority)
        
        /**
         * Applies color scales to all NodePaths in the collection.  The existing
         * color scale is replaced.
         */
        
        /**
         * Applies color scales to all NodePaths in the collection.  The existing
         * color scale is replaced.
         */
        """
        pass

    def setTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_texture(const NodePathCollection self, Texture tex)
        set_texture(const NodePathCollection self, TextureStage stage, Texture tex, int priority)
        set_texture(const NodePathCollection self, Texture tex, int priority)
        
        /**
         * Adds the indicated texture to the list of textures that will be rendered on
         * the default texture stage.
         *
         * This is the deprecated single-texture variant of this method; it is now
         * superceded by set_texture() that accepts a stage and texture.  However,
         * this method may be used in the presence of multitexture if you just want to
         * adjust the default stage.
         */
        
        /**
         * Adds the indicated texture to the list of textures that will be rendered on
         * the indicated multitexture stage.  If there are multiple texture stages
         * specified (possibly on multiple different nodes at different levels), they
         * will all be applied to geometry together, according to the stage
         * specification set up in the TextureStage object.
         */
        """
        pass

    def setTextureOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_texture_off(const NodePathCollection self)
        set_texture_off(const NodePathCollection self, TextureStage stage, int priority)
        set_texture_off(const NodePathCollection self, int priority)
        
        /**
         * Sets the geometry at this level and below to render using no texture, on
         * any stage.  This is different from not specifying a texture; rather, this
         * specifically contradicts set_texture() at a higher node level (or, with a
         * priority, overrides a set_texture() at a lower level).
         */
        
        /**
         * Sets the geometry at this level and below to render using no texture, on
         * the indicated stage.  This is different from not specifying a texture;
         * rather, this specifically contradicts set_texture() at a higher node level
         * (or, with a priority, overrides a set_texture() at a lower level).
         */
        """
        pass

    def set_attrib(self, const_NodePathCollection_self, const_RenderAttrib_attrib, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_attrib(const NodePathCollection self, const RenderAttrib attrib, int priority)
        
        /**
         * Applies the indicated RenderAttrib to all NodePaths in the collection.  An
         * effort is made to apply the attrib to many NodePaths as quickly as
         * possible; redundant RenderState compositions are not duplicated.
         */
        """
        pass

    def set_collide_mask(self, const_NodePathCollection_self, BitMask_new_mask, BitMask_bits_to_change, TypeHandle_node_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_collide_mask(const NodePathCollection self, BitMask new_mask, BitMask bits_to_change, TypeHandle node_type)
        
        /**
         * Recursively applies the indicated CollideMask to the into_collide_masks for
         * all nodes at this level and below.
         *
         * The default is to change all bits, but if bits_to_change is not all bits
         * on, then only the bits that are set in bits_to_change are modified,
         * allowing this call to change only a subset of the bits in the subgraph.
         */
        """
        pass

    def set_color(self, const_NodePathCollection_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color(const NodePathCollection self, const LVecBase4f color)
        set_color(const NodePathCollection self, const LVecBase4f color, int priority)
        set_color(const NodePathCollection self, float r, float g, float b, float a, int priority)
        
        /**
         * Colors all NodePaths in the collection
         */
        
        /**
         * Colors all NodePaths in the collection
         */
        """
        pass

    def set_color_scale(self, const_NodePathCollection_self, const_LVecBase4f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color_scale(const NodePathCollection self, const LVecBase4f scale)
        set_color_scale(const NodePathCollection self, const LVecBase4f scale, int priority)
        set_color_scale(const NodePathCollection self, float r, float g, float b, float a, int priority)
        
        /**
         * Applies color scales to all NodePaths in the collection.  The existing
         * color scale is replaced.
         */
        
        /**
         * Applies color scales to all NodePaths in the collection.  The existing
         * color scale is replaced.
         */
        """
        pass

    def set_texture(self, const_NodePathCollection_self, Texture_tex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_texture(const NodePathCollection self, Texture tex)
        set_texture(const NodePathCollection self, TextureStage stage, Texture tex, int priority)
        set_texture(const NodePathCollection self, Texture tex, int priority)
        
        /**
         * Adds the indicated texture to the list of textures that will be rendered on
         * the default texture stage.
         *
         * This is the deprecated single-texture variant of this method; it is now
         * superceded by set_texture() that accepts a stage and texture.  However,
         * this method may be used in the presence of multitexture if you just want to
         * adjust the default stage.
         */
        
        /**
         * Adds the indicated texture to the list of textures that will be rendered on
         * the indicated multitexture stage.  If there are multiple texture stages
         * specified (possibly on multiple different nodes at different levels), they
         * will all be applied to geometry together, according to the stage
         * specification set up in the TextureStage object.
         */
        """
        pass

    def set_texture_off(self, const_NodePathCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_texture_off(const NodePathCollection self)
        set_texture_off(const NodePathCollection self, TextureStage stage, int priority)
        set_texture_off(const NodePathCollection self, int priority)
        
        /**
         * Sets the geometry at this level and below to render using no texture, on
         * any stage.  This is different from not specifying a texture; rather, this
         * specifically contradicts set_texture() at a higher node level (or, with a
         * priority, overrides a set_texture() at a lower level).
         */
        
        /**
         * Sets the geometry at this level and below to render using no texture, on
         * the indicated stage.  This is different from not specifying a texture;
         * rather, this specifically contradicts set_texture() at a higher node level
         * (or, with a priority, overrides a set_texture() at a lower level).
         */
        """
        pass

    def show(self, const_NodePathCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        show(const NodePathCollection self)
        
        /**
         * Shows all NodePaths in the collection.
         */
        """
        pass

    def stash(self, const_NodePathCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        stash(const NodePathCollection self)
        
        /**
         * Stashes all NodePaths in the collection.
         */
        """
        pass

    def unstash(self, const_NodePathCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unstash(const NodePathCollection self)
        
        /**
         * Unstashes all NodePaths in the collection.
         */
        """
        pass

    def write(self, NodePathCollection_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(NodePathCollection self, ostream out, int indent_level)
        
        /**
         * Writes a complete multi-line description of the NodePathCollection to the
         * indicated output stream.
         */
        """
        pass

    def wrtReparentTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        wrt_reparent_to(const NodePathCollection self, const NodePath other)
        
        /**
         * Reparents all the NodePaths in the collection to the indicated node,
         * adjusting each transform so as not to move in world coordinates.
         */
        """
        pass

    def wrt_reparent_to(self, const_NodePathCollection_self, const_NodePath_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        wrt_reparent_to(const NodePathCollection self, const NodePath other)
        
        /**
         * Reparents all the NodePaths in the collection to the indicated node,
         * adjusting each transform so as not to move in world coordinates.
         */
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self, NodePathCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __reduce__(NodePathCollection self)
        """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__add__': None, # (!) real value is "<slot wrapper '__add__' of 'panda3d.core.NodePathCollection' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.NodePathCollection' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.NodePathCollection' objects>"
        '__doc__': "/**\n * This is a set of zero or more NodePaths.  It's handy for returning from\n * functions that need to return multiple NodePaths (for instance,\n * NodePaths::get_children).\n */",
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.core.NodePathCollection' objects>"
        '__iadd__': None, # (!) real value is "<slot wrapper '__iadd__' of 'panda3d.core.NodePathCollection' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.NodePathCollection' objects>"
        '__len__': None, # (!) real value is "<slot wrapper '__len__' of 'panda3d.core.NodePathCollection' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE293C40>'
        '__radd__': None, # (!) real value is "<slot wrapper '__radd__' of 'panda3d.core.NodePathCollection' objects>"
        '__reduce__': None, # (!) real value is "<method '__reduce__' of 'panda3d.core.NodePathCollection' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.NodePathCollection' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.NodePathCollection' objects>"
        'addPath': None, # (!) real value is "<method 'addPath' of 'panda3d.core.NodePathCollection' objects>"
        'addPathsFrom': None, # (!) real value is "<method 'addPathsFrom' of 'panda3d.core.NodePathCollection' objects>"
        'add_path': None, # (!) real value is "<method 'add_path' of 'panda3d.core.NodePathCollection' objects>"
        'add_paths_from': None, # (!) real value is "<method 'add_paths_from' of 'panda3d.core.NodePathCollection' objects>"
        'append': None, # (!) real value is "<method 'append' of 'panda3d.core.NodePathCollection' objects>"
        'calcTightBounds': None, # (!) real value is "<method 'calcTightBounds' of 'panda3d.core.NodePathCollection' objects>"
        'calc_tight_bounds': None, # (!) real value is "<method 'calc_tight_bounds' of 'panda3d.core.NodePathCollection' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.NodePathCollection' objects>"
        'composeColorScale': None, # (!) real value is "<method 'composeColorScale' of 'panda3d.core.NodePathCollection' objects>"
        'compose_color_scale': None, # (!) real value is "<method 'compose_color_scale' of 'panda3d.core.NodePathCollection' objects>"
        'detach': None, # (!) real value is "<method 'detach' of 'panda3d.core.NodePathCollection' objects>"
        'extend': None, # (!) real value is "<method 'extend' of 'panda3d.core.NodePathCollection' objects>"
        'findAllMatches': None, # (!) real value is "<method 'findAllMatches' of 'panda3d.core.NodePathCollection' objects>"
        'find_all_matches': None, # (!) real value is "<method 'find_all_matches' of 'panda3d.core.NodePathCollection' objects>"
        'getCollideMask': None, # (!) real value is "<method 'getCollideMask' of 'panda3d.core.NodePathCollection' objects>"
        'getNumPaths': None, # (!) real value is "<method 'getNumPaths' of 'panda3d.core.NodePathCollection' objects>"
        'getPath': None, # (!) real value is "<method 'getPath' of 'panda3d.core.NodePathCollection' objects>"
        'getPaths': None, # (!) real value is "<method 'getPaths' of 'panda3d.core.NodePathCollection' objects>"
        'getTightBounds': None, # (!) real value is "<method 'getTightBounds' of 'panda3d.core.NodePathCollection' objects>"
        'get_collide_mask': None, # (!) real value is "<method 'get_collide_mask' of 'panda3d.core.NodePathCollection' objects>"
        'get_num_paths': None, # (!) real value is "<method 'get_num_paths' of 'panda3d.core.NodePathCollection' objects>"
        'get_path': None, # (!) real value is "<method 'get_path' of 'panda3d.core.NodePathCollection' objects>"
        'get_paths': None, # (!) real value is "<method 'get_paths' of 'panda3d.core.NodePathCollection' objects>"
        'get_tight_bounds': None, # (!) real value is "<method 'get_tight_bounds' of 'panda3d.core.NodePathCollection' objects>"
        'hasPath': None, # (!) real value is "<method 'hasPath' of 'panda3d.core.NodePathCollection' objects>"
        'has_path': None, # (!) real value is "<method 'has_path' of 'panda3d.core.NodePathCollection' objects>"
        'hide': None, # (!) real value is "<method 'hide' of 'panda3d.core.NodePathCollection' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.core.NodePathCollection' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.core.NodePathCollection' objects>"
        'ls': None, # (!) real value is "<method 'ls' of 'panda3d.core.NodePathCollection' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.NodePathCollection' objects>"
        'removeDuplicatePaths': None, # (!) real value is "<method 'removeDuplicatePaths' of 'panda3d.core.NodePathCollection' objects>"
        'removePath': None, # (!) real value is "<method 'removePath' of 'panda3d.core.NodePathCollection' objects>"
        'removePathsFrom': None, # (!) real value is "<method 'removePathsFrom' of 'panda3d.core.NodePathCollection' objects>"
        'remove_duplicate_paths': None, # (!) real value is "<method 'remove_duplicate_paths' of 'panda3d.core.NodePathCollection' objects>"
        'remove_path': None, # (!) real value is "<method 'remove_path' of 'panda3d.core.NodePathCollection' objects>"
        'remove_paths_from': None, # (!) real value is "<method 'remove_paths_from' of 'panda3d.core.NodePathCollection' objects>"
        'reparentTo': None, # (!) real value is "<method 'reparentTo' of 'panda3d.core.NodePathCollection' objects>"
        'reparent_to': None, # (!) real value is "<method 'reparent_to' of 'panda3d.core.NodePathCollection' objects>"
        'reserve': None, # (!) real value is "<method 'reserve' of 'panda3d.core.NodePathCollection' objects>"
        'setAttrib': None, # (!) real value is "<method 'setAttrib' of 'panda3d.core.NodePathCollection' objects>"
        'setCollideMask': None, # (!) real value is "<method 'setCollideMask' of 'panda3d.core.NodePathCollection' objects>"
        'setColor': None, # (!) real value is "<method 'setColor' of 'panda3d.core.NodePathCollection' objects>"
        'setColorScale': None, # (!) real value is "<method 'setColorScale' of 'panda3d.core.NodePathCollection' objects>"
        'setTexture': None, # (!) real value is "<method 'setTexture' of 'panda3d.core.NodePathCollection' objects>"
        'setTextureOff': None, # (!) real value is "<method 'setTextureOff' of 'panda3d.core.NodePathCollection' objects>"
        'set_attrib': None, # (!) real value is "<method 'set_attrib' of 'panda3d.core.NodePathCollection' objects>"
        'set_collide_mask': None, # (!) real value is "<method 'set_collide_mask' of 'panda3d.core.NodePathCollection' objects>"
        'set_color': None, # (!) real value is "<method 'set_color' of 'panda3d.core.NodePathCollection' objects>"
        'set_color_scale': None, # (!) real value is "<method 'set_color_scale' of 'panda3d.core.NodePathCollection' objects>"
        'set_texture': None, # (!) real value is "<method 'set_texture' of 'panda3d.core.NodePathCollection' objects>"
        'set_texture_off': None, # (!) real value is "<method 'set_texture_off' of 'panda3d.core.NodePathCollection' objects>"
        'show': None, # (!) real value is "<method 'show' of 'panda3d.core.NodePathCollection' objects>"
        'stash': None, # (!) real value is "<method 'stash' of 'panda3d.core.NodePathCollection' objects>"
        'unstash': None, # (!) real value is "<method 'unstash' of 'panda3d.core.NodePathCollection' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.NodePathCollection' objects>"
        'wrtReparentTo': None, # (!) real value is "<method 'wrtReparentTo' of 'panda3d.core.NodePathCollection' objects>"
        'wrt_reparent_to': None, # (!) real value is "<method 'wrt_reparent_to' of 'panda3d.core.NodePathCollection' objects>"
    }


