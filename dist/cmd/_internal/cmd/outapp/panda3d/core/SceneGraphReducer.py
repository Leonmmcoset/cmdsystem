# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class SceneGraphReducer(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * An interface for simplifying ("flattening") scene graphs by eliminating
     * unneeded nodes and collapsing out unneeded state changes and transforms.
     *
     * This class is designed so that it may be inherited from and specialized, if
     * needed, to fine-tune the flattening behavior, but normally the default
     * behavior is sufficient.
     */
    """
    def applyAttribs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_attribs(const SceneGraphReducer self, PandaNode node, int attrib_types)
        
        /**
         * Walks the scene graph, accumulating attribs of the indicated types,
         * applying them to the vertices, and removing them from the scene graph.
         * This has a performance optimization benefit in itself, but is especially
         * useful to pave the way for a call to flatten() and greatly improve the
         * effectiveness of the flattening operation.
         *
         * Multiply instanced geometry is duplicated before the attribs are applied.
         *
         * Of course, this operation does make certain dynamic operations impossible.
         */
        
        /**
         * This flavor of apply_attribs() can be called recursively from within
         * another flatten process (e.g.  from
         * PandaNode::apply_attribs_to_vertices()). The parameters were presumably
         * received from a parent SceneGraphReducer object.
         */
        """
        pass

    def apply_attribs(self, const_SceneGraphReducer_self, PandaNode_node, int_attrib_types): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_attribs(const SceneGraphReducer self, PandaNode node, int attrib_types)
        
        /**
         * Walks the scene graph, accumulating attribs of the indicated types,
         * applying them to the vertices, and removing them from the scene graph.
         * This has a performance optimization benefit in itself, but is especially
         * useful to pave the way for a call to flatten() and greatly improve the
         * effectiveness of the flattening operation.
         *
         * Multiply instanced geometry is duplicated before the attribs are applied.
         *
         * Of course, this operation does make certain dynamic operations impossible.
         */
        
        /**
         * This flavor of apply_attribs() can be called recursively from within
         * another flatten process (e.g.  from
         * PandaNode::apply_attribs_to_vertices()). The parameters were presumably
         * received from a parent SceneGraphReducer object.
         */
        """
        pass

    def checkLiveFlatten(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        check_live_flatten(const SceneGraphReducer self, PandaNode node)
        
        /**
         * In a non-release build, returns false if the node is correctly not in a
         * live scene graph.  (Calling flatten on a node that is part of a live scene
         * graph, for instance, a node somewhere under render, can cause problems in a
         * multithreaded environment.)
         *
         * If allow_live_flatten is true, or in a release build, this always returns
         * true.
         */
        """
        pass

    def check_live_flatten(self, const_SceneGraphReducer_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        check_live_flatten(const SceneGraphReducer self, PandaNode node)
        
        /**
         * In a non-release build, returns false if the node is correctly not in a
         * live scene graph.  (Calling flatten on a node that is part of a live scene
         * graph, for instance, a node somewhere under render, can cause problems in a
         * multithreaded environment.)
         *
         * If allow_live_flatten is true, or in a release build, this always returns
         * true.
         */
        """
        pass

    def clearGsg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_gsg(const SceneGraphReducer self)
        
        /**
         * Specifies that no particular GraphicsStateGuardian will be used to guide
         * the optimization.  The SceneGraphReducer will instead use config variables
         * such as max-collect-vertices and max-collect-indices.
         */
        """
        pass

    def clear_gsg(self, const_SceneGraphReducer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_gsg(const SceneGraphReducer self)
        
        /**
         * Specifies that no particular GraphicsStateGuardian will be used to guide
         * the optimization.  The SceneGraphReducer will instead use config variables
         * such as max-collect-vertices and max-collect-indices.
         */
        """
        pass

    def collectVertexData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        collect_vertex_data(const SceneGraphReducer self, PandaNode root, int collect_bits)
        
        /**
         * Collects all different GeomVertexData blocks that have compatible formats
         * at this node and below into a single, unified block (or at least multiple
         * larger blocks).  This is intended to reduce rendering overhead incurred by
         * switching vertex buffers.  It can also make a subsequent call to unify()
         * much more effective than it would have been otherwise.
         *
         * The set of bits passed in collect_bits indicates which properties are used
         * to differentiate GeomVertexData blocks.  If it is 0, then more blocks will
         * be combined together than if it is nonzero.
         */
        """
        pass

    def collect_vertex_data(self, const_SceneGraphReducer_self, PandaNode_root, int_collect_bits): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        collect_vertex_data(const SceneGraphReducer self, PandaNode root, int collect_bits)
        
        /**
         * Collects all different GeomVertexData blocks that have compatible formats
         * at this node and below into a single, unified block (or at least multiple
         * larger blocks).  This is intended to reduce rendering overhead incurred by
         * switching vertex buffers.  It can also make a subsequent call to unify()
         * much more effective than it would have been otherwise.
         *
         * The set of bits passed in collect_bits indicates which properties are used
         * to differentiate GeomVertexData blocks.  If it is 0, then more blocks will
         * be combined together than if it is nonzero.
         */
        """
        pass

    def decompose(self, const_SceneGraphReducer_self, PandaNode_root): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        decompose(const SceneGraphReducer self, PandaNode root)
        
        /**
         * Calls decompose() on every GeomNode at this level and below.
         *
         * There is usually no reason to call this explicitly, since unify() will do
         * this anyway if it needs to be done.  However, calling it ahead of time can
         * make that future call to unify() run a little bit faster.
         *
         * This operation has no effect if the config variable preserve-triangle-
         * strips has been set true.
         */
        """
        pass

    def flatten(self, const_SceneGraphReducer_self, PandaNode_root, int_combine_siblings_bits): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flatten(const SceneGraphReducer self, PandaNode root, int combine_siblings_bits)
        
        /**
         * Simplifies the graph by removing unnecessary nodes and nodes.
         *
         * In general, a node (and its parent node) is a candidate for removal if the
         * node has no siblings and the node has no special properties.
         *
         * If combine_siblings_bits is nonzero, some sibling nodes (according to the
         * bits set in combine_siblings_bits) may also be collapsed into a single
         * node.  This will further reduce scene graph complexity, sometimes
         * substantially, at the cost of reduced spatial separation.
         *
         * Returns the number of nodes removed from the graph.
         */
        """
        pass

    def getCombineRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_combine_radius(SceneGraphReducer self)
        
        /**
         * Returns the radius that is used in conjunction with CS_within_radius.  See
         * set_combine_radius().
         */
        """
        pass

    def getGsg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_gsg(SceneGraphReducer self)
        
        /**
         * Returns the particular GraphicsStateGuardian that this object will attempt
         * to optimize to.  See set_gsg().
         */
        """
        pass

    def get_combine_radius(self, SceneGraphReducer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_combine_radius(SceneGraphReducer self)
        
        /**
         * Returns the radius that is used in conjunction with CS_within_radius.  See
         * set_combine_radius().
         */
        """
        pass

    def get_gsg(self, SceneGraphReducer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_gsg(SceneGraphReducer self)
        
        /**
         * Returns the particular GraphicsStateGuardian that this object will attempt
         * to optimize to.  See set_gsg().
         */
        """
        pass

    def makeCompatibleFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_compatible_format(const SceneGraphReducer self, PandaNode root, int collect_bits)
        
        /**
         * Walks through the tree at this node and below and unifies the
         * GeomVertexFormat for any GeomVertexData objects that are found, so that all
         * eligible vdatas (according to collect_bits; see collect_vertex_data) will
         * share the same vertex format.
         *
         * This will add unused columns where necessary to match formats.  It can
         * result in suboptimal performance if used needlessly.
         *
         * There is usually no reason to call this explicitly, since
         * collect_vertex_data() will do this anyway if it has not been done already.
         * However, calling it ahead of time can make that future call to
         * collect_vertex_data() run a little bit faster.
         *
         * The return value is the number of vertex datas modified.
         */
        """
        pass

    def makeCompatibleState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_compatible_state(const SceneGraphReducer self, PandaNode root)
        
        /**
         * Searches for GeomNodes that contain multiple Geoms that differ only in
         * their ColorAttribs.  If such a GeomNode is found, then all the colors are
         * pushed down into the vertices.  This makes it feasible for the geoms to be
         * unified later.
         */
        """
        pass

    def makeNonindexed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_nonindexed(const SceneGraphReducer self, PandaNode root, int nonindexed_bits)
        
        /**
         * Converts indexed geometry to nonindexed geometry at the indicated node and
         * below, by duplicating vertices where necessary.  The parameter
         * nonindexed_bits is a union of bits defined in
         * SceneGraphReducer::MakeNonindexed, which specifes which types of geometry
         * to avoid making nonindexed.
         */
        """
        pass

    def make_compatible_format(self, const_SceneGraphReducer_self, PandaNode_root, int_collect_bits): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_compatible_format(const SceneGraphReducer self, PandaNode root, int collect_bits)
        
        /**
         * Walks through the tree at this node and below and unifies the
         * GeomVertexFormat for any GeomVertexData objects that are found, so that all
         * eligible vdatas (according to collect_bits; see collect_vertex_data) will
         * share the same vertex format.
         *
         * This will add unused columns where necessary to match formats.  It can
         * result in suboptimal performance if used needlessly.
         *
         * There is usually no reason to call this explicitly, since
         * collect_vertex_data() will do this anyway if it has not been done already.
         * However, calling it ahead of time can make that future call to
         * collect_vertex_data() run a little bit faster.
         *
         * The return value is the number of vertex datas modified.
         */
        """
        pass

    def make_compatible_state(self, const_SceneGraphReducer_self, PandaNode_root): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_compatible_state(const SceneGraphReducer self, PandaNode root)
        
        /**
         * Searches for GeomNodes that contain multiple Geoms that differ only in
         * their ColorAttribs.  If such a GeomNode is found, then all the colors are
         * pushed down into the vertices.  This makes it feasible for the geoms to be
         * unified later.
         */
        """
        pass

    def make_nonindexed(self, const_SceneGraphReducer_self, PandaNode_root, int_nonindexed_bits): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_nonindexed(const SceneGraphReducer self, PandaNode root, int nonindexed_bits)
        
        /**
         * Converts indexed geometry to nonindexed geometry at the indicated node and
         * below, by duplicating vertices where necessary.  The parameter
         * nonindexed_bits is a union of bits defined in
         * SceneGraphReducer::MakeNonindexed, which specifes which types of geometry
         * to avoid making nonindexed.
         */
        """
        pass

    def premunge(self, const_SceneGraphReducer_self, PandaNode_root, const_RenderState_initial_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        premunge(const SceneGraphReducer self, PandaNode root, const RenderState initial_state)
        
        /**
         * Walks the scene graph rooted at this node and below, and uses the indicated
         * GSG to premunge every Geom found to optimize it for eventual rendering on
         * the indicated GSG.  If there is no GSG indicated for the SceneGraphReducer,
         * this is a no-op.
         *
         * This operation will also apply to stashed children.
         */
        """
        pass

    def removeColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_column(const SceneGraphReducer self, PandaNode root, const InternalName column)
        
        /**
         * Removes the indicated data column from any GeomVertexDatas found at the
         * indicated root and below.  Returns the number of GeomNodes modified.
         */
        """
        pass

    def removeUnusedVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_unused_vertices(const SceneGraphReducer self, PandaNode root)
        
        /**
         * Removes any vertices in GeomVertexDatas that are no longer used at this
         * level and below.  This requires remapping vertex indices in all of the
         * GeomPrimitives, to remove holes in the GeomVertexDatas.  It is normally not
         * necessary to call this explicitly.
         */
        """
        pass

    def remove_column(self, const_SceneGraphReducer_self, PandaNode_root, const_InternalName_column): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_column(const SceneGraphReducer self, PandaNode root, const InternalName column)
        
        /**
         * Removes the indicated data column from any GeomVertexDatas found at the
         * indicated root and below.  Returns the number of GeomNodes modified.
         */
        """
        pass

    def remove_unused_vertices(self, const_SceneGraphReducer_self, PandaNode_root): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_unused_vertices(const SceneGraphReducer self, PandaNode root)
        
        /**
         * Removes any vertices in GeomVertexDatas that are no longer used at this
         * level and below.  This requires remapping vertex indices in all of the
         * GeomPrimitives, to remove holes in the GeomVertexDatas.  It is normally not
         * necessary to call this explicitly.
         */
        """
        pass

    def setCombineRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_combine_radius(const SceneGraphReducer self, float combine_radius)
        
        /**
         * Specifies the radius that is used in conjunction with CS_within_radius to
         * decide whether a subgraph's siblings should be combined into a single node
         * or not.
         *
         * If the CS_within_radius bit is included in the combine_siblings_bits
         * parameter passed to flatten, than any nodes whose bounding volume is
         * smaller than the indicated radius will be combined together (as if CS_other
         * were set).
         */
        """
        pass

    def setGsg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_gsg(const SceneGraphReducer self, GraphicsStateGuardianBase gsg)
        
        /**
         * Specifies the particular GraphicsStateGuardian that this object will
         * attempt to optimize to.  The GSG may specify parameters such as maximum
         * number of vertices per vertex data, max number of vertices per primitive,
         * and whether triangle strips are preferred.  It also affects the types of
         * vertex column data that is created by premunge().
         */
        """
        pass

    def set_combine_radius(self, const_SceneGraphReducer_self, float_combine_radius): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_combine_radius(const SceneGraphReducer self, float combine_radius)
        
        /**
         * Specifies the radius that is used in conjunction with CS_within_radius to
         * decide whether a subgraph's siblings should be combined into a single node
         * or not.
         *
         * If the CS_within_radius bit is included in the combine_siblings_bits
         * parameter passed to flatten, than any nodes whose bounding volume is
         * smaller than the indicated radius will be combined together (as if CS_other
         * were set).
         */
        """
        pass

    def set_gsg(self, const_SceneGraphReducer_self, GraphicsStateGuardianBase_gsg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_gsg(const SceneGraphReducer self, GraphicsStateGuardianBase gsg)
        
        /**
         * Specifies the particular GraphicsStateGuardian that this object will
         * attempt to optimize to.  The GSG may specify parameters such as maximum
         * number of vertices per vertex data, max number of vertices per primitive,
         * and whether triangle strips are preferred.  It also affects the types of
         * vertex column data that is created by premunge().
         */
        """
        pass

    def unify(self, const_SceneGraphReducer_self, PandaNode_root, bool_preserve_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unify(const SceneGraphReducer self, PandaNode root, bool preserve_order)
        
        /**
         * Calls unify() on every GeomNode at this level and below.  This attempts to
         * reduce the total number of individual Geoms and GeomPrimitives by combining
         * these objects wherever possible.  See GeomNode::unify().
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

    CSGeomNode = 1
    CSOther = 4
    CSRecurse = 8
    CSWithinRadius = 2
    CS_geom_node = 1
    CS_other = 4
    CS_recurse = 8
    CS_within_radius = 2
    CVDAnimationType = 128
    CVDAvoidDynamic = 8
    CVDFormat = 32
    CVDModel = 2
    CVDName = 1
    CVDOneNodeOnly = 16
    CVDTransform = 4
    CVDUsageHint = 64
    CVD_animation_type = 128
    CVD_avoid_dynamic = 8
    CVD_format = 32
    CVD_model = 2
    CVD_name = 1
    CVD_one_node_only = 16
    CVD_transform = 4
    CVD_usage_hint = 64
    DtoolClassDict = {
        'CSGeomNode': 1,
        'CSOther': 4,
        'CSRecurse': 8,
        'CSWithinRadius': 2,
        'CS_geom_node': 1,
        'CS_other': 4,
        'CS_recurse': 8,
        'CS_within_radius': 2,
        'CVDAnimationType': 128,
        'CVDAvoidDynamic': 8,
        'CVDFormat': 32,
        'CVDModel': 2,
        'CVDName': 1,
        'CVDOneNodeOnly': 16,
        'CVDTransform': 4,
        'CVDUsageHint': 64,
        'CVD_animation_type': 128,
        'CVD_avoid_dynamic': 8,
        'CVD_format': 32,
        'CVD_model': 2,
        'CVD_name': 1,
        'CVD_one_node_only': 16,
        'CVD_transform': 4,
        'CVD_usage_hint': 64,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'MNAvoidAnimated': 2,
        'MNAvoidDynamic': 4,
        'MNCompositeOnly': 1,
        'MN_avoid_animated': 2,
        'MN_avoid_dynamic': 4,
        'MN_composite_only': 1,
        'TTApplyTextureColor': 64,
        'TTClipPlane': 16,
        'TTColor': 2,
        'TTColorScale': 4,
        'TTCullFace': 32,
        'TTOther': 128,
        'TTTexMatrix': 8,
        'TTTransform': 1,
        'TT_apply_texture_color': 64,
        'TT_clip_plane': 16,
        'TT_color': 2,
        'TT_color_scale': 4,
        'TT_cull_face': 32,
        'TT_other': 128,
        'TT_tex_matrix': 8,
        'TT_transform': 1,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.SceneGraphReducer' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.SceneGraphReducer' objects>"
        '__doc__': '/**\n * An interface for simplifying ("flattening") scene graphs by eliminating\n * unneeded nodes and collapsing out unneeded state changes and transforms.\n *\n * This class is designed so that it may be inherited from and specialized, if\n * needed, to fine-tune the flattening behavior, but normally the default\n * behavior is sufficient.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SceneGraphReducer' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE29A900>'
        'applyAttribs': None, # (!) real value is "<method 'applyAttribs' of 'panda3d.core.SceneGraphReducer' objects>"
        'apply_attribs': None, # (!) real value is "<method 'apply_attribs' of 'panda3d.core.SceneGraphReducer' objects>"
        'checkLiveFlatten': None, # (!) real value is "<method 'checkLiveFlatten' of 'panda3d.core.SceneGraphReducer' objects>"
        'check_live_flatten': None, # (!) real value is "<method 'check_live_flatten' of 'panda3d.core.SceneGraphReducer' objects>"
        'clearGsg': None, # (!) real value is "<method 'clearGsg' of 'panda3d.core.SceneGraphReducer' objects>"
        'clear_gsg': None, # (!) real value is "<method 'clear_gsg' of 'panda3d.core.SceneGraphReducer' objects>"
        'collectVertexData': None, # (!) real value is "<method 'collectVertexData' of 'panda3d.core.SceneGraphReducer' objects>"
        'collect_vertex_data': None, # (!) real value is "<method 'collect_vertex_data' of 'panda3d.core.SceneGraphReducer' objects>"
        'decompose': None, # (!) real value is "<method 'decompose' of 'panda3d.core.SceneGraphReducer' objects>"
        'flatten': None, # (!) real value is "<method 'flatten' of 'panda3d.core.SceneGraphReducer' objects>"
        'getCombineRadius': None, # (!) real value is "<method 'getCombineRadius' of 'panda3d.core.SceneGraphReducer' objects>"
        'getGsg': None, # (!) real value is "<method 'getGsg' of 'panda3d.core.SceneGraphReducer' objects>"
        'get_combine_radius': None, # (!) real value is "<method 'get_combine_radius' of 'panda3d.core.SceneGraphReducer' objects>"
        'get_gsg': None, # (!) real value is "<method 'get_gsg' of 'panda3d.core.SceneGraphReducer' objects>"
        'makeCompatibleFormat': None, # (!) real value is "<method 'makeCompatibleFormat' of 'panda3d.core.SceneGraphReducer' objects>"
        'makeCompatibleState': None, # (!) real value is "<method 'makeCompatibleState' of 'panda3d.core.SceneGraphReducer' objects>"
        'makeNonindexed': None, # (!) real value is "<method 'makeNonindexed' of 'panda3d.core.SceneGraphReducer' objects>"
        'make_compatible_format': None, # (!) real value is "<method 'make_compatible_format' of 'panda3d.core.SceneGraphReducer' objects>"
        'make_compatible_state': None, # (!) real value is "<method 'make_compatible_state' of 'panda3d.core.SceneGraphReducer' objects>"
        'make_nonindexed': None, # (!) real value is "<method 'make_nonindexed' of 'panda3d.core.SceneGraphReducer' objects>"
        'premunge': None, # (!) real value is "<method 'premunge' of 'panda3d.core.SceneGraphReducer' objects>"
        'removeColumn': None, # (!) real value is "<method 'removeColumn' of 'panda3d.core.SceneGraphReducer' objects>"
        'removeUnusedVertices': None, # (!) real value is "<method 'removeUnusedVertices' of 'panda3d.core.SceneGraphReducer' objects>"
        'remove_column': None, # (!) real value is "<method 'remove_column' of 'panda3d.core.SceneGraphReducer' objects>"
        'remove_unused_vertices': None, # (!) real value is "<method 'remove_unused_vertices' of 'panda3d.core.SceneGraphReducer' objects>"
        'setCombineRadius': None, # (!) real value is "<method 'setCombineRadius' of 'panda3d.core.SceneGraphReducer' objects>"
        'setGsg': None, # (!) real value is "<method 'setGsg' of 'panda3d.core.SceneGraphReducer' objects>"
        'set_combine_radius': None, # (!) real value is "<method 'set_combine_radius' of 'panda3d.core.SceneGraphReducer' objects>"
        'set_gsg': None, # (!) real value is "<method 'set_gsg' of 'panda3d.core.SceneGraphReducer' objects>"
        'unify': None, # (!) real value is "<method 'unify' of 'panda3d.core.SceneGraphReducer' objects>"
    }
    MNAvoidAnimated = 2
    MNAvoidDynamic = 4
    MNCompositeOnly = 1
    MN_avoid_animated = 2
    MN_avoid_dynamic = 4
    MN_composite_only = 1
    TTApplyTextureColor = 64
    TTClipPlane = 16
    TTColor = 2
    TTColorScale = 4
    TTCullFace = 32
    TTOther = 128
    TTTexMatrix = 8
    TTTransform = 1
    TT_apply_texture_color = 64
    TT_clip_plane = 16
    TT_color = 2
    TT_color_scale = 4
    TT_cull_face = 32
    TT_other = 128
    TT_tex_matrix = 8
    TT_transform = 1


