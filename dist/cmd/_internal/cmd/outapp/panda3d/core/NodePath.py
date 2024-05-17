# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class NodePath(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * NodePath is the fundamental system for disambiguating instances, and also
     * provides a higher-level interface for manipulating the scene graph.
     *
     * A NodePath is a list of connected nodes from the root of the graph to any
     * sub-node.  Each NodePath therefore uniquely describes one instance of a
     * node.
     *
     * NodePaths themselves are lightweight objects that may easily be copied and
     * passed by value.  Their data is stored as a series of NodePathComponents
     * that are stored on the nodes.  Holding a NodePath will keep a reference
     * count to all the nodes in the path.  However, if any node in the path is
     * removed or reparented (perhaps through a different NodePath), the NodePath
     * will automatically be updated to reflect the changes.
     */
    """
    def addHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_hash(NodePath self, int hash)
        
        /**
         * Adds the NodePath into the running hash.  This is intended to be used by
         * lower-level code that computes a hash for each NodePath.  It modifies the
         * hash value passed in by a unique adjustment for each NodePath, and returns
         * the modified hash.
         *
         * This is similar to the unique integer returned by get_key(), but it is not
         * guaranteed to remain unique beyond the lifetime of this particular
         * NodePath.  Once this NodePath destructs, a different NodePath may be
         * created which shares the same hash value.
         */
        """
        pass

    def add_hash(self, NodePath_self, int_hash): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_hash(NodePath self, int hash)
        
        /**
         * Adds the NodePath into the running hash.  This is intended to be used by
         * lower-level code that computes a hash for each NodePath.  It modifies the
         * hash value passed in by a unique adjustment for each NodePath, and returns
         * the modified hash.
         *
         * This is similar to the unique integer returned by get_key(), but it is not
         * guaranteed to remain unique beyond the lifetime of this particular
         * NodePath.  Once this NodePath destructs, a different NodePath may be
         * created which shares the same hash value.
         */
        """
        pass

    def adjustAllPriorities(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        adjust_all_priorities(const NodePath self, int adjustment)
        
        /**
         * Adds the indicated adjustment amount (which may be negative) to the
         * priority for all transitions on the referenced node, and for all nodes in
         * the subgraph below.  This can be used to force these nodes not to be
         * overridden by a high-level state change above.  If the priority would drop
         * below zero, it is set to zero.
         */
        """
        pass

    def adjust_all_priorities(self, const_NodePath_self, int_adjustment): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        adjust_all_priorities(const NodePath self, int adjustment)
        
        /**
         * Adds the indicated adjustment amount (which may be negative) to the
         * priority for all transitions on the referenced node, and for all nodes in
         * the subgraph below.  This can be used to force these nodes not to be
         * overridden by a high-level state change above.  If the priority would drop
         * below zero, it is set to zero.
         */
        """
        pass

    def anyPath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        any_path(PandaNode node, Thread current_thread)
        
        /**
         * Returns a new NodePath that represents any arbitrary path from the root to
         * the indicated node.  This is the same thing that would be returned by
         * NodePath(node), except that no warning is issued if the path is ambiguous.
         */
        """
        pass

    def any_path(self, PandaNode_node, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        any_path(PandaNode node, Thread current_thread)
        
        /**
         * Returns a new NodePath that represents any arbitrary path from the root to
         * the indicated node.  This is the same thing that would be returned by
         * NodePath(node), except that no warning is issued if the path is ambiguous.
         */
        """
        pass

    def applyTextureColors(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_texture_colors(const NodePath self)
        
        /**
         * Removes textures from Geoms at this node and below by applying the texture
         * colors to the vertices.  This is primarily useful to simplify a low-LOD
         * model.  The texture colors are replaced by flat colors that approximate the
         * original textures.
         *
         * Only the bottommost texture on each Geom is used (if there is more than
         * one), and it is applied as if it were M_modulate, and WM_repeat, regardless
         * of its actual settings.  If the texture has a simple_ram_image, this may be
         * used if the main image isn't resident.
         *
         * After this call, there will be no texturing specified at this level and
         * below.  Of course, there might still be texturing inherited from above.
         */
        """
        pass

    def apply_texture_colors(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_texture_colors(const NodePath self)
        
        /**
         * Removes textures from Geoms at this node and below by applying the texture
         * colors to the vertices.  This is primarily useful to simplify a low-LOD
         * model.  The texture colors are replaced by flat colors that approximate the
         * original textures.
         *
         * Only the bottommost texture on each Geom is used (if there is more than
         * one), and it is applied as if it were M_modulate, and WM_repeat, regardless
         * of its actual settings.  If the texture has a simple_ram_image, this may be
         * used if the main image isn't resident.
         *
         * After this call, there will be no texturing specified at this level and
         * below.  Of course, there might still be texturing inherited from above.
         */
        """
        pass

    def assign(self, const_NodePath_self, const_NodePath_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const NodePath self, const NodePath copy)
        """
        pass

    def attachNewNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        attach_new_node(NodePath self, PandaNode node, int sort, Thread current_thread)
        attach_new_node(NodePath self, str name, int sort, Thread current_thread)
        
        /**
         * Creates an ordinary PandaNode and attaches it below the current NodePath,
         * returning a new NodePath that references it.
         */
        
        /**
         * Attaches a new node, with or without existing parents, to the scene graph
         * below the referenced node of this NodePath.  This is the preferred way to
         * add nodes to the graph.
         *
         * If the node was already a child of the parent, this returns a NodePath to
         * the existing child.
         *
         * This does *not* automatically extend the current NodePath to reflect the
         * attachment; however, a NodePath that does reflect this extension is
         * returned.
         */
        """
        pass

    def attach_new_node(self, NodePath_self, PandaNode_node, int_sort, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        attach_new_node(NodePath self, PandaNode node, int sort, Thread current_thread)
        attach_new_node(NodePath self, str name, int sort, Thread current_thread)
        
        /**
         * Creates an ordinary PandaNode and attaches it below the current NodePath,
         * returning a new NodePath that references it.
         */
        
        /**
         * Attaches a new node, with or without existing parents, to the scene graph
         * below the referenced node of this NodePath.  This is the preferred way to
         * add nodes to the graph.
         *
         * If the node was already a child of the parent, this returns a NodePath to
         * the existing child.
         *
         * This does *not* automatically extend the current NodePath to reflect the
         * attachment; however, a NodePath that does reflect this extension is
         * returned.
         */
        """
        pass

    def calcTightBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        calc_tight_bounds(NodePath self, LPoint3f min_point, LPoint3f max_point, const NodePath other, Thread current_thread)
        
        /**
         * Calculates the minimum and maximum vertices of all Geoms at this NodePath's
         * bottom node and below.  This is a tight bounding box; it will generally be
         * tighter than the bounding volume returned by get_bounds() (but it is more
         * expensive to compute).
         *
         * The bounding box is computed relative to the parent node's coordinate
         * system by default.  You can optionally specify a different NodePath to
         * compute the bounds relative to.  Note that the box is always axis-aligned
         * against the given NodePath's coordinate system, so you might get a
         * differently sized box depending on which node you pass.
         *
         * The return value is true if any points are within the bounding volume, or
         * false if none are.
         */
        """
        pass

    def calc_tight_bounds(self, NodePath_self, LPoint3f_min_point, LPoint3f_max_point, const_NodePath_other, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        calc_tight_bounds(NodePath self, LPoint3f min_point, LPoint3f max_point, const NodePath other, Thread current_thread)
        
        /**
         * Calculates the minimum and maximum vertices of all Geoms at this NodePath's
         * bottom node and below.  This is a tight bounding box; it will generally be
         * tighter than the bounding volume returned by get_bounds() (but it is more
         * expensive to compute).
         *
         * The bounding box is computed relative to the parent node's coordinate
         * system by default.  You can optionally specify a different NodePath to
         * compute the bounds relative to.  Note that the box is always axis-aligned
         * against the given NodePath's coordinate system, so you might get a
         * differently sized box depending on which node you pass.
         *
         * The return value is true if any points are within the bounding volume, or
         * false if none are.
         */
        """
        pass

    def clear(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const NodePath self)
        
        /**
         * Sets this NodePath to the empty NodePath.  It will no longer point to any
         * node.
         */
        """
        pass

    def clearAntialias(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_antialias(const NodePath self)
        
        /**
         * Completely removes any antialias setting that may have been set on this
         * node via set_antialias().
         */
        """
        pass

    def clearAttrib(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_attrib(const NodePath self, TypeHandle type)
        
        /**
         * Removes the render attribute of the given type from this node.  This node,
         * and the subgraph below, will now inherit the indicated render attribute
         * from the nodes above this one.
         */
        """
        pass

    def clearAudioVolume(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_audio_volume(const NodePath self)
        
        /**
         * Completely removes any audio volume from the referenced node.  This is
         * preferable to simply setting the audio volume to identity, as it also
         * removes the overhead associated with having an audio volume at all.
         */
        """
        pass

    def clearBillboard(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_billboard(const NodePath self)
        
        /**
         * Removes any billboard effect from the node.
         */
        """
        pass

    def clearBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_bin(const NodePath self)
        
        /**
         * Completely removes any bin adjustment that may have been set via set_bin()
         * from this particular node.
         */
        """
        pass

    def clearClipPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_clip_plane(const NodePath self)
        clear_clip_plane(const NodePath self, const NodePath clip_plane)
        
        /**
         * Completely removes any clip planes that may have been set via
         * set_clip_plane() or set_clip_plane_off() from this particular node.
         */
        
        /**
         * Removes any reference to the indicated clipping plane from the NodePath.
         */
        """
        pass

    def clearColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_color(const NodePath self)
        
        /**
         * Completely removes any color adjustment from the node.  This allows the
         * natural color of the geometry, or whatever color transitions might be
         * otherwise affecting the geometry, to show instead.
         */
        """
        pass

    def clearColorScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_color_scale(const NodePath self)
        
        /**
         * Completely removes any color scale from the referenced node.  This is
         * preferable to simply setting the color scale to identity, as it also
         * removes the overhead associated with having a color scale at all.
         */
        """
        pass

    def clearCompass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_compass(const NodePath self)
        
        /**
         * Removes any compass effect from the node.
         */
        """
        pass

    def clearDepthOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_depth_offset(const NodePath self)
        
        /**
         * Completely removes any depth-offset adjustment that may have been set on
         * this node via set_depth_offset().
         */
        """
        pass

    def clearDepthTest(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_depth_test(const NodePath self)
        
        /**
         * Completely removes any depth-test adjustment that may have been set on this
         * node via set_depth_test().
         */
        """
        pass

    def clearDepthWrite(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_depth_write(const NodePath self)
        
        /**
         * Completely removes any depth-write adjustment that may have been set on
         * this node via set_depth_write().
         */
        """
        pass

    def clearEffect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_effect(const NodePath self, TypeHandle type)
        
        /**
         * Removes the render effect of the given type from this node.
         */
        """
        pass

    def clearEffects(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_effects(const NodePath self)
        
        /**
         * Resets this node to have no render effects.
         */
        """
        pass

    def clearFog(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_fog(const NodePath self)
        
        /**
         * Completely removes any fog adjustment that may have been set via set_fog()
         * or set_fog_off() from this particular node.  This allows whatever fogs
         * might be otherwise affecting the geometry to show instead.
         */
        """
        pass

    def clearLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_light(const NodePath self)
        clear_light(const NodePath self, const NodePath light)
        
        /**
         * Completely removes any lighting operations that may have been set via
         * set_light() or set_light_off() from this particular node.
         */
        
        /**
         * Removes any reference to the indicated Light or PolylightNode from the
         * NodePath.
         */
        """
        pass

    def clearLogicOp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_logic_op(const NodePath self)
        
        /**
         * Completely removes any logical operation that may have been set on this
         * node via set_logic_op(). The geometry at this level and below will
         * subsequently be rendered using standard color blending.
         *
         * @since 1.10.0
         */
        """
        pass

    def clearMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_mat(const NodePath self)
        
        /**
         * Completely removes any transform from the referenced node.
         */
        """
        pass

    def clearMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_material(const NodePath self)
        
        /**
         * Completely removes any material adjustment that may have been set via
         * set_material() from this particular node.
         */
        """
        pass

    def clearModelNodes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_model_nodes(const NodePath self)
        
        /**
         * Recursively walks through the scene graph at this level and below, looking
         * for ModelNodes, and calls model_node->set_preserve_transform(PT_drop_node)
         * on each one.  This allows a subsequent call to flatten_strong() to
         * eliminate all of the ModelNodes.
         *
         * Returns the number of ModelNodes found.
         */
        """
        pass

    def clearOccluder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_occluder(const NodePath self)
        clear_occluder(const NodePath self, const NodePath occluder)
        
        /**
         * Completely removes any occluders that may have been set via set_occluder()
         * from this particular node.
         */
        
        /**
         * Removes any reference to the indicated occluder from the NodePath.
         */
        """
        pass

    def clearProjectTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_project_texture(const NodePath self, TextureStage stage)
        
        /**
         * Undoes the effect of project_texture().
         */
        """
        pass

    def clearPythonTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_python_tag(const NodePath self, object keys)
        """
        pass

    def clearRenderMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_render_mode(const NodePath self)
        
        /**
         * Completely removes any render mode adjustment that may have been set on
         * this node via set_render_mode_wireframe() or set_render_mode_filled().
         */
        """
        pass

    def clearScissor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_scissor(const NodePath self)
        
        /**
         * Removes the scissor region that was defined at this node level by a
         * previous call to set_scissor().
         */
        """
        pass

    def clearShader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_shader(const NodePath self)
        
        /**
         *
         */
        """
        pass

    def clearShaderInput(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_shader_input(const NodePath self, const InternalName id)
        
        /**
         *
         */
        """
        pass

    def clearTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_tag(const NodePath self, str key)
        
        /**
         * Removes the value defined for this key on this particular node.  After a
         * call to clear_tag(), has_tag() will return false for the indicated key.
         */
        """
        pass

    def clearTexGen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_tex_gen(const NodePath self)
        clear_tex_gen(const NodePath self, TextureStage stage)
        
        /**
         * Removes the texture coordinate generation mode from all texture stages on
         * this node.
         */
        
        /**
         * Disables automatic texture coordinate generation for the indicated texture
         * stage.
         */
        """
        pass

    def clearTexProjector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_tex_projector(const NodePath self)
        clear_tex_projector(const NodePath self, TextureStage stage)
        
        /**
         * Removes the TexProjectorEffect for the indicated stage from this node.
         */
        
        /**
         * Removes the TexProjectorEffect for all stages from this node.
         */
        """
        pass

    def clearTexTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_tex_transform(const NodePath self)
        clear_tex_transform(const NodePath self, TextureStage stage)
        
        /**
         * Removes all texture matrices from the current node.
         */
        
        /**
         * Removes the texture matrix on the current node for the given stage.
         */
        """
        pass

    def clearTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_texture(const NodePath self)
        clear_texture(const NodePath self, TextureStage stage)
        
        /**
         * Completely removes any texture adjustment that may have been set via
         * set_texture() or set_texture_off() from this particular node.  This allows
         * whatever textures might be otherwise affecting the geometry to show
         * instead.
         */
        
        /**
         * Removes any reference to the indicated texture stage from the NodePath.
         */
        """
        pass

    def clearTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_transform(const NodePath self)
        clear_transform(const NodePath self, const NodePath other, Thread current_thread)
        clear_transform(const NodePath self, Thread current_thread)
        
        /**
         * Sets the transform object on this node to identity.
         */
        
        /**
         * Sets the transform object on this node to identity, relative to the other
         * node.  This effectively places this node at the same position as the other
         * node.
         */
        """
        pass

    def clearTransparency(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_transparency(const NodePath self)
        
        /**
         * Completely removes any transparency adjustment that may have been set on
         * this node via set_transparency(). The geometry at this level and below will
         * subsequently be rendered either transparent or not, to whatever other nodes
         * may have had set_transparency() on them.
         */
        """
        pass

    def clearTwoSided(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_two_sided(const NodePath self)
        
        /**
         * Completely removes any two-sided adjustment that may have been set on this
         * node via set_two_sided(). The geometry at this level and below will
         * subsequently be rendered either two-sided or one-sided, according to
         * whatever other nodes may have had set_two_sided() on it, or according to
         * the initial state otherwise.
         */
        """
        pass

    def clear_antialias(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_antialias(const NodePath self)
        
        /**
         * Completely removes any antialias setting that may have been set on this
         * node via set_antialias().
         */
        """
        pass

    def clear_attrib(self, const_NodePath_self, TypeHandle_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_attrib(const NodePath self, TypeHandle type)
        
        /**
         * Removes the render attribute of the given type from this node.  This node,
         * and the subgraph below, will now inherit the indicated render attribute
         * from the nodes above this one.
         */
        """
        pass

    def clear_audio_volume(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_audio_volume(const NodePath self)
        
        /**
         * Completely removes any audio volume from the referenced node.  This is
         * preferable to simply setting the audio volume to identity, as it also
         * removes the overhead associated with having an audio volume at all.
         */
        """
        pass

    def clear_billboard(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_billboard(const NodePath self)
        
        /**
         * Removes any billboard effect from the node.
         */
        """
        pass

    def clear_bin(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_bin(const NodePath self)
        
        /**
         * Completely removes any bin adjustment that may have been set via set_bin()
         * from this particular node.
         */
        """
        pass

    def clear_clip_plane(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_clip_plane(const NodePath self)
        clear_clip_plane(const NodePath self, const NodePath clip_plane)
        
        /**
         * Completely removes any clip planes that may have been set via
         * set_clip_plane() or set_clip_plane_off() from this particular node.
         */
        
        /**
         * Removes any reference to the indicated clipping plane from the NodePath.
         */
        """
        pass

    def clear_color(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_color(const NodePath self)
        
        /**
         * Completely removes any color adjustment from the node.  This allows the
         * natural color of the geometry, or whatever color transitions might be
         * otherwise affecting the geometry, to show instead.
         */
        """
        pass

    def clear_color_scale(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_color_scale(const NodePath self)
        
        /**
         * Completely removes any color scale from the referenced node.  This is
         * preferable to simply setting the color scale to identity, as it also
         * removes the overhead associated with having a color scale at all.
         */
        """
        pass

    def clear_compass(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_compass(const NodePath self)
        
        /**
         * Removes any compass effect from the node.
         */
        """
        pass

    def clear_depth_offset(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_depth_offset(const NodePath self)
        
        /**
         * Completely removes any depth-offset adjustment that may have been set on
         * this node via set_depth_offset().
         */
        """
        pass

    def clear_depth_test(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_depth_test(const NodePath self)
        
        /**
         * Completely removes any depth-test adjustment that may have been set on this
         * node via set_depth_test().
         */
        """
        pass

    def clear_depth_write(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_depth_write(const NodePath self)
        
        /**
         * Completely removes any depth-write adjustment that may have been set on
         * this node via set_depth_write().
         */
        """
        pass

    def clear_effect(self, const_NodePath_self, TypeHandle_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_effect(const NodePath self, TypeHandle type)
        
        /**
         * Removes the render effect of the given type from this node.
         */
        """
        pass

    def clear_effects(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_effects(const NodePath self)
        
        /**
         * Resets this node to have no render effects.
         */
        """
        pass

    def clear_fog(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_fog(const NodePath self)
        
        /**
         * Completely removes any fog adjustment that may have been set via set_fog()
         * or set_fog_off() from this particular node.  This allows whatever fogs
         * might be otherwise affecting the geometry to show instead.
         */
        """
        pass

    def clear_light(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_light(const NodePath self)
        clear_light(const NodePath self, const NodePath light)
        
        /**
         * Completely removes any lighting operations that may have been set via
         * set_light() or set_light_off() from this particular node.
         */
        
        /**
         * Removes any reference to the indicated Light or PolylightNode from the
         * NodePath.
         */
        """
        pass

    def clear_logic_op(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_logic_op(const NodePath self)
        
        /**
         * Completely removes any logical operation that may have been set on this
         * node via set_logic_op(). The geometry at this level and below will
         * subsequently be rendered using standard color blending.
         *
         * @since 1.10.0
         */
        """
        pass

    def clear_mat(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_mat(const NodePath self)
        
        /**
         * Completely removes any transform from the referenced node.
         */
        """
        pass

    def clear_material(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_material(const NodePath self)
        
        /**
         * Completely removes any material adjustment that may have been set via
         * set_material() from this particular node.
         */
        """
        pass

    def clear_model_nodes(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_model_nodes(const NodePath self)
        
        /**
         * Recursively walks through the scene graph at this level and below, looking
         * for ModelNodes, and calls model_node->set_preserve_transform(PT_drop_node)
         * on each one.  This allows a subsequent call to flatten_strong() to
         * eliminate all of the ModelNodes.
         *
         * Returns the number of ModelNodes found.
         */
        """
        pass

    def clear_occluder(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_occluder(const NodePath self)
        clear_occluder(const NodePath self, const NodePath occluder)
        
        /**
         * Completely removes any occluders that may have been set via set_occluder()
         * from this particular node.
         */
        
        /**
         * Removes any reference to the indicated occluder from the NodePath.
         */
        """
        pass

    def clear_project_texture(self, const_NodePath_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_project_texture(const NodePath self, TextureStage stage)
        
        /**
         * Undoes the effect of project_texture().
         */
        """
        pass

    def clear_python_tag(self, const_NodePath_self, object_keys): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_python_tag(const NodePath self, object keys)
        """
        pass

    def clear_render_mode(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_render_mode(const NodePath self)
        
        /**
         * Completely removes any render mode adjustment that may have been set on
         * this node via set_render_mode_wireframe() or set_render_mode_filled().
         */
        """
        pass

    def clear_scissor(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_scissor(const NodePath self)
        
        /**
         * Removes the scissor region that was defined at this node level by a
         * previous call to set_scissor().
         */
        """
        pass

    def clear_shader(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_shader(const NodePath self)
        
        /**
         *
         */
        """
        pass

    def clear_shader_input(self, const_NodePath_self, const_InternalName_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_shader_input(const NodePath self, const InternalName id)
        
        /**
         *
         */
        """
        pass

    def clear_tag(self, const_NodePath_self, str_key): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_tag(const NodePath self, str key)
        
        /**
         * Removes the value defined for this key on this particular node.  After a
         * call to clear_tag(), has_tag() will return false for the indicated key.
         */
        """
        pass

    def clear_texture(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_texture(const NodePath self)
        clear_texture(const NodePath self, TextureStage stage)
        
        /**
         * Completely removes any texture adjustment that may have been set via
         * set_texture() or set_texture_off() from this particular node.  This allows
         * whatever textures might be otherwise affecting the geometry to show
         * instead.
         */
        
        /**
         * Removes any reference to the indicated texture stage from the NodePath.
         */
        """
        pass

    def clear_tex_gen(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_tex_gen(const NodePath self)
        clear_tex_gen(const NodePath self, TextureStage stage)
        
        /**
         * Removes the texture coordinate generation mode from all texture stages on
         * this node.
         */
        
        /**
         * Disables automatic texture coordinate generation for the indicated texture
         * stage.
         */
        """
        pass

    def clear_tex_projector(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_tex_projector(const NodePath self)
        clear_tex_projector(const NodePath self, TextureStage stage)
        
        /**
         * Removes the TexProjectorEffect for the indicated stage from this node.
         */
        
        /**
         * Removes the TexProjectorEffect for all stages from this node.
         */
        """
        pass

    def clear_tex_transform(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_tex_transform(const NodePath self)
        clear_tex_transform(const NodePath self, TextureStage stage)
        
        /**
         * Removes all texture matrices from the current node.
         */
        
        /**
         * Removes the texture matrix on the current node for the given stage.
         */
        """
        pass

    def clear_transform(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_transform(const NodePath self)
        clear_transform(const NodePath self, const NodePath other, Thread current_thread)
        clear_transform(const NodePath self, Thread current_thread)
        
        /**
         * Sets the transform object on this node to identity.
         */
        
        /**
         * Sets the transform object on this node to identity, relative to the other
         * node.  This effectively places this node at the same position as the other
         * node.
         */
        """
        pass

    def clear_transparency(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_transparency(const NodePath self)
        
        /**
         * Completely removes any transparency adjustment that may have been set on
         * this node via set_transparency(). The geometry at this level and below will
         * subsequently be rendered either transparent or not, to whatever other nodes
         * may have had set_transparency() on them.
         */
        """
        pass

    def clear_two_sided(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_two_sided(const NodePath self)
        
        /**
         * Completely removes any two-sided adjustment that may have been set on this
         * node via set_two_sided(). The geometry at this level and below will
         * subsequently be rendered either two-sided or one-sided, according to
         * whatever other nodes may have had set_two_sided() on it, or according to
         * the initial state otherwise.
         */
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(NodePath self, const WeakNodePath other)
        compare_to(NodePath self, const NodePath other)
        
        /**
         * Returns a number less than zero if this NodePath sorts before the other
         * one, greater than zero if it sorts after, or zero if they are equivalent.
         *
         * Two NodePaths are considered equivalent if they consist of exactly the same
         * list of nodes in the same order.  Otherwise, they are different; different
         * NodePaths will be ranked in a consistent but undefined ordering; the
         * ordering is useful only for placing the NodePaths in a sorted container
         * like an STL set.
         */
        
        /**
         * Returns a number less than zero if this NodePath sorts before the other
         * one, greater than zero if it sorts after, or zero if they are equivalent.
         *
         * Two NodePaths are considered equivalent if they consist of exactly the same
         * list of nodes in the same order.  Otherwise, they are different; different
         * NodePaths will be ranked in a consistent but undefined ordering; the
         * ordering is useful only for placing the NodePaths in a sorted container
         * like an STL set.
         */
        """
        pass

    def compare_to(self, NodePath_self, const_WeakNodePath_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(NodePath self, const WeakNodePath other)
        compare_to(NodePath self, const NodePath other)
        
        /**
         * Returns a number less than zero if this NodePath sorts before the other
         * one, greater than zero if it sorts after, or zero if they are equivalent.
         *
         * Two NodePaths are considered equivalent if they consist of exactly the same
         * list of nodes in the same order.  Otherwise, they are different; different
         * NodePaths will be ranked in a consistent but undefined ordering; the
         * ordering is useful only for placing the NodePaths in a sorted container
         * like an STL set.
         */
        
        /**
         * Returns a number less than zero if this NodePath sorts before the other
         * one, greater than zero if it sorts after, or zero if they are equivalent.
         *
         * Two NodePaths are considered equivalent if they consist of exactly the same
         * list of nodes in the same order.  Otherwise, they are different; different
         * NodePaths will be ranked in a consistent but undefined ordering; the
         * ordering is useful only for placing the NodePaths in a sorted container
         * like an STL set.
         */
        """
        pass

    def composeColorScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compose_color_scale(const NodePath self, const LVecBase4f scale)
        compose_color_scale(const NodePath self, const LVecBase4f scale, int priority)
        compose_color_scale(const NodePath self, float sx, float sy, float sz, float sa, int priority)
        
        /**
         * Sets the color scale component of the transform
         */
        
        /**
         * multiplies the color scale component of the transform, with previous color
         * scale leaving translation and rotation untouched.
         */
        """
        pass

    def compose_color_scale(self, const_NodePath_self, const_LVecBase4f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compose_color_scale(const NodePath self, const LVecBase4f scale)
        compose_color_scale(const NodePath self, const LVecBase4f scale, int priority)
        compose_color_scale(const NodePath self, float sx, float sy, float sz, float sa, int priority)
        
        /**
         * Sets the color scale component of the transform
         */
        
        /**
         * multiplies the color scale component of the transform, with previous color
         * scale leaving translation and rotation untouched.
         */
        """
        pass

    def copyTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_to(NodePath self, const NodePath other, int sort, Thread current_thread)
        
        /**
         * Functions like instance_to(), except a deep copy is made of the referenced
         * node and all of its descendents, which is then parented to the indicated
         * node.  A NodePath to the newly created copy is returned.
         */
        """
        pass

    def copy_to(self, NodePath_self, const_NodePath_other, int_sort, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_to(NodePath self, const NodePath other, int sort, Thread current_thread)
        
        /**
         * Functions like instance_to(), except a deep copy is made of the referenced
         * node and all of its descendents, which is then parented to the indicated
         * node.  A NodePath to the newly created copy is returned.
         */
        """
        pass

    def countNumDescendants(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        count_num_descendants(NodePath self)
        
        /**
         * Returns the number of nodes at and below this level.
         */
        """
        pass

    def count_num_descendants(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        count_num_descendants(NodePath self)
        
        /**
         * Returns the number of nodes at and below this level.
         */
        """
        pass

    def decodeFromBamStream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        decode_from_bam_stream(bytes data, BamReader reader)
        
        /**
         * Reads the string created by a previous call to encode_to_bam_stream(), and
         * extracts and returns the NodePath on that string.  Returns NULL on error.
         */
        """
        pass

    def decode_from_bam_stream(self, bytes_data, BamReader_reader): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        decode_from_bam_stream(bytes data, BamReader reader)
        
        /**
         * Reads the string created by a previous call to encode_to_bam_stream(), and
         * extracts and returns the NodePath on that string.  Returns NULL on error.
         */
        """
        pass

    def detachNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        detach_node(const NodePath self, Thread current_thread)
        
        /**
         * Disconnects the referenced node from its parent, but does not immediately
         * delete it.  The NodePath retains a pointer to the node, and becomes a
         * singleton NodePath.
         *
         * This should be called to detach a node from the scene graph, with the
         * option of reattaching it later to the same parent or to a different parent.
         *
         * In practice, the only difference between remove_node() and detach_node() is
         * that remove_node() also resets the NodePath to empty, which will cause the
         * node to be deleted immediately if there are no other references.  On the
         * other hand, detach_node() leaves the NodePath referencing the node, which
         * will keep at least one reference to the node for as long as the NodePath
         * exists.
         */
        """
        pass

    def detach_node(self, const_NodePath_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        detach_node(const NodePath self, Thread current_thread)
        
        /**
         * Disconnects the referenced node from its parent, but does not immediately
         * delete it.  The NodePath retains a pointer to the node, and becomes a
         * singleton NodePath.
         *
         * This should be called to detach a node from the scene graph, with the
         * option of reattaching it later to the same parent or to a different parent.
         *
         * In practice, the only difference between remove_node() and detach_node() is
         * that remove_node() also resets the NodePath to empty, which will cause the
         * node to be deleted immediately if there are no other references.  On the
         * other hand, detach_node() leaves the NodePath referencing the node, which
         * will keep at least one reference to the node for as long as the NodePath
         * exists.
         */
        """
        pass

    def doBillboardAxis(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        do_billboard_axis(const NodePath self, const NodePath camera, float offset)
        
        /**
         * Performs a billboard-type rotate to the indicated camera node, one time
         * only, and leaves the object rotated.  This is similar in principle to
         * heads_up().
         */
        """
        pass

    def doBillboardPointEye(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        do_billboard_point_eye(const NodePath self, const NodePath camera, float offset)
        
        /**
         * Performs a billboard-type rotate to the indicated camera node, one time
         * only, and leaves the object rotated.  This is similar in principle to
         * look_at(), although the point_eye billboard effect cannot be achieved using
         * the ordinary look_at() call.
         */
        """
        pass

    def doBillboardPointWorld(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        do_billboard_point_world(const NodePath self, const NodePath camera, float offset)
        
        /**
         * Performs a billboard-type rotate to the indicated camera node, one time
         * only, and leaves the object rotated.  This is similar in principle to
         * look_at().
         */
        """
        pass

    def do_billboard_axis(self, const_NodePath_self, const_NodePath_camera, float_offset): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        do_billboard_axis(const NodePath self, const NodePath camera, float offset)
        
        /**
         * Performs a billboard-type rotate to the indicated camera node, one time
         * only, and leaves the object rotated.  This is similar in principle to
         * heads_up().
         */
        """
        pass

    def do_billboard_point_eye(self, const_NodePath_self, const_NodePath_camera, float_offset): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        do_billboard_point_eye(const NodePath self, const NodePath camera, float offset)
        
        /**
         * Performs a billboard-type rotate to the indicated camera node, one time
         * only, and leaves the object rotated.  This is similar in principle to
         * look_at(), although the point_eye billboard effect cannot be achieved using
         * the ordinary look_at() call.
         */
        """
        pass

    def do_billboard_point_world(self, const_NodePath_self, const_NodePath_camera, float_offset): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        do_billboard_point_world(const NodePath self, const NodePath camera, float offset)
        
        /**
         * Performs a billboard-type rotate to the indicated camera node, one time
         * only, and leaves the object rotated.  This is similar in principle to
         * look_at().
         */
        """
        pass

    def encodeToBamStream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        encode_to_bam_stream(NodePath self)
        
        /**
         * Converts the NodePath object into a single stream of data using a
         * BamWriter, and returns that data as a string string.  Returns empty string
         * on failure.  This is similar to write_bam_stream().
         *
         * This method is used by __reduce__ to handle streaming of NodePaths to a
         * pickle file.
         */
        
        /**
         * Converts the NodePath object into a single stream of data using a
         * BamWriter, and stores that data in the indicated string.  Returns true on
         * success, false on failure.
         *
         * If the BamWriter is NULL, this behaves the same way as
         * NodePath::write_bam_stream() and PandaNode::encode_to_bam_stream(), in the
         * sense that it only writes this node and all nodes below it.
         *
         * However, if the BamWriter is not NULL, it behaves very differently.  In
         * this case, it encodes the *entire graph* of all nodes connected to the
         * NodePath, including all parent nodes and siblings.  This is necessary for
         * correct streaming of related NodePaths and restoration of instances, etc.,
         * but it does mean you must detach() a node before writing it if you want to
         * limit the nodes that get written.
         *
         * This method is used by __reduce__ to handle streaming of NodePaths to a
         * pickle file.  The BamWriter case is used by the direct.stdpy.pickle module,
         * while the saner, non-BamWriter case is used when the standard pickle module
         * calls this function.
         */
        """
        pass

    def encode_to_bam_stream(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        encode_to_bam_stream(NodePath self)
        
        /**
         * Converts the NodePath object into a single stream of data using a
         * BamWriter, and returns that data as a string string.  Returns empty string
         * on failure.  This is similar to write_bam_stream().
         *
         * This method is used by __reduce__ to handle streaming of NodePaths to a
         * pickle file.
         */
        
        /**
         * Converts the NodePath object into a single stream of data using a
         * BamWriter, and stores that data in the indicated string.  Returns true on
         * success, false on failure.
         *
         * If the BamWriter is NULL, this behaves the same way as
         * NodePath::write_bam_stream() and PandaNode::encode_to_bam_stream(), in the
         * sense that it only writes this node and all nodes below it.
         *
         * However, if the BamWriter is not NULL, it behaves very differently.  In
         * this case, it encodes the *entire graph* of all nodes connected to the
         * NodePath, including all parent nodes and siblings.  This is necessary for
         * correct streaming of related NodePaths and restoration of instances, etc.,
         * but it does mean you must detach() a node before writing it if you want to
         * limit the nodes that get written.
         *
         * This method is used by __reduce__ to handle streaming of NodePaths to a
         * pickle file.  The BamWriter case is used by the direct.stdpy.pickle module,
         * while the saner, non-BamWriter case is used when the standard pickle module
         * calls this function.
         */
        """
        pass

    def fail(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fail()
        
        /**
         * Creates a NodePath with the ET_fail error type set.
         */
        """
        pass

    def find(self, NodePath_self, str_path): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find(NodePath self, str path)
        
        /**
         * Searches for a node below the referenced node that matches the indicated
         * string.  Returns the shortest match found, if any, or an empty NodePath if
         * no match can be found.
         *
         * The referenced node itself is not considered in the search.
         */
        """
        pass

    def findAllMatches(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_all_matches(NodePath self, str path)
        
        /**
         * Returns the complete set of all NodePaths that begin with this NodePath and
         * can be extended by path.  The shortest paths will be listed first.
         *
         * The referenced node itself is not considered in the search.
         */
        """
        pass

    def findAllMaterials(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_all_materials(NodePath self)
        find_all_materials(NodePath self, str name)
        
        /**
         * Returns a list of a materials applied to geometry at this node and below.
         */
        
        /**
         * Returns a list of a materials applied to geometry at this node and below
         * that match the indicated name (which may contain wildcard characters).
         */
        """
        pass

    def findAllPathsTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_all_paths_to(NodePath self, PandaNode node)
        
        /**
         * Returns the set of all NodePaths that extend from this NodePath down to the
         * indicated node.  The shortest paths will be listed first.
         */
        """
        pass

    def findAllTexcoords(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_all_texcoords(NodePath self)
        find_all_texcoords(NodePath self, str name)
        
        /**
         * Returns a list of all texture coordinate sets used by any geometry at this
         * node level and below.
         */
        
        /**
         * Returns a list of all texture coordinate sets used by any geometry at this
         * node level and below that match the indicated name (which may contain
         * wildcard characters).
         */
        """
        pass

    def findAllTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_all_textures(NodePath self)
        find_all_textures(NodePath self, TextureStage stage)
        find_all_textures(NodePath self, str name)
        
        /**
         * Returns a list of a textures applied to geometry at this node and below.
         */
        
        /**
         * Returns a list of a textures applied to geometry at this node and below
         * that match the indicated name (which may contain wildcard characters).
         */
        
        /**
         * Returns a list of a textures on geometry at this node and below that are
         * assigned to the indicated texture stage.
         */
        """
        pass

    def findAllTextureStages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_all_texture_stages(NodePath self)
        find_all_texture_stages(NodePath self, str name)
        
        /**
         * Returns a list of a TextureStages applied to geometry at this node and
         * below.
         */
        
        /**
         * Returns a list of a TextureStages applied to geometry at this node and
         * below that match the indicated name (which may contain wildcard
         * characters).
         */
        """
        pass

    def findAllVertexColumns(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_all_vertex_columns(NodePath self)
        find_all_vertex_columns(NodePath self, str name)
        
        /**
         * Returns a list of all vertex array columns stored on some geometry found at
         * this node level and below.
         */
        
        /**
         * Returns a list of all vertex array columns stored on some geometry found at
         * this node level and below that match the indicated name (which may contain
         * wildcard characters).
         */
        """
        pass

    def findMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_material(NodePath self, str name)
        
        /**
         * Returns the first material found applied to geometry at this node or below
         * that matches the indicated name (which may contain wildcards).  Returns the
         * material if it is found, or NULL if it is not.
         */
        """
        pass

    def findNetPythonTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_net_python_tag(NodePath self, object keys)
        """
        pass

    def findNetTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_net_tag(NodePath self, str key)
        
        /**
         * Returns the lowest ancestor of this node that contains a tag definition
         * with the indicated key, if any, or an empty NodePath if no ancestor of this
         * node contains this tag definition.  See set_tag().
         */
        """
        pass

    def findPathTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_path_to(NodePath self, PandaNode node)
        
        /**
         * Searches for the indicated node below this node and returns the shortest
         * NodePath that connects them.
         */
        """
        pass

    def findTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_texture(NodePath self, TextureStage stage)
        find_texture(NodePath self, str name)
        
        /**
         * Returns the first texture found applied to geometry at this node or below
         * that matches the indicated name (which may contain wildcards).  Returns the
         * texture if it is found, or NULL if it is not.
         */
        
        /**
         * Returns the first texture found applied to geometry at this node or below
         * that is assigned to the indicated texture stage.  Returns the texture if it
         * is found, or NULL if it is not.
         */
        """
        pass

    def findTextureStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_texture_stage(NodePath self, str name)
        
        /**
         * Returns the first TextureStage found applied to geometry at this node or
         * below that matches the indicated name (which may contain wildcards).
         * Returns the TextureStage if it is found, or NULL if it is not.
         */
        """
        pass

    def find_all_matches(self, NodePath_self, str_path): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_all_matches(NodePath self, str path)
        
        /**
         * Returns the complete set of all NodePaths that begin with this NodePath and
         * can be extended by path.  The shortest paths will be listed first.
         *
         * The referenced node itself is not considered in the search.
         */
        """
        pass

    def find_all_materials(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_all_materials(NodePath self)
        find_all_materials(NodePath self, str name)
        
        /**
         * Returns a list of a materials applied to geometry at this node and below.
         */
        
        /**
         * Returns a list of a materials applied to geometry at this node and below
         * that match the indicated name (which may contain wildcard characters).
         */
        """
        pass

    def find_all_paths_to(self, NodePath_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_all_paths_to(NodePath self, PandaNode node)
        
        /**
         * Returns the set of all NodePaths that extend from this NodePath down to the
         * indicated node.  The shortest paths will be listed first.
         */
        """
        pass

    def find_all_texcoords(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_all_texcoords(NodePath self)
        find_all_texcoords(NodePath self, str name)
        
        /**
         * Returns a list of all texture coordinate sets used by any geometry at this
         * node level and below.
         */
        
        /**
         * Returns a list of all texture coordinate sets used by any geometry at this
         * node level and below that match the indicated name (which may contain
         * wildcard characters).
         */
        """
        pass

    def find_all_textures(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_all_textures(NodePath self)
        find_all_textures(NodePath self, TextureStage stage)
        find_all_textures(NodePath self, str name)
        
        /**
         * Returns a list of a textures applied to geometry at this node and below.
         */
        
        /**
         * Returns a list of a textures applied to geometry at this node and below
         * that match the indicated name (which may contain wildcard characters).
         */
        
        /**
         * Returns a list of a textures on geometry at this node and below that are
         * assigned to the indicated texture stage.
         */
        """
        pass

    def find_all_texture_stages(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_all_texture_stages(NodePath self)
        find_all_texture_stages(NodePath self, str name)
        
        /**
         * Returns a list of a TextureStages applied to geometry at this node and
         * below.
         */
        
        /**
         * Returns a list of a TextureStages applied to geometry at this node and
         * below that match the indicated name (which may contain wildcard
         * characters).
         */
        """
        pass

    def find_all_vertex_columns(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_all_vertex_columns(NodePath self)
        find_all_vertex_columns(NodePath self, str name)
        
        /**
         * Returns a list of all vertex array columns stored on some geometry found at
         * this node level and below.
         */
        
        /**
         * Returns a list of all vertex array columns stored on some geometry found at
         * this node level and below that match the indicated name (which may contain
         * wildcard characters).
         */
        """
        pass

    def find_material(self, NodePath_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_material(NodePath self, str name)
        
        /**
         * Returns the first material found applied to geometry at this node or below
         * that matches the indicated name (which may contain wildcards).  Returns the
         * material if it is found, or NULL if it is not.
         */
        """
        pass

    def find_net_python_tag(self, NodePath_self, object_keys): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_net_python_tag(NodePath self, object keys)
        """
        pass

    def find_net_tag(self, NodePath_self, str_key): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_net_tag(NodePath self, str key)
        
        /**
         * Returns the lowest ancestor of this node that contains a tag definition
         * with the indicated key, if any, or an empty NodePath if no ancestor of this
         * node contains this tag definition.  See set_tag().
         */
        """
        pass

    def find_path_to(self, NodePath_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_path_to(NodePath self, PandaNode node)
        
        /**
         * Searches for the indicated node below this node and returns the shortest
         * NodePath that connects them.
         */
        """
        pass

    def find_texture(self, NodePath_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_texture(NodePath self, TextureStage stage)
        find_texture(NodePath self, str name)
        
        /**
         * Returns the first texture found applied to geometry at this node or below
         * that matches the indicated name (which may contain wildcards).  Returns the
         * texture if it is found, or NULL if it is not.
         */
        
        /**
         * Returns the first texture found applied to geometry at this node or below
         * that is assigned to the indicated texture stage.  Returns the texture if it
         * is found, or NULL if it is not.
         */
        """
        pass

    def find_texture_stage(self, NodePath_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_texture_stage(NodePath self, str name)
        
        /**
         * Returns the first TextureStage found applied to geometry at this node or
         * below that matches the indicated name (which may contain wildcards).
         * Returns the TextureStage if it is found, or NULL if it is not.
         */
        """
        pass

    def flattenLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        flatten_light(const NodePath self)
        
        /**
         * Lightly flattens out the hierarchy below this node by applying transforms,
         * colors, and texture matrices from the nodes onto the vertices, but does not
         * remove any nodes.
         *
         * This can result in improved rendering performance because there will be
         * fewer transforms in the resulting scene graph, but the number of nodes will
         * remain the same.
         *
         * In particular, any NodePaths that reference nodes within this hierarchy
         * will not be damaged.  However, since this operation will remove transforms
         * from the scene graph, it may be dangerous to apply to nodes where you
         * expect to dynamically modify the transform, or where you expect the
         * geometry to remain in a particular local coordinate system.
         *
         * The return value is always 0, since flatten_light does not remove any
         * nodes.
         */
        """
        pass

    def flattenMedium(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        flatten_medium(const NodePath self)
        
        /**
         * A more thorough flattening than flatten_light(), this first applies all the
         * transforms, colors, and texture matrices from the nodes onto the vertices,
         * and then removes unneeded grouping nodes--nodes that have exactly one
         * child, for instance, but have no special properties in themselves.
         *
         * This results in improved performance over flatten_light() because the
         * number of nodes in the scene graph is reduced.
         *
         * The return value is the number of nodes removed.
         */
        """
        pass

    def flattenStrong(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        flatten_strong(const NodePath self)
        
        /**
         * The strongest possible flattening.  This first applies all of the
         * transforms to the vertices, as in flatten_medium(), but then it will
         * combine sibling nodes together when possible, in addition to removing
         * unnecessary parent-child nodes.  This can result in substantially fewer
         * nodes, but any nicely-grouped hierachical bounding volumes may be lost.
         *
         * It is generally a good idea to apply this kind of flattening only to nodes
         * that will be culled largely as a single unit, like a car.  Applying this to
         * an entire scene may result in overall poorer performance because of less-
         * effective culling.
         */
        """
        pass

    def flatten_light(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flatten_light(const NodePath self)
        
        /**
         * Lightly flattens out the hierarchy below this node by applying transforms,
         * colors, and texture matrices from the nodes onto the vertices, but does not
         * remove any nodes.
         *
         * This can result in improved rendering performance because there will be
         * fewer transforms in the resulting scene graph, but the number of nodes will
         * remain the same.
         *
         * In particular, any NodePaths that reference nodes within this hierarchy
         * will not be damaged.  However, since this operation will remove transforms
         * from the scene graph, it may be dangerous to apply to nodes where you
         * expect to dynamically modify the transform, or where you expect the
         * geometry to remain in a particular local coordinate system.
         *
         * The return value is always 0, since flatten_light does not remove any
         * nodes.
         */
        """
        pass

    def flatten_medium(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flatten_medium(const NodePath self)
        
        /**
         * A more thorough flattening than flatten_light(), this first applies all the
         * transforms, colors, and texture matrices from the nodes onto the vertices,
         * and then removes unneeded grouping nodes--nodes that have exactly one
         * child, for instance, but have no special properties in themselves.
         *
         * This results in improved performance over flatten_light() because the
         * number of nodes in the scene graph is reduced.
         *
         * The return value is the number of nodes removed.
         */
        """
        pass

    def flatten_strong(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flatten_strong(const NodePath self)
        
        /**
         * The strongest possible flattening.  This first applies all of the
         * transforms to the vertices, as in flatten_medium(), but then it will
         * combine sibling nodes together when possible, in addition to removing
         * unnecessary parent-child nodes.  This can result in substantially fewer
         * nodes, but any nicely-grouped hierachical bounding volumes may be lost.
         *
         * It is generally a good idea to apply this kind of flattening only to nodes
         * that will be culled largely as a single unit, like a car.  Applying this to
         * an entire scene may result in overall poorer performance because of less-
         * effective culling.
         */
        """
        pass

    def forceRecomputeBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        force_recompute_bounds(const NodePath self)
        
        /**
         * Forces the recomputing of all the bounding volumes at every node in the
         * subgraph beginning at this node and below.
         *
         * This should not normally need to be called, since the bounding volumes are
         * supposed to be recomputed automatically when necessary.  It may be useful
         * when debugging, to verify that the bounding volumes have not become
         * inadvertently stale; it may also be useful to force animated characters to
         * update their bounding volumes (which does not presently happen
         * automatically).
         */
        """
        pass

    def force_recompute_bounds(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        force_recompute_bounds(const NodePath self)
        
        /**
         * Forces the recomputing of all the bounding volumes at every node in the
         * subgraph beginning at this node and below.
         *
         * This should not normally need to be called, since the bounding volumes are
         * supposed to be recomputed automatically when necessary.  It may be useful
         * when debugging, to verify that the bounding volumes have not become
         * inadvertently stale; it may also be useful to force animated characters to
         * update their bounding volumes (which does not presently happen
         * automatically).
         */
        """
        pass

    def getAncestor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ancestor(NodePath self, int index, Thread current_thread)
        
        /**
         * Returns the nth ancestor of the path, where 0 is the NodePath itself and
         * get_num_nodes() - 1 is get_top(). This requires iterating through the path.
         *
         * Also see get_node(), which returns the same thing as a PandaNode pointer,
         * not a NodePath.
         */
        """
        pass

    def getAncestors(self, *args, **kwargs): # real signature unknown
        pass

    def getAntialias(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_antialias(NodePath self)
        
        /**
         * Returns the antialias setting that has been specifically set on this node
         * via set_antialias(), or M_none if no setting has been made.
         */
        """
        pass

    def getAttrib(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_attrib(NodePath self, TypeHandle type)
        
        /**
         * Returns the render attribute of the indicated type, if it is defined on the
         * node, or NULL if it is not.  This checks only what is set on this
         * particular node level, and has nothing to do with what render attributes
         * may be inherited from parent nodes.
         */
        """
        pass

    def getAudioVolume(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_audio_volume(NodePath self)
        
        /**
         * Returns the complete audio volume that has been applied to this node via a
         * previous call to set_audio_volume(), or 1. (identity) if no volume has been
         * applied to this particular node.
         */
        """
        pass

    def getBinDrawOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bin_draw_order(NodePath self)
        
        /**
         * Returns the drawing order associated with the bin that this particular node
         * was assigned to via set_bin(), or 0 if no bin was assigned.  See set_bin()
         * and has_bin().
         */
        """
        pass

    def getBinName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bin_name(NodePath self)
        
        /**
         * Returns the name of the bin that this particular node was assigned to via
         * set_bin(), or the empty string if no bin was assigned.  See set_bin() and
         * has_bin().
         */
        """
        pass

    def getBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bounds(NodePath self, Thread current_thread)
        
        /**
         * Returns a newly-allocated bounding volume containing the bottom node and
         * all of its descendants.  This is the bounding volume on the bottom arc,
         * converted to the local coordinate space of the node.
         */
        """
        pass

    def getChild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_child(NodePath self, int n, Thread current_thread)
        
        /**
         * Returns a NodePath representing the nth child of the referenced node.
         */
        """
        pass

    def getChildren(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_children(NodePath self, Thread current_thread)
        
        /**
         * Returns the set of all child nodes of the referenced node.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collide_mask(NodePath self)
        
        /**
         * Returns the union of all of the into_collide_masks for nodes at this level
         * and below.  This is the same thing as node()->get_net_collide_mask().
         *
         * If you want to return what the into_collide_mask of this node itself is,
         * without regard to its children, use node()->get_into_collide_mask().
         */
        """
        pass

    def getColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_color(NodePath self)
        
        /**
         * Returns the color that has been assigned to the node, or black if no color
         * has been assigned.
         */
        """
        pass

    def getColorScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_color_scale(NodePath self)
        
        /**
         * Returns the complete color scale vector that has been applied to this node
         * via a previous call to set_color_scale() and/or set_alpha_scale(), or all
         * 1's (identity) if no scale has been applied to this particular node.
         */
        """
        pass

    def getCommonAncestor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_common_ancestor(NodePath self, const NodePath other, Thread current_thread)
        
        /**
         * Returns the lowest NodePath that both of these two NodePaths have in
         * common: the first ancestor that both of them share.  If the two NodePaths
         * are unrelated, returns NodePath::not_found().
         */
        """
        pass

    def getDepthOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_depth_offset(NodePath self)
        
        /**
         * Returns the depth offset value if it has been specified using
         * set_depth_offset, or 0 if not.
         */
        """
        pass

    def getDepthTest(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_depth_test(NodePath self)
        
        /**
         * Returns true if depth-test rendering has been specifically set on this node
         * via set_depth_test(), or false if depth-test rendering has been
         * specifically disabled.  If nothing has been specifically set, returns true.
         * See also has_depth_test().
         */
        """
        pass

    def getDepthWrite(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_depth_write(NodePath self)
        
        /**
         * Returns true if depth-write rendering has been specifically set on this
         * node via set_depth_write(), or false if depth-write rendering has been
         * specifically disabled.  If nothing has been specifically set, returns true.
         * See also has_depth_write().
         */
        """
        pass

    def getDistance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_distance(NodePath self, const NodePath other)
        
        /**
         * Returns the straight-line distance between this referenced node's
         * coordinate frame's origin, and that of the other node's origin.
         */
        """
        pass

    def getEffect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_effect(NodePath self, TypeHandle type)
        
        /**
         * Returns the render effect of the indicated type, if it is defined on the
         * node, or NULL if it is not.
         */
        """
        pass

    def getEffects(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_effects(NodePath self)
        
        /**
         * Returns the complete RenderEffects that will be applied to this node.
         */
        """
        pass

    def getErrorType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_error_type(NodePath self)
        
        /**
         * If is_empty() is true, this returns a code that represents the reason why
         * the NodePath is empty.
         */
        """
        pass

    def getFog(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fog(NodePath self)
        
        /**
         * Returns the fog that has been set on this particular node, or NULL if no
         * fog has been set.  This is not necessarily the fog that will be applied to
         * the geometry at or below this level, as another fog at a higher or lower
         * level may override.
         */
        """
        pass

    def getH(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_h(NodePath self)
        get_h(NodePath self, const NodePath other)
        """
        pass

    def getHiddenAncestor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hidden_ancestor(NodePath self, BitMask camera_mask, Thread current_thread)
        
        /**
         * Returns the NodePath at or above the referenced node that is hidden to the
         * indicated camera(s), or an empty NodePath if no ancestor of the referenced
         * node is hidden (and the node should be visible).
         */
        """
        pass

    def getHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hpr(NodePath self)
        get_hpr(NodePath self, const NodePath other)
        
        /**
         * Retrieves the rotation component of the transform.
         */
        
        /**
         * Returns the relative orientation of the bottom node as seen from the other
         * node.
         */
        """
        pass

    def getInstanceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_instance_count(NodePath self)
        
        /**
         * Returns the geometry instance count, or 0 if disabled.  See
         * set_instance_count.
         */
        """
        pass

    def getKey(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_key(NodePath self)
        
        /**
         * Returns an integer that is guaranteed to be the same for all NodePaths that
         * represent the same node instance, and different for all NodePaths that
         * represent a different node instance.
         *
         * The same key will be returned for a particular instance as long as at least
         * one NodePath exists that represents that instance; if all NodePaths for a
         * particular instance destruct and a new one is later created, it may have a
         * different index.  However, a given key will never be reused for a different
         * instance (unless the app has been running long enough that we overflow the
         * integer key value).
         */
        """
        pass

    def getLogicOp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_logic_op(NodePath self)
        
        /**
         * Returns the logical operation that has been specifically set on this node
         * via set_logic_op(), or O_none if standard color blending has been
         * specifically set, or if nothing has been specifically set.  See also
         * has_logic_op().  This does not necessarily imply that the geometry will
         * or will not be rendered with the given logical operation, as there may be
         * other nodes that override.
         *
         * @since 1.10.0
         */
        """
        pass

    def getMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mat(NodePath self)
        get_mat(NodePath self, const NodePath other)
        
        /**
         * Returns the transform matrix that has been applied to the referenced node,
         * or the identity matrix if no matrix has been applied.
         */
        
        /**
         * Returns the matrix that describes the coordinate space of the bottom node,
         * relative to the other path's bottom node's coordinate space.
         */
        """
        pass

    def getMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_material(NodePath self)
        
        /**
         * Returns the material that has been set on this particular node, or NULL if
         * no material has been set.  This is not necessarily the material that will
         * be applied to the geometry at or below this level, as another material at a
         * higher or lower level may override.
         *
         * See also find_material().
         */
        """
        pass

    def getMaxSearchDepth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_search_depth()
        
        /**
         * Returns the current setting of the search depth limit.  See
         * set_max_search_depth.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(NodePath self)
        
        /**
         * Returns the name of the referenced node.
         */
        """
        pass

    def getNetAudioVolume(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_net_audio_volume(NodePath self)
        
        /**
         * Returns the complete audio volume for this node taking highers nodes in the
         * graph into account.
         */
        """
        pass

    def getNetPrevTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_net_prev_transform(NodePath self, Thread current_thread)
        
        /**
         * Returns the net "previous" transform on this node from the root.  See
         * set_prev_transform().
         */
        """
        pass

    def getNetPythonTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_net_python_tag(NodePath self, object keys)
        """
        pass

    def getNetState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_net_state(NodePath self, Thread current_thread)
        
        /**
         * Returns the net state on this node from the root.
         */
        """
        pass

    def getNetTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_net_tag(NodePath self, str key)
        
        /**
         * Returns the tag value that has been defined on this node, or the nearest
         * ancestor node, for the indicated key.  If no value has been defined for the
         * indicated key on any ancestor node, returns the empty string.  See also
         * get_tag().
         */
        """
        pass

    def getNetTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_net_transform(NodePath self, Thread current_thread)
        
        /**
         * Returns the net transform on this node from the root.
         */
        """
        pass

    def getNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node(NodePath self, int index, Thread current_thread)
        
        /**
         * Returns the nth node of the path, where 0 is the referenced (bottom) node
         * and get_num_nodes() - 1 is the top node.  This requires iterating through
         * the path.
         *
         * Also see node(), which is a convenience function to return the same thing
         * as get_node(0) (since the bottom node is the most important node in the
         * NodePath, and is the one most frequently referenced).
         *
         * Note that this function returns the same thing as
         * get_ancestor(index).node().
         */
        """
        pass

    def getNodes(self, *args, **kwargs): # real signature unknown
        pass

    def getNumChildren(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_children(NodePath self, Thread current_thread)
        
        /**
         * Returns the number of children of the referenced node.
         */
        """
        pass

    def getNumNodes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_nodes(NodePath self, Thread current_thread)
        
        /**
         * Returns the number of nodes in the path.
         */
        """
        pass

    def getP(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_p(NodePath self)
        get_p(NodePath self, const NodePath other)
        """
        pass

    def getParent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_parent(NodePath self, Thread current_thread)
        
        /**
         * Returns the NodePath to the parent of the referenced node: that is, this
         * NodePath, shortened by one node.  The parent of a singleton NodePath is
         * defined to be the empty NodePath.
         */
        """
        pass

    def getPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pos(NodePath self)
        get_pos(NodePath self, const NodePath other)
        
        /**
         * Retrieves the translation component of the transform.
         */
        
        /**
         * Returns the relative position of the referenced node as seen from the other
         * node.
         */
        """
        pass

    def getPosDelta(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pos_delta(NodePath self)
        get_pos_delta(NodePath self, const NodePath other)
        
        /**
         * Returns the delta vector from this node's position in the previous frame
         * (according to set_prev_transform(), typically set via the use of
         * set_fluid_pos()) and its position in the current frame.  This is the vector
         * used to determine collisions.  Generally, if the node was last repositioned
         * via set_pos(), the delta will be zero; if it was adjusted via
         * set_fluid_pos(), the delta will represent the change from the previous
         * frame's position.
         */
        
        /**
         * Returns the delta vector from this node's position in the previous frame
         * (according to set_prev_transform(), typically set via the use of
         * set_fluid_pos()) and its position in the current frame, as seen in the
         * indicated node's coordinate space.  This is the vector used to determine
         * collisions.  Generally, if the node was last repositioned via set_pos(),
         * the delta will be zero; if it was adjusted via set_fluid_pos(), the delta
         * will represent the change from the previous frame's position.
         */
        """
        pass

    def getPrevTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_prev_transform(NodePath self)
        get_prev_transform(NodePath self, const NodePath other, Thread current_thread)
        get_prev_transform(NodePath self, Thread current_thread)
        
        /**
         * Returns the transform that has been set as this node's "previous" position.
         * See set_prev_transform().
         */
        
        /**
         * Returns the relative "previous" transform to this node from the other node;
         * i.e.  the position of this node in the previous frame, as seen by the other
         * node in the previous frame.
         */
        """
        pass

    def getPythonTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_python_tag(NodePath self, object keys)
        """
        pass

    def getPythonTagKeys(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_python_tag_keys(NodePath self)
        """
        pass

    def getPythonTags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_python_tags(const NodePath self)
        """
        pass

    def getQuat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_quat(NodePath self)
        get_quat(NodePath self, const NodePath other)
        
        /**
         * Retrieves the rotation component of the transform.
         */
        
        /**
         * Returns the relative orientation of the bottom node as seen from the other
         * node.
         */
        """
        pass

    def getR(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_r(NodePath self)
        get_r(NodePath self, const NodePath other)
        """
        pass

    def getRelativePoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_relative_point(NodePath self, const NodePath other, const LVecBase3f point)
        
        /**
         * Given that the indicated point is in the coordinate system of the other
         * node, returns the same point in this node's coordinate system.
         */
        """
        pass

    def getRelativeVector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_relative_vector(NodePath self, const NodePath other, const LVecBase3f vec)
        
        /**
         * Given that the indicated vector is in the coordinate system of the other
         * node, returns the same vector in this node's coordinate system.
         */
        """
        pass

    def getRenderMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_render_mode(NodePath self)
        
        /**
         * Returns the render mode that has been specifically set on this node via
         * set_render_mode(), or M_unchanged if nothing has been set.
         */
        """
        pass

    def getRenderModePerspective(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_render_mode_perspective(NodePath self)
        
        /**
         * Returns the flag that has been set on this node via
         * set_render_mode_perspective(), or false if no flag has been set.
         */
        """
        pass

    def getRenderModeThickness(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_render_mode_thickness(NodePath self)
        
        /**
         * Returns the render mode thickness that has been specifically set on this
         * node via set_render_mode(), or 1.0 if nothing has been set.
         */
        """
        pass

    def getSa(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sa(NodePath self)
        
        /**
         * Gets the alpha component of the color scale.
         * @see get_color_scale()
         */
        """
        pass

    def getSb(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sb(NodePath self)
        
        /**
         * Gets the blue component of the color scale.
         * @see get_color_scale()
         */
        """
        pass

    def getScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scale(NodePath self)
        get_scale(NodePath self, const NodePath other)
        
        /**
         * Retrieves the scale component of the transform.
         */
        
        /**
         * Returns the relative scale of the bottom node as seen from the other node.
         */
        """
        pass

    def getSg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sg(NodePath self)
        
        /**
         * Gets the green component of the color scale.
         * @see get_color_scale()
         */
        """
        pass

    def getShader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shader(NodePath self)
        
        /**
         *
         */
        """
        pass

    def getShaderInput(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shader_input(NodePath self, const InternalName id)
        
        /**
         *
         */
        """
        pass

    def getShear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shear(NodePath self)
        get_shear(NodePath self, const NodePath other)
        
        /**
         * Retrieves the shear component of the transform.
         */
        
        /**
         * Returns the relative shear of the bottom node as seen from the other node.
         */
        """
        pass

    def getShxy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shxy(NodePath self)
        get_shxy(NodePath self, const NodePath other)
        
        /**
         * Returns the relative shear of the referenced node as seen from the other
         * node.
         */
        """
        pass

    def getShxz(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shxz(NodePath self)
        get_shxz(NodePath self, const NodePath other)
        """
        pass

    def getShyz(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shyz(NodePath self)
        get_shyz(NodePath self, const NodePath other)
        """
        pass

    def getSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sort(NodePath self, Thread current_thread)
        
        /**
         * Returns the sort value of the referenced node within its parent; that is,
         * the sort number passed on the last reparenting operation for this node.
         * This will control the position of the node within its parent's list of
         * children.
         */
        """
        pass

    def getSr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sr(NodePath self)
        
        /**
         * Gets the red component of the color scale.
         * @see get_color_scale()
         */
        """
        pass

    def getStashedAncestor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_stashed_ancestor(NodePath self, Thread current_thread)
        
        /**
         * Returns the NodePath at or above the referenced node that is stashed, or an
         * empty NodePath if no ancestor of the referenced node is stashed (and the
         * node should be visible).
         */
        """
        pass

    def getStashedChildren(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_stashed_children(NodePath self, Thread current_thread)
        
        /**
         * Returns the set of all child nodes of the referenced node that have been
         * stashed.  These children are not normally visible on the node, and do not
         * appear in the list returned by get_children().
         */
        """
        pass

    def getState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_state(NodePath self)
        get_state(NodePath self, const NodePath other, Thread current_thread)
        get_state(NodePath self, Thread current_thread)
        
        // Aggregate transform and state information.
        
        /**
         * Returns the complete state object set on this node.
         */
        
        /**
         * Returns the state changes that must be made to transition to the render
         * state of this node from the render state of the other node.
         */
        """
        pass

    def getSx(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sx(NodePath self)
        get_sx(NodePath self, const NodePath other)
        
        /**
         * Returns the relative scale of the referenced node as seen from the other
         * node.
         */
        """
        pass

    def getSy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sy(NodePath self)
        get_sy(NodePath self, const NodePath other)
        """
        pass

    def getSz(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sz(NodePath self)
        get_sz(NodePath self, const NodePath other)
        """
        pass

    def getTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tag(NodePath self, str key)
        
        /**
         * Retrieves the user-defined value that was previously set on this node for
         * the particular key, if any.  If no value has been previously set, returns
         * the empty string.  See also get_net_tag().
         */
        """
        pass

    def getTagKeys(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tag_keys(NodePath self)
        
        /**
         * Fills the given vector up with the list of tags on this PandaNode.
         *
         * It is the user's responsibility to ensure that the keys vector is empty
         * before making this call; otherwise, the new files will be appended to it.
         */
        """
        pass

    def getTags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tags(NodePath self)
        """
        pass

    def getTexGen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tex_gen(NodePath self, TextureStage stage)
        
        /**
         * Returns the texture coordinate generation mode for the given stage, or
         * M_off if there is no explicit mode set for the given stage.
         */
        """
        pass

    def getTexHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tex_hpr(NodePath self, TextureStage stage)
        get_tex_hpr(NodePath self, const NodePath other, TextureStage stage)
        
        /**
         * Returns the 3-D HPR set for the UVW's for the given stage on the current
         * node.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Returns the 3-D HPR set for the UVW's for the given stage on the current
         * node.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        """
        pass

    def getTexOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tex_offset(NodePath self, TextureStage stage)
        get_tex_offset(NodePath self, const NodePath other, TextureStage stage)
        
        /**
         * Returns the offset set for the UV's for the given stage on the current
         * node.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Returns the offset set for the UV's for the given stage on the current
         * node.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        """
        pass

    def getTexPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tex_pos(NodePath self, TextureStage stage)
        get_tex_pos(NodePath self, const NodePath other, TextureStage stage)
        
        /**
         * Returns the offset set for the UVW's for the given stage on the current
         * node.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Returns the offset set for the UVW's for the given stage on the current
         * node.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        """
        pass

    def getTexProjectorFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tex_projector_from(NodePath self, TextureStage stage)
        
        /**
         * Returns the "from" node associated with the TexProjectorEffect on the
         * indicated stage.  The relative transform between the "from" and the "to"
         * nodes is automatically applied to the texture transform each frame.
         */
        """
        pass

    def getTexProjectorTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tex_projector_to(NodePath self, TextureStage stage)
        
        /**
         * Returns the "to" node associated with the TexProjectorEffect on the
         * indicated stage.  The relative transform between the "from" and the "to"
         * nodes is automatically applied to the texture transform each frame.
         */
        """
        pass

    def getTexRotate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tex_rotate(NodePath self, TextureStage stage)
        get_tex_rotate(NodePath self, const NodePath other, TextureStage stage)
        
        /**
         * Returns the rotation set for the UV's for the given stage on the current
         * node.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Returns the rotation set for the UV's for the given stage on the current
         * node.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        """
        pass

    def getTexScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tex_scale(NodePath self, TextureStage stage)
        get_tex_scale(NodePath self, const NodePath other, TextureStage stage)
        
        /**
         * Returns the scale set for the UV's for the given stage on the current node.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Returns the scale set for the UV's for the given stage on the current node.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        """
        pass

    def getTexScale3d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tex_scale_3d(NodePath self, TextureStage stage)
        get_tex_scale_3d(NodePath self, const NodePath other, TextureStage stage)
        
        /**
         * Returns the scale set for the UVW's for the given stage on the current
         * node.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Returns the scale set for the UVW's for the given stage on the current
         * node.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        """
        pass

    def getTexTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tex_transform(NodePath self, TextureStage stage)
        get_tex_transform(NodePath self, const NodePath other, TextureStage stage)
        
        /**
         * Returns the texture matrix on the current node for the given stage, or
         * identity transform if there is no explicit transform set for the given
         * stage.
         */
        
        /**
         * Returns the texture matrix on the current node for the given stage,
         * relative to the other node.
         */
        """
        pass

    def getTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture(NodePath self)
        get_texture(NodePath self, TextureStage stage)
        
        /**
         * Returns the base-level texture that has been set on this particular node,
         * or NULL if no texture has been set.  This is not necessarily the texture
         * that will be applied to the geometry at or below this level, as another
         * texture at a higher or lower level may override.
         *
         * See also find_texture().
         */
        
        /**
         * Returns the texture that has been set on the indicated stage for this
         * particular node, or NULL if no texture has been set for this stage.
         */
        """
        pass

    def getTextureSampler(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture_sampler(NodePath self)
        get_texture_sampler(NodePath self, TextureStage stage)
        
        /**
         * Returns the sampler state that has been given for the base-level texture
         * that has been set on this particular node.  If no sampler state was given,
         * this returns the texture's default sampler settings.
         *
         * It is an error to call this if there is no base-level texture applied to
         * this particular node.
         */
        
        /**
         * Returns the sampler state that has been given for the indicated texture
         * stage that has been set on this particular node.  If no sampler state was
         * given, this returns the texture's default sampler settings.
         *
         * It is an error to call this if there is no texture set for this stage on
         * this particular node.
         */
        """
        pass

    def getTightBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tight_bounds(NodePath self, const NodePath other)
        """
        pass

    def getTop(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_top(NodePath self, Thread current_thread)
        
        /**
         * Returns a singleton NodePath that represents the top of the path, or empty
         * NodePath if this path is empty.
         */
        """
        pass

    def getTopNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_top_node(NodePath self, Thread current_thread)
        
        /**
         * Returns the top node of the path, or NULL if the path is empty.  This
         * requires iterating through the path.
         */
        """
        pass

    def getTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_transform(NodePath self)
        get_transform(NodePath self, const NodePath other, Thread current_thread)
        get_transform(NodePath self, Thread current_thread)
        
        /**
         * Returns the complete transform object set on this node.
         */
        
        /**
         * Returns the relative transform to this node from the other node; i.e.  the
         * transformation of this node as seen from the other node.
         */
        """
        pass

    def getTransparency(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_transparency(NodePath self)
        
        /**
         * Returns the transparent rendering that has been specifically set on this
         * node via set_transparency(), or M_none if nontransparent rendering has been
         * specifically set, or if nothing has been specifically set.  See also
         * has_transparency().  This does not necessarily imply that the geometry will
         * or will not be rendered transparent, as there may be other nodes that
         * override.
         */
        """
        pass

    def getTwoSided(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_two_sided(NodePath self)
        
        /**
         * Returns true if two-sided rendering has been specifically set on this node
         * via set_two_sided(), or false if one-sided rendering has been specifically
         * set, or if nothing has been specifically set.  See also has_two_sided().
         * This does not necessarily imply that the geometry will or will not be
         * rendered two-sided, as there may be other nodes that override.
         */
        """
        pass

    def getX(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_x(NodePath self)
        get_x(NodePath self, const NodePath other)
        """
        pass

    def getY(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_y(NodePath self)
        get_y(NodePath self, const NodePath other)
        """
        pass

    def getZ(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_z(NodePath self)
        get_z(NodePath self, const NodePath other)
        """
        pass

    def get_ancestor(self, NodePath_self, int_index, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ancestor(NodePath self, int index, Thread current_thread)
        
        /**
         * Returns the nth ancestor of the path, where 0 is the NodePath itself and
         * get_num_nodes() - 1 is get_top(). This requires iterating through the path.
         *
         * Also see get_node(), which returns the same thing as a PandaNode pointer,
         * not a NodePath.
         */
        """
        pass

    def get_ancestors(self, *args, **kwargs): # real signature unknown
        pass

    def get_antialias(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_antialias(NodePath self)
        
        /**
         * Returns the antialias setting that has been specifically set on this node
         * via set_antialias(), or M_none if no setting has been made.
         */
        """
        pass

    def get_attrib(self, NodePath_self, TypeHandle_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_attrib(NodePath self, TypeHandle type)
        
        /**
         * Returns the render attribute of the indicated type, if it is defined on the
         * node, or NULL if it is not.  This checks only what is set on this
         * particular node level, and has nothing to do with what render attributes
         * may be inherited from parent nodes.
         */
        """
        pass

    def get_audio_volume(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_audio_volume(NodePath self)
        
        /**
         * Returns the complete audio volume that has been applied to this node via a
         * previous call to set_audio_volume(), or 1. (identity) if no volume has been
         * applied to this particular node.
         */
        """
        pass

    def get_bin_draw_order(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bin_draw_order(NodePath self)
        
        /**
         * Returns the drawing order associated with the bin that this particular node
         * was assigned to via set_bin(), or 0 if no bin was assigned.  See set_bin()
         * and has_bin().
         */
        """
        pass

    def get_bin_name(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bin_name(NodePath self)
        
        /**
         * Returns the name of the bin that this particular node was assigned to via
         * set_bin(), or the empty string if no bin was assigned.  See set_bin() and
         * has_bin().
         */
        """
        pass

    def get_bounds(self, NodePath_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bounds(NodePath self, Thread current_thread)
        
        /**
         * Returns a newly-allocated bounding volume containing the bottom node and
         * all of its descendants.  This is the bounding volume on the bottom arc,
         * converted to the local coordinate space of the node.
         */
        """
        pass

    def get_child(self, NodePath_self, int_n, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_child(NodePath self, int n, Thread current_thread)
        
        /**
         * Returns a NodePath representing the nth child of the referenced node.
         */
        """
        pass

    def get_children(self, NodePath_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_children(NodePath self, Thread current_thread)
        
        /**
         * Returns the set of all child nodes of the referenced node.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_collide_mask(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collide_mask(NodePath self)
        
        /**
         * Returns the union of all of the into_collide_masks for nodes at this level
         * and below.  This is the same thing as node()->get_net_collide_mask().
         *
         * If you want to return what the into_collide_mask of this node itself is,
         * without regard to its children, use node()->get_into_collide_mask().
         */
        """
        pass

    def get_color(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color(NodePath self)
        
        /**
         * Returns the color that has been assigned to the node, or black if no color
         * has been assigned.
         */
        """
        pass

    def get_color_scale(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color_scale(NodePath self)
        
        /**
         * Returns the complete color scale vector that has been applied to this node
         * via a previous call to set_color_scale() and/or set_alpha_scale(), or all
         * 1's (identity) if no scale has been applied to this particular node.
         */
        """
        pass

    def get_common_ancestor(self, NodePath_self, const_NodePath_other, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_common_ancestor(NodePath self, const NodePath other, Thread current_thread)
        
        /**
         * Returns the lowest NodePath that both of these two NodePaths have in
         * common: the first ancestor that both of them share.  If the two NodePaths
         * are unrelated, returns NodePath::not_found().
         */
        """
        pass

    def get_depth_offset(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_depth_offset(NodePath self)
        
        /**
         * Returns the depth offset value if it has been specified using
         * set_depth_offset, or 0 if not.
         */
        """
        pass

    def get_depth_test(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_depth_test(NodePath self)
        
        /**
         * Returns true if depth-test rendering has been specifically set on this node
         * via set_depth_test(), or false if depth-test rendering has been
         * specifically disabled.  If nothing has been specifically set, returns true.
         * See also has_depth_test().
         */
        """
        pass

    def get_depth_write(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_depth_write(NodePath self)
        
        /**
         * Returns true if depth-write rendering has been specifically set on this
         * node via set_depth_write(), or false if depth-write rendering has been
         * specifically disabled.  If nothing has been specifically set, returns true.
         * See also has_depth_write().
         */
        """
        pass

    def get_distance(self, NodePath_self, const_NodePath_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_distance(NodePath self, const NodePath other)
        
        /**
         * Returns the straight-line distance between this referenced node's
         * coordinate frame's origin, and that of the other node's origin.
         */
        """
        pass

    def get_effect(self, NodePath_self, TypeHandle_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_effect(NodePath self, TypeHandle type)
        
        /**
         * Returns the render effect of the indicated type, if it is defined on the
         * node, or NULL if it is not.
         */
        """
        pass

    def get_effects(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_effects(NodePath self)
        
        /**
         * Returns the complete RenderEffects that will be applied to this node.
         */
        """
        pass

    def get_error_type(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_error_type(NodePath self)
        
        /**
         * If is_empty() is true, this returns a code that represents the reason why
         * the NodePath is empty.
         */
        """
        pass

    def get_fog(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fog(NodePath self)
        
        /**
         * Returns the fog that has been set on this particular node, or NULL if no
         * fog has been set.  This is not necessarily the fog that will be applied to
         * the geometry at or below this level, as another fog at a higher or lower
         * level may override.
         */
        """
        pass

    def get_h(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_h(NodePath self)
        get_h(NodePath self, const NodePath other)
        """
        pass

    def get_hidden_ancestor(self, NodePath_self, BitMask_camera_mask, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hidden_ancestor(NodePath self, BitMask camera_mask, Thread current_thread)
        
        /**
         * Returns the NodePath at or above the referenced node that is hidden to the
         * indicated camera(s), or an empty NodePath if no ancestor of the referenced
         * node is hidden (and the node should be visible).
         */
        """
        pass

    def get_hpr(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hpr(NodePath self)
        get_hpr(NodePath self, const NodePath other)
        
        /**
         * Retrieves the rotation component of the transform.
         */
        
        /**
         * Returns the relative orientation of the bottom node as seen from the other
         * node.
         */
        """
        pass

    def get_instance_count(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_instance_count(NodePath self)
        
        /**
         * Returns the geometry instance count, or 0 if disabled.  See
         * set_instance_count.
         */
        """
        pass

    def get_key(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_key(NodePath self)
        
        /**
         * Returns an integer that is guaranteed to be the same for all NodePaths that
         * represent the same node instance, and different for all NodePaths that
         * represent a different node instance.
         *
         * The same key will be returned for a particular instance as long as at least
         * one NodePath exists that represents that instance; if all NodePaths for a
         * particular instance destruct and a new one is later created, it may have a
         * different index.  However, a given key will never be reused for a different
         * instance (unless the app has been running long enough that we overflow the
         * integer key value).
         */
        """
        pass

    def get_logic_op(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_logic_op(NodePath self)
        
        /**
         * Returns the logical operation that has been specifically set on this node
         * via set_logic_op(), or O_none if standard color blending has been
         * specifically set, or if nothing has been specifically set.  See also
         * has_logic_op().  This does not necessarily imply that the geometry will
         * or will not be rendered with the given logical operation, as there may be
         * other nodes that override.
         *
         * @since 1.10.0
         */
        """
        pass

    def get_mat(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mat(NodePath self)
        get_mat(NodePath self, const NodePath other)
        
        /**
         * Returns the transform matrix that has been applied to the referenced node,
         * or the identity matrix if no matrix has been applied.
         */
        
        /**
         * Returns the matrix that describes the coordinate space of the bottom node,
         * relative to the other path's bottom node's coordinate space.
         */
        """
        pass

    def get_material(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_material(NodePath self)
        
        /**
         * Returns the material that has been set on this particular node, or NULL if
         * no material has been set.  This is not necessarily the material that will
         * be applied to the geometry at or below this level, as another material at a
         * higher or lower level may override.
         *
         * See also find_material().
         */
        """
        pass

    def get_max_search_depth(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_search_depth()
        
        /**
         * Returns the current setting of the search depth limit.  See
         * set_max_search_depth.
         */
        """
        pass

    def get_name(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(NodePath self)
        
        /**
         * Returns the name of the referenced node.
         */
        """
        pass

    def get_net_audio_volume(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_net_audio_volume(NodePath self)
        
        /**
         * Returns the complete audio volume for this node taking highers nodes in the
         * graph into account.
         */
        """
        pass

    def get_net_prev_transform(self, NodePath_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_net_prev_transform(NodePath self, Thread current_thread)
        
        /**
         * Returns the net "previous" transform on this node from the root.  See
         * set_prev_transform().
         */
        """
        pass

    def get_net_python_tag(self, NodePath_self, object_keys): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_net_python_tag(NodePath self, object keys)
        """
        pass

    def get_net_state(self, NodePath_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_net_state(NodePath self, Thread current_thread)
        
        /**
         * Returns the net state on this node from the root.
         */
        """
        pass

    def get_net_tag(self, NodePath_self, str_key): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_net_tag(NodePath self, str key)
        
        /**
         * Returns the tag value that has been defined on this node, or the nearest
         * ancestor node, for the indicated key.  If no value has been defined for the
         * indicated key on any ancestor node, returns the empty string.  See also
         * get_tag().
         */
        """
        pass

    def get_net_transform(self, NodePath_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_net_transform(NodePath self, Thread current_thread)
        
        /**
         * Returns the net transform on this node from the root.
         */
        """
        pass

    def get_node(self, NodePath_self, int_index, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node(NodePath self, int index, Thread current_thread)
        
        /**
         * Returns the nth node of the path, where 0 is the referenced (bottom) node
         * and get_num_nodes() - 1 is the top node.  This requires iterating through
         * the path.
         *
         * Also see node(), which is a convenience function to return the same thing
         * as get_node(0) (since the bottom node is the most important node in the
         * NodePath, and is the one most frequently referenced).
         *
         * Note that this function returns the same thing as
         * get_ancestor(index).node().
         */
        """
        pass

    def get_nodes(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_children(self, NodePath_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_children(NodePath self, Thread current_thread)
        
        /**
         * Returns the number of children of the referenced node.
         */
        """
        pass

    def get_num_nodes(self, NodePath_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_nodes(NodePath self, Thread current_thread)
        
        /**
         * Returns the number of nodes in the path.
         */
        """
        pass

    def get_p(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_p(NodePath self)
        get_p(NodePath self, const NodePath other)
        """
        pass

    def get_parent(self, NodePath_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_parent(NodePath self, Thread current_thread)
        
        /**
         * Returns the NodePath to the parent of the referenced node: that is, this
         * NodePath, shortened by one node.  The parent of a singleton NodePath is
         * defined to be the empty NodePath.
         */
        """
        pass

    def get_pos(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pos(NodePath self)
        get_pos(NodePath self, const NodePath other)
        
        /**
         * Retrieves the translation component of the transform.
         */
        
        /**
         * Returns the relative position of the referenced node as seen from the other
         * node.
         */
        """
        pass

    def get_pos_delta(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pos_delta(NodePath self)
        get_pos_delta(NodePath self, const NodePath other)
        
        /**
         * Returns the delta vector from this node's position in the previous frame
         * (according to set_prev_transform(), typically set via the use of
         * set_fluid_pos()) and its position in the current frame.  This is the vector
         * used to determine collisions.  Generally, if the node was last repositioned
         * via set_pos(), the delta will be zero; if it was adjusted via
         * set_fluid_pos(), the delta will represent the change from the previous
         * frame's position.
         */
        
        /**
         * Returns the delta vector from this node's position in the previous frame
         * (according to set_prev_transform(), typically set via the use of
         * set_fluid_pos()) and its position in the current frame, as seen in the
         * indicated node's coordinate space.  This is the vector used to determine
         * collisions.  Generally, if the node was last repositioned via set_pos(),
         * the delta will be zero; if it was adjusted via set_fluid_pos(), the delta
         * will represent the change from the previous frame's position.
         */
        """
        pass

    def get_prev_transform(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_prev_transform(NodePath self)
        get_prev_transform(NodePath self, const NodePath other, Thread current_thread)
        get_prev_transform(NodePath self, Thread current_thread)
        
        /**
         * Returns the transform that has been set as this node's "previous" position.
         * See set_prev_transform().
         */
        
        /**
         * Returns the relative "previous" transform to this node from the other node;
         * i.e.  the position of this node in the previous frame, as seen by the other
         * node in the previous frame.
         */
        """
        pass

    def get_python_tag(self, NodePath_self, object_keys): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_python_tag(NodePath self, object keys)
        """
        pass

    def get_python_tags(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_python_tags(const NodePath self)
        """
        pass

    def get_python_tag_keys(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_python_tag_keys(NodePath self)
        """
        pass

    def get_quat(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_quat(NodePath self)
        get_quat(NodePath self, const NodePath other)
        
        /**
         * Retrieves the rotation component of the transform.
         */
        
        /**
         * Returns the relative orientation of the bottom node as seen from the other
         * node.
         */
        """
        pass

    def get_r(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_r(NodePath self)
        get_r(NodePath self, const NodePath other)
        """
        pass

    def get_relative_point(self, NodePath_self, const_NodePath_other, const_LVecBase3f_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_relative_point(NodePath self, const NodePath other, const LVecBase3f point)
        
        /**
         * Given that the indicated point is in the coordinate system of the other
         * node, returns the same point in this node's coordinate system.
         */
        """
        pass

    def get_relative_vector(self, NodePath_self, const_NodePath_other, const_LVecBase3f_vec): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_relative_vector(NodePath self, const NodePath other, const LVecBase3f vec)
        
        /**
         * Given that the indicated vector is in the coordinate system of the other
         * node, returns the same vector in this node's coordinate system.
         */
        """
        pass

    def get_render_mode(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_render_mode(NodePath self)
        
        /**
         * Returns the render mode that has been specifically set on this node via
         * set_render_mode(), or M_unchanged if nothing has been set.
         */
        """
        pass

    def get_render_mode_perspective(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_render_mode_perspective(NodePath self)
        
        /**
         * Returns the flag that has been set on this node via
         * set_render_mode_perspective(), or false if no flag has been set.
         */
        """
        pass

    def get_render_mode_thickness(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_render_mode_thickness(NodePath self)
        
        /**
         * Returns the render mode thickness that has been specifically set on this
         * node via set_render_mode(), or 1.0 if nothing has been set.
         */
        """
        pass

    def get_sa(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sa(NodePath self)
        
        /**
         * Gets the alpha component of the color scale.
         * @see get_color_scale()
         */
        """
        pass

    def get_sb(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sb(NodePath self)
        
        /**
         * Gets the blue component of the color scale.
         * @see get_color_scale()
         */
        """
        pass

    def get_scale(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scale(NodePath self)
        get_scale(NodePath self, const NodePath other)
        
        /**
         * Retrieves the scale component of the transform.
         */
        
        /**
         * Returns the relative scale of the bottom node as seen from the other node.
         */
        """
        pass

    def get_sg(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sg(NodePath self)
        
        /**
         * Gets the green component of the color scale.
         * @see get_color_scale()
         */
        """
        pass

    def get_shader(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shader(NodePath self)
        
        /**
         *
         */
        """
        pass

    def get_shader_input(self, NodePath_self, const_InternalName_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shader_input(NodePath self, const InternalName id)
        
        /**
         *
         */
        """
        pass

    def get_shear(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shear(NodePath self)
        get_shear(NodePath self, const NodePath other)
        
        /**
         * Retrieves the shear component of the transform.
         */
        
        /**
         * Returns the relative shear of the bottom node as seen from the other node.
         */
        """
        pass

    def get_shxy(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shxy(NodePath self)
        get_shxy(NodePath self, const NodePath other)
        
        /**
         * Returns the relative shear of the referenced node as seen from the other
         * node.
         */
        """
        pass

    def get_shxz(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shxz(NodePath self)
        get_shxz(NodePath self, const NodePath other)
        """
        pass

    def get_shyz(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shyz(NodePath self)
        get_shyz(NodePath self, const NodePath other)
        """
        pass

    def get_sort(self, NodePath_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sort(NodePath self, Thread current_thread)
        
        /**
         * Returns the sort value of the referenced node within its parent; that is,
         * the sort number passed on the last reparenting operation for this node.
         * This will control the position of the node within its parent's list of
         * children.
         */
        """
        pass

    def get_sr(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sr(NodePath self)
        
        /**
         * Gets the red component of the color scale.
         * @see get_color_scale()
         */
        """
        pass

    def get_stashed_ancestor(self, NodePath_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_stashed_ancestor(NodePath self, Thread current_thread)
        
        /**
         * Returns the NodePath at or above the referenced node that is stashed, or an
         * empty NodePath if no ancestor of the referenced node is stashed (and the
         * node should be visible).
         */
        """
        pass

    def get_stashed_children(self, NodePath_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_stashed_children(NodePath self, Thread current_thread)
        
        /**
         * Returns the set of all child nodes of the referenced node that have been
         * stashed.  These children are not normally visible on the node, and do not
         * appear in the list returned by get_children().
         */
        """
        pass

    def get_state(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_state(NodePath self)
        get_state(NodePath self, const NodePath other, Thread current_thread)
        get_state(NodePath self, Thread current_thread)
        
        // Aggregate transform and state information.
        
        /**
         * Returns the complete state object set on this node.
         */
        
        /**
         * Returns the state changes that must be made to transition to the render
         * state of this node from the render state of the other node.
         */
        """
        pass

    def get_sx(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sx(NodePath self)
        get_sx(NodePath self, const NodePath other)
        
        /**
         * Returns the relative scale of the referenced node as seen from the other
         * node.
         */
        """
        pass

    def get_sy(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sy(NodePath self)
        get_sy(NodePath self, const NodePath other)
        """
        pass

    def get_sz(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sz(NodePath self)
        get_sz(NodePath self, const NodePath other)
        """
        pass

    def get_tag(self, NodePath_self, str_key): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tag(NodePath self, str key)
        
        /**
         * Retrieves the user-defined value that was previously set on this node for
         * the particular key, if any.  If no value has been previously set, returns
         * the empty string.  See also get_net_tag().
         */
        """
        pass

    def get_tags(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tags(NodePath self)
        """
        pass

    def get_tag_keys(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tag_keys(NodePath self)
        
        /**
         * Fills the given vector up with the list of tags on this PandaNode.
         *
         * It is the user's responsibility to ensure that the keys vector is empty
         * before making this call; otherwise, the new files will be appended to it.
         */
        """
        pass

    def get_texture(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture(NodePath self)
        get_texture(NodePath self, TextureStage stage)
        
        /**
         * Returns the base-level texture that has been set on this particular node,
         * or NULL if no texture has been set.  This is not necessarily the texture
         * that will be applied to the geometry at or below this level, as another
         * texture at a higher or lower level may override.
         *
         * See also find_texture().
         */
        
        /**
         * Returns the texture that has been set on the indicated stage for this
         * particular node, or NULL if no texture has been set for this stage.
         */
        """
        pass

    def get_texture_sampler(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture_sampler(NodePath self)
        get_texture_sampler(NodePath self, TextureStage stage)
        
        /**
         * Returns the sampler state that has been given for the base-level texture
         * that has been set on this particular node.  If no sampler state was given,
         * this returns the texture's default sampler settings.
         *
         * It is an error to call this if there is no base-level texture applied to
         * this particular node.
         */
        
        /**
         * Returns the sampler state that has been given for the indicated texture
         * stage that has been set on this particular node.  If no sampler state was
         * given, this returns the texture's default sampler settings.
         *
         * It is an error to call this if there is no texture set for this stage on
         * this particular node.
         */
        """
        pass

    def get_tex_gen(self, NodePath_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tex_gen(NodePath self, TextureStage stage)
        
        /**
         * Returns the texture coordinate generation mode for the given stage, or
         * M_off if there is no explicit mode set for the given stage.
         */
        """
        pass

    def get_tex_hpr(self, NodePath_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tex_hpr(NodePath self, TextureStage stage)
        get_tex_hpr(NodePath self, const NodePath other, TextureStage stage)
        
        /**
         * Returns the 3-D HPR set for the UVW's for the given stage on the current
         * node.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Returns the 3-D HPR set for the UVW's for the given stage on the current
         * node.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        """
        pass

    def get_tex_offset(self, NodePath_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tex_offset(NodePath self, TextureStage stage)
        get_tex_offset(NodePath self, const NodePath other, TextureStage stage)
        
        /**
         * Returns the offset set for the UV's for the given stage on the current
         * node.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Returns the offset set for the UV's for the given stage on the current
         * node.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        """
        pass

    def get_tex_pos(self, NodePath_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tex_pos(NodePath self, TextureStage stage)
        get_tex_pos(NodePath self, const NodePath other, TextureStage stage)
        
        /**
         * Returns the offset set for the UVW's for the given stage on the current
         * node.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Returns the offset set for the UVW's for the given stage on the current
         * node.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        """
        pass

    def get_tex_projector_from(self, NodePath_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tex_projector_from(NodePath self, TextureStage stage)
        
        /**
         * Returns the "from" node associated with the TexProjectorEffect on the
         * indicated stage.  The relative transform between the "from" and the "to"
         * nodes is automatically applied to the texture transform each frame.
         */
        """
        pass

    def get_tex_projector_to(self, NodePath_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tex_projector_to(NodePath self, TextureStage stage)
        
        /**
         * Returns the "to" node associated with the TexProjectorEffect on the
         * indicated stage.  The relative transform between the "from" and the "to"
         * nodes is automatically applied to the texture transform each frame.
         */
        """
        pass

    def get_tex_rotate(self, NodePath_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tex_rotate(NodePath self, TextureStage stage)
        get_tex_rotate(NodePath self, const NodePath other, TextureStage stage)
        
        /**
         * Returns the rotation set for the UV's for the given stage on the current
         * node.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Returns the rotation set for the UV's for the given stage on the current
         * node.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        """
        pass

    def get_tex_scale(self, NodePath_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tex_scale(NodePath self, TextureStage stage)
        get_tex_scale(NodePath self, const NodePath other, TextureStage stage)
        
        /**
         * Returns the scale set for the UV's for the given stage on the current node.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Returns the scale set for the UV's for the given stage on the current node.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        """
        pass

    def get_tex_scale_3d(self, NodePath_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tex_scale_3d(NodePath self, TextureStage stage)
        get_tex_scale_3d(NodePath self, const NodePath other, TextureStage stage)
        
        /**
         * Returns the scale set for the UVW's for the given stage on the current
         * node.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Returns the scale set for the UVW's for the given stage on the current
         * node.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        """
        pass

    def get_tex_transform(self, NodePath_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tex_transform(NodePath self, TextureStage stage)
        get_tex_transform(NodePath self, const NodePath other, TextureStage stage)
        
        /**
         * Returns the texture matrix on the current node for the given stage, or
         * identity transform if there is no explicit transform set for the given
         * stage.
         */
        
        /**
         * Returns the texture matrix on the current node for the given stage,
         * relative to the other node.
         */
        """
        pass

    def get_tight_bounds(self, NodePath_self, const_NodePath_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tight_bounds(NodePath self, const NodePath other)
        """
        pass

    def get_top(self, NodePath_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_top(NodePath self, Thread current_thread)
        
        /**
         * Returns a singleton NodePath that represents the top of the path, or empty
         * NodePath if this path is empty.
         */
        """
        pass

    def get_top_node(self, NodePath_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_top_node(NodePath self, Thread current_thread)
        
        /**
         * Returns the top node of the path, or NULL if the path is empty.  This
         * requires iterating through the path.
         */
        """
        pass

    def get_transform(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_transform(NodePath self)
        get_transform(NodePath self, const NodePath other, Thread current_thread)
        get_transform(NodePath self, Thread current_thread)
        
        /**
         * Returns the complete transform object set on this node.
         */
        
        /**
         * Returns the relative transform to this node from the other node; i.e.  the
         * transformation of this node as seen from the other node.
         */
        """
        pass

    def get_transparency(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_transparency(NodePath self)
        
        /**
         * Returns the transparent rendering that has been specifically set on this
         * node via set_transparency(), or M_none if nontransparent rendering has been
         * specifically set, or if nothing has been specifically set.  See also
         * has_transparency().  This does not necessarily imply that the geometry will
         * or will not be rendered transparent, as there may be other nodes that
         * override.
         */
        """
        pass

    def get_two_sided(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_two_sided(NodePath self)
        
        /**
         * Returns true if two-sided rendering has been specifically set on this node
         * via set_two_sided(), or false if one-sided rendering has been specifically
         * set, or if nothing has been specifically set.  See also has_two_sided().
         * This does not necessarily imply that the geometry will or will not be
         * rendered two-sided, as there may be other nodes that override.
         */
        """
        pass

    def get_x(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_x(NodePath self)
        get_x(NodePath self, const NodePath other)
        """
        pass

    def get_y(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_y(NodePath self)
        get_y(NodePath self, const NodePath other)
        """
        pass

    def get_z(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_z(NodePath self)
        get_z(NodePath self, const NodePath other)
        """
        pass

    def hasAntialias(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_antialias(NodePath self)
        
        /**
         * Returns true if an antialias setting has been explicitly mode on this
         * particular node via set_antialias().  If this returns true, then
         * get_antialias() may be called to determine what the setting was.
         */
        """
        pass

    def hasAttrib(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_attrib(NodePath self, TypeHandle type)
        
        /**
         * Returns true if there is a render attribute of the indicated type defined
         * on this node, or false if there is not.
         */
        """
        pass

    def hasAudioVolume(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_audio_volume(NodePath self)
        
        /**
         * Returns true if an audio volume has been applied to the referenced node,
         * false otherwise.  It is still possible that volume at this node might have
         * been scaled by an ancestor node.
         */
        """
        pass

    def hasBillboard(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_billboard(NodePath self)
        
        /**
         * Returns true if there is any billboard effect on the node.
         */
        """
        pass

    def hasBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_bin(NodePath self)
        
        /**
         * Returns true if the node has been assigned to the a particular rendering
         * bin via set_bin(), false otherwise.
         */
        """
        pass

    def hasClipPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_clip_plane(NodePath self, const NodePath clip_plane)
        
        /**
         * Returns true if the indicated clipping plane has been specifically applied
         * to this particular node.  This means that someone called set_clip_plane()
         * on this node with the indicated clip_plane.
         */
        """
        pass

    def hasClipPlaneOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_clip_plane_off(NodePath self)
        has_clip_plane_off(NodePath self, const NodePath clip_plane)
        
        /**
         * Returns true if all clipping planes have been specifically disabled on this
         * particular node.  This means that someone called set_clip_plane_off() on
         * this node with no parameters.
         */
        
        /**
         * Returns true if the indicated clipping plane has been specifically disabled
         * on this particular node.  This means that someone called
         * set_clip_plane_off() on this node with the indicated clip_plane.
         */
        """
        pass

    def hasColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_color(NodePath self)
        
        /**
         * Returns true if a color has been applied to the given node, false
         * otherwise.
         */
        """
        pass

    def hasColorScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_color_scale(NodePath self)
        
        /**
         * Returns true if a color scale has been applied to the referenced node,
         * false otherwise.  It is still possible that color at this node might have
         * been scaled by an ancestor node.
         */
        """
        pass

    def hasCompass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_compass(NodePath self)
        
        /**
         * Returns true if there is any compass effect on the node.
         */
        """
        pass

    def hasDepthOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_depth_offset(NodePath self)
        
        /**
         * Returns true if a depth-offset adjustment has been explicitly set on this
         * particular node via set_depth_offset().  If this returns true, then
         * get_depth_offset() may be called to determine which has been set.
         */
        """
        pass

    def hasDepthTest(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_depth_test(NodePath self)
        
        /**
         * Returns true if a depth-test adjustment has been explicitly set on this
         * particular node via set_depth_test().  If this returns true, then
         * get_depth_test() may be called to determine which has been set.
         */
        """
        pass

    def hasDepthWrite(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_depth_write(NodePath self)
        
        /**
         * Returns true if a depth-write adjustment has been explicitly set on this
         * particular node via set_depth_write().  If this returns true, then
         * get_depth_write() may be called to determine which has been set.
         */
        """
        pass

    def hasEffect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_effect(NodePath self, TypeHandle type)
        
        /**
         * Returns true if there is a render effect of the indicated type defined on
         * this node, or false if there is not.
         */
        """
        pass

    def hasFog(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_fog(NodePath self)
        
        /**
         * Returns true if a fog has been applied to this particular node via
         * set_fog(), false otherwise.  This is not the same thing as asking whether
         * the geometry at this node will be rendered with fog, as there may be a fog
         * in effect from a higher or lower level.
         */
        """
        pass

    def hasFogOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_fog_off(NodePath self)
        
        /**
         * Returns true if a fog has been specifically disabled on this particular
         * node via set_fog_off(), false otherwise.  This is not the same thing as
         * asking whether the geometry at this node will be rendered unfogged, as
         * there may be a fog in effect from a higher or lower level.
         */
        """
        pass

    def hasLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_light(NodePath self, const NodePath light)
        
        /**
         * Returns true if the indicated Light or PolylightNode has been specifically
         * enabled on this particular node.  This means that someone called
         * set_light() on this node with the indicated light.
         */
        """
        pass

    def hasLightOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_light_off(NodePath self)
        has_light_off(NodePath self, const NodePath light)
        
        /**
         * Returns true if all Lights have been specifically disabled on this
         * particular node.  This means that someone called set_light_off() on this
         * node with no parameters.
         */
        
        /**
         * Returns true if the indicated Light has been specifically disabled on this
         * particular node.  This means that someone called set_light_off() on this
         * node with the indicated light.
         *
         * This interface does not support PolylightNodes, which cannot be turned off
         * at a lower level.
         */
        """
        pass

    def hasLogicOp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_logic_op(NodePath self)
        
        /**
         * Returns true if a logical operation has been explicitly set on this
         * particular node via set_logic_op().  If this returns true, then
         * get_logic_op() may be called to determine whether a logical operation has
         * been explicitly disabled for this node or set to particular operation.
         *
         * @since 1.10.0
         */
        """
        pass

    def hasMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_mat(NodePath self)
        
        /**
         * Returns true if a non-identity transform matrix has been applied to the
         * referenced node, false otherwise.
         */
        """
        pass

    def hasMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_material(NodePath self)
        
        /**
         * Returns true if a material has been applied to this particular node via
         * set_material(), false otherwise.
         */
        """
        pass

    def hasNetPythonTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_net_python_tag(NodePath self, object keys)
        """
        pass

    def hasNetTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_net_tag(NodePath self, str key)
        
        /**
         * Returns true if the indicated tag value has been defined on this node or on
         * any ancestor node, or false otherwise.  See also has_tag().
         */
        """
        pass

    def hasOccluder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_occluder(NodePath self, const NodePath occluder)
        
        /**
         * Returns true if the indicated occluder has been specifically applied to
         * this particular node.  This means that someone called set_occluder() on
         * this node with the indicated occluder.
         */
        """
        pass

    def hasParent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_parent(NodePath self, Thread current_thread)
        
        /**
         * Returns true if the referenced node has a parent; i.e.  the NodePath chain
         * contains at least two nodes.
         */
        """
        pass

    def hasPythonTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_python_tag(NodePath self, object keys)
        """
        pass

    def hasRenderMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_render_mode(NodePath self)
        
        /**
         * Returns true if a render mode has been explicitly set on this particular
         * node via set_render_mode() (or set_render_mode_wireframe() or
         * set_render_mode_filled()), false otherwise.
         */
        """
        pass

    def hasScissor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_scissor(NodePath self)
        
        /**
         * Returns true if a scissor region was defined at this node by a previous
         * call to set_scissor().  This does not check for scissor regions inherited
         * from a parent class.  It also does not check for the presence of a low-
         * level ScissorAttrib, which is different from the ScissorEffect added by
         * set_scissor.
         */
        """
        pass

    def hasTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_tag(NodePath self, str key)
        
        /**
         * Returns true if a value has been defined on this node for the particular
         * key (even if that value is the empty string), or false if no value has been
         * set.  See also has_net_tag().
         */
        """
        pass

    def hasTexcoord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_texcoord(NodePath self, str texcoord_name)
        
        /**
         * Returns true if there are at least some vertices at this node and below
         * that use the named texture coordinate set, false otherwise.  Pass the empty
         * string for the default texture coordinate set.
         */
        """
        pass

    def hasTexGen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_tex_gen(NodePath self, TextureStage stage)
        
        /**
         * Returns true if there is a mode for automatic texture coordinate generation
         * on the current node for the given stage.
         */
        """
        pass

    def hasTexProjector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_tex_projector(NodePath self, TextureStage stage)
        
        /**
         * Returns true if this node has a TexProjectorEffect for the indicated stage,
         * false otherwise.
         */
        """
        pass

    def hasTexTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_tex_transform(NodePath self, TextureStage stage)
        
        /**
         * Returns true if there is an explicit texture matrix on the current node for
         * the given stage.
         */
        """
        pass

    def hasTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_texture(NodePath self)
        has_texture(NodePath self, TextureStage stage)
        
        /**
         * Returns true if a texture has been applied to this particular node via
         * set_texture(), false otherwise.  This is not the same thing as asking
         * whether the geometry at this node will be rendered with texturing, as there
         * may be a texture in effect from a higher or lower level.
         */
        
        /**
         * Returns true if texturing has been specifically enabled on this particular
         * node for the indicated stage.  This means that someone called set_texture()
         * on this node with the indicated stage name, or the stage_name is the
         * default stage_name, and someone called set_texture() on this node.
         */
        """
        pass

    def hasTextureOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_texture_off(NodePath self)
        has_texture_off(NodePath self, TextureStage stage)
        
        /**
         * Returns true if texturing has been specifically disabled on this particular
         * node via set_texture_off(), false otherwise.  This is not the same thing as
         * asking whether the geometry at this node will be rendered untextured, as
         * there may be a texture in effect from a higher or lower level.
         */
        
        /**
         * Returns true if texturing has been specifically disabled on this particular
         * node for the indicated stage.  This means that someone called
         * set_texture_off() on this node with the indicated stage name, or that
         * someone called set_texture_off() on this node to remove all stages.
         */
        """
        pass

    def hasTransparency(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_transparency(NodePath self)
        
        /**
         * Returns true if a transparent-rendering adjustment has been explicitly set
         * on this particular node via set_transparency().  If this returns true, then
         * get_transparency() may be called to determine whether transparency has been
         * explicitly enabled or explicitly disabled for this node.
         */
        """
        pass

    def hasTwoSided(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_two_sided(NodePath self)
        
        /**
         * Returns true if a two-sided adjustment has been explicitly set on this
         * particular node via set_two_sided().  If this returns true, then
         * get_two_sided() may be called to determine which has been set.
         */
        """
        pass

    def hasVertexColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_vertex_column(NodePath self, const InternalName name)
        
        /**
         * Returns true if there are at least some vertices at this node and below
         * that contain a reference to the indicated vertex data column name, false
         * otherwise.
         *
         * This is particularly useful for testing whether a particular model has a
         * given texture coordinate set (but see has_texcoord()).
         */
        """
        pass

    def has_antialias(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_antialias(NodePath self)
        
        /**
         * Returns true if an antialias setting has been explicitly mode on this
         * particular node via set_antialias().  If this returns true, then
         * get_antialias() may be called to determine what the setting was.
         */
        """
        pass

    def has_attrib(self, NodePath_self, TypeHandle_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_attrib(NodePath self, TypeHandle type)
        
        /**
         * Returns true if there is a render attribute of the indicated type defined
         * on this node, or false if there is not.
         */
        """
        pass

    def has_audio_volume(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_audio_volume(NodePath self)
        
        /**
         * Returns true if an audio volume has been applied to the referenced node,
         * false otherwise.  It is still possible that volume at this node might have
         * been scaled by an ancestor node.
         */
        """
        pass

    def has_billboard(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_billboard(NodePath self)
        
        /**
         * Returns true if there is any billboard effect on the node.
         */
        """
        pass

    def has_bin(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_bin(NodePath self)
        
        /**
         * Returns true if the node has been assigned to the a particular rendering
         * bin via set_bin(), false otherwise.
         */
        """
        pass

    def has_clip_plane(self, NodePath_self, const_NodePath_clip_plane): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_clip_plane(NodePath self, const NodePath clip_plane)
        
        /**
         * Returns true if the indicated clipping plane has been specifically applied
         * to this particular node.  This means that someone called set_clip_plane()
         * on this node with the indicated clip_plane.
         */
        """
        pass

    def has_clip_plane_off(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_clip_plane_off(NodePath self)
        has_clip_plane_off(NodePath self, const NodePath clip_plane)
        
        /**
         * Returns true if all clipping planes have been specifically disabled on this
         * particular node.  This means that someone called set_clip_plane_off() on
         * this node with no parameters.
         */
        
        /**
         * Returns true if the indicated clipping plane has been specifically disabled
         * on this particular node.  This means that someone called
         * set_clip_plane_off() on this node with the indicated clip_plane.
         */
        """
        pass

    def has_color(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_color(NodePath self)
        
        /**
         * Returns true if a color has been applied to the given node, false
         * otherwise.
         */
        """
        pass

    def has_color_scale(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_color_scale(NodePath self)
        
        /**
         * Returns true if a color scale has been applied to the referenced node,
         * false otherwise.  It is still possible that color at this node might have
         * been scaled by an ancestor node.
         */
        """
        pass

    def has_compass(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_compass(NodePath self)
        
        /**
         * Returns true if there is any compass effect on the node.
         */
        """
        pass

    def has_depth_offset(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_depth_offset(NodePath self)
        
        /**
         * Returns true if a depth-offset adjustment has been explicitly set on this
         * particular node via set_depth_offset().  If this returns true, then
         * get_depth_offset() may be called to determine which has been set.
         */
        """
        pass

    def has_depth_test(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_depth_test(NodePath self)
        
        /**
         * Returns true if a depth-test adjustment has been explicitly set on this
         * particular node via set_depth_test().  If this returns true, then
         * get_depth_test() may be called to determine which has been set.
         */
        """
        pass

    def has_depth_write(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_depth_write(NodePath self)
        
        /**
         * Returns true if a depth-write adjustment has been explicitly set on this
         * particular node via set_depth_write().  If this returns true, then
         * get_depth_write() may be called to determine which has been set.
         */
        """
        pass

    def has_effect(self, NodePath_self, TypeHandle_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_effect(NodePath self, TypeHandle type)
        
        /**
         * Returns true if there is a render effect of the indicated type defined on
         * this node, or false if there is not.
         */
        """
        pass

    def has_fog(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_fog(NodePath self)
        
        /**
         * Returns true if a fog has been applied to this particular node via
         * set_fog(), false otherwise.  This is not the same thing as asking whether
         * the geometry at this node will be rendered with fog, as there may be a fog
         * in effect from a higher or lower level.
         */
        """
        pass

    def has_fog_off(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_fog_off(NodePath self)
        
        /**
         * Returns true if a fog has been specifically disabled on this particular
         * node via set_fog_off(), false otherwise.  This is not the same thing as
         * asking whether the geometry at this node will be rendered unfogged, as
         * there may be a fog in effect from a higher or lower level.
         */
        """
        pass

    def has_light(self, NodePath_self, const_NodePath_light): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_light(NodePath self, const NodePath light)
        
        /**
         * Returns true if the indicated Light or PolylightNode has been specifically
         * enabled on this particular node.  This means that someone called
         * set_light() on this node with the indicated light.
         */
        """
        pass

    def has_light_off(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_light_off(NodePath self)
        has_light_off(NodePath self, const NodePath light)
        
        /**
         * Returns true if all Lights have been specifically disabled on this
         * particular node.  This means that someone called set_light_off() on this
         * node with no parameters.
         */
        
        /**
         * Returns true if the indicated Light has been specifically disabled on this
         * particular node.  This means that someone called set_light_off() on this
         * node with the indicated light.
         *
         * This interface does not support PolylightNodes, which cannot be turned off
         * at a lower level.
         */
        """
        pass

    def has_logic_op(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_logic_op(NodePath self)
        
        /**
         * Returns true if a logical operation has been explicitly set on this
         * particular node via set_logic_op().  If this returns true, then
         * get_logic_op() may be called to determine whether a logical operation has
         * been explicitly disabled for this node or set to particular operation.
         *
         * @since 1.10.0
         */
        """
        pass

    def has_mat(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_mat(NodePath self)
        
        /**
         * Returns true if a non-identity transform matrix has been applied to the
         * referenced node, false otherwise.
         */
        """
        pass

    def has_material(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_material(NodePath self)
        
        /**
         * Returns true if a material has been applied to this particular node via
         * set_material(), false otherwise.
         */
        """
        pass

    def has_net_python_tag(self, NodePath_self, object_keys): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_net_python_tag(NodePath self, object keys)
        """
        pass

    def has_net_tag(self, NodePath_self, str_key): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_net_tag(NodePath self, str key)
        
        /**
         * Returns true if the indicated tag value has been defined on this node or on
         * any ancestor node, or false otherwise.  See also has_tag().
         */
        """
        pass

    def has_occluder(self, NodePath_self, const_NodePath_occluder): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_occluder(NodePath self, const NodePath occluder)
        
        /**
         * Returns true if the indicated occluder has been specifically applied to
         * this particular node.  This means that someone called set_occluder() on
         * this node with the indicated occluder.
         */
        """
        pass

    def has_parent(self, NodePath_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_parent(NodePath self, Thread current_thread)
        
        /**
         * Returns true if the referenced node has a parent; i.e.  the NodePath chain
         * contains at least two nodes.
         */
        """
        pass

    def has_python_tag(self, NodePath_self, object_keys): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_python_tag(NodePath self, object keys)
        """
        pass

    def has_render_mode(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_render_mode(NodePath self)
        
        /**
         * Returns true if a render mode has been explicitly set on this particular
         * node via set_render_mode() (or set_render_mode_wireframe() or
         * set_render_mode_filled()), false otherwise.
         */
        """
        pass

    def has_scissor(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_scissor(NodePath self)
        
        /**
         * Returns true if a scissor region was defined at this node by a previous
         * call to set_scissor().  This does not check for scissor regions inherited
         * from a parent class.  It also does not check for the presence of a low-
         * level ScissorAttrib, which is different from the ScissorEffect added by
         * set_scissor.
         */
        """
        pass

    def has_tag(self, NodePath_self, str_key): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_tag(NodePath self, str key)
        
        /**
         * Returns true if a value has been defined on this node for the particular
         * key (even if that value is the empty string), or false if no value has been
         * set.  See also has_net_tag().
         */
        """
        pass

    def has_texcoord(self, NodePath_self, str_texcoord_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_texcoord(NodePath self, str texcoord_name)
        
        /**
         * Returns true if there are at least some vertices at this node and below
         * that use the named texture coordinate set, false otherwise.  Pass the empty
         * string for the default texture coordinate set.
         */
        """
        pass

    def has_texture(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_texture(NodePath self)
        has_texture(NodePath self, TextureStage stage)
        
        /**
         * Returns true if a texture has been applied to this particular node via
         * set_texture(), false otherwise.  This is not the same thing as asking
         * whether the geometry at this node will be rendered with texturing, as there
         * may be a texture in effect from a higher or lower level.
         */
        
        /**
         * Returns true if texturing has been specifically enabled on this particular
         * node for the indicated stage.  This means that someone called set_texture()
         * on this node with the indicated stage name, or the stage_name is the
         * default stage_name, and someone called set_texture() on this node.
         */
        """
        pass

    def has_texture_off(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_texture_off(NodePath self)
        has_texture_off(NodePath self, TextureStage stage)
        
        /**
         * Returns true if texturing has been specifically disabled on this particular
         * node via set_texture_off(), false otherwise.  This is not the same thing as
         * asking whether the geometry at this node will be rendered untextured, as
         * there may be a texture in effect from a higher or lower level.
         */
        
        /**
         * Returns true if texturing has been specifically disabled on this particular
         * node for the indicated stage.  This means that someone called
         * set_texture_off() on this node with the indicated stage name, or that
         * someone called set_texture_off() on this node to remove all stages.
         */
        """
        pass

    def has_tex_gen(self, NodePath_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_tex_gen(NodePath self, TextureStage stage)
        
        /**
         * Returns true if there is a mode for automatic texture coordinate generation
         * on the current node for the given stage.
         */
        """
        pass

    def has_tex_projector(self, NodePath_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_tex_projector(NodePath self, TextureStage stage)
        
        /**
         * Returns true if this node has a TexProjectorEffect for the indicated stage,
         * false otherwise.
         */
        """
        pass

    def has_tex_transform(self, NodePath_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_tex_transform(NodePath self, TextureStage stage)
        
        /**
         * Returns true if there is an explicit texture matrix on the current node for
         * the given stage.
         */
        """
        pass

    def has_transparency(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_transparency(NodePath self)
        
        /**
         * Returns true if a transparent-rendering adjustment has been explicitly set
         * on this particular node via set_transparency().  If this returns true, then
         * get_transparency() may be called to determine whether transparency has been
         * explicitly enabled or explicitly disabled for this node.
         */
        """
        pass

    def has_two_sided(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_two_sided(NodePath self)
        
        /**
         * Returns true if a two-sided adjustment has been explicitly set on this
         * particular node via set_two_sided().  If this returns true, then
         * get_two_sided() may be called to determine which has been set.
         */
        """
        pass

    def has_vertex_column(self, NodePath_self, const_InternalName_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_vertex_column(NodePath self, const InternalName name)
        
        /**
         * Returns true if there are at least some vertices at this node and below
         * that contain a reference to the indicated vertex data column name, false
         * otherwise.
         *
         * This is particularly useful for testing whether a particular model has a
         * given texture coordinate set (but see has_texcoord()).
         */
        """
        pass

    def headsUp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        heads_up(const NodePath self, const NodePath other)
        heads_up(const NodePath self, const LPoint3f point)
        heads_up(const NodePath self, const NodePath other, const LPoint3f point)
        heads_up(const NodePath self, const LPoint3f point, const LVector3f up)
        heads_up(const NodePath self, const NodePath other, const LPoint3f point, const LVector3f up)
        heads_up(const NodePath self, float x, float y, float z)
        heads_up(const NodePath self, const NodePath other, float x, float y, float z)
        
        /**
         * Behaves like look_at(), but with a strong preference to keeping the up
         * vector oriented in the indicated "up" direction.
         */
        
        /**
         * Behaves like look_at(), but with a strong preference to keeping the up
         * vector oriented in the indicated "up" direction.
         */
        
        /**
         * Behaves like look_at(), but with a strong preference to keeping the up
         * vector oriented in the indicated "up" direction.
         */
        
        /**
         * Behaves like look_at(), but with a strong preference to keeping the up
         * vector oriented in the indicated "up" direction.
         */
        """
        pass

    def heads_up(self, const_NodePath_self, const_NodePath_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        heads_up(const NodePath self, const NodePath other)
        heads_up(const NodePath self, const LPoint3f point)
        heads_up(const NodePath self, const NodePath other, const LPoint3f point)
        heads_up(const NodePath self, const LPoint3f point, const LVector3f up)
        heads_up(const NodePath self, const NodePath other, const LPoint3f point, const LVector3f up)
        heads_up(const NodePath self, float x, float y, float z)
        heads_up(const NodePath self, const NodePath other, float x, float y, float z)
        
        /**
         * Behaves like look_at(), but with a strong preference to keeping the up
         * vector oriented in the indicated "up" direction.
         */
        
        /**
         * Behaves like look_at(), but with a strong preference to keeping the up
         * vector oriented in the indicated "up" direction.
         */
        
        /**
         * Behaves like look_at(), but with a strong preference to keeping the up
         * vector oriented in the indicated "up" direction.
         */
        
        /**
         * Behaves like look_at(), but with a strong preference to keeping the up
         * vector oriented in the indicated "up" direction.
         */
        """
        pass

    def hide(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        hide(const NodePath self)
        hide(const NodePath self, BitMask camera_mask)
        
        /**
         * Makes the referenced node (and the entire subgraph below this node)
         * invisible to all cameras.  It remains part of the scene graph, its bounding
         * volume still contributes to its parent's bounding volume, and it will still
         * be involved in collision tests.
         *
         * To undo this, call show().
         */
        
        /**
         * Makes the referenced node invisible just to the cameras whose camera_mask
         * shares the indicated bits.
         *
         * This will also hide any nodes below this node in the scene graph, including
         * those nodes for which show() has been called, but it will not hide
         * descendent nodes for which show_through() has been called.
         */
        """
        pass

    def hideBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        hide_bounds(const NodePath self)
        
        /**
         * Stops the rendering of the bounding volume begun with show_bounds().
         */
        """
        pass

    def hide_bounds(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        hide_bounds(const NodePath self)
        
        /**
         * Stops the rendering of the bounding volume begun with show_bounds().
         */
        """
        pass

    def instanceTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        instance_to(NodePath self, const NodePath other, int sort, Thread current_thread)
        
        /**
         * Adds the referenced node of the NodePath as a child of the referenced node
         * of the indicated other NodePath.  Any other parent-child relations of the
         * node are unchanged; in particular, the node is not removed from its
         * existing parent, if any.
         *
         * If the node already had an existing parent, this method will create a new
         * instance of the node within the scene graph.
         *
         * This does not change the NodePath itself, but does return a new NodePath
         * that reflects the new instance node.
         *
         * If the destination NodePath is empty, this creates a new instance which is
         * not yet parented to any node.  A new instance of this sort cannot easily be
         * differentiated from other similar instances, but it is nevertheless a
         * different instance and it will return a different get_id() value.
         *
         * If the referenced node is already a child of the indicated NodePath,
         * returns that already-existing instance, unstashing it first if necessary.
         */
        """
        pass

    def instanceUnderNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        instance_under_node(NodePath self, const NodePath other, str name, int sort, Thread current_thread)
        
        /**
         * Behaves like instance_to(), but implicitly creates a new node to instance
         * the geometry under, and returns a NodePath to that new node.  This allows
         * the programmer to set a unique state and/or transform on this instance.
         */
        """
        pass

    def instance_to(self, NodePath_self, const_NodePath_other, int_sort, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        instance_to(NodePath self, const NodePath other, int sort, Thread current_thread)
        
        /**
         * Adds the referenced node of the NodePath as a child of the referenced node
         * of the indicated other NodePath.  Any other parent-child relations of the
         * node are unchanged; in particular, the node is not removed from its
         * existing parent, if any.
         *
         * If the node already had an existing parent, this method will create a new
         * instance of the node within the scene graph.
         *
         * This does not change the NodePath itself, but does return a new NodePath
         * that reflects the new instance node.
         *
         * If the destination NodePath is empty, this creates a new instance which is
         * not yet parented to any node.  A new instance of this sort cannot easily be
         * differentiated from other similar instances, but it is nevertheless a
         * different instance and it will return a different get_id() value.
         *
         * If the referenced node is already a child of the indicated NodePath,
         * returns that already-existing instance, unstashing it first if necessary.
         */
        """
        pass

    def instance_under_node(self, NodePath_self, const_NodePath_other, str_name, int_sort, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        instance_under_node(NodePath self, const NodePath other, str name, int sort, Thread current_thread)
        
        /**
         * Behaves like instance_to(), but implicitly creates a new node to instance
         * the geometry under, and returns a NodePath to that new node.  This allows
         * the programmer to set a unique state and/or transform on this instance.
         */
        """
        pass

    def isAncestorOf(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_ancestor_of(NodePath self, const NodePath other, Thread current_thread)
        
        /**
         * Returns true if the node represented by this NodePath is a parent or other
         * ancestor of the other NodePath, or false if it is not.
         */
        """
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(NodePath self)
        
        // Methods to query a NodePath's contents.
        
        /**
         * Returns true if the NodePath contains no nodes.
         */
        """
        pass

    def isHidden(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_hidden(NodePath self, BitMask camera_mask)
        
        /**
         * Returns true if the referenced node is hidden from the indicated camera(s)
         * either directly, or because some ancestor is hidden.
         */
        """
        pass

    def isSameGraph(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_same_graph(NodePath self, const NodePath other, Thread current_thread)
        
        /**
         * Returns true if the node represented by this NodePath is parented within
         * the same graph as that of the other NodePath.  This is essentially the same
         * thing as asking whether get_top() of both NodePaths is the same (e.g., both
         * "render").
         */
        """
        pass

    def isSingleton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_singleton(NodePath self, Thread current_thread)
        
        /**
         * Returns true if the NodePath contains exactly one node.
         */
        """
        pass

    def isStashed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_stashed(NodePath self)
        
        /**
         * Returns true if the referenced node is stashed either directly, or because
         * some ancestor is stashed.
         */
        """
        pass

    def is_ancestor_of(self, NodePath_self, const_NodePath_other, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_ancestor_of(NodePath self, const NodePath other, Thread current_thread)
        
        /**
         * Returns true if the node represented by this NodePath is a parent or other
         * ancestor of the other NodePath, or false if it is not.
         */
        """
        pass

    def is_empty(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(NodePath self)
        
        // Methods to query a NodePath's contents.
        
        /**
         * Returns true if the NodePath contains no nodes.
         */
        """
        pass

    def is_hidden(self, NodePath_self, BitMask_camera_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_hidden(NodePath self, BitMask camera_mask)
        
        /**
         * Returns true if the referenced node is hidden from the indicated camera(s)
         * either directly, or because some ancestor is hidden.
         */
        """
        pass

    def is_same_graph(self, NodePath_self, const_NodePath_other, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_same_graph(NodePath self, const NodePath other, Thread current_thread)
        
        /**
         * Returns true if the node represented by this NodePath is parented within
         * the same graph as that of the other NodePath.  This is essentially the same
         * thing as asking whether get_top() of both NodePaths is the same (e.g., both
         * "render").
         */
        """
        pass

    def is_singleton(self, NodePath_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_singleton(NodePath self, Thread current_thread)
        
        /**
         * Returns true if the NodePath contains exactly one node.
         */
        """
        pass

    def is_stashed(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_stashed(NodePath self)
        
        /**
         * Returns true if the referenced node is stashed either directly, or because
         * some ancestor is stashed.
         */
        """
        pass

    def listTags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        list_tags(NodePath self)
        
        /**
         * Lists the tags to the nout stream, one per line.  See
         * PandaNode::list_tags() for a variant that allows you to specify the output
         * stream.
         */
        """
        pass

    def list_tags(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        list_tags(NodePath self)
        
        /**
         * Lists the tags to the nout stream, one per line.  See
         * PandaNode::list_tags() for a variant that allows you to specify the output
         * stream.
         */
        """
        pass

    def lookAt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        look_at(const NodePath self, const NodePath other)
        look_at(const NodePath self, const LPoint3f point)
        look_at(const NodePath self, const NodePath other, const LPoint3f point)
        look_at(const NodePath self, const LPoint3f point, const LVector3f up)
        look_at(const NodePath self, const NodePath other, const LPoint3f point, const LVector3f up)
        look_at(const NodePath self, float x, float y, float z)
        look_at(const NodePath self, const NodePath other, float x, float y, float z)
        
        /**
         * Sets the transform on this NodePath so that it rotates to face the
         * indicated point in space.  This will overwrite any previously existing
         * scale on the node, although it will preserve any translation.
         */
        
        /**
         * Sets the hpr on this NodePath so that it rotates to face the indicated
         * point in space, which is relative to the other NodePath.
         */
        
        /**
         * Sets the hpr on this NodePath so that it rotates to face the indicated
         * point in space.
         */
        
        /**
         * Sets the transform on this NodePath so that it rotates to face the
         * indicated point in space, which is relative to the other NodePath.
         */
        """
        pass

    def look_at(self, const_NodePath_self, const_NodePath_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        look_at(const NodePath self, const NodePath other)
        look_at(const NodePath self, const LPoint3f point)
        look_at(const NodePath self, const NodePath other, const LPoint3f point)
        look_at(const NodePath self, const LPoint3f point, const LVector3f up)
        look_at(const NodePath self, const NodePath other, const LPoint3f point, const LVector3f up)
        look_at(const NodePath self, float x, float y, float z)
        look_at(const NodePath self, const NodePath other, float x, float y, float z)
        
        /**
         * Sets the transform on this NodePath so that it rotates to face the
         * indicated point in space.  This will overwrite any previously existing
         * scale on the node, although it will preserve any translation.
         */
        
        /**
         * Sets the hpr on this NodePath so that it rotates to face the indicated
         * point in space, which is relative to the other NodePath.
         */
        
        /**
         * Sets the hpr on this NodePath so that it rotates to face the indicated
         * point in space.
         */
        
        /**
         * Sets the transform on this NodePath so that it rotates to face the
         * indicated point in space, which is relative to the other NodePath.
         */
        """
        pass

    def ls(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ls(NodePath self)
        ls(NodePath self, ostream out, int indent_level)
        
        /**
         * Lists the hierarchy at and below the referenced node.
         */
        
        /**
         * Lists the hierarchy at and below the referenced node.
         */
        """
        pass

    def node(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        node(NodePath self)
        
        /**
         * Returns the referenced node of the path.
         */
        """
        pass

    def notFound(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        not_found()
        
        /**
         * Creates a NodePath with the ET_not_found error type set.
         */
        """
        pass

    def not_found(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        not_found()
        
        /**
         * Creates a NodePath with the ET_not_found error type set.
         */
        """
        pass

    def output(self, NodePath_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(NodePath self, ostream out)
        
        /**
         * Writes a sensible description of the NodePath to the indicated output
         * stream.
         */
        """
        pass

    def premungeScene(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        premunge_scene(const NodePath self, GraphicsStateGuardianBase gsg)
        
        /**
         * Walks through the scene graph beginning at the bottom node, and internally
         * adjusts any GeomVertexFormats for optimal rendering on the indicated GSG.
         * If this step is not done prior to rendering, the formats will be optimized
         * at render time instead, for a small cost.
         *
         * It is not normally necessary to do this on a model loaded directly from
         * disk, since the loader will do this by default.
         */
        """
        pass

    def premunge_scene(self, const_NodePath_self, GraphicsStateGuardianBase_gsg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        premunge_scene(const NodePath self, GraphicsStateGuardianBase gsg)
        
        /**
         * Walks through the scene graph beginning at the bottom node, and internally
         * adjusts any GeomVertexFormats for optimal rendering on the indicated GSG.
         * If this step is not done prior to rendering, the formats will be optimized
         * at render time instead, for a small cost.
         *
         * It is not normally necessary to do this on a model loaded directly from
         * disk, since the loader will do this by default.
         */
        """
        pass

    def prepareScene(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        prepare_scene(const NodePath self, GraphicsStateGuardianBase gsg)
        
        /**
         * Walks through the scene graph beginning at the bottom node, and does
         * whatever initialization is required to render the scene properly with the
         * indicated GSG.  It is not strictly necessary to call this, since the GSG
         * will initialize itself when the scene is rendered, but this may take some
         * of the overhead away from that process.
         *
         * In particular, this will ensure that textures and vertex buffers within the
         * scene are loaded into graphics memory.
         */
        """
        pass

    def prepare_scene(self, const_NodePath_self, GraphicsStateGuardianBase_gsg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare_scene(const NodePath self, GraphicsStateGuardianBase gsg)
        
        /**
         * Walks through the scene graph beginning at the bottom node, and does
         * whatever initialization is required to render the scene properly with the
         * indicated GSG.  It is not strictly necessary to call this, since the GSG
         * will initialize itself when the scene is rendered, but this may take some
         * of the overhead away from that process.
         *
         * In particular, this will ensure that textures and vertex buffers within the
         * scene are loaded into graphics memory.
         */
        """
        pass

    def projectTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        project_texture(const NodePath self, TextureStage stage, Texture tex, const NodePath projector)
        
        /**
         * A convenience function to enable projective texturing at this node level
         * and below, using the indicated NodePath (which should contain a LensNode)
         * as the projector.
         */
        """
        pass

    def project_texture(self, const_NodePath_self, TextureStage_stage, Texture_tex, const_NodePath_projector): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        project_texture(const NodePath self, TextureStage stage, Texture tex, const NodePath projector)
        
        /**
         * A convenience function to enable projective texturing at this node level
         * and below, using the indicated NodePath (which should contain a LensNode)
         * as the projector.
         */
        """
        pass

    def removed(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        removed()
        
        /**
         * Creates a NodePath with the ET_removed error type set.
         */
        """
        pass

    def removeNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_node(const NodePath self, Thread current_thread)
        
        /**
         * Disconnects the referenced node from the scene graph.  This will also
         * delete the node if there are no other pointers to it.
         *
         * Normally, this should be called only when you are really done with the
         * node.  If you want to remove a node from the scene graph but keep it around
         * for later, you should probably use detach_node() instead.
         *
         * In practice, the only difference between remove_node() and detach_node() is
         * that remove_node() also resets the NodePath to empty, which will cause the
         * node to be deleted immediately if there are no other references.  On the
         * other hand, detach_node() leaves the NodePath referencing the node, which
         * will keep at least one reference to the node for as long as the NodePath
         * exists.
         */
        """
        pass

    def remove_node(self, const_NodePath_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_node(const NodePath self, Thread current_thread)
        
        /**
         * Disconnects the referenced node from the scene graph.  This will also
         * delete the node if there are no other pointers to it.
         *
         * Normally, this should be called only when you are really done with the
         * node.  If you want to remove a node from the scene graph but keep it around
         * for later, you should probably use detach_node() instead.
         *
         * In practice, the only difference between remove_node() and detach_node() is
         * that remove_node() also resets the NodePath to empty, which will cause the
         * node to be deleted immediately if there are no other references.  On the
         * other hand, detach_node() leaves the NodePath referencing the node, which
         * will keep at least one reference to the node for as long as the NodePath
         * exists.
         */
        """
        pass

    def reparentTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reparent_to(const NodePath self, const NodePath other, int sort, Thread current_thread)
        
        // Methods that actually move nodes around in the scene graph.  The optional
        // "sort" parameter can be used to force a particular ordering between
        // sibling nodes, useful when dealing with LOD's and similar switch nodes.
        // If the sort value is the same, nodes will be arranged in the order they
        // were added.
        
        /**
         * Removes the referenced node of the NodePath from its current parent and
         * attaches it to the referenced node of the indicated NodePath.
         *
         * If the destination NodePath is empty, this is the same thing as
         * detach_node().
         *
         * If the referenced node is already a child of the indicated NodePath (via
         * some other instance), this operation fails and leaves the NodePath
         * detached.
         */
        """
        pass

    def reparent_to(self, const_NodePath_self, const_NodePath_other, int_sort, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reparent_to(const NodePath self, const NodePath other, int sort, Thread current_thread)
        
        // Methods that actually move nodes around in the scene graph.  The optional
        // "sort" parameter can be used to force a particular ordering between
        // sibling nodes, useful when dealing with LOD's and similar switch nodes.
        // If the sort value is the same, nodes will be arranged in the order they
        // were added.
        
        /**
         * Removes the referenced node of the NodePath from its current parent and
         * attaches it to the referenced node of the indicated NodePath.
         *
         * If the destination NodePath is empty, this is the same thing as
         * detach_node().
         *
         * If the referenced node is already a child of the indicated NodePath (via
         * some other instance), this operation fails and leaves the NodePath
         * detached.
         */
        """
        pass

    def replaceMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        replace_material(const NodePath self, Material mat, Material new_mat)
        replace_material(const NodePath self, Material mat, NoneType new_mat)
        
        // Let interrogate know this also accepts None
        
        /**
         * Recursively searches the scene graph for references to the given material,
         * and replaces them with the new material.
         *
         * As of Panda3D 1.10.13, new_mat may be null to remove the material.
         *
         * @since 1.10.0
         */
        """
        pass

    def replaceTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        replace_texture(const NodePath self, Texture tex, Texture new_tex)
        replace_texture(const NodePath self, Texture tex, NoneType new_tex)
        
        // Let interrogate know this also accepts None
        
        /**
         * Recursively searches the scene graph for references to the given texture,
         * and replaces them with the new texture.
         *
         * As of Panda3D 1.10.13, new_tex may be null to remove the texture.
         *
         * @since 1.10.4
         */
        """
        pass

    def replace_material(self, const_NodePath_self, Material_mat, Material_new_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        replace_material(const NodePath self, Material mat, Material new_mat)
        replace_material(const NodePath self, Material mat, NoneType new_mat)
        
        // Let interrogate know this also accepts None
        
        /**
         * Recursively searches the scene graph for references to the given material,
         * and replaces them with the new material.
         *
         * As of Panda3D 1.10.13, new_mat may be null to remove the material.
         *
         * @since 1.10.0
         */
        """
        pass

    def replace_texture(self, const_NodePath_self, Texture_tex, Texture_new_tex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        replace_texture(const NodePath self, Texture tex, Texture new_tex)
        replace_texture(const NodePath self, Texture tex, NoneType new_tex)
        
        // Let interrogate know this also accepts None
        
        /**
         * Recursively searches the scene graph for references to the given texture,
         * and replaces them with the new texture.
         *
         * As of Panda3D 1.10.13, new_tex may be null to remove the texture.
         *
         * @since 1.10.4
         */
        """
        pass

    def reverseLs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reverse_ls(NodePath self)
        reverse_ls(NodePath self, ostream out, int indent_level)
        
        /**
         * Lists the hierarchy at and above the referenced node.
         */
        
        /**
         * Lists the hierarchy at and above the referenced node.
         */
        """
        pass

    def reverse_ls(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reverse_ls(NodePath self)
        reverse_ls(NodePath self, ostream out, int indent_level)
        
        /**
         * Lists the hierarchy at and above the referenced node.
         */
        
        /**
         * Lists the hierarchy at and above the referenced node.
         */
        """
        pass

    def setAllColorScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_all_color_scale(const NodePath self, float scale, int priority)
        
        /**
         * Scales all the color components of the object by the same amount, darkening
         * the object, without (much) affecting alpha.  Note that any priority
         * specified will also apply to the alpha scale.
         */
        """
        pass

    def setAlphaScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_alpha_scale(const NodePath self, float scale, int priority)
        
        /**
         * Sets the alpha scale component of the transform without (much) affecting
         * the color scale.  Note that any priority specified will also apply to the
         * color scale.
         */
        """
        pass

    def setAntialias(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_antialias(const NodePath self, int mode, int priority)
        
        /**
         * Specifies the antialiasing type that should be applied at this node and
         * below.  See AntialiasAttrib.
         */
        """
        pass

    def setAttrib(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_attrib(const NodePath self, const RenderAttrib attrib, int priority)
        
        /**
         * Adds the indicated render attribute to the scene graph on this node.  This
         * attribute will now apply to this node and everything below.  If there was
         * already an attribute of the same type, it is replaced.
         */
        """
        pass

    def setAudioVolume(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_audio_volume(const NodePath self, float volume, int priority)
        
        /**
         * Sets the audio volume component of the transform
         */
        """
        pass

    def setAudioVolumeOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_audio_volume_off(const NodePath self, int priority)
        
        /**
         * Disables any audio volume attribute inherited from above.  This is not the
         * same thing as clear_audio_volume(), which undoes any previous
         * set_audio_volume() operation on this node; rather, this actively disables
         * any set_audio_volume() that might be inherited from a parent node.
         *
         * It is legal to specify a new volume on the same node with a subsequent call
         * to set_audio_volume(); this new scale will apply to lower nodes.
         */
        """
        pass

    def setBillboardAxis(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_billboard_axis(const NodePath self)
        set_billboard_axis(const NodePath self, float offset)
        set_billboard_axis(const NodePath self, const NodePath camera, float offset)
        
        /**
         * Puts a billboard transition on the node such that it will rotate in two
         * dimensions around the up axis.
         */
        
        /**
         * Puts a billboard transition on the node such that it will rotate in two
         * dimensions around the up axis, towards a specified "camera" instead of to
         * the viewing camera.
         */
        """
        pass

    def setBillboardPointEye(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_billboard_point_eye(const NodePath self)
        set_billboard_point_eye(const NodePath self, float offset)
        set_billboard_point_eye(const NodePath self, const NodePath camera, float offset, bool fixed_depth)
        set_billboard_point_eye(const NodePath self, float offset, bool fixed_depth)
        
        /**
         * Puts a billboard transition on the node such that it will rotate in three
         * dimensions about the origin, keeping its up vector oriented to the top of
         * the camera.
         */
        
        /**
         * Puts a billboard transition on the node such that it will rotate in three
         * dimensions about the origin, keeping its up vector oriented to the top of
         * the camera, towards a specified "camera" instead of to the viewing camera.
         */
        """
        pass

    def setBillboardPointWorld(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_billboard_point_world(const NodePath self)
        set_billboard_point_world(const NodePath self, float offset)
        set_billboard_point_world(const NodePath self, const NodePath camera, float offset)
        
        /**
         * Puts a billboard transition on the node such that it will rotate in three
         * dimensions about the origin, keeping its up vector oriented to the sky.
         */
        
        /**
         * Puts a billboard transition on the node such that it will rotate in three
         * dimensions about the origin, keeping its up vector oriented to the sky,
         * towards a specified "camera" instead of to the viewing camera.
         */
        """
        pass

    def setBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bin(const NodePath self, str bin_name, int draw_order, int priority)
        
        /**
         * Assigns the geometry at this level and below to the named rendering bin.
         * It is the user's responsibility to ensure that such a bin already exists,
         * either via the cull-bin Configrc variable, or by explicitly creating a
         * GeomBin of the appropriate type at runtime.
         *
         * There are two default bins created when Panda is started: "default" and
         * "fixed".  Normally, all geometry is assigned to "default" unless specified
         * otherwise.  This bin renders opaque geometry in state-sorted order,
         * followed by transparent geometry sorted back-to-front.  If any geometry is
         * assigned to "fixed", this will be rendered following all the geometry in
         * "default", in the order specified by draw_order for each piece of geometry
         * so assigned.
         *
         * The draw_order parameter is meaningful only for GeomBinFixed type bins,
         * e.g.  "fixed".  Other kinds of bins ignore it.
         */
        """
        pass

    def setClipPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_clip_plane(const NodePath self, const NodePath clip_plane, int priority)
        
        /**
         * Adds the indicated clipping plane to the list of planes that apply to
         * geometry at this node and below.  The clipping plane itself, a PlaneNode,
         * should be parented into the scene graph elsewhere, to represent the plane's
         * position in space; but until set_clip_plane() is called it will clip no
         * geometry.
         */
        """
        pass

    def setClipPlaneOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_clip_plane_off(const NodePath self)
        set_clip_plane_off(const NodePath self, const NodePath clip_plane, int priority)
        set_clip_plane_off(const NodePath self, int priority)
        
        /**
         * Sets the geometry at this level and below to render using no clip_planes at
         * all.  This is different from not specifying a clip_plane; rather, this
         * specifically contradicts set_clip_plane() at a higher node level (or, with
         * a priority, overrides a set_clip_plane() at a lower level).
         *
         * If no clip_planes are in effect on a particular piece of geometry, that
         * geometry is rendered without being clipped (other than by the viewing
         * frustum).
         */
        
        /**
         * Sets the geometry at this level and below to render without being clipped
         * by the indicated PlaneNode.  This is different from not specifying the
         * PlaneNode; rather, this specifically contradicts set_clip_plane() at a
         * higher node level (or, with a priority, overrides a set_clip_plane() at a
         * lower level).
         */
        """
        pass

    def setCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_collide_mask(const NodePath self, BitMask new_mask, BitMask bits_to_change, TypeHandle node_type)
        
        /**
         * Recursively applies the indicated CollideMask to the into_collide_masks for
         * all nodes at this level and below.  If node_type is not TypeHandle::none(),
         * then only nodes matching (or inheriting from) the indicated PandaNode
         * subclass are modified.
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
        set_color(const NodePath self, const LVecBase4f color)
        set_color(const NodePath self, const LVecBase4f color, int priority)
        set_color(const NodePath self, float r, float g, float b, float a, int priority)
        
        /**
         * Applies a scene-graph color to the referenced node.  This color will apply
         * to all geometry at this level and below (that does not specify a new color
         * or a set_color_off()).
         */
        
        /**
         * Applies a scene-graph color to the referenced node.  This color will apply
         * to all geometry at this level and below (that does not specify a new color
         * or a set_color_off()).
         */
        """
        pass

    def setColorOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color_off(const NodePath self, int priority)
        
        /**
         * Sets the geometry at this level and below to render using the geometry
         * color.  This is normally the default, but it may be useful to use this to
         * contradict set_color() at a higher node level (or, with a priority, to
         * override a set_color() at a lower level).
         */
        """
        pass

    def setColorScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color_scale(const NodePath self, const LVecBase4f scale)
        set_color_scale(const NodePath self, const LVecBase4f scale, int priority)
        set_color_scale(const NodePath self, float sx, float sy, float sz, float sa, int priority)
        
        /**
         * Sets the color scale component of the transform
         */
        
        /**
         * Sets the color scale component of the transform, leaving translation and
         * rotation untouched.
         */
        """
        pass

    def setColorScaleOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color_scale_off(const NodePath self, int priority)
        
        /**
         * Disables any color scale attribute inherited from above.  This is not the
         * same thing as clear_color_scale(), which undoes any previous
         * set_color_scale() operation on this node; rather, this actively disables
         * any set_color_scale() that might be inherited from a parent node.  This
         * also disables set_alpha_scale() at the same time.
         *
         * It is legal to specify a new color scale on the same node with a subsequent
         * call to set_color_scale() or set_alpha_scale(); this new scale will apply
         * to lower geometry.
         */
        """
        pass

    def setCompass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_compass(const NodePath self, const NodePath reference)
        
        /**
         * Puts a compass effect on the node, so that it will retain a fixed rotation
         * relative to the reference node (or render if the reference node is empty)
         * regardless of the transforms above it.
         */
        """
        pass

    def setDepthOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_depth_offset(const NodePath self, int bias, int priority)
        
        /**
         * This instructs the graphics driver to apply an offset or bias to the
         * generated depth values for rendered polygons, before they are written to
         * the depth buffer.  This can be used to shift polygons forward slightly, to
         * resolve depth conflicts, or self-shadowing artifacts on thin objects.  The
         * bias is always an integer number, and each integer increment represents the
         * smallest possible increment in Z that is sufficient to completely resolve
         * two coplanar polygons.  Positive numbers are closer towards the camera.
         */
        """
        pass

    def setDepthTest(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_depth_test(const NodePath self, bool depth_test, int priority)
        
        /**
         * Specifically sets or disables the testing of the depth buffer on this
         * particular node.  This is normally on in the 3-d scene graph and off in the
         * 2-d scene graph; it should be on for rendering most 3-d objects properly.
         */
        """
        pass

    def setDepthWrite(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_depth_write(const NodePath self, bool depth_write, int priority)
        
        /**
         * Specifically sets or disables the writing to the depth buffer on this
         * particular node.  This is normally on in the 3-d scene graph and off in the
         * 2-d scene graph; it should be on for rendering most 3-d objects properly.
         */
        """
        pass

    def setEffect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_effect(const NodePath self, const RenderEffect effect)
        
        /**
         * Adds the indicated render effect to the scene graph on this node.  If there
         * was already an effect of the same type, it is replaced.
         */
        """
        pass

    def setEffects(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_effects(const NodePath self, const RenderEffects effects)
        
        /**
         * Sets the complete RenderEffects that will be applied this node.  This
         * completely replaces whatever has been set on this node via repeated calls
         * to set_attrib().
         */
        """
        pass

    def setFluidPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fluid_pos(const NodePath self, const LVecBase3f pos)
        set_fluid_pos(const NodePath self, const NodePath other, const LVecBase3f pos)
        set_fluid_pos(const NodePath self, float x, float y, float z)
        set_fluid_pos(const NodePath self, const NodePath other, float x, float y, float z)
        
        /**
         * Sets the translation component, without changing the "previous" position,
         * so that the collision system will see the node as moving fluidly from its
         * previous position to its new position.
         */
        
        /**
         * Sets the translation component, without changing the "previous" position,
         * so that the collision system will see the node as moving fluidly from its
         * previous position to its new position.
         */
        
        /**
         * Sets the translation component, without changing the "previous" position,
         * so that the collision system will see the node as moving fluidly from its
         * previous position to its new position.  See Also: NodePath::set_pos
         */
        
        /**
         * Sets the translation component of the transform, relative to the other
         * node.
         */
        """
        pass

    def setFluidX(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fluid_x(const NodePath self, float x)
        set_fluid_x(const NodePath self, const NodePath other, float x)
        """
        pass

    def setFluidY(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fluid_y(const NodePath self, float y)
        set_fluid_y(const NodePath self, const NodePath other, float y)
        """
        pass

    def setFluidZ(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fluid_z(const NodePath self, float z)
        set_fluid_z(const NodePath self, const NodePath other, float z)
        """
        pass

    def setFog(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fog(const NodePath self, Fog fog, int priority)
        
        /**
         * Sets the geometry at this level and below to render using the indicated
         * fog.
         */
        """
        pass

    def setFogOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fog_off(const NodePath self, int priority)
        
        /**
         * Sets the geometry at this level and below to render using no fog.  This is
         * normally the default, but it may be useful to use this to contradict
         * set_fog() at a higher node level (or, with a priority, to override a
         * set_fog() at a lower level).
         */
        """
        pass

    def setH(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_h(const NodePath self, float h)
        set_h(const NodePath self, const NodePath other, float h)
        """
        pass

    def setHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_hpr(const NodePath self, const LVecBase3f hpr)
        set_hpr(const NodePath self, const NodePath other, const LVecBase3f hpr)
        set_hpr(const NodePath self, float h, float p, float r)
        set_hpr(const NodePath self, const NodePath other, float h, float p, float r)
        
        /**
         * Sets the rotation component of the transform, leaving translation and scale
         * untouched.
         */
        
        /**
         * Sets the rotation component of the transform, relative to the other node.
         */
        
        /**
         * Sets the rotation component of the transform, leaving translation and scale
         * untouched.
         */
        
        /**
         * Sets the rotation component of the transform, relative to the other node.
         */
        """
        pass

    def setHprScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_hpr_scale(const NodePath self, const LVecBase3f hpr, const LVecBase3f scale)
        set_hpr_scale(const NodePath self, const NodePath other, const LVecBase3f hpr, const LVecBase3f scale)
        set_hpr_scale(const NodePath self, float h, float p, float r, float sx, float sy, float sz)
        set_hpr_scale(const NodePath self, const NodePath other, float h, float p, float r, float sx, float sy, float sz)
        
        /**
         * Sets the rotation and scale components of the transform, leaving
         * translation untouched.
         */
        
        /**
         * Sets the rotation and scale components of the transform, leaving
         * translation untouched.  This, or set_pos_hpr_scale, is the preferred way to
         * update a transform when both hpr and scale are to be changed.
         */
        
        /**
         * Sets the rotation and scale components of the transform, leaving
         * translation untouched.
         */
        
        /**
         * Sets the rotation and scale components of the transform, leaving
         * translation untouched.  This, or set_pos_hpr_scale, is the preferred way to
         * update a transform when both hpr and scale are to be changed.
         */
        """
        pass

    def setInstanceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_instance_count(const NodePath self, int instance_count)
        
        /**
         * Sets the geometry instance count, or 0 if geometry instancing should be
         * disabled.  Do not confuse with instanceTo which only applies to animation
         * instancing.
         */
        """
        pass

    def setLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_light(const NodePath self, const NodePath light, int priority)
        
        /**
         * Adds the indicated Light or PolylightNode to the list of lights that
         * illuminate geometry at this node and below.  The light itself should be
         * parented into the scene graph elsewhere, to represent the light's position
         * in space; but until set_light() is called it will illuminate no geometry.
         */
        """
        pass

    def setLightOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_light_off(const NodePath self)
        set_light_off(const NodePath self, const NodePath light, int priority)
        set_light_off(const NodePath self, int priority)
        
        /**
         * Sets the geometry at this level and below to render using no lights at all.
         * This is different from not specifying a light; rather, this specifically
         * contradicts set_light() at a higher node level (or, with a priority,
         * overrides a set_light() at a lower level).
         *
         * If no lights are in effect on a particular piece of geometry, that geometry
         * is rendered with lighting disabled.
         */
        
        /**
         * Sets the geometry at this level and below to render without using the
         * indicated Light.  This is different from not specifying the Light; rather,
         * this specifically contradicts set_light() at a higher node level (or, with
         * a priority, overrides a set_light() at a lower level).
         *
         * This interface does not support PolylightNodes, which cannot be turned off
         * at a lower level.
         */
        """
        pass

    def setLogicOp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_logic_op(const NodePath self, int op, int priority)
        
        /**
         * Specifically sets or disables a logical operation on this particular node.
         * If no other nodes override, this will cause geometry to be rendered without
         * color blending but instead using the given logical operator.
         *
         * @since 1.10.0
         */
        """
        pass

    def setMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_mat(const NodePath self, const LMatrix4f mat)
        set_mat(const NodePath self, const NodePath other, const LMatrix4f mat)
        
        /**
         * Directly sets an arbitrary 4x4 transform matrix.
         */
        
        /**
         * Converts the indicated matrix from the other's coordinate space to the
         * local coordinate space, and applies it to the node.
         */
        """
        pass

    def setMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_material(const NodePath self, Material tex, int priority)
        
        /**
         * Sets the geometry at this level and below to render using the indicated
         * material.
         *
         * Previously, this operation made a copy of the material structure, but
         * nowadays it assigns the pointer directly.
         */
        """
        pass

    def setMaterialOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_material_off(const NodePath self, int priority)
        
        /**
         * Sets the geometry at this level and below to render using no material.
         * This is normally the default, but it may be useful to use this to
         * contradict set_material() at a higher node level (or, with a priority, to
         * override a set_material() at a lower level).
         */
        """
        pass

    def setMaxSearchDepth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_search_depth(int max_search_depth)
        
        /**
         * Certain operations, such as find() or find_all_matches(), require a
         * traversal of the scene graph to search for the target node or nodes.  This
         * traversal does not attempt to detect cycles, so an arbitrary cap is set on
         * the depth of the traversal as a poor man's cycle detection, in the event
         * that a cycle has inadvertently been introduced into the scene graph.
         *
         * There may be other reasons you'd want to truncate a search before the
         * bottom of the scene graph has been reached.  In any event, this function
         * sets the limit on the number of levels that a traversal will continue, and
         * hence the maximum length of a path that may be returned by a traversal.
         *
         * This is a static method, and so changing this parameter affects all of the
         * NodePaths in the universe.
         */
        """
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_name(const NodePath self, str name)
        
        /**
         * Changes the name of the referenced node.
         */
        """
        pass

    def setOccluder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_occluder(const NodePath self, const NodePath occluder)
        
        /**
         * Adds the indicated occluder to the list of occluders that apply to geometry
         * at this node and below.  The occluder itself, an OccluderNode, should be
         * parented into the scene graph elsewhere, to represent the occluder's
         * position in space; but until set_occluder() is called it will clip no
         * geometry.
         */
        """
        pass

    def setP(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_p(const NodePath self, float p)
        set_p(const NodePath self, const NodePath other, float p)
        """
        pass

    def setPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pos(const NodePath self, const LVecBase3f pos)
        set_pos(const NodePath self, const NodePath other, const LVecBase3f pos)
        set_pos(const NodePath self, float x, float y, float z)
        set_pos(const NodePath self, const NodePath other, float x, float y, float z)
        
        /**
         * Sets the translation component of the transform, leaving rotation and scale
         * untouched.  This also resets the node's "previous" position, so that the
         * collision system will see the node as having suddenly appeared in the new
         * position, without passing any points in between.
         */
        
        /**
         * Sets the translation component of the transform, relative to the other
         * node.
         */
        
        /**
         * Sets the translation component of the transform, leaving rotation and scale
         * untouched.  This also resets the node's "previous" position, so that the
         * collision system will see the node as having suddenly appeared in the new
         * position, without passing any points in between.  See Also:
         * NodePath::set_fluid_pos
         */
        
        /**
         * Sets the translation component of the transform, relative to the other
         * node.
         */
        """
        pass

    def setPosHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pos_hpr(const NodePath self, const LVecBase3f pos, const LVecBase3f hpr)
        set_pos_hpr(const NodePath self, const NodePath other, const LVecBase3f pos, const LVecBase3f hpr)
        set_pos_hpr(const NodePath self, float x, float y, float z, float h, float p, float r)
        set_pos_hpr(const NodePath self, const NodePath other, float x, float y, float z, float h, float p, float r)
        
        /**
         * Sets the translation and rotation component of the transform, leaving scale
         * untouched.
         */
        
        /**
         * Sets the translation and rotation component of the transform, relative to
         * the other node.
         */
        
        /**
         * Sets the translation and rotation component of the transform, leaving scale
         * untouched.
         */
        
        /**
         * Sets the translation and rotation component of the transform, relative to
         * the other node.
         */
        """
        pass

    def setPosHprScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pos_hpr_scale(const NodePath self, const LVecBase3f pos, const LVecBase3f hpr, const LVecBase3f scale)
        set_pos_hpr_scale(const NodePath self, const NodePath other, const LVecBase3f pos, const LVecBase3f hpr, const LVecBase3f scale)
        set_pos_hpr_scale(const NodePath self, float x, float y, float z, float h, float p, float r, float sx, float sy, float sz)
        set_pos_hpr_scale(const NodePath self, const NodePath other, float x, float y, float z, float h, float p, float r, float sx, float sy, float sz)
        
        /**
         * Completely replaces the transform with new translation, rotation, and scale
         * components.
         */
        
        /**
         * Completely replaces the transform with new translation, rotation, and scale
         * components, relative to the other node.
         */
        
        /**
         * Replaces the translation, rotation, and scale components, implicitly
         * setting shear to 0.
         */
        
        /**
         * Completely replaces the transform with new translation, rotation, and scale
         * components, relative to the other node, implicitly setting shear to 0.
         */
        """
        pass

    def setPosHprScaleShear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pos_hpr_scale_shear(const NodePath self, const LVecBase3f pos, const LVecBase3f hpr, const LVecBase3f scale, const LVecBase3f shear)
        set_pos_hpr_scale_shear(const NodePath self, const NodePath other, const LVecBase3f pos, const LVecBase3f hpr, const LVecBase3f scale, const LVecBase3f shear)
        
        /**
         * Completely replaces the transform with new translation, rotation, scale,
         * and shear components.
         */
        
        /**
         * Completely replaces the transform with new translation, rotation, scale,
         * and shear components, relative to the other node.
         */
        """
        pass

    def setPosQuat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pos_quat(const NodePath self, const LVecBase3f pos, const LQuaternionf quat)
        set_pos_quat(const NodePath self, const NodePath other, const LVecBase3f pos, const LQuaternionf quat)
        
        /**
         * Sets the translation and rotation component of the transform, leaving scale
         * untouched.
         */
        
        /**
         * Sets the translation and rotation component of the transform, relative to
         * the other node.
         */
        """
        pass

    def setPosQuatScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pos_quat_scale(const NodePath self, const LVecBase3f pos, const LQuaternionf quat, const LVecBase3f scale)
        set_pos_quat_scale(const NodePath self, const NodePath other, const LVecBase3f pos, const LQuaternionf quat, const LVecBase3f scale)
        
        /**
         * Replaces the translation, rotation, and scale components, implicitly
         * setting shear to 0.
         */
        
        /**
         * Completely replaces the transform with new translation, rotation, and scale
         * components, relative to the other node, implicitly setting shear to 0.
         */
        """
        pass

    def setPosQuatScaleShear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pos_quat_scale_shear(const NodePath self, const LVecBase3f pos, const LQuaternionf quat, const LVecBase3f scale, const LVecBase3f shear)
        set_pos_quat_scale_shear(const NodePath self, const NodePath other, const LVecBase3f pos, const LQuaternionf quat, const LVecBase3f scale, const LVecBase3f shear)
        
        /**
         * Completely replaces the transform with new translation, rotation, scale,
         * and shear components.
         */
        
        /**
         * Completely replaces the transform with new translation, rotation, scale,
         * and shear components, relative to the other node.
         */
        """
        pass

    def setPrevTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_prev_transform(const NodePath self, const TransformState transform)
        set_prev_transform(const NodePath self, const NodePath other, const TransformState transform, Thread current_thread)
        set_prev_transform(const NodePath self, const TransformState transform, Thread current_thread)
        
        /**
         * Sets the transform that represents this node's "previous" position, one
         * frame ago, for the purposes of detecting motion for accurate collision
         * calculations.
         */
        
        /**
         * Sets the "previous" transform object on this node, relative to the other
         * node.  This computes a new transform object that will have the indicated
         * value when seen from the other node.
         */
        """
        pass

    def setPythonTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_python_tag(const NodePath self, object keys, object value)
        """
        pass

    def setQuat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_quat(const NodePath self, const LQuaternionf quat)
        set_quat(const NodePath self, const NodePath other, const LQuaternionf quat)
        
        /**
         * Sets the rotation component of the transform, leaving translation and scale
         * untouched.
         */
        
        /**
         * Sets the rotation component of the transform, relative to the other node.
         */
        """
        pass

    def setQuatScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_quat_scale(const NodePath self, const LQuaternionf quat, const LVecBase3f scale)
        set_quat_scale(const NodePath self, const NodePath other, const LQuaternionf quat, const LVecBase3f scale)
        
        /**
         * Sets the rotation and scale components of the transform, leaving
         * translation untouched.
         */
        
        /**
         * Sets the rotation and scale components of the transform, leaving
         * translation untouched.  This, or set_pos_quat_scale, is the preferred way
         * to update a transform when both quat and scale are to be changed.
         */
        """
        pass

    def setR(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_r(const NodePath self, float r)
        set_r(const NodePath self, const NodePath other, float r)
        """
        pass

    def setRenderMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_render_mode(const NodePath self, int mode, float thickness, int priority)
        
        /**
         * Sets up the geometry at this level and below (unless overridden) to render
         * in the specified mode and with the indicated line and/or point thickness.
         */
        """
        pass

    def setRenderModeFilled(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_render_mode_filled(const NodePath self, int priority)
        
        /**
         * Sets up the geometry at this level and below (unless overridden) to render
         * in filled (i.e.  not wireframe) mode.
         */
        """
        pass

    def setRenderModeFilledWireframe(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_render_mode_filled_wireframe(const NodePath self, const LVecBase4f wireframe_color, int priority)
        
        /**
         * Sets up the geometry at this level and below (unless overridden) to render
         * in filled, but overlay the wireframe on top with a fixed color.  This is
         * useful for debug visualizations.
         */
        """
        pass

    def setRenderModePerspective(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_render_mode_perspective(const NodePath self, bool perspective, int priority)
        
        /**
         * Sets up the point geometry at this level and below to render as perspective
         * sprites (that is, billboarded quads).  The thickness, as specified with
         * set_render_mode_thickness(), is the width of each point in 3-D units,
         * unless it is overridden on a per-vertex basis.  This does not affect
         * geometry other than points.
         *
         * If you want the quads to be individually textured, you should also set a
         * TexGenAttrib::M_point_sprite on the node.
         */
        """
        pass

    def setRenderModeThickness(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_render_mode_thickness(const NodePath self, float thickness, int priority)
        
        /**
         * Sets up the point geometry at this level and below to render as thick
         * points (that is, billboarded quads).  The thickness is in pixels, unless
         * set_render_mode_perspective is also true, in which case it is in 3-D units.
         *
         * If you want the quads to be individually textured, you should also set a
         * TexGenAttrib::M_point_sprite on the node.
         */
        """
        pass

    def setRenderModeWireframe(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_render_mode_wireframe(const NodePath self, int priority)
        
        /**
         * Sets up the geometry at this level and below (unless overridden) to render
         * in wireframe mode.
         */
        """
        pass

    def setSa(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_sa(const NodePath self, float sa)
        
        /**
         * Sets the alpha component of the color scale.
         * @see set_color_scale()
         */
        """
        pass

    def setSb(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_sb(const NodePath self, float sb)
        
        /**
         * Sets the blue component of the color scale.
         * @see set_color_scale()
         */
        """
        pass

    def setScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scale(const NodePath self, const LVecBase3f scale)
        set_scale(const NodePath self, float scale)
        set_scale(const NodePath self, const NodePath other, const LVecBase3f scale)
        set_scale(const NodePath self, const NodePath other, float scale)
        set_scale(const NodePath self, float sx, float sy, float sz)
        set_scale(const NodePath self, const NodePath other, float sx, float sy, float sz)
        
        /**
         * Sets the scale component of the transform, leaving translation and rotation
         * untouched.
         */
        
        /**
         * Sets the scale component of the transform, relative to the other node.
         */
        
        /**
         * Sets the scale component of the transform, relative to the other node.
         */
        
        /**
         * Sets the scale component of the transform, leaving translation and rotation
         * untouched.
         */
        
        /**
         * Sets the scale component of the transform, relative to the other node.
         */
        """
        pass

    def setScissor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scissor(const NodePath self, const LPoint3f a, const LPoint3f b)
        set_scissor(const NodePath self, const NodePath other, const LPoint3f a, const LPoint3f b)
        set_scissor(const NodePath self, const LPoint3f a, const LPoint3f b, const LPoint3f c, const LPoint3f d)
        set_scissor(const NodePath self, float left, float right, float bottom, float top)
        set_scissor(const NodePath self, const NodePath other, const LPoint3f a, const LPoint3f b, const LPoint3f c, const LPoint3f d)
        
        /**
         * Sets up a scissor region on the nodes rendered at this level and below.
         * The four coordinates are understood to define a rectangle in screen space.
         * These numbers are relative to the current DisplayRegion, where (0,0) is the
         * lower-left corner of the DisplayRegion, and (1,1) is the upper-right
         * corner.
         */
        
        /**
         * Sets up a scissor region on the nodes rendered at this level and below.
         * The two points are understood to be relative to this node.  When these
         * points are projected into screen space, they define the diagonally-opposite
         * points that determine the scissor region.
         */
        
        /**
         * Sets up a scissor region on the nodes rendered at this level and below.
         * The four points are understood to be relative to this node.  When these
         * points are projected into screen space, they define the bounding volume of
         * the scissor region (the scissor region is the smallest onscreen rectangle
         * that encloses all four points).
         */
        
        /**
         * Sets up a scissor region on the nodes rendered at this level and below.
         * The two points are understood to be relative to the indicated other node.
         * When these points are projected into screen space, they define the
         * diagonally-opposite points that determine the scissor region.
         */
        
        /**
         * Sets up a scissor region on the nodes rendered at this level and below.
         * The four points are understood to be relative to the indicated other node.
         * When these points are projected into screen space, they define the bounding
         * volume of the scissor region (the scissor region is the smallest onscreen
         * rectangle that encloses all four points).
         */
        """
        pass

    def setSg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_sg(const NodePath self, float sg)
        
        /**
         * Sets the green component of the color scale.
         * @see set_color_scale()
         */
        """
        pass

    def setShader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shader(const NodePath self, const Shader sha, int priority)
        
        /**
         *
         */
        """
        pass

    def setShaderAuto(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shader_auto(const NodePath self)
        set_shader_auto(const NodePath self, BitMask shader_switch, int priority)
        set_shader_auto(const NodePath self, int priority)
        
        /**
         *
         */
        
        /**
         * overloaded for auto shader customization
         */
        """
        pass

    def setShaderInput(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shader_input(const NodePath self, const ShaderInput input)
        set_shader_input(const NodePath self, const InternalName param0, object param1)
        set_shader_input(const NodePath self, const InternalName id, int n1, int n2)
        set_shader_input(const NodePath self, const InternalName id, float n1, float n2)
        set_shader_input(const NodePath self, const InternalName id, Texture tex, const SamplerState sampler)
        set_shader_input(const NodePath self, const InternalName param0, object param1, int priority)
        set_shader_input(const NodePath self, const InternalName id, Texture tex, bool read, bool write, int z, int n, int priority)
        set_shader_input(const NodePath self, const InternalName id, int n1, int n2, int n3, int n4, int priority)
        set_shader_input(const NodePath self, const InternalName id, float n1, float n2, float n3, float n4, int priority)
        set_shader_input(const NodePath self, const InternalName id, Texture tex, const SamplerState sampler, int priority)
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def setShaderInputs(self, *args, **kwargs): # real signature unknown
        pass

    def setShaderOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shader_off(const NodePath self, int priority)
        
        /**
         *
         */
        """
        pass

    def setShear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shear(const NodePath self, const LVecBase3f shear)
        set_shear(const NodePath self, const NodePath other, const LVecBase3f shear)
        set_shear(const NodePath self, float shxy, float shxz, float shyz)
        set_shear(const NodePath self, const NodePath other, float shxy, float shxz, float shyz)
        
        /**
         * Sets the shear component of the transform, leaving translation, rotation,
         * and scale untouched.
         */
        
        /**
         * Sets the shear component of the transform, relative to the other node.
         */
        
        /**
         * Sets the shear component of the transform, leaving translation and rotation
         * untouched.
         */
        
        /**
         * Sets the shear component of the transform, relative to the other node.
         */
        """
        pass

    def setShxy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shxy(const NodePath self, float shxy)
        set_shxy(const NodePath self, const NodePath other, float shxy)
        """
        pass

    def setShxz(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shxz(const NodePath self, float shxz)
        set_shxz(const NodePath self, const NodePath other, float shxz)
        """
        pass

    def setShyz(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shyz(const NodePath self, float shyz)
        set_shyz(const NodePath self, const NodePath other, float shyz)
        """
        pass

    def setSr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_sr(const NodePath self, float sr)
        
        /**
         * Sets the red component of the color scale.
         * @see set_color_scale()
         */
        """
        pass

    def setState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_state(const NodePath self, const RenderState state)
        set_state(const NodePath self, const NodePath other, const RenderState state, Thread current_thread)
        set_state(const NodePath self, const RenderState state, Thread current_thread)
        
        /**
         * Changes the complete state object on this node.
         */
        
        /**
         * Sets the state object on this node, relative to the other node.  This
         * computes a new state object that will have the indicated value when seen
         * from the other node.
         */
        """
        pass

    def setSx(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_sx(const NodePath self, float sx)
        set_sx(const NodePath self, const NodePath other, float sx)
        
        /**
         * Sets the x-scale component of the transform, leaving other components
         * untouched.
         * @see set_scale()
         */
        """
        pass

    def setSy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_sy(const NodePath self, float sy)
        set_sy(const NodePath self, const NodePath other, float sy)
        
        /**
         * Sets the y-scale component of the transform, leaving other components
         * untouched.
         * @see set_scale()
         */
        """
        pass

    def setSz(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_sz(const NodePath self, float sz)
        set_sz(const NodePath self, const NodePath other, float sz)
        
        /**
         * Sets the z-scale component of the transform, leaving other components
         * untouched.
         * @see set_scale()
         */
        """
        pass

    def setTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tag(const NodePath self, str key, str value)
        
        /**
         * Associates a user-defined value with a user-defined key which is stored on
         * the node.  This value has no meaning to Panda; but it is stored
         * indefinitely on the node until it is requested again.
         *
         * Each unique key stores a different string value.  There is no effective
         * limit on the number of different keys that may be stored or on the length
         * of any one key's value.
         */
        """
        pass

    def setTexGen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tex_gen(const NodePath self, TextureStage stage, int mode)
        set_tex_gen(const NodePath self, TextureStage stage, int mode, const LPoint3f constant_value, int priority)
        set_tex_gen(const NodePath self, TextureStage stage, int mode, int priority)
        
        /**
         * Enables automatic texture coordinate generation for the indicated texture
         * stage.
         */
        
        /**
         * Enables automatic texture coordinate generation for the indicated texture
         * stage.  This version of this method is useful when setting M_constant,
         * which requires a constant texture coordinate value.
         */
        """
        pass

    def setTexHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tex_hpr(const NodePath self, TextureStage stage, const LVecBase3f hpr)
        set_tex_hpr(const NodePath self, const NodePath other, TextureStage stage, const LVecBase3f hpr)
        set_tex_hpr(const NodePath self, TextureStage stage, float h, float p, float r)
        set_tex_hpr(const NodePath self, const NodePath other, TextureStage stage, float h, float p, float r)
        
        /**
         * Sets a texture matrix on the current node to apply the indicated rotation,
         * as a 3-D HPR, to UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated rotation,
         * as a 3-D HPR, to UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated rotation,
         * as a 3-D HPR, to UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated rotation,
         * as a 3-D HPR, to UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        """
        pass

    def setTexOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tex_offset(const NodePath self, TextureStage stage, const LVecBase2f uv)
        set_tex_offset(const NodePath self, TextureStage stage, float u, float v)
        set_tex_offset(const NodePath self, const NodePath other, TextureStage stage, float u, float v)
        
        /**
         * Sets a texture matrix on the current node to apply the indicated offset to
         * UV's for the given stage.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated offset to
         * UV's for the given stage.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated offset to
         * UV's for the given stage.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated offset to
         * UV's for the given stage.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        """
        pass

    def setTexPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tex_pos(const NodePath self, TextureStage stage, const LVecBase3f uvw)
        set_tex_pos(const NodePath self, const NodePath other, TextureStage stage, const LVecBase3f uvw)
        set_tex_pos(const NodePath self, TextureStage stage, float u, float v, float w)
        set_tex_pos(const NodePath self, const NodePath other, TextureStage stage, float u, float v, float w)
        
        /**
         * Sets a texture matrix on the current node to apply the indicated offset to
         * UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated offset to
         * UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated offset to
         * UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated offset to
         * UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        """
        pass

    def setTexProjector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tex_projector(const NodePath self, TextureStage stage, const NodePath from, const NodePath to, int lens_index)
        
        /**
         * Establishes a TexProjectorEffect on this node, which can be used to
         * establish projective texturing (but see also the
         * NodePath::project_texture() convenience function), or it can be used to
         * bind this node's texture transform to particular node's position in space,
         * allowing a LerpInterval (for instance) to adjust this node's texture
         * coordinates.
         *
         * If to is a LensNode, then the fourth parameter, lens_index, can be provided
         * to select a particular lens to apply.  Otherwise lens_index is not used.
         */
        """
        pass

    def setTexRotate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tex_rotate(const NodePath self, TextureStage stage, float r)
        set_tex_rotate(const NodePath self, const NodePath other, TextureStage stage, float r)
        
        /**
         * Sets a texture matrix on the current node to apply the indicated rotation,
         * clockwise in degrees, to UV's for the given stage.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated rotation,
         * clockwise in degrees, to UV's for the given stage.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        """
        pass

    def setTexScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tex_scale(const NodePath self, TextureStage stage, const LVecBase2f scale)
        set_tex_scale(const NodePath self, TextureStage stage, const LVecBase3f scale)
        set_tex_scale(const NodePath self, TextureStage stage, float scale)
        set_tex_scale(const NodePath self, TextureStage stage, float su, float sv)
        set_tex_scale(const NodePath self, const NodePath other, TextureStage stage, const LVecBase3f scale)
        set_tex_scale(const NodePath self, const NodePath other, TextureStage stage, const LVecBase2f scale)
        set_tex_scale(const NodePath self, const NodePath other, TextureStage stage, float scale)
        set_tex_scale(const NodePath self, TextureStage stage, float su, float sv, float sw)
        set_tex_scale(const NodePath self, const NodePath other, TextureStage stage, float su, float sv)
        set_tex_scale(const NodePath self, const NodePath other, TextureStage stage, float su, float sv, float sw)
        
        /**
         * Sets a texture matrix on the current node to apply the indicated scale to
         * UVW's for the given stage.
         *
         * This call is appropriate for 2-d or 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated scale to
         * UV's for the given stage.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated scale to
         * UV's for the given stage.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated scale to
         * UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated scale to
         * UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated scale to
         * UV's for the given stage.
         *
         * This call is appropriate for 2-d or 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated scale to
         * UV's for the given stage.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated scale to
         * UV's for the given stage.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated scale to
         * UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated scale to
         * UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        """
        pass

    def setTexTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tex_transform(const NodePath self, TextureStage stage, const TransformState transform)
        set_tex_transform(const NodePath self, const NodePath other, TextureStage stage, const TransformState transform)
        
        /**
         * Sets the texture matrix on the current node to the indicated transform for
         * the given stage.
         */
        
        /**
         * Sets the texture matrix on the current node to the indicated transform for
         * the given stage.
         */
        """
        pass

    def setTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_texture(const NodePath self, Texture tex)
        set_texture(const NodePath self, TextureStage stage, Texture tex)
        set_texture(const NodePath self, Texture tex, const SamplerState sampler)
        set_texture(const NodePath self, Texture tex, int priority)
        set_texture(const NodePath self, TextureStage stage, Texture tex, const SamplerState sampler, int priority)
        set_texture(const NodePath self, TextureStage stage, Texture tex, int priority)
        set_texture(const NodePath self, Texture tex, const SamplerState sampler, int priority)
        
        /**
         * Adds the indicated texture to the list of textures that will be rendered on
         * the default texture stage.
         *
         * This is the convenience single-texture variant of this method; it is now
         * superceded by set_texture() that accepts a stage and texture.  You may use
         * this method if you just want to adjust the default stage.
         */
        
        /**
         * Adds the indicated texture to the list of textures that will be rendered on
         * the indicated multitexture stage.  If there are multiple texture stages
         * specified (possibly on multiple different nodes at different levels), they
         * will all be applied to geometry together, according to the stage
         * specification set up in the TextureStage object.
         */
        
        /**
         * Adds the indicated texture to the list of textures that will be rendered on
         * the default texture stage.
         *
         * The given sampler state will override the sampling settings on the texture
         * itself.  Note that this method makes a copy of the sampler settings that
         * you give; further changes to this object will not be reflected.
         *
         * This is the convenience single-texture variant of this method; it is now
         * superceded by set_texture() that accepts a stage and texture.  You may use
         * this method if you just want to adjust the default stage.
         */
        
        /**
         * Adds the indicated texture to the list of textures that will be rendered on
         * the indicated multitexture stage.  If there are multiple texture stages
         * specified (possibly on multiple different nodes at different levels), they
         * will all be applied to geometry together, according to the stage
         * specification set up in the TextureStage object.
         *
         * The given sampler state will override the sampling settings on the texture
         * itself.  Note that this method makes a copy of the sampler settings that
         * you give; further changes to this object will not be reflected.
         */
        """
        pass

    def setTextureOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_texture_off(const NodePath self)
        set_texture_off(const NodePath self, TextureStage stage, int priority)
        set_texture_off(const NodePath self, int priority)
        
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

    def setTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_transform(const NodePath self, const TransformState transform)
        set_transform(const NodePath self, const NodePath other, const TransformState transform, Thread current_thread)
        set_transform(const NodePath self, const TransformState transform, Thread current_thread)
        
        /**
         * Changes the complete transform object on this node.
         */
        
        /**
         * Sets the transform object on this node, relative to the other node.  This
         * computes a new transform object that will have the indicated value when
         * seen from the other node.
         */
        """
        pass

    def setTransparency(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_transparency(const NodePath self, int mode, int priority)
        
        /**
         * Specifically sets or disables transparent rendering mode on this particular
         * node.  If no other nodes override, this will cause items with a non-1 value
         * for alpha color to be rendered partially transparent.
         */
        """
        pass

    def setTwoSided(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_two_sided(const NodePath self, bool two_sided, int priority)
        
        /**
         * Specifically sets or disables two-sided rendering mode on this particular
         * node.  If no other nodes override, this will cause backfacing polygons to
         * be drawn (in two-sided mode, true) or culled (in one-sided mode, false).
         */
        """
        pass

    def setX(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_x(const NodePath self, float x)
        set_x(const NodePath self, const NodePath other, float x)
        
        /**
         * Sets the X component of the position transform, leaving other components
         * untouched.
         * @see set_pos()
         */
        """
        pass

    def setY(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_y(const NodePath self, float y)
        set_y(const NodePath self, const NodePath other, float y)
        
        /**
         * Sets the Y component of the position transform, leaving other components
         * untouched.
         * @see set_pos()
         */
        """
        pass

    def setZ(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_z(const NodePath self, float z)
        set_z(const NodePath self, const NodePath other, float z)
        
        /**
         * Sets the Z component of the position transform, leaving other components
         * untouched.
         * @see set_pos()
         */
        """
        pass

    def set_all_color_scale(self, const_NodePath_self, float_scale, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_all_color_scale(const NodePath self, float scale, int priority)
        
        /**
         * Scales all the color components of the object by the same amount, darkening
         * the object, without (much) affecting alpha.  Note that any priority
         * specified will also apply to the alpha scale.
         */
        """
        pass

    def set_alpha_scale(self, const_NodePath_self, float_scale, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_alpha_scale(const NodePath self, float scale, int priority)
        
        /**
         * Sets the alpha scale component of the transform without (much) affecting
         * the color scale.  Note that any priority specified will also apply to the
         * color scale.
         */
        """
        pass

    def set_antialias(self, const_NodePath_self, int_mode, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_antialias(const NodePath self, int mode, int priority)
        
        /**
         * Specifies the antialiasing type that should be applied at this node and
         * below.  See AntialiasAttrib.
         */
        """
        pass

    def set_attrib(self, const_NodePath_self, const_RenderAttrib_attrib, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_attrib(const NodePath self, const RenderAttrib attrib, int priority)
        
        /**
         * Adds the indicated render attribute to the scene graph on this node.  This
         * attribute will now apply to this node and everything below.  If there was
         * already an attribute of the same type, it is replaced.
         */
        """
        pass

    def set_audio_volume(self, const_NodePath_self, float_volume, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_audio_volume(const NodePath self, float volume, int priority)
        
        /**
         * Sets the audio volume component of the transform
         */
        """
        pass

    def set_audio_volume_off(self, const_NodePath_self, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_audio_volume_off(const NodePath self, int priority)
        
        /**
         * Disables any audio volume attribute inherited from above.  This is not the
         * same thing as clear_audio_volume(), which undoes any previous
         * set_audio_volume() operation on this node; rather, this actively disables
         * any set_audio_volume() that might be inherited from a parent node.
         *
         * It is legal to specify a new volume on the same node with a subsequent call
         * to set_audio_volume(); this new scale will apply to lower nodes.
         */
        """
        pass

    def set_billboard_axis(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_billboard_axis(const NodePath self)
        set_billboard_axis(const NodePath self, float offset)
        set_billboard_axis(const NodePath self, const NodePath camera, float offset)
        
        /**
         * Puts a billboard transition on the node such that it will rotate in two
         * dimensions around the up axis.
         */
        
        /**
         * Puts a billboard transition on the node such that it will rotate in two
         * dimensions around the up axis, towards a specified "camera" instead of to
         * the viewing camera.
         */
        """
        pass

    def set_billboard_point_eye(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_billboard_point_eye(const NodePath self)
        set_billboard_point_eye(const NodePath self, float offset)
        set_billboard_point_eye(const NodePath self, const NodePath camera, float offset, bool fixed_depth)
        set_billboard_point_eye(const NodePath self, float offset, bool fixed_depth)
        
        /**
         * Puts a billboard transition on the node such that it will rotate in three
         * dimensions about the origin, keeping its up vector oriented to the top of
         * the camera.
         */
        
        /**
         * Puts a billboard transition on the node such that it will rotate in three
         * dimensions about the origin, keeping its up vector oriented to the top of
         * the camera, towards a specified "camera" instead of to the viewing camera.
         */
        """
        pass

    def set_billboard_point_world(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_billboard_point_world(const NodePath self)
        set_billboard_point_world(const NodePath self, float offset)
        set_billboard_point_world(const NodePath self, const NodePath camera, float offset)
        
        /**
         * Puts a billboard transition on the node such that it will rotate in three
         * dimensions about the origin, keeping its up vector oriented to the sky.
         */
        
        /**
         * Puts a billboard transition on the node such that it will rotate in three
         * dimensions about the origin, keeping its up vector oriented to the sky,
         * towards a specified "camera" instead of to the viewing camera.
         */
        """
        pass

    def set_bin(self, const_NodePath_self, str_bin_name, int_draw_order, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bin(const NodePath self, str bin_name, int draw_order, int priority)
        
        /**
         * Assigns the geometry at this level and below to the named rendering bin.
         * It is the user's responsibility to ensure that such a bin already exists,
         * either via the cull-bin Configrc variable, or by explicitly creating a
         * GeomBin of the appropriate type at runtime.
         *
         * There are two default bins created when Panda is started: "default" and
         * "fixed".  Normally, all geometry is assigned to "default" unless specified
         * otherwise.  This bin renders opaque geometry in state-sorted order,
         * followed by transparent geometry sorted back-to-front.  If any geometry is
         * assigned to "fixed", this will be rendered following all the geometry in
         * "default", in the order specified by draw_order for each piece of geometry
         * so assigned.
         *
         * The draw_order parameter is meaningful only for GeomBinFixed type bins,
         * e.g.  "fixed".  Other kinds of bins ignore it.
         */
        """
        pass

    def set_clip_plane(self, const_NodePath_self, const_NodePath_clip_plane, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_clip_plane(const NodePath self, const NodePath clip_plane, int priority)
        
        /**
         * Adds the indicated clipping plane to the list of planes that apply to
         * geometry at this node and below.  The clipping plane itself, a PlaneNode,
         * should be parented into the scene graph elsewhere, to represent the plane's
         * position in space; but until set_clip_plane() is called it will clip no
         * geometry.
         */
        """
        pass

    def set_clip_plane_off(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_clip_plane_off(const NodePath self)
        set_clip_plane_off(const NodePath self, const NodePath clip_plane, int priority)
        set_clip_plane_off(const NodePath self, int priority)
        
        /**
         * Sets the geometry at this level and below to render using no clip_planes at
         * all.  This is different from not specifying a clip_plane; rather, this
         * specifically contradicts set_clip_plane() at a higher node level (or, with
         * a priority, overrides a set_clip_plane() at a lower level).
         *
         * If no clip_planes are in effect on a particular piece of geometry, that
         * geometry is rendered without being clipped (other than by the viewing
         * frustum).
         */
        
        /**
         * Sets the geometry at this level and below to render without being clipped
         * by the indicated PlaneNode.  This is different from not specifying the
         * PlaneNode; rather, this specifically contradicts set_clip_plane() at a
         * higher node level (or, with a priority, overrides a set_clip_plane() at a
         * lower level).
         */
        """
        pass

    def set_collide_mask(self, const_NodePath_self, BitMask_new_mask, BitMask_bits_to_change, TypeHandle_node_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_collide_mask(const NodePath self, BitMask new_mask, BitMask bits_to_change, TypeHandle node_type)
        
        /**
         * Recursively applies the indicated CollideMask to the into_collide_masks for
         * all nodes at this level and below.  If node_type is not TypeHandle::none(),
         * then only nodes matching (or inheriting from) the indicated PandaNode
         * subclass are modified.
         *
         * The default is to change all bits, but if bits_to_change is not all bits
         * on, then only the bits that are set in bits_to_change are modified,
         * allowing this call to change only a subset of the bits in the subgraph.
         */
        """
        pass

    def set_color(self, const_NodePath_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color(const NodePath self, const LVecBase4f color)
        set_color(const NodePath self, const LVecBase4f color, int priority)
        set_color(const NodePath self, float r, float g, float b, float a, int priority)
        
        /**
         * Applies a scene-graph color to the referenced node.  This color will apply
         * to all geometry at this level and below (that does not specify a new color
         * or a set_color_off()).
         */
        
        /**
         * Applies a scene-graph color to the referenced node.  This color will apply
         * to all geometry at this level and below (that does not specify a new color
         * or a set_color_off()).
         */
        """
        pass

    def set_color_off(self, const_NodePath_self, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color_off(const NodePath self, int priority)
        
        /**
         * Sets the geometry at this level and below to render using the geometry
         * color.  This is normally the default, but it may be useful to use this to
         * contradict set_color() at a higher node level (or, with a priority, to
         * override a set_color() at a lower level).
         */
        """
        pass

    def set_color_scale(self, const_NodePath_self, const_LVecBase4f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color_scale(const NodePath self, const LVecBase4f scale)
        set_color_scale(const NodePath self, const LVecBase4f scale, int priority)
        set_color_scale(const NodePath self, float sx, float sy, float sz, float sa, int priority)
        
        /**
         * Sets the color scale component of the transform
         */
        
        /**
         * Sets the color scale component of the transform, leaving translation and
         * rotation untouched.
         */
        """
        pass

    def set_color_scale_off(self, const_NodePath_self, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color_scale_off(const NodePath self, int priority)
        
        /**
         * Disables any color scale attribute inherited from above.  This is not the
         * same thing as clear_color_scale(), which undoes any previous
         * set_color_scale() operation on this node; rather, this actively disables
         * any set_color_scale() that might be inherited from a parent node.  This
         * also disables set_alpha_scale() at the same time.
         *
         * It is legal to specify a new color scale on the same node with a subsequent
         * call to set_color_scale() or set_alpha_scale(); this new scale will apply
         * to lower geometry.
         */
        """
        pass

    def set_compass(self, const_NodePath_self, const_NodePath_reference): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_compass(const NodePath self, const NodePath reference)
        
        /**
         * Puts a compass effect on the node, so that it will retain a fixed rotation
         * relative to the reference node (or render if the reference node is empty)
         * regardless of the transforms above it.
         */
        """
        pass

    def set_depth_offset(self, const_NodePath_self, int_bias, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_depth_offset(const NodePath self, int bias, int priority)
        
        /**
         * This instructs the graphics driver to apply an offset or bias to the
         * generated depth values for rendered polygons, before they are written to
         * the depth buffer.  This can be used to shift polygons forward slightly, to
         * resolve depth conflicts, or self-shadowing artifacts on thin objects.  The
         * bias is always an integer number, and each integer increment represents the
         * smallest possible increment in Z that is sufficient to completely resolve
         * two coplanar polygons.  Positive numbers are closer towards the camera.
         */
        """
        pass

    def set_depth_test(self, const_NodePath_self, bool_depth_test, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_depth_test(const NodePath self, bool depth_test, int priority)
        
        /**
         * Specifically sets or disables the testing of the depth buffer on this
         * particular node.  This is normally on in the 3-d scene graph and off in the
         * 2-d scene graph; it should be on for rendering most 3-d objects properly.
         */
        """
        pass

    def set_depth_write(self, const_NodePath_self, bool_depth_write, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_depth_write(const NodePath self, bool depth_write, int priority)
        
        /**
         * Specifically sets or disables the writing to the depth buffer on this
         * particular node.  This is normally on in the 3-d scene graph and off in the
         * 2-d scene graph; it should be on for rendering most 3-d objects properly.
         */
        """
        pass

    def set_effect(self, const_NodePath_self, const_RenderEffect_effect): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_effect(const NodePath self, const RenderEffect effect)
        
        /**
         * Adds the indicated render effect to the scene graph on this node.  If there
         * was already an effect of the same type, it is replaced.
         */
        """
        pass

    def set_effects(self, const_NodePath_self, const_RenderEffects_effects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_effects(const NodePath self, const RenderEffects effects)
        
        /**
         * Sets the complete RenderEffects that will be applied this node.  This
         * completely replaces whatever has been set on this node via repeated calls
         * to set_attrib().
         */
        """
        pass

    def set_fluid_pos(self, const_NodePath_self, const_LVecBase3f_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fluid_pos(const NodePath self, const LVecBase3f pos)
        set_fluid_pos(const NodePath self, const NodePath other, const LVecBase3f pos)
        set_fluid_pos(const NodePath self, float x, float y, float z)
        set_fluid_pos(const NodePath self, const NodePath other, float x, float y, float z)
        
        /**
         * Sets the translation component, without changing the "previous" position,
         * so that the collision system will see the node as moving fluidly from its
         * previous position to its new position.
         */
        
        /**
         * Sets the translation component, without changing the "previous" position,
         * so that the collision system will see the node as moving fluidly from its
         * previous position to its new position.
         */
        
        /**
         * Sets the translation component, without changing the "previous" position,
         * so that the collision system will see the node as moving fluidly from its
         * previous position to its new position.  See Also: NodePath::set_pos
         */
        
        /**
         * Sets the translation component of the transform, relative to the other
         * node.
         */
        """
        pass

    def set_fluid_x(self, const_NodePath_self, float_x): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fluid_x(const NodePath self, float x)
        set_fluid_x(const NodePath self, const NodePath other, float x)
        """
        pass

    def set_fluid_y(self, const_NodePath_self, float_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fluid_y(const NodePath self, float y)
        set_fluid_y(const NodePath self, const NodePath other, float y)
        """
        pass

    def set_fluid_z(self, const_NodePath_self, float_z): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fluid_z(const NodePath self, float z)
        set_fluid_z(const NodePath self, const NodePath other, float z)
        """
        pass

    def set_fog(self, const_NodePath_self, Fog_fog, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fog(const NodePath self, Fog fog, int priority)
        
        /**
         * Sets the geometry at this level and below to render using the indicated
         * fog.
         */
        """
        pass

    def set_fog_off(self, const_NodePath_self, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fog_off(const NodePath self, int priority)
        
        /**
         * Sets the geometry at this level and below to render using no fog.  This is
         * normally the default, but it may be useful to use this to contradict
         * set_fog() at a higher node level (or, with a priority, to override a
         * set_fog() at a lower level).
         */
        """
        pass

    def set_h(self, const_NodePath_self, float_h): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_h(const NodePath self, float h)
        set_h(const NodePath self, const NodePath other, float h)
        """
        pass

    def set_hpr(self, const_NodePath_self, const_LVecBase3f_hpr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_hpr(const NodePath self, const LVecBase3f hpr)
        set_hpr(const NodePath self, const NodePath other, const LVecBase3f hpr)
        set_hpr(const NodePath self, float h, float p, float r)
        set_hpr(const NodePath self, const NodePath other, float h, float p, float r)
        
        /**
         * Sets the rotation component of the transform, leaving translation and scale
         * untouched.
         */
        
        /**
         * Sets the rotation component of the transform, relative to the other node.
         */
        
        /**
         * Sets the rotation component of the transform, leaving translation and scale
         * untouched.
         */
        
        /**
         * Sets the rotation component of the transform, relative to the other node.
         */
        """
        pass

    def set_hpr_scale(self, const_NodePath_self, const_LVecBase3f_hpr, const_LVecBase3f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_hpr_scale(const NodePath self, const LVecBase3f hpr, const LVecBase3f scale)
        set_hpr_scale(const NodePath self, const NodePath other, const LVecBase3f hpr, const LVecBase3f scale)
        set_hpr_scale(const NodePath self, float h, float p, float r, float sx, float sy, float sz)
        set_hpr_scale(const NodePath self, const NodePath other, float h, float p, float r, float sx, float sy, float sz)
        
        /**
         * Sets the rotation and scale components of the transform, leaving
         * translation untouched.
         */
        
        /**
         * Sets the rotation and scale components of the transform, leaving
         * translation untouched.  This, or set_pos_hpr_scale, is the preferred way to
         * update a transform when both hpr and scale are to be changed.
         */
        
        /**
         * Sets the rotation and scale components of the transform, leaving
         * translation untouched.
         */
        
        /**
         * Sets the rotation and scale components of the transform, leaving
         * translation untouched.  This, or set_pos_hpr_scale, is the preferred way to
         * update a transform when both hpr and scale are to be changed.
         */
        """
        pass

    def set_instance_count(self, const_NodePath_self, int_instance_count): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_instance_count(const NodePath self, int instance_count)
        
        /**
         * Sets the geometry instance count, or 0 if geometry instancing should be
         * disabled.  Do not confuse with instanceTo which only applies to animation
         * instancing.
         */
        """
        pass

    def set_light(self, const_NodePath_self, const_NodePath_light, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_light(const NodePath self, const NodePath light, int priority)
        
        /**
         * Adds the indicated Light or PolylightNode to the list of lights that
         * illuminate geometry at this node and below.  The light itself should be
         * parented into the scene graph elsewhere, to represent the light's position
         * in space; but until set_light() is called it will illuminate no geometry.
         */
        """
        pass

    def set_light_off(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_light_off(const NodePath self)
        set_light_off(const NodePath self, const NodePath light, int priority)
        set_light_off(const NodePath self, int priority)
        
        /**
         * Sets the geometry at this level and below to render using no lights at all.
         * This is different from not specifying a light; rather, this specifically
         * contradicts set_light() at a higher node level (or, with a priority,
         * overrides a set_light() at a lower level).
         *
         * If no lights are in effect on a particular piece of geometry, that geometry
         * is rendered with lighting disabled.
         */
        
        /**
         * Sets the geometry at this level and below to render without using the
         * indicated Light.  This is different from not specifying the Light; rather,
         * this specifically contradicts set_light() at a higher node level (or, with
         * a priority, overrides a set_light() at a lower level).
         *
         * This interface does not support PolylightNodes, which cannot be turned off
         * at a lower level.
         */
        """
        pass

    def set_logic_op(self, const_NodePath_self, int_op, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_logic_op(const NodePath self, int op, int priority)
        
        /**
         * Specifically sets or disables a logical operation on this particular node.
         * If no other nodes override, this will cause geometry to be rendered without
         * color blending but instead using the given logical operator.
         *
         * @since 1.10.0
         */
        """
        pass

    def set_mat(self, const_NodePath_self, const_LMatrix4f_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_mat(const NodePath self, const LMatrix4f mat)
        set_mat(const NodePath self, const NodePath other, const LMatrix4f mat)
        
        /**
         * Directly sets an arbitrary 4x4 transform matrix.
         */
        
        /**
         * Converts the indicated matrix from the other's coordinate space to the
         * local coordinate space, and applies it to the node.
         */
        """
        pass

    def set_material(self, const_NodePath_self, Material_tex, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_material(const NodePath self, Material tex, int priority)
        
        /**
         * Sets the geometry at this level and below to render using the indicated
         * material.
         *
         * Previously, this operation made a copy of the material structure, but
         * nowadays it assigns the pointer directly.
         */
        """
        pass

    def set_material_off(self, const_NodePath_self, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_material_off(const NodePath self, int priority)
        
        /**
         * Sets the geometry at this level and below to render using no material.
         * This is normally the default, but it may be useful to use this to
         * contradict set_material() at a higher node level (or, with a priority, to
         * override a set_material() at a lower level).
         */
        """
        pass

    def set_max_search_depth(self, int_max_search_depth): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_search_depth(int max_search_depth)
        
        /**
         * Certain operations, such as find() or find_all_matches(), require a
         * traversal of the scene graph to search for the target node or nodes.  This
         * traversal does not attempt to detect cycles, so an arbitrary cap is set on
         * the depth of the traversal as a poor man's cycle detection, in the event
         * that a cycle has inadvertently been introduced into the scene graph.
         *
         * There may be other reasons you'd want to truncate a search before the
         * bottom of the scene graph has been reached.  In any event, this function
         * sets the limit on the number of levels that a traversal will continue, and
         * hence the maximum length of a path that may be returned by a traversal.
         *
         * This is a static method, and so changing this parameter affects all of the
         * NodePaths in the universe.
         */
        """
        pass

    def set_name(self, const_NodePath_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_name(const NodePath self, str name)
        
        /**
         * Changes the name of the referenced node.
         */
        """
        pass

    def set_occluder(self, const_NodePath_self, const_NodePath_occluder): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_occluder(const NodePath self, const NodePath occluder)
        
        /**
         * Adds the indicated occluder to the list of occluders that apply to geometry
         * at this node and below.  The occluder itself, an OccluderNode, should be
         * parented into the scene graph elsewhere, to represent the occluder's
         * position in space; but until set_occluder() is called it will clip no
         * geometry.
         */
        """
        pass

    def set_p(self, const_NodePath_self, float_p): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_p(const NodePath self, float p)
        set_p(const NodePath self, const NodePath other, float p)
        """
        pass

    def set_pos(self, const_NodePath_self, const_LVecBase3f_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pos(const NodePath self, const LVecBase3f pos)
        set_pos(const NodePath self, const NodePath other, const LVecBase3f pos)
        set_pos(const NodePath self, float x, float y, float z)
        set_pos(const NodePath self, const NodePath other, float x, float y, float z)
        
        /**
         * Sets the translation component of the transform, leaving rotation and scale
         * untouched.  This also resets the node's "previous" position, so that the
         * collision system will see the node as having suddenly appeared in the new
         * position, without passing any points in between.
         */
        
        /**
         * Sets the translation component of the transform, relative to the other
         * node.
         */
        
        /**
         * Sets the translation component of the transform, leaving rotation and scale
         * untouched.  This also resets the node's "previous" position, so that the
         * collision system will see the node as having suddenly appeared in the new
         * position, without passing any points in between.  See Also:
         * NodePath::set_fluid_pos
         */
        
        /**
         * Sets the translation component of the transform, relative to the other
         * node.
         */
        """
        pass

    def set_pos_hpr(self, const_NodePath_self, const_LVecBase3f_pos, const_LVecBase3f_hpr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pos_hpr(const NodePath self, const LVecBase3f pos, const LVecBase3f hpr)
        set_pos_hpr(const NodePath self, const NodePath other, const LVecBase3f pos, const LVecBase3f hpr)
        set_pos_hpr(const NodePath self, float x, float y, float z, float h, float p, float r)
        set_pos_hpr(const NodePath self, const NodePath other, float x, float y, float z, float h, float p, float r)
        
        /**
         * Sets the translation and rotation component of the transform, leaving scale
         * untouched.
         */
        
        /**
         * Sets the translation and rotation component of the transform, relative to
         * the other node.
         */
        
        /**
         * Sets the translation and rotation component of the transform, leaving scale
         * untouched.
         */
        
        /**
         * Sets the translation and rotation component of the transform, relative to
         * the other node.
         */
        """
        pass

    def set_pos_hpr_scale(self, const_NodePath_self, const_LVecBase3f_pos, const_LVecBase3f_hpr, const_LVecBase3f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pos_hpr_scale(const NodePath self, const LVecBase3f pos, const LVecBase3f hpr, const LVecBase3f scale)
        set_pos_hpr_scale(const NodePath self, const NodePath other, const LVecBase3f pos, const LVecBase3f hpr, const LVecBase3f scale)
        set_pos_hpr_scale(const NodePath self, float x, float y, float z, float h, float p, float r, float sx, float sy, float sz)
        set_pos_hpr_scale(const NodePath self, const NodePath other, float x, float y, float z, float h, float p, float r, float sx, float sy, float sz)
        
        /**
         * Completely replaces the transform with new translation, rotation, and scale
         * components.
         */
        
        /**
         * Completely replaces the transform with new translation, rotation, and scale
         * components, relative to the other node.
         */
        
        /**
         * Replaces the translation, rotation, and scale components, implicitly
         * setting shear to 0.
         */
        
        /**
         * Completely replaces the transform with new translation, rotation, and scale
         * components, relative to the other node, implicitly setting shear to 0.
         */
        """
        pass

    def set_pos_hpr_scale_shear(self, const_NodePath_self, const_LVecBase3f_pos, const_LVecBase3f_hpr, const_LVecBase3f_scale, const_LVecBase3f_shear): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pos_hpr_scale_shear(const NodePath self, const LVecBase3f pos, const LVecBase3f hpr, const LVecBase3f scale, const LVecBase3f shear)
        set_pos_hpr_scale_shear(const NodePath self, const NodePath other, const LVecBase3f pos, const LVecBase3f hpr, const LVecBase3f scale, const LVecBase3f shear)
        
        /**
         * Completely replaces the transform with new translation, rotation, scale,
         * and shear components.
         */
        
        /**
         * Completely replaces the transform with new translation, rotation, scale,
         * and shear components, relative to the other node.
         */
        """
        pass

    def set_pos_quat(self, const_NodePath_self, const_LVecBase3f_pos, const_LQuaternionf_quat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pos_quat(const NodePath self, const LVecBase3f pos, const LQuaternionf quat)
        set_pos_quat(const NodePath self, const NodePath other, const LVecBase3f pos, const LQuaternionf quat)
        
        /**
         * Sets the translation and rotation component of the transform, leaving scale
         * untouched.
         */
        
        /**
         * Sets the translation and rotation component of the transform, relative to
         * the other node.
         */
        """
        pass

    def set_pos_quat_scale(self, const_NodePath_self, const_LVecBase3f_pos, const_LQuaternionf_quat, const_LVecBase3f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pos_quat_scale(const NodePath self, const LVecBase3f pos, const LQuaternionf quat, const LVecBase3f scale)
        set_pos_quat_scale(const NodePath self, const NodePath other, const LVecBase3f pos, const LQuaternionf quat, const LVecBase3f scale)
        
        /**
         * Replaces the translation, rotation, and scale components, implicitly
         * setting shear to 0.
         */
        
        /**
         * Completely replaces the transform with new translation, rotation, and scale
         * components, relative to the other node, implicitly setting shear to 0.
         */
        """
        pass

    def set_pos_quat_scale_shear(self, const_NodePath_self, const_LVecBase3f_pos, const_LQuaternionf_quat, const_LVecBase3f_scale, const_LVecBase3f_shear): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pos_quat_scale_shear(const NodePath self, const LVecBase3f pos, const LQuaternionf quat, const LVecBase3f scale, const LVecBase3f shear)
        set_pos_quat_scale_shear(const NodePath self, const NodePath other, const LVecBase3f pos, const LQuaternionf quat, const LVecBase3f scale, const LVecBase3f shear)
        
        /**
         * Completely replaces the transform with new translation, rotation, scale,
         * and shear components.
         */
        
        /**
         * Completely replaces the transform with new translation, rotation, scale,
         * and shear components, relative to the other node.
         */
        """
        pass

    def set_prev_transform(self, const_NodePath_self, const_TransformState_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_prev_transform(const NodePath self, const TransformState transform)
        set_prev_transform(const NodePath self, const NodePath other, const TransformState transform, Thread current_thread)
        set_prev_transform(const NodePath self, const TransformState transform, Thread current_thread)
        
        /**
         * Sets the transform that represents this node's "previous" position, one
         * frame ago, for the purposes of detecting motion for accurate collision
         * calculations.
         */
        
        /**
         * Sets the "previous" transform object on this node, relative to the other
         * node.  This computes a new transform object that will have the indicated
         * value when seen from the other node.
         */
        """
        pass

    def set_python_tag(self, const_NodePath_self, object_keys, object_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_python_tag(const NodePath self, object keys, object value)
        """
        pass

    def set_quat(self, const_NodePath_self, const_LQuaternionf_quat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_quat(const NodePath self, const LQuaternionf quat)
        set_quat(const NodePath self, const NodePath other, const LQuaternionf quat)
        
        /**
         * Sets the rotation component of the transform, leaving translation and scale
         * untouched.
         */
        
        /**
         * Sets the rotation component of the transform, relative to the other node.
         */
        """
        pass

    def set_quat_scale(self, const_NodePath_self, const_LQuaternionf_quat, const_LVecBase3f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_quat_scale(const NodePath self, const LQuaternionf quat, const LVecBase3f scale)
        set_quat_scale(const NodePath self, const NodePath other, const LQuaternionf quat, const LVecBase3f scale)
        
        /**
         * Sets the rotation and scale components of the transform, leaving
         * translation untouched.
         */
        
        /**
         * Sets the rotation and scale components of the transform, leaving
         * translation untouched.  This, or set_pos_quat_scale, is the preferred way
         * to update a transform when both quat and scale are to be changed.
         */
        """
        pass

    def set_r(self, const_NodePath_self, float_r): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_r(const NodePath self, float r)
        set_r(const NodePath self, const NodePath other, float r)
        """
        pass

    def set_render_mode(self, const_NodePath_self, int_mode, float_thickness, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_render_mode(const NodePath self, int mode, float thickness, int priority)
        
        /**
         * Sets up the geometry at this level and below (unless overridden) to render
         * in the specified mode and with the indicated line and/or point thickness.
         */
        """
        pass

    def set_render_mode_filled(self, const_NodePath_self, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_render_mode_filled(const NodePath self, int priority)
        
        /**
         * Sets up the geometry at this level and below (unless overridden) to render
         * in filled (i.e.  not wireframe) mode.
         */
        """
        pass

    def set_render_mode_filled_wireframe(self, const_NodePath_self, const_LVecBase4f_wireframe_color, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_render_mode_filled_wireframe(const NodePath self, const LVecBase4f wireframe_color, int priority)
        
        /**
         * Sets up the geometry at this level and below (unless overridden) to render
         * in filled, but overlay the wireframe on top with a fixed color.  This is
         * useful for debug visualizations.
         */
        """
        pass

    def set_render_mode_perspective(self, const_NodePath_self, bool_perspective, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_render_mode_perspective(const NodePath self, bool perspective, int priority)
        
        /**
         * Sets up the point geometry at this level and below to render as perspective
         * sprites (that is, billboarded quads).  The thickness, as specified with
         * set_render_mode_thickness(), is the width of each point in 3-D units,
         * unless it is overridden on a per-vertex basis.  This does not affect
         * geometry other than points.
         *
         * If you want the quads to be individually textured, you should also set a
         * TexGenAttrib::M_point_sprite on the node.
         */
        """
        pass

    def set_render_mode_thickness(self, const_NodePath_self, float_thickness, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_render_mode_thickness(const NodePath self, float thickness, int priority)
        
        /**
         * Sets up the point geometry at this level and below to render as thick
         * points (that is, billboarded quads).  The thickness is in pixels, unless
         * set_render_mode_perspective is also true, in which case it is in 3-D units.
         *
         * If you want the quads to be individually textured, you should also set a
         * TexGenAttrib::M_point_sprite on the node.
         */
        """
        pass

    def set_render_mode_wireframe(self, const_NodePath_self, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_render_mode_wireframe(const NodePath self, int priority)
        
        /**
         * Sets up the geometry at this level and below (unless overridden) to render
         * in wireframe mode.
         */
        """
        pass

    def set_sa(self, const_NodePath_self, float_sa): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_sa(const NodePath self, float sa)
        
        /**
         * Sets the alpha component of the color scale.
         * @see set_color_scale()
         */
        """
        pass

    def set_sb(self, const_NodePath_self, float_sb): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_sb(const NodePath self, float sb)
        
        /**
         * Sets the blue component of the color scale.
         * @see set_color_scale()
         */
        """
        pass

    def set_scale(self, const_NodePath_self, const_LVecBase3f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scale(const NodePath self, const LVecBase3f scale)
        set_scale(const NodePath self, float scale)
        set_scale(const NodePath self, const NodePath other, const LVecBase3f scale)
        set_scale(const NodePath self, const NodePath other, float scale)
        set_scale(const NodePath self, float sx, float sy, float sz)
        set_scale(const NodePath self, const NodePath other, float sx, float sy, float sz)
        
        /**
         * Sets the scale component of the transform, leaving translation and rotation
         * untouched.
         */
        
        /**
         * Sets the scale component of the transform, relative to the other node.
         */
        
        /**
         * Sets the scale component of the transform, relative to the other node.
         */
        
        /**
         * Sets the scale component of the transform, leaving translation and rotation
         * untouched.
         */
        
        /**
         * Sets the scale component of the transform, relative to the other node.
         */
        """
        pass

    def set_scissor(self, const_NodePath_self, const_LPoint3f_a, const_LPoint3f_b): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scissor(const NodePath self, const LPoint3f a, const LPoint3f b)
        set_scissor(const NodePath self, const NodePath other, const LPoint3f a, const LPoint3f b)
        set_scissor(const NodePath self, const LPoint3f a, const LPoint3f b, const LPoint3f c, const LPoint3f d)
        set_scissor(const NodePath self, float left, float right, float bottom, float top)
        set_scissor(const NodePath self, const NodePath other, const LPoint3f a, const LPoint3f b, const LPoint3f c, const LPoint3f d)
        
        /**
         * Sets up a scissor region on the nodes rendered at this level and below.
         * The four coordinates are understood to define a rectangle in screen space.
         * These numbers are relative to the current DisplayRegion, where (0,0) is the
         * lower-left corner of the DisplayRegion, and (1,1) is the upper-right
         * corner.
         */
        
        /**
         * Sets up a scissor region on the nodes rendered at this level and below.
         * The two points are understood to be relative to this node.  When these
         * points are projected into screen space, they define the diagonally-opposite
         * points that determine the scissor region.
         */
        
        /**
         * Sets up a scissor region on the nodes rendered at this level and below.
         * The four points are understood to be relative to this node.  When these
         * points are projected into screen space, they define the bounding volume of
         * the scissor region (the scissor region is the smallest onscreen rectangle
         * that encloses all four points).
         */
        
        /**
         * Sets up a scissor region on the nodes rendered at this level and below.
         * The two points are understood to be relative to the indicated other node.
         * When these points are projected into screen space, they define the
         * diagonally-opposite points that determine the scissor region.
         */
        
        /**
         * Sets up a scissor region on the nodes rendered at this level and below.
         * The four points are understood to be relative to the indicated other node.
         * When these points are projected into screen space, they define the bounding
         * volume of the scissor region (the scissor region is the smallest onscreen
         * rectangle that encloses all four points).
         */
        """
        pass

    def set_sg(self, const_NodePath_self, float_sg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_sg(const NodePath self, float sg)
        
        /**
         * Sets the green component of the color scale.
         * @see set_color_scale()
         */
        """
        pass

    def set_shader(self, const_NodePath_self, const_Shader_sha, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shader(const NodePath self, const Shader sha, int priority)
        
        /**
         *
         */
        """
        pass

    def set_shader_auto(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shader_auto(const NodePath self)
        set_shader_auto(const NodePath self, BitMask shader_switch, int priority)
        set_shader_auto(const NodePath self, int priority)
        
        /**
         *
         */
        
        /**
         * overloaded for auto shader customization
         */
        """
        pass

    def set_shader_input(self, const_NodePath_self, const_ShaderInput_input): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shader_input(const NodePath self, const ShaderInput input)
        set_shader_input(const NodePath self, const InternalName param0, object param1)
        set_shader_input(const NodePath self, const InternalName id, int n1, int n2)
        set_shader_input(const NodePath self, const InternalName id, float n1, float n2)
        set_shader_input(const NodePath self, const InternalName id, Texture tex, const SamplerState sampler)
        set_shader_input(const NodePath self, const InternalName param0, object param1, int priority)
        set_shader_input(const NodePath self, const InternalName id, Texture tex, bool read, bool write, int z, int n, int priority)
        set_shader_input(const NodePath self, const InternalName id, int n1, int n2, int n3, int n4, int priority)
        set_shader_input(const NodePath self, const InternalName id, float n1, float n2, float n3, float n4, int priority)
        set_shader_input(const NodePath self, const InternalName id, Texture tex, const SamplerState sampler, int priority)
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def set_shader_inputs(self, *args, **kwargs): # real signature unknown
        pass

    def set_shader_off(self, const_NodePath_self, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shader_off(const NodePath self, int priority)
        
        /**
         *
         */
        """
        pass

    def set_shear(self, const_NodePath_self, const_LVecBase3f_shear): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shear(const NodePath self, const LVecBase3f shear)
        set_shear(const NodePath self, const NodePath other, const LVecBase3f shear)
        set_shear(const NodePath self, float shxy, float shxz, float shyz)
        set_shear(const NodePath self, const NodePath other, float shxy, float shxz, float shyz)
        
        /**
         * Sets the shear component of the transform, leaving translation, rotation,
         * and scale untouched.
         */
        
        /**
         * Sets the shear component of the transform, relative to the other node.
         */
        
        /**
         * Sets the shear component of the transform, leaving translation and rotation
         * untouched.
         */
        
        /**
         * Sets the shear component of the transform, relative to the other node.
         */
        """
        pass

    def set_shxy(self, const_NodePath_self, float_shxy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shxy(const NodePath self, float shxy)
        set_shxy(const NodePath self, const NodePath other, float shxy)
        """
        pass

    def set_shxz(self, const_NodePath_self, float_shxz): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shxz(const NodePath self, float shxz)
        set_shxz(const NodePath self, const NodePath other, float shxz)
        """
        pass

    def set_shyz(self, const_NodePath_self, float_shyz): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shyz(const NodePath self, float shyz)
        set_shyz(const NodePath self, const NodePath other, float shyz)
        """
        pass

    def set_sr(self, const_NodePath_self, float_sr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_sr(const NodePath self, float sr)
        
        /**
         * Sets the red component of the color scale.
         * @see set_color_scale()
         */
        """
        pass

    def set_state(self, const_NodePath_self, const_RenderState_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_state(const NodePath self, const RenderState state)
        set_state(const NodePath self, const NodePath other, const RenderState state, Thread current_thread)
        set_state(const NodePath self, const RenderState state, Thread current_thread)
        
        /**
         * Changes the complete state object on this node.
         */
        
        /**
         * Sets the state object on this node, relative to the other node.  This
         * computes a new state object that will have the indicated value when seen
         * from the other node.
         */
        """
        pass

    def set_sx(self, const_NodePath_self, float_sx): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_sx(const NodePath self, float sx)
        set_sx(const NodePath self, const NodePath other, float sx)
        
        /**
         * Sets the x-scale component of the transform, leaving other components
         * untouched.
         * @see set_scale()
         */
        """
        pass

    def set_sy(self, const_NodePath_self, float_sy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_sy(const NodePath self, float sy)
        set_sy(const NodePath self, const NodePath other, float sy)
        
        /**
         * Sets the y-scale component of the transform, leaving other components
         * untouched.
         * @see set_scale()
         */
        """
        pass

    def set_sz(self, const_NodePath_self, float_sz): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_sz(const NodePath self, float sz)
        set_sz(const NodePath self, const NodePath other, float sz)
        
        /**
         * Sets the z-scale component of the transform, leaving other components
         * untouched.
         * @see set_scale()
         */
        """
        pass

    def set_tag(self, const_NodePath_self, str_key, str_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tag(const NodePath self, str key, str value)
        
        /**
         * Associates a user-defined value with a user-defined key which is stored on
         * the node.  This value has no meaning to Panda; but it is stored
         * indefinitely on the node until it is requested again.
         *
         * Each unique key stores a different string value.  There is no effective
         * limit on the number of different keys that may be stored or on the length
         * of any one key's value.
         */
        """
        pass

    def set_texture(self, const_NodePath_self, Texture_tex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_texture(const NodePath self, Texture tex)
        set_texture(const NodePath self, TextureStage stage, Texture tex)
        set_texture(const NodePath self, Texture tex, const SamplerState sampler)
        set_texture(const NodePath self, Texture tex, int priority)
        set_texture(const NodePath self, TextureStage stage, Texture tex, const SamplerState sampler, int priority)
        set_texture(const NodePath self, TextureStage stage, Texture tex, int priority)
        set_texture(const NodePath self, Texture tex, const SamplerState sampler, int priority)
        
        /**
         * Adds the indicated texture to the list of textures that will be rendered on
         * the default texture stage.
         *
         * This is the convenience single-texture variant of this method; it is now
         * superceded by set_texture() that accepts a stage and texture.  You may use
         * this method if you just want to adjust the default stage.
         */
        
        /**
         * Adds the indicated texture to the list of textures that will be rendered on
         * the indicated multitexture stage.  If there are multiple texture stages
         * specified (possibly on multiple different nodes at different levels), they
         * will all be applied to geometry together, according to the stage
         * specification set up in the TextureStage object.
         */
        
        /**
         * Adds the indicated texture to the list of textures that will be rendered on
         * the default texture stage.
         *
         * The given sampler state will override the sampling settings on the texture
         * itself.  Note that this method makes a copy of the sampler settings that
         * you give; further changes to this object will not be reflected.
         *
         * This is the convenience single-texture variant of this method; it is now
         * superceded by set_texture() that accepts a stage and texture.  You may use
         * this method if you just want to adjust the default stage.
         */
        
        /**
         * Adds the indicated texture to the list of textures that will be rendered on
         * the indicated multitexture stage.  If there are multiple texture stages
         * specified (possibly on multiple different nodes at different levels), they
         * will all be applied to geometry together, according to the stage
         * specification set up in the TextureStage object.
         *
         * The given sampler state will override the sampling settings on the texture
         * itself.  Note that this method makes a copy of the sampler settings that
         * you give; further changes to this object will not be reflected.
         */
        """
        pass

    def set_texture_off(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_texture_off(const NodePath self)
        set_texture_off(const NodePath self, TextureStage stage, int priority)
        set_texture_off(const NodePath self, int priority)
        
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

    def set_tex_gen(self, const_NodePath_self, TextureStage_stage, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tex_gen(const NodePath self, TextureStage stage, int mode)
        set_tex_gen(const NodePath self, TextureStage stage, int mode, const LPoint3f constant_value, int priority)
        set_tex_gen(const NodePath self, TextureStage stage, int mode, int priority)
        
        /**
         * Enables automatic texture coordinate generation for the indicated texture
         * stage.
         */
        
        /**
         * Enables automatic texture coordinate generation for the indicated texture
         * stage.  This version of this method is useful when setting M_constant,
         * which requires a constant texture coordinate value.
         */
        """
        pass

    def set_tex_hpr(self, const_NodePath_self, TextureStage_stage, const_LVecBase3f_hpr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tex_hpr(const NodePath self, TextureStage stage, const LVecBase3f hpr)
        set_tex_hpr(const NodePath self, const NodePath other, TextureStage stage, const LVecBase3f hpr)
        set_tex_hpr(const NodePath self, TextureStage stage, float h, float p, float r)
        set_tex_hpr(const NodePath self, const NodePath other, TextureStage stage, float h, float p, float r)
        
        /**
         * Sets a texture matrix on the current node to apply the indicated rotation,
         * as a 3-D HPR, to UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated rotation,
         * as a 3-D HPR, to UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated rotation,
         * as a 3-D HPR, to UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated rotation,
         * as a 3-D HPR, to UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        """
        pass

    def set_tex_offset(self, const_NodePath_self, TextureStage_stage, const_LVecBase2f_uv): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tex_offset(const NodePath self, TextureStage stage, const LVecBase2f uv)
        set_tex_offset(const NodePath self, TextureStage stage, float u, float v)
        set_tex_offset(const NodePath self, const NodePath other, TextureStage stage, float u, float v)
        
        /**
         * Sets a texture matrix on the current node to apply the indicated offset to
         * UV's for the given stage.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated offset to
         * UV's for the given stage.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated offset to
         * UV's for the given stage.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated offset to
         * UV's for the given stage.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        """
        pass

    def set_tex_pos(self, const_NodePath_self, TextureStage_stage, const_LVecBase3f_uvw): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tex_pos(const NodePath self, TextureStage stage, const LVecBase3f uvw)
        set_tex_pos(const NodePath self, const NodePath other, TextureStage stage, const LVecBase3f uvw)
        set_tex_pos(const NodePath self, TextureStage stage, float u, float v, float w)
        set_tex_pos(const NodePath self, const NodePath other, TextureStage stage, float u, float v, float w)
        
        /**
         * Sets a texture matrix on the current node to apply the indicated offset to
         * UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated offset to
         * UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated offset to
         * UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated offset to
         * UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        """
        pass

    def set_tex_projector(self, const_NodePath_self, TextureStage_stage, const_NodePath_from, const_NodePath_to, int_lens_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tex_projector(const NodePath self, TextureStage stage, const NodePath from, const NodePath to, int lens_index)
        
        /**
         * Establishes a TexProjectorEffect on this node, which can be used to
         * establish projective texturing (but see also the
         * NodePath::project_texture() convenience function), or it can be used to
         * bind this node's texture transform to particular node's position in space,
         * allowing a LerpInterval (for instance) to adjust this node's texture
         * coordinates.
         *
         * If to is a LensNode, then the fourth parameter, lens_index, can be provided
         * to select a particular lens to apply.  Otherwise lens_index is not used.
         */
        """
        pass

    def set_tex_rotate(self, const_NodePath_self, TextureStage_stage, float_r): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tex_rotate(const NodePath self, TextureStage stage, float r)
        set_tex_rotate(const NodePath self, const NodePath other, TextureStage stage, float r)
        
        /**
         * Sets a texture matrix on the current node to apply the indicated rotation,
         * clockwise in degrees, to UV's for the given stage.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated rotation,
         * clockwise in degrees, to UV's for the given stage.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        """
        pass

    def set_tex_scale(self, const_NodePath_self, TextureStage_stage, const_LVecBase2f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tex_scale(const NodePath self, TextureStage stage, const LVecBase2f scale)
        set_tex_scale(const NodePath self, TextureStage stage, const LVecBase3f scale)
        set_tex_scale(const NodePath self, TextureStage stage, float scale)
        set_tex_scale(const NodePath self, TextureStage stage, float su, float sv)
        set_tex_scale(const NodePath self, const NodePath other, TextureStage stage, const LVecBase3f scale)
        set_tex_scale(const NodePath self, const NodePath other, TextureStage stage, const LVecBase2f scale)
        set_tex_scale(const NodePath self, const NodePath other, TextureStage stage, float scale)
        set_tex_scale(const NodePath self, TextureStage stage, float su, float sv, float sw)
        set_tex_scale(const NodePath self, const NodePath other, TextureStage stage, float su, float sv)
        set_tex_scale(const NodePath self, const NodePath other, TextureStage stage, float su, float sv, float sw)
        
        /**
         * Sets a texture matrix on the current node to apply the indicated scale to
         * UVW's for the given stage.
         *
         * This call is appropriate for 2-d or 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated scale to
         * UV's for the given stage.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated scale to
         * UV's for the given stage.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated scale to
         * UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated scale to
         * UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated scale to
         * UV's for the given stage.
         *
         * This call is appropriate for 2-d or 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated scale to
         * UV's for the given stage.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated scale to
         * UV's for the given stage.
         *
         * This call is appropriate for ordinary 2-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated scale to
         * UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        
        /**
         * Sets a texture matrix on the current node to apply the indicated scale to
         * UVW's for the given stage.
         *
         * This call is appropriate for 3-d texture coordinates.
         */
        """
        pass

    def set_tex_transform(self, const_NodePath_self, TextureStage_stage, const_TransformState_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tex_transform(const NodePath self, TextureStage stage, const TransformState transform)
        set_tex_transform(const NodePath self, const NodePath other, TextureStage stage, const TransformState transform)
        
        /**
         * Sets the texture matrix on the current node to the indicated transform for
         * the given stage.
         */
        
        /**
         * Sets the texture matrix on the current node to the indicated transform for
         * the given stage.
         */
        """
        pass

    def set_transform(self, const_NodePath_self, const_TransformState_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_transform(const NodePath self, const TransformState transform)
        set_transform(const NodePath self, const NodePath other, const TransformState transform, Thread current_thread)
        set_transform(const NodePath self, const TransformState transform, Thread current_thread)
        
        /**
         * Changes the complete transform object on this node.
         */
        
        /**
         * Sets the transform object on this node, relative to the other node.  This
         * computes a new transform object that will have the indicated value when
         * seen from the other node.
         */
        """
        pass

    def set_transparency(self, const_NodePath_self, int_mode, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_transparency(const NodePath self, int mode, int priority)
        
        /**
         * Specifically sets or disables transparent rendering mode on this particular
         * node.  If no other nodes override, this will cause items with a non-1 value
         * for alpha color to be rendered partially transparent.
         */
        """
        pass

    def set_two_sided(self, const_NodePath_self, bool_two_sided, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_two_sided(const NodePath self, bool two_sided, int priority)
        
        /**
         * Specifically sets or disables two-sided rendering mode on this particular
         * node.  If no other nodes override, this will cause backfacing polygons to
         * be drawn (in two-sided mode, true) or culled (in one-sided mode, false).
         */
        """
        pass

    def set_x(self, const_NodePath_self, float_x): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_x(const NodePath self, float x)
        set_x(const NodePath self, const NodePath other, float x)
        
        /**
         * Sets the X component of the position transform, leaving other components
         * untouched.
         * @see set_pos()
         */
        """
        pass

    def set_y(self, const_NodePath_self, float_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_y(const NodePath self, float y)
        set_y(const NodePath self, const NodePath other, float y)
        
        /**
         * Sets the Y component of the position transform, leaving other components
         * untouched.
         * @see set_pos()
         */
        """
        pass

    def set_z(self, const_NodePath_self, float_z): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_z(const NodePath self, float z)
        set_z(const NodePath self, const NodePath other, float z)
        
        /**
         * Sets the Z component of the position transform, leaving other components
         * untouched.
         * @see set_pos()
         */
        """
        pass

    def show(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        show(const NodePath self)
        show(const NodePath self, BitMask camera_mask)
        
        // Variants on show and hide
        
        /**
         * Undoes the effect of a previous hide() on this node: makes the referenced
         * node (and the entire subgraph below this node) visible to all cameras.
         *
         * This will not reveal the node if a parent node has been hidden.
         */
        
        /**
         * Makes the referenced node visible just to the cameras whose camera_mask
         * shares the indicated bits.
         *
         * This undoes the effect of a previous hide() call.  It will not reveal the
         * node if a parent node has been hidden.  However, see show_through().
         */
        """
        pass

    def showBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        show_bounds(const NodePath self)
        
        /**
         * Causes the bounding volume of the bottom node and all of its descendants
         * (that is, the bounding volume associated with the the bottom arc) to be
         * rendered, if possible.  The rendering method is less than optimal; this is
         * intended primarily for debugging.
         */
        """
        pass

    def showThrough(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        show_through(const NodePath self)
        show_through(const NodePath self, BitMask camera_mask)
        
        /**
         * Makes the referenced node visible just to the cameras whose camera_mask
         * shares the indicated bits.
         *
         * Unlike show(), this will reveal the node even if a parent node has been
         * hidden, thus "showing through" a parent's hide().
         */
        
        /**
         * Makes the referenced node visible just to the cameras whose camera_mask
         * shares the indicated bits.
         *
         * Unlike show(), this will reveal the node even if a parent node has been
         * hidden via the one-parameter hide() method, thus "showing through" a
         * parent's hide().  (However, it will not show through a parent's hide() call
         * if the no-parameter form of hide() was used.)
         */
        """
        pass

    def showTightBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        show_tight_bounds(const NodePath self)
        
        /**
         * Similar to show_bounds(), this draws a bounding box representing the
         * "tight" bounds of this node and all of its descendants.  The bounding box
         * is recomputed every frame by reexamining all of the vertices; this is far
         * from efficient, but this is intended for debugging.
         */
        """
        pass

    def show_bounds(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        show_bounds(const NodePath self)
        
        /**
         * Causes the bounding volume of the bottom node and all of its descendants
         * (that is, the bounding volume associated with the the bottom arc) to be
         * rendered, if possible.  The rendering method is less than optimal; this is
         * intended primarily for debugging.
         */
        """
        pass

    def show_through(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        show_through(const NodePath self)
        show_through(const NodePath self, BitMask camera_mask)
        
        /**
         * Makes the referenced node visible just to the cameras whose camera_mask
         * shares the indicated bits.
         *
         * Unlike show(), this will reveal the node even if a parent node has been
         * hidden, thus "showing through" a parent's hide().
         */
        
        /**
         * Makes the referenced node visible just to the cameras whose camera_mask
         * shares the indicated bits.
         *
         * Unlike show(), this will reveal the node even if a parent node has been
         * hidden via the one-parameter hide() method, thus "showing through" a
         * parent's hide().  (However, it will not show through a parent's hide() call
         * if the no-parameter form of hide() was used.)
         */
        """
        pass

    def show_tight_bounds(self, const_NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        show_tight_bounds(const NodePath self)
        
        /**
         * Similar to show_bounds(), this draws a bounding box representing the
         * "tight" bounds of this node and all of its descendants.  The bounding box
         * is recomputed every frame by reexamining all of the vertices; this is far
         * from efficient, but this is intended for debugging.
         */
        """
        pass

    def stash(self, const_NodePath_self, int_sort, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        stash(const NodePath self, int sort, Thread current_thread)
        
        /**
         * Removes the referenced node (and the entire subgraph below this node) from
         * the scene graph in any normal sense.  The node will no longer be visible
         * and is not tested for collisions; furthermore, no normal scene graph
         * traversal will visit the node.  The node's bounding volume no longer
         * contributes to its parent's bounding volume.
         *
         * A stashed node cannot be located by a normal find() operation (although a
         * special find string can still retrieve it).
         */
        """
        pass

    def stashTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        stash_to(const NodePath self, const NodePath other, int sort, Thread current_thread)
        
        /**
         * Similar to reparent_to(), but the node is added to its new parent's stashed
         * list, so that the result is equivalent to calling reparent_to() immediately
         * followed by stash().
         */
        """
        pass

    def stash_to(self, const_NodePath_self, const_NodePath_other, int_sort, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        stash_to(const NodePath self, const NodePath other, int sort, Thread current_thread)
        
        /**
         * Similar to reparent_to(), but the node is added to its new parent's stashed
         * list, so that the result is equivalent to calling reparent_to() immediately
         * followed by stash().
         */
        """
        pass

    def unifyTextureStages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unify_texture_stages(const NodePath self, TextureStage stage)
        
        /**
         * Searches through all TextureStages at this node and below.  Any
         * TextureStages that share the same name as the indicated TextureStage object
         * are replaced with this object, thus ensuring that all geometry at this node
         * and below with a particular TextureStage name is using the same
         * TextureStage object.
         */
        """
        pass

    def unify_texture_stages(self, const_NodePath_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unify_texture_stages(const NodePath self, TextureStage stage)
        
        /**
         * Searches through all TextureStages at this node and below.  Any
         * TextureStages that share the same name as the indicated TextureStage object
         * are replaced with this object, thus ensuring that all geometry at this node
         * and below with a particular TextureStage name is using the same
         * TextureStage object.
         */
        """
        pass

    def unstash(self, const_NodePath_self, int_sort, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unstash(const NodePath self, int sort, Thread current_thread)
        
        /**
         * Undoes the effect of a previous stash() on this node: makes the referenced
         * node (and the entire subgraph below this node) once again part of the scene
         * graph.
         */
        """
        pass

    def unstashAll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unstash_all(const NodePath self, Thread current_thread)
        
        /**
         * Unstashes this node and all stashed child nodes.
         */
        """
        pass

    def unstash_all(self, const_NodePath_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unstash_all(const NodePath self, Thread current_thread)
        
        /**
         * Unstashes this node and all stashed child nodes.
         */
        """
        pass

    def verifyComplete(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        verify_complete(NodePath self, Thread current_thread)
        
        // Miscellaneous
        
        /**
         * Returns true if all of the nodes described in the NodePath are connected,
         * or false otherwise.
         */
        """
        pass

    def verify_complete(self, NodePath_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        verify_complete(NodePath self, Thread current_thread)
        
        // Miscellaneous
        
        /**
         * Returns true if all of the nodes described in the NodePath are connected,
         * or false otherwise.
         */
        """
        pass

    def writeBamFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_bam_file(NodePath self, const Filename filename)
        
        /**
         * Writes the contents of this node and below out to a bam file with the
         * indicated filename.  This file may then be read in again, as is, at some
         * later point.  Returns true if successful, false on some kind of error.
         */
        """
        pass

    def writeBamStream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_bam_stream(NodePath self, ostream out)
        
        /**
         * Writes the contents of this node and below out to the indicated stream.
         */
        """
        pass

    def writeBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_bounds(NodePath self, ostream out)
        
        /**
         * Writes a description of the bounding volume containing the bottom node and
         * all of its descendants to the indicated output stream.
         */
        """
        pass

    def write_bam_file(self, NodePath_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_bam_file(NodePath self, const Filename filename)
        
        /**
         * Writes the contents of this node and below out to a bam file with the
         * indicated filename.  This file may then be read in again, as is, at some
         * later point.  Returns true if successful, false on some kind of error.
         */
        """
        pass

    def write_bam_stream(self, NodePath_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_bam_stream(NodePath self, ostream out)
        
        /**
         * Writes the contents of this node and below out to the indicated stream.
         */
        """
        pass

    def write_bounds(self, NodePath_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_bounds(NodePath self, ostream out)
        
        /**
         * Writes a description of the bounding volume containing the bottom node and
         * all of its descendants to the indicated output stream.
         */
        """
        pass

    def wrtReparentTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        wrt_reparent_to(const NodePath self, const NodePath other, int sort, Thread current_thread)
        
        /**
         * This functions identically to reparent_to(), except the transform on this
         * node is also adjusted so that the node remains in the same place in world
         * coordinates, even if it is reparented into a different coordinate system.
         */
        """
        pass

    def wrt_reparent_to(self, const_NodePath_self, const_NodePath_other, int_sort, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        wrt_reparent_to(const NodePath self, const NodePath other, int sort, Thread current_thread)
        
        /**
         * This functions identically to reparent_to(), except the transform on this
         * node is also adjusted so that the node remains in the same place in world
         * coordinates, even if it is reparented into a different coordinate system.
         */
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __copy__(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __copy__(NodePath self)
        """
        pass

    def __deepcopy__(self, NodePath_self, object_memo): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __deepcopy__(NodePath self, object memo)
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_persist__(self, NodePath_self, object_pickler): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __reduce_persist__(NodePath self, object pickler)
        """
        pass

    def __reduce__(self, NodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __reduce__(NodePath self)
        """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    ancestors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    error_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    net_tags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    python_tags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stashed_children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'ETFail': 3,
        'ETNotFound': 1,
        'ETOk': 0,
        'ETRemoved': 2,
        'ET_fail': 3,
        'ET_not_found': 1,
        'ET_ok': 0,
        'ET_removed': 2,
        '__bool__': None, # (!) real value is "<slot wrapper '__bool__' of 'panda3d.core.NodePath' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.NodePath' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.NodePath' objects>"
        '__doc__': '/**\n * NodePath is the fundamental system for disambiguating instances, and also\n * provides a higher-level interface for manipulating the scene graph.\n *\n * A NodePath is a list of connected nodes from the root of the graph to any\n * sub-node.  Each NodePath therefore uniquely describes one instance of a\n * node.\n *\n * NodePaths themselves are lightweight objects that may easily be copied and\n * passed by value.  Their data is stored as a series of NodePathComponents\n * that are stored on the nodes.  Holding a NodePath will keep a reference\n * count to all the nodes in the path.  However, if any node in the path is\n * removed or reparented (perhaps through a different NodePath), the NodePath\n * will automatically be updated to reflect the changes.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.NodePath' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.NodePath' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.NodePath' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.NodePath' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.NodePath' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.NodePath' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.NodePath' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.NodePath' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE293A70>'
        '__reduce__': None, # (!) real value is "<method '__reduce__' of 'panda3d.core.NodePath' objects>"
        '__reduce_persist__': None, # (!) real value is "<method '__reduce_persist__' of 'panda3d.core.NodePath' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.NodePath' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.NodePath' objects>"
        'addHash': None, # (!) real value is "<method 'addHash' of 'panda3d.core.NodePath' objects>"
        'add_hash': None, # (!) real value is "<method 'add_hash' of 'panda3d.core.NodePath' objects>"
        'adjustAllPriorities': None, # (!) real value is "<method 'adjustAllPriorities' of 'panda3d.core.NodePath' objects>"
        'adjust_all_priorities': None, # (!) real value is "<method 'adjust_all_priorities' of 'panda3d.core.NodePath' objects>"
        'ancestors': None, # (!) real value is "<attribute 'ancestors' of 'panda3d.core.NodePath' objects>"
        'anyPath': None, # (!) real value is '<staticmethod(<built-in method anyPath of type object at 0x00007FFCFE293A70>)>'
        'any_path': None, # (!) real value is '<staticmethod(<built-in method any_path of type object at 0x00007FFCFE293A70>)>'
        'applyTextureColors': None, # (!) real value is "<method 'applyTextureColors' of 'panda3d.core.NodePath' objects>"
        'apply_texture_colors': None, # (!) real value is "<method 'apply_texture_colors' of 'panda3d.core.NodePath' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.NodePath' objects>"
        'attachNewNode': None, # (!) real value is "<method 'attachNewNode' of 'panda3d.core.NodePath' objects>"
        'attach_new_node': None, # (!) real value is "<method 'attach_new_node' of 'panda3d.core.NodePath' objects>"
        'calcTightBounds': None, # (!) real value is "<method 'calcTightBounds' of 'panda3d.core.NodePath' objects>"
        'calc_tight_bounds': None, # (!) real value is "<method 'calc_tight_bounds' of 'panda3d.core.NodePath' objects>"
        'children': None, # (!) real value is "<attribute 'children' of 'panda3d.core.NodePath' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.NodePath' objects>"
        'clearAntialias': None, # (!) real value is "<method 'clearAntialias' of 'panda3d.core.NodePath' objects>"
        'clearAttrib': None, # (!) real value is "<method 'clearAttrib' of 'panda3d.core.NodePath' objects>"
        'clearAudioVolume': None, # (!) real value is "<method 'clearAudioVolume' of 'panda3d.core.NodePath' objects>"
        'clearBillboard': None, # (!) real value is "<method 'clearBillboard' of 'panda3d.core.NodePath' objects>"
        'clearBin': None, # (!) real value is "<method 'clearBin' of 'panda3d.core.NodePath' objects>"
        'clearClipPlane': None, # (!) real value is "<method 'clearClipPlane' of 'panda3d.core.NodePath' objects>"
        'clearColor': None, # (!) real value is "<method 'clearColor' of 'panda3d.core.NodePath' objects>"
        'clearColorScale': None, # (!) real value is "<method 'clearColorScale' of 'panda3d.core.NodePath' objects>"
        'clearCompass': None, # (!) real value is "<method 'clearCompass' of 'panda3d.core.NodePath' objects>"
        'clearDepthOffset': None, # (!) real value is "<method 'clearDepthOffset' of 'panda3d.core.NodePath' objects>"
        'clearDepthTest': None, # (!) real value is "<method 'clearDepthTest' of 'panda3d.core.NodePath' objects>"
        'clearDepthWrite': None, # (!) real value is "<method 'clearDepthWrite' of 'panda3d.core.NodePath' objects>"
        'clearEffect': None, # (!) real value is "<method 'clearEffect' of 'panda3d.core.NodePath' objects>"
        'clearEffects': None, # (!) real value is "<method 'clearEffects' of 'panda3d.core.NodePath' objects>"
        'clearFog': None, # (!) real value is "<method 'clearFog' of 'panda3d.core.NodePath' objects>"
        'clearLight': None, # (!) real value is "<method 'clearLight' of 'panda3d.core.NodePath' objects>"
        'clearLogicOp': None, # (!) real value is "<method 'clearLogicOp' of 'panda3d.core.NodePath' objects>"
        'clearMat': None, # (!) real value is "<method 'clearMat' of 'panda3d.core.NodePath' objects>"
        'clearMaterial': None, # (!) real value is "<method 'clearMaterial' of 'panda3d.core.NodePath' objects>"
        'clearModelNodes': None, # (!) real value is "<method 'clearModelNodes' of 'panda3d.core.NodePath' objects>"
        'clearOccluder': None, # (!) real value is "<method 'clearOccluder' of 'panda3d.core.NodePath' objects>"
        'clearProjectTexture': None, # (!) real value is "<method 'clearProjectTexture' of 'panda3d.core.NodePath' objects>"
        'clearPythonTag': None, # (!) real value is "<method 'clearPythonTag' of 'panda3d.core.NodePath' objects>"
        'clearRenderMode': None, # (!) real value is "<method 'clearRenderMode' of 'panda3d.core.NodePath' objects>"
        'clearScissor': None, # (!) real value is "<method 'clearScissor' of 'panda3d.core.NodePath' objects>"
        'clearShader': None, # (!) real value is "<method 'clearShader' of 'panda3d.core.NodePath' objects>"
        'clearShaderInput': None, # (!) real value is "<method 'clearShaderInput' of 'panda3d.core.NodePath' objects>"
        'clearTag': None, # (!) real value is "<method 'clearTag' of 'panda3d.core.NodePath' objects>"
        'clearTexGen': None, # (!) real value is "<method 'clearTexGen' of 'panda3d.core.NodePath' objects>"
        'clearTexProjector': None, # (!) real value is "<method 'clearTexProjector' of 'panda3d.core.NodePath' objects>"
        'clearTexTransform': None, # (!) real value is "<method 'clearTexTransform' of 'panda3d.core.NodePath' objects>"
        'clearTexture': None, # (!) real value is "<method 'clearTexture' of 'panda3d.core.NodePath' objects>"
        'clearTransform': None, # (!) real value is "<method 'clearTransform' of 'panda3d.core.NodePath' objects>"
        'clearTransparency': None, # (!) real value is "<method 'clearTransparency' of 'panda3d.core.NodePath' objects>"
        'clearTwoSided': None, # (!) real value is "<method 'clearTwoSided' of 'panda3d.core.NodePath' objects>"
        'clear_antialias': None, # (!) real value is "<method 'clear_antialias' of 'panda3d.core.NodePath' objects>"
        'clear_attrib': None, # (!) real value is "<method 'clear_attrib' of 'panda3d.core.NodePath' objects>"
        'clear_audio_volume': None, # (!) real value is "<method 'clear_audio_volume' of 'panda3d.core.NodePath' objects>"
        'clear_billboard': None, # (!) real value is "<method 'clear_billboard' of 'panda3d.core.NodePath' objects>"
        'clear_bin': None, # (!) real value is "<method 'clear_bin' of 'panda3d.core.NodePath' objects>"
        'clear_clip_plane': None, # (!) real value is "<method 'clear_clip_plane' of 'panda3d.core.NodePath' objects>"
        'clear_color': None, # (!) real value is "<method 'clear_color' of 'panda3d.core.NodePath' objects>"
        'clear_color_scale': None, # (!) real value is "<method 'clear_color_scale' of 'panda3d.core.NodePath' objects>"
        'clear_compass': None, # (!) real value is "<method 'clear_compass' of 'panda3d.core.NodePath' objects>"
        'clear_depth_offset': None, # (!) real value is "<method 'clear_depth_offset' of 'panda3d.core.NodePath' objects>"
        'clear_depth_test': None, # (!) real value is "<method 'clear_depth_test' of 'panda3d.core.NodePath' objects>"
        'clear_depth_write': None, # (!) real value is "<method 'clear_depth_write' of 'panda3d.core.NodePath' objects>"
        'clear_effect': None, # (!) real value is "<method 'clear_effect' of 'panda3d.core.NodePath' objects>"
        'clear_effects': None, # (!) real value is "<method 'clear_effects' of 'panda3d.core.NodePath' objects>"
        'clear_fog': None, # (!) real value is "<method 'clear_fog' of 'panda3d.core.NodePath' objects>"
        'clear_light': None, # (!) real value is "<method 'clear_light' of 'panda3d.core.NodePath' objects>"
        'clear_logic_op': None, # (!) real value is "<method 'clear_logic_op' of 'panda3d.core.NodePath' objects>"
        'clear_mat': None, # (!) real value is "<method 'clear_mat' of 'panda3d.core.NodePath' objects>"
        'clear_material': None, # (!) real value is "<method 'clear_material' of 'panda3d.core.NodePath' objects>"
        'clear_model_nodes': None, # (!) real value is "<method 'clear_model_nodes' of 'panda3d.core.NodePath' objects>"
        'clear_occluder': None, # (!) real value is "<method 'clear_occluder' of 'panda3d.core.NodePath' objects>"
        'clear_project_texture': None, # (!) real value is "<method 'clear_project_texture' of 'panda3d.core.NodePath' objects>"
        'clear_python_tag': None, # (!) real value is "<method 'clear_python_tag' of 'panda3d.core.NodePath' objects>"
        'clear_render_mode': None, # (!) real value is "<method 'clear_render_mode' of 'panda3d.core.NodePath' objects>"
        'clear_scissor': None, # (!) real value is "<method 'clear_scissor' of 'panda3d.core.NodePath' objects>"
        'clear_shader': None, # (!) real value is "<method 'clear_shader' of 'panda3d.core.NodePath' objects>"
        'clear_shader_input': None, # (!) real value is "<method 'clear_shader_input' of 'panda3d.core.NodePath' objects>"
        'clear_tag': None, # (!) real value is "<method 'clear_tag' of 'panda3d.core.NodePath' objects>"
        'clear_tex_gen': None, # (!) real value is "<method 'clear_tex_gen' of 'panda3d.core.NodePath' objects>"
        'clear_tex_projector': None, # (!) real value is "<method 'clear_tex_projector' of 'panda3d.core.NodePath' objects>"
        'clear_tex_transform': None, # (!) real value is "<method 'clear_tex_transform' of 'panda3d.core.NodePath' objects>"
        'clear_texture': None, # (!) real value is "<method 'clear_texture' of 'panda3d.core.NodePath' objects>"
        'clear_transform': None, # (!) real value is "<method 'clear_transform' of 'panda3d.core.NodePath' objects>"
        'clear_transparency': None, # (!) real value is "<method 'clear_transparency' of 'panda3d.core.NodePath' objects>"
        'clear_two_sided': None, # (!) real value is "<method 'clear_two_sided' of 'panda3d.core.NodePath' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.NodePath' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.NodePath' objects>"
        'composeColorScale': None, # (!) real value is "<method 'composeColorScale' of 'panda3d.core.NodePath' objects>"
        'compose_color_scale': None, # (!) real value is "<method 'compose_color_scale' of 'panda3d.core.NodePath' objects>"
        'copyTo': None, # (!) real value is "<method 'copyTo' of 'panda3d.core.NodePath' objects>"
        'copy_to': None, # (!) real value is "<method 'copy_to' of 'panda3d.core.NodePath' objects>"
        'countNumDescendants': None, # (!) real value is "<method 'countNumDescendants' of 'panda3d.core.NodePath' objects>"
        'count_num_descendants': None, # (!) real value is "<method 'count_num_descendants' of 'panda3d.core.NodePath' objects>"
        'decodeFromBamStream': None, # (!) real value is '<staticmethod(<built-in method decodeFromBamStream of type object at 0x00007FFCFE293A70>)>'
        'decode_from_bam_stream': None, # (!) real value is '<staticmethod(<built-in method decode_from_bam_stream of type object at 0x00007FFCFE293A70>)>'
        'detachNode': None, # (!) real value is "<method 'detachNode' of 'panda3d.core.NodePath' objects>"
        'detach_node': None, # (!) real value is "<method 'detach_node' of 'panda3d.core.NodePath' objects>"
        'doBillboardAxis': None, # (!) real value is "<method 'doBillboardAxis' of 'panda3d.core.NodePath' objects>"
        'doBillboardPointEye': None, # (!) real value is "<method 'doBillboardPointEye' of 'panda3d.core.NodePath' objects>"
        'doBillboardPointWorld': None, # (!) real value is "<method 'doBillboardPointWorld' of 'panda3d.core.NodePath' objects>"
        'do_billboard_axis': None, # (!) real value is "<method 'do_billboard_axis' of 'panda3d.core.NodePath' objects>"
        'do_billboard_point_eye': None, # (!) real value is "<method 'do_billboard_point_eye' of 'panda3d.core.NodePath' objects>"
        'do_billboard_point_world': None, # (!) real value is "<method 'do_billboard_point_world' of 'panda3d.core.NodePath' objects>"
        'encodeToBamStream': None, # (!) real value is "<method 'encodeToBamStream' of 'panda3d.core.NodePath' objects>"
        'encode_to_bam_stream': None, # (!) real value is "<method 'encode_to_bam_stream' of 'panda3d.core.NodePath' objects>"
        'error_type': None, # (!) real value is "<attribute 'error_type' of 'panda3d.core.NodePath' objects>"
        'fail': None, # (!) real value is '<staticmethod(<built-in method fail of type object at 0x00007FFCFE293A70>)>'
        'find': None, # (!) real value is "<method 'find' of 'panda3d.core.NodePath' objects>"
        'findAllMatches': None, # (!) real value is "<method 'findAllMatches' of 'panda3d.core.NodePath' objects>"
        'findAllMaterials': None, # (!) real value is "<method 'findAllMaterials' of 'panda3d.core.NodePath' objects>"
        'findAllPathsTo': None, # (!) real value is "<method 'findAllPathsTo' of 'panda3d.core.NodePath' objects>"
        'findAllTexcoords': None, # (!) real value is "<method 'findAllTexcoords' of 'panda3d.core.NodePath' objects>"
        'findAllTextureStages': None, # (!) real value is "<method 'findAllTextureStages' of 'panda3d.core.NodePath' objects>"
        'findAllTextures': None, # (!) real value is "<method 'findAllTextures' of 'panda3d.core.NodePath' objects>"
        'findAllVertexColumns': None, # (!) real value is "<method 'findAllVertexColumns' of 'panda3d.core.NodePath' objects>"
        'findMaterial': None, # (!) real value is "<method 'findMaterial' of 'panda3d.core.NodePath' objects>"
        'findNetPythonTag': None, # (!) real value is "<method 'findNetPythonTag' of 'panda3d.core.NodePath' objects>"
        'findNetTag': None, # (!) real value is "<method 'findNetTag' of 'panda3d.core.NodePath' objects>"
        'findPathTo': None, # (!) real value is "<method 'findPathTo' of 'panda3d.core.NodePath' objects>"
        'findTexture': None, # (!) real value is "<method 'findTexture' of 'panda3d.core.NodePath' objects>"
        'findTextureStage': None, # (!) real value is "<method 'findTextureStage' of 'panda3d.core.NodePath' objects>"
        'find_all_matches': None, # (!) real value is "<method 'find_all_matches' of 'panda3d.core.NodePath' objects>"
        'find_all_materials': None, # (!) real value is "<method 'find_all_materials' of 'panda3d.core.NodePath' objects>"
        'find_all_paths_to': None, # (!) real value is "<method 'find_all_paths_to' of 'panda3d.core.NodePath' objects>"
        'find_all_texcoords': None, # (!) real value is "<method 'find_all_texcoords' of 'panda3d.core.NodePath' objects>"
        'find_all_texture_stages': None, # (!) real value is "<method 'find_all_texture_stages' of 'panda3d.core.NodePath' objects>"
        'find_all_textures': None, # (!) real value is "<method 'find_all_textures' of 'panda3d.core.NodePath' objects>"
        'find_all_vertex_columns': None, # (!) real value is "<method 'find_all_vertex_columns' of 'panda3d.core.NodePath' objects>"
        'find_material': None, # (!) real value is "<method 'find_material' of 'panda3d.core.NodePath' objects>"
        'find_net_python_tag': None, # (!) real value is "<method 'find_net_python_tag' of 'panda3d.core.NodePath' objects>"
        'find_net_tag': None, # (!) real value is "<method 'find_net_tag' of 'panda3d.core.NodePath' objects>"
        'find_path_to': None, # (!) real value is "<method 'find_path_to' of 'panda3d.core.NodePath' objects>"
        'find_texture': None, # (!) real value is "<method 'find_texture' of 'panda3d.core.NodePath' objects>"
        'find_texture_stage': None, # (!) real value is "<method 'find_texture_stage' of 'panda3d.core.NodePath' objects>"
        'flattenLight': None, # (!) real value is "<method 'flattenLight' of 'panda3d.core.NodePath' objects>"
        'flattenMedium': None, # (!) real value is "<method 'flattenMedium' of 'panda3d.core.NodePath' objects>"
        'flattenStrong': None, # (!) real value is "<method 'flattenStrong' of 'panda3d.core.NodePath' objects>"
        'flatten_light': None, # (!) real value is "<method 'flatten_light' of 'panda3d.core.NodePath' objects>"
        'flatten_medium': None, # (!) real value is "<method 'flatten_medium' of 'panda3d.core.NodePath' objects>"
        'flatten_strong': None, # (!) real value is "<method 'flatten_strong' of 'panda3d.core.NodePath' objects>"
        'forceRecomputeBounds': None, # (!) real value is "<method 'forceRecomputeBounds' of 'panda3d.core.NodePath' objects>"
        'force_recompute_bounds': None, # (!) real value is "<method 'force_recompute_bounds' of 'panda3d.core.NodePath' objects>"
        'getAncestor': None, # (!) real value is "<method 'getAncestor' of 'panda3d.core.NodePath' objects>"
        'getAncestors': None, # (!) real value is "<method 'getAncestors' of 'panda3d.core.NodePath' objects>"
        'getAntialias': None, # (!) real value is "<method 'getAntialias' of 'panda3d.core.NodePath' objects>"
        'getAttrib': None, # (!) real value is "<method 'getAttrib' of 'panda3d.core.NodePath' objects>"
        'getAudioVolume': None, # (!) real value is "<method 'getAudioVolume' of 'panda3d.core.NodePath' objects>"
        'getBinDrawOrder': None, # (!) real value is "<method 'getBinDrawOrder' of 'panda3d.core.NodePath' objects>"
        'getBinName': None, # (!) real value is "<method 'getBinName' of 'panda3d.core.NodePath' objects>"
        'getBounds': None, # (!) real value is "<method 'getBounds' of 'panda3d.core.NodePath' objects>"
        'getChild': None, # (!) real value is "<method 'getChild' of 'panda3d.core.NodePath' objects>"
        'getChildren': None, # (!) real value is "<method 'getChildren' of 'panda3d.core.NodePath' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE293A70>)>'
        'getCollideMask': None, # (!) real value is "<method 'getCollideMask' of 'panda3d.core.NodePath' objects>"
        'getColor': None, # (!) real value is "<method 'getColor' of 'panda3d.core.NodePath' objects>"
        'getColorScale': None, # (!) real value is "<method 'getColorScale' of 'panda3d.core.NodePath' objects>"
        'getCommonAncestor': None, # (!) real value is "<method 'getCommonAncestor' of 'panda3d.core.NodePath' objects>"
        'getDepthOffset': None, # (!) real value is "<method 'getDepthOffset' of 'panda3d.core.NodePath' objects>"
        'getDepthTest': None, # (!) real value is "<method 'getDepthTest' of 'panda3d.core.NodePath' objects>"
        'getDepthWrite': None, # (!) real value is "<method 'getDepthWrite' of 'panda3d.core.NodePath' objects>"
        'getDistance': None, # (!) real value is "<method 'getDistance' of 'panda3d.core.NodePath' objects>"
        'getEffect': None, # (!) real value is "<method 'getEffect' of 'panda3d.core.NodePath' objects>"
        'getEffects': None, # (!) real value is "<method 'getEffects' of 'panda3d.core.NodePath' objects>"
        'getErrorType': None, # (!) real value is "<method 'getErrorType' of 'panda3d.core.NodePath' objects>"
        'getFog': None, # (!) real value is "<method 'getFog' of 'panda3d.core.NodePath' objects>"
        'getH': None, # (!) real value is "<method 'getH' of 'panda3d.core.NodePath' objects>"
        'getHiddenAncestor': None, # (!) real value is "<method 'getHiddenAncestor' of 'panda3d.core.NodePath' objects>"
        'getHpr': None, # (!) real value is "<method 'getHpr' of 'panda3d.core.NodePath' objects>"
        'getInstanceCount': None, # (!) real value is "<method 'getInstanceCount' of 'panda3d.core.NodePath' objects>"
        'getKey': None, # (!) real value is "<method 'getKey' of 'panda3d.core.NodePath' objects>"
        'getLogicOp': None, # (!) real value is "<method 'getLogicOp' of 'panda3d.core.NodePath' objects>"
        'getMat': None, # (!) real value is "<method 'getMat' of 'panda3d.core.NodePath' objects>"
        'getMaterial': None, # (!) real value is "<method 'getMaterial' of 'panda3d.core.NodePath' objects>"
        'getMaxSearchDepth': None, # (!) real value is '<staticmethod(<built-in method getMaxSearchDepth of type object at 0x00007FFCFE293A70>)>'
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.NodePath' objects>"
        'getNetAudioVolume': None, # (!) real value is "<method 'getNetAudioVolume' of 'panda3d.core.NodePath' objects>"
        'getNetPrevTransform': None, # (!) real value is "<method 'getNetPrevTransform' of 'panda3d.core.NodePath' objects>"
        'getNetPythonTag': None, # (!) real value is "<method 'getNetPythonTag' of 'panda3d.core.NodePath' objects>"
        'getNetState': None, # (!) real value is "<method 'getNetState' of 'panda3d.core.NodePath' objects>"
        'getNetTag': None, # (!) real value is "<method 'getNetTag' of 'panda3d.core.NodePath' objects>"
        'getNetTransform': None, # (!) real value is "<method 'getNetTransform' of 'panda3d.core.NodePath' objects>"
        'getNode': None, # (!) real value is "<method 'getNode' of 'panda3d.core.NodePath' objects>"
        'getNodes': None, # (!) real value is "<method 'getNodes' of 'panda3d.core.NodePath' objects>"
        'getNumChildren': None, # (!) real value is "<method 'getNumChildren' of 'panda3d.core.NodePath' objects>"
        'getNumNodes': None, # (!) real value is "<method 'getNumNodes' of 'panda3d.core.NodePath' objects>"
        'getP': None, # (!) real value is "<method 'getP' of 'panda3d.core.NodePath' objects>"
        'getParent': None, # (!) real value is "<method 'getParent' of 'panda3d.core.NodePath' objects>"
        'getPos': None, # (!) real value is "<method 'getPos' of 'panda3d.core.NodePath' objects>"
        'getPosDelta': None, # (!) real value is "<method 'getPosDelta' of 'panda3d.core.NodePath' objects>"
        'getPrevTransform': None, # (!) real value is "<method 'getPrevTransform' of 'panda3d.core.NodePath' objects>"
        'getPythonTag': None, # (!) real value is "<method 'getPythonTag' of 'panda3d.core.NodePath' objects>"
        'getPythonTagKeys': None, # (!) real value is "<method 'getPythonTagKeys' of 'panda3d.core.NodePath' objects>"
        'getPythonTags': None, # (!) real value is "<method 'getPythonTags' of 'panda3d.core.NodePath' objects>"
        'getQuat': None, # (!) real value is "<method 'getQuat' of 'panda3d.core.NodePath' objects>"
        'getR': None, # (!) real value is "<method 'getR' of 'panda3d.core.NodePath' objects>"
        'getRelativePoint': None, # (!) real value is "<method 'getRelativePoint' of 'panda3d.core.NodePath' objects>"
        'getRelativeVector': None, # (!) real value is "<method 'getRelativeVector' of 'panda3d.core.NodePath' objects>"
        'getRenderMode': None, # (!) real value is "<method 'getRenderMode' of 'panda3d.core.NodePath' objects>"
        'getRenderModePerspective': None, # (!) real value is "<method 'getRenderModePerspective' of 'panda3d.core.NodePath' objects>"
        'getRenderModeThickness': None, # (!) real value is "<method 'getRenderModeThickness' of 'panda3d.core.NodePath' objects>"
        'getSa': None, # (!) real value is "<method 'getSa' of 'panda3d.core.NodePath' objects>"
        'getSb': None, # (!) real value is "<method 'getSb' of 'panda3d.core.NodePath' objects>"
        'getScale': None, # (!) real value is "<method 'getScale' of 'panda3d.core.NodePath' objects>"
        'getSg': None, # (!) real value is "<method 'getSg' of 'panda3d.core.NodePath' objects>"
        'getShader': None, # (!) real value is "<method 'getShader' of 'panda3d.core.NodePath' objects>"
        'getShaderInput': None, # (!) real value is "<method 'getShaderInput' of 'panda3d.core.NodePath' objects>"
        'getShear': None, # (!) real value is "<method 'getShear' of 'panda3d.core.NodePath' objects>"
        'getShxy': None, # (!) real value is "<method 'getShxy' of 'panda3d.core.NodePath' objects>"
        'getShxz': None, # (!) real value is "<method 'getShxz' of 'panda3d.core.NodePath' objects>"
        'getShyz': None, # (!) real value is "<method 'getShyz' of 'panda3d.core.NodePath' objects>"
        'getSort': None, # (!) real value is "<method 'getSort' of 'panda3d.core.NodePath' objects>"
        'getSr': None, # (!) real value is "<method 'getSr' of 'panda3d.core.NodePath' objects>"
        'getStashedAncestor': None, # (!) real value is "<method 'getStashedAncestor' of 'panda3d.core.NodePath' objects>"
        'getStashedChildren': None, # (!) real value is "<method 'getStashedChildren' of 'panda3d.core.NodePath' objects>"
        'getState': None, # (!) real value is "<method 'getState' of 'panda3d.core.NodePath' objects>"
        'getSx': None, # (!) real value is "<method 'getSx' of 'panda3d.core.NodePath' objects>"
        'getSy': None, # (!) real value is "<method 'getSy' of 'panda3d.core.NodePath' objects>"
        'getSz': None, # (!) real value is "<method 'getSz' of 'panda3d.core.NodePath' objects>"
        'getTag': None, # (!) real value is "<method 'getTag' of 'panda3d.core.NodePath' objects>"
        'getTagKeys': None, # (!) real value is "<method 'getTagKeys' of 'panda3d.core.NodePath' objects>"
        'getTags': None, # (!) real value is "<method 'getTags' of 'panda3d.core.NodePath' objects>"
        'getTexGen': None, # (!) real value is "<method 'getTexGen' of 'panda3d.core.NodePath' objects>"
        'getTexHpr': None, # (!) real value is "<method 'getTexHpr' of 'panda3d.core.NodePath' objects>"
        'getTexOffset': None, # (!) real value is "<method 'getTexOffset' of 'panda3d.core.NodePath' objects>"
        'getTexPos': None, # (!) real value is "<method 'getTexPos' of 'panda3d.core.NodePath' objects>"
        'getTexProjectorFrom': None, # (!) real value is "<method 'getTexProjectorFrom' of 'panda3d.core.NodePath' objects>"
        'getTexProjectorTo': None, # (!) real value is "<method 'getTexProjectorTo' of 'panda3d.core.NodePath' objects>"
        'getTexRotate': None, # (!) real value is "<method 'getTexRotate' of 'panda3d.core.NodePath' objects>"
        'getTexScale': None, # (!) real value is "<method 'getTexScale' of 'panda3d.core.NodePath' objects>"
        'getTexScale3d': None, # (!) real value is "<method 'getTexScale3d' of 'panda3d.core.NodePath' objects>"
        'getTexTransform': None, # (!) real value is "<method 'getTexTransform' of 'panda3d.core.NodePath' objects>"
        'getTexture': None, # (!) real value is "<method 'getTexture' of 'panda3d.core.NodePath' objects>"
        'getTextureSampler': None, # (!) real value is "<method 'getTextureSampler' of 'panda3d.core.NodePath' objects>"
        'getTightBounds': None, # (!) real value is "<method 'getTightBounds' of 'panda3d.core.NodePath' objects>"
        'getTop': None, # (!) real value is "<method 'getTop' of 'panda3d.core.NodePath' objects>"
        'getTopNode': None, # (!) real value is "<method 'getTopNode' of 'panda3d.core.NodePath' objects>"
        'getTransform': None, # (!) real value is "<method 'getTransform' of 'panda3d.core.NodePath' objects>"
        'getTransparency': None, # (!) real value is "<method 'getTransparency' of 'panda3d.core.NodePath' objects>"
        'getTwoSided': None, # (!) real value is "<method 'getTwoSided' of 'panda3d.core.NodePath' objects>"
        'getX': None, # (!) real value is "<method 'getX' of 'panda3d.core.NodePath' objects>"
        'getY': None, # (!) real value is "<method 'getY' of 'panda3d.core.NodePath' objects>"
        'getZ': None, # (!) real value is "<method 'getZ' of 'panda3d.core.NodePath' objects>"
        'get_ancestor': None, # (!) real value is "<method 'get_ancestor' of 'panda3d.core.NodePath' objects>"
        'get_ancestors': None, # (!) real value is "<method 'get_ancestors' of 'panda3d.core.NodePath' objects>"
        'get_antialias': None, # (!) real value is "<method 'get_antialias' of 'panda3d.core.NodePath' objects>"
        'get_attrib': None, # (!) real value is "<method 'get_attrib' of 'panda3d.core.NodePath' objects>"
        'get_audio_volume': None, # (!) real value is "<method 'get_audio_volume' of 'panda3d.core.NodePath' objects>"
        'get_bin_draw_order': None, # (!) real value is "<method 'get_bin_draw_order' of 'panda3d.core.NodePath' objects>"
        'get_bin_name': None, # (!) real value is "<method 'get_bin_name' of 'panda3d.core.NodePath' objects>"
        'get_bounds': None, # (!) real value is "<method 'get_bounds' of 'panda3d.core.NodePath' objects>"
        'get_child': None, # (!) real value is "<method 'get_child' of 'panda3d.core.NodePath' objects>"
        'get_children': None, # (!) real value is "<method 'get_children' of 'panda3d.core.NodePath' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE293A70>)>'
        'get_collide_mask': None, # (!) real value is "<method 'get_collide_mask' of 'panda3d.core.NodePath' objects>"
        'get_color': None, # (!) real value is "<method 'get_color' of 'panda3d.core.NodePath' objects>"
        'get_color_scale': None, # (!) real value is "<method 'get_color_scale' of 'panda3d.core.NodePath' objects>"
        'get_common_ancestor': None, # (!) real value is "<method 'get_common_ancestor' of 'panda3d.core.NodePath' objects>"
        'get_depth_offset': None, # (!) real value is "<method 'get_depth_offset' of 'panda3d.core.NodePath' objects>"
        'get_depth_test': None, # (!) real value is "<method 'get_depth_test' of 'panda3d.core.NodePath' objects>"
        'get_depth_write': None, # (!) real value is "<method 'get_depth_write' of 'panda3d.core.NodePath' objects>"
        'get_distance': None, # (!) real value is "<method 'get_distance' of 'panda3d.core.NodePath' objects>"
        'get_effect': None, # (!) real value is "<method 'get_effect' of 'panda3d.core.NodePath' objects>"
        'get_effects': None, # (!) real value is "<method 'get_effects' of 'panda3d.core.NodePath' objects>"
        'get_error_type': None, # (!) real value is "<method 'get_error_type' of 'panda3d.core.NodePath' objects>"
        'get_fog': None, # (!) real value is "<method 'get_fog' of 'panda3d.core.NodePath' objects>"
        'get_h': None, # (!) real value is "<method 'get_h' of 'panda3d.core.NodePath' objects>"
        'get_hidden_ancestor': None, # (!) real value is "<method 'get_hidden_ancestor' of 'panda3d.core.NodePath' objects>"
        'get_hpr': None, # (!) real value is "<method 'get_hpr' of 'panda3d.core.NodePath' objects>"
        'get_instance_count': None, # (!) real value is "<method 'get_instance_count' of 'panda3d.core.NodePath' objects>"
        'get_key': None, # (!) real value is "<method 'get_key' of 'panda3d.core.NodePath' objects>"
        'get_logic_op': None, # (!) real value is "<method 'get_logic_op' of 'panda3d.core.NodePath' objects>"
        'get_mat': None, # (!) real value is "<method 'get_mat' of 'panda3d.core.NodePath' objects>"
        'get_material': None, # (!) real value is "<method 'get_material' of 'panda3d.core.NodePath' objects>"
        'get_max_search_depth': None, # (!) real value is '<staticmethod(<built-in method get_max_search_depth of type object at 0x00007FFCFE293A70>)>'
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.NodePath' objects>"
        'get_net_audio_volume': None, # (!) real value is "<method 'get_net_audio_volume' of 'panda3d.core.NodePath' objects>"
        'get_net_prev_transform': None, # (!) real value is "<method 'get_net_prev_transform' of 'panda3d.core.NodePath' objects>"
        'get_net_python_tag': None, # (!) real value is "<method 'get_net_python_tag' of 'panda3d.core.NodePath' objects>"
        'get_net_state': None, # (!) real value is "<method 'get_net_state' of 'panda3d.core.NodePath' objects>"
        'get_net_tag': None, # (!) real value is "<method 'get_net_tag' of 'panda3d.core.NodePath' objects>"
        'get_net_transform': None, # (!) real value is "<method 'get_net_transform' of 'panda3d.core.NodePath' objects>"
        'get_node': None, # (!) real value is "<method 'get_node' of 'panda3d.core.NodePath' objects>"
        'get_nodes': None, # (!) real value is "<method 'get_nodes' of 'panda3d.core.NodePath' objects>"
        'get_num_children': None, # (!) real value is "<method 'get_num_children' of 'panda3d.core.NodePath' objects>"
        'get_num_nodes': None, # (!) real value is "<method 'get_num_nodes' of 'panda3d.core.NodePath' objects>"
        'get_p': None, # (!) real value is "<method 'get_p' of 'panda3d.core.NodePath' objects>"
        'get_parent': None, # (!) real value is "<method 'get_parent' of 'panda3d.core.NodePath' objects>"
        'get_pos': None, # (!) real value is "<method 'get_pos' of 'panda3d.core.NodePath' objects>"
        'get_pos_delta': None, # (!) real value is "<method 'get_pos_delta' of 'panda3d.core.NodePath' objects>"
        'get_prev_transform': None, # (!) real value is "<method 'get_prev_transform' of 'panda3d.core.NodePath' objects>"
        'get_python_tag': None, # (!) real value is "<method 'get_python_tag' of 'panda3d.core.NodePath' objects>"
        'get_python_tag_keys': None, # (!) real value is "<method 'get_python_tag_keys' of 'panda3d.core.NodePath' objects>"
        'get_python_tags': None, # (!) real value is "<method 'get_python_tags' of 'panda3d.core.NodePath' objects>"
        'get_quat': None, # (!) real value is "<method 'get_quat' of 'panda3d.core.NodePath' objects>"
        'get_r': None, # (!) real value is "<method 'get_r' of 'panda3d.core.NodePath' objects>"
        'get_relative_point': None, # (!) real value is "<method 'get_relative_point' of 'panda3d.core.NodePath' objects>"
        'get_relative_vector': None, # (!) real value is "<method 'get_relative_vector' of 'panda3d.core.NodePath' objects>"
        'get_render_mode': None, # (!) real value is "<method 'get_render_mode' of 'panda3d.core.NodePath' objects>"
        'get_render_mode_perspective': None, # (!) real value is "<method 'get_render_mode_perspective' of 'panda3d.core.NodePath' objects>"
        'get_render_mode_thickness': None, # (!) real value is "<method 'get_render_mode_thickness' of 'panda3d.core.NodePath' objects>"
        'get_sa': None, # (!) real value is "<method 'get_sa' of 'panda3d.core.NodePath' objects>"
        'get_sb': None, # (!) real value is "<method 'get_sb' of 'panda3d.core.NodePath' objects>"
        'get_scale': None, # (!) real value is "<method 'get_scale' of 'panda3d.core.NodePath' objects>"
        'get_sg': None, # (!) real value is "<method 'get_sg' of 'panda3d.core.NodePath' objects>"
        'get_shader': None, # (!) real value is "<method 'get_shader' of 'panda3d.core.NodePath' objects>"
        'get_shader_input': None, # (!) real value is "<method 'get_shader_input' of 'panda3d.core.NodePath' objects>"
        'get_shear': None, # (!) real value is "<method 'get_shear' of 'panda3d.core.NodePath' objects>"
        'get_shxy': None, # (!) real value is "<method 'get_shxy' of 'panda3d.core.NodePath' objects>"
        'get_shxz': None, # (!) real value is "<method 'get_shxz' of 'panda3d.core.NodePath' objects>"
        'get_shyz': None, # (!) real value is "<method 'get_shyz' of 'panda3d.core.NodePath' objects>"
        'get_sort': None, # (!) real value is "<method 'get_sort' of 'panda3d.core.NodePath' objects>"
        'get_sr': None, # (!) real value is "<method 'get_sr' of 'panda3d.core.NodePath' objects>"
        'get_stashed_ancestor': None, # (!) real value is "<method 'get_stashed_ancestor' of 'panda3d.core.NodePath' objects>"
        'get_stashed_children': None, # (!) real value is "<method 'get_stashed_children' of 'panda3d.core.NodePath' objects>"
        'get_state': None, # (!) real value is "<method 'get_state' of 'panda3d.core.NodePath' objects>"
        'get_sx': None, # (!) real value is "<method 'get_sx' of 'panda3d.core.NodePath' objects>"
        'get_sy': None, # (!) real value is "<method 'get_sy' of 'panda3d.core.NodePath' objects>"
        'get_sz': None, # (!) real value is "<method 'get_sz' of 'panda3d.core.NodePath' objects>"
        'get_tag': None, # (!) real value is "<method 'get_tag' of 'panda3d.core.NodePath' objects>"
        'get_tag_keys': None, # (!) real value is "<method 'get_tag_keys' of 'panda3d.core.NodePath' objects>"
        'get_tags': None, # (!) real value is "<method 'get_tags' of 'panda3d.core.NodePath' objects>"
        'get_tex_gen': None, # (!) real value is "<method 'get_tex_gen' of 'panda3d.core.NodePath' objects>"
        'get_tex_hpr': None, # (!) real value is "<method 'get_tex_hpr' of 'panda3d.core.NodePath' objects>"
        'get_tex_offset': None, # (!) real value is "<method 'get_tex_offset' of 'panda3d.core.NodePath' objects>"
        'get_tex_pos': None, # (!) real value is "<method 'get_tex_pos' of 'panda3d.core.NodePath' objects>"
        'get_tex_projector_from': None, # (!) real value is "<method 'get_tex_projector_from' of 'panda3d.core.NodePath' objects>"
        'get_tex_projector_to': None, # (!) real value is "<method 'get_tex_projector_to' of 'panda3d.core.NodePath' objects>"
        'get_tex_rotate': None, # (!) real value is "<method 'get_tex_rotate' of 'panda3d.core.NodePath' objects>"
        'get_tex_scale': None, # (!) real value is "<method 'get_tex_scale' of 'panda3d.core.NodePath' objects>"
        'get_tex_scale_3d': None, # (!) real value is "<method 'get_tex_scale_3d' of 'panda3d.core.NodePath' objects>"
        'get_tex_transform': None, # (!) real value is "<method 'get_tex_transform' of 'panda3d.core.NodePath' objects>"
        'get_texture': None, # (!) real value is "<method 'get_texture' of 'panda3d.core.NodePath' objects>"
        'get_texture_sampler': None, # (!) real value is "<method 'get_texture_sampler' of 'panda3d.core.NodePath' objects>"
        'get_tight_bounds': None, # (!) real value is "<method 'get_tight_bounds' of 'panda3d.core.NodePath' objects>"
        'get_top': None, # (!) real value is "<method 'get_top' of 'panda3d.core.NodePath' objects>"
        'get_top_node': None, # (!) real value is "<method 'get_top_node' of 'panda3d.core.NodePath' objects>"
        'get_transform': None, # (!) real value is "<method 'get_transform' of 'panda3d.core.NodePath' objects>"
        'get_transparency': None, # (!) real value is "<method 'get_transparency' of 'panda3d.core.NodePath' objects>"
        'get_two_sided': None, # (!) real value is "<method 'get_two_sided' of 'panda3d.core.NodePath' objects>"
        'get_x': None, # (!) real value is "<method 'get_x' of 'panda3d.core.NodePath' objects>"
        'get_y': None, # (!) real value is "<method 'get_y' of 'panda3d.core.NodePath' objects>"
        'get_z': None, # (!) real value is "<method 'get_z' of 'panda3d.core.NodePath' objects>"
        'hasAntialias': None, # (!) real value is "<method 'hasAntialias' of 'panda3d.core.NodePath' objects>"
        'hasAttrib': None, # (!) real value is "<method 'hasAttrib' of 'panda3d.core.NodePath' objects>"
        'hasAudioVolume': None, # (!) real value is "<method 'hasAudioVolume' of 'panda3d.core.NodePath' objects>"
        'hasBillboard': None, # (!) real value is "<method 'hasBillboard' of 'panda3d.core.NodePath' objects>"
        'hasBin': None, # (!) real value is "<method 'hasBin' of 'panda3d.core.NodePath' objects>"
        'hasClipPlane': None, # (!) real value is "<method 'hasClipPlane' of 'panda3d.core.NodePath' objects>"
        'hasClipPlaneOff': None, # (!) real value is "<method 'hasClipPlaneOff' of 'panda3d.core.NodePath' objects>"
        'hasColor': None, # (!) real value is "<method 'hasColor' of 'panda3d.core.NodePath' objects>"
        'hasColorScale': None, # (!) real value is "<method 'hasColorScale' of 'panda3d.core.NodePath' objects>"
        'hasCompass': None, # (!) real value is "<method 'hasCompass' of 'panda3d.core.NodePath' objects>"
        'hasDepthOffset': None, # (!) real value is "<method 'hasDepthOffset' of 'panda3d.core.NodePath' objects>"
        'hasDepthTest': None, # (!) real value is "<method 'hasDepthTest' of 'panda3d.core.NodePath' objects>"
        'hasDepthWrite': None, # (!) real value is "<method 'hasDepthWrite' of 'panda3d.core.NodePath' objects>"
        'hasEffect': None, # (!) real value is "<method 'hasEffect' of 'panda3d.core.NodePath' objects>"
        'hasFog': None, # (!) real value is "<method 'hasFog' of 'panda3d.core.NodePath' objects>"
        'hasFogOff': None, # (!) real value is "<method 'hasFogOff' of 'panda3d.core.NodePath' objects>"
        'hasLight': None, # (!) real value is "<method 'hasLight' of 'panda3d.core.NodePath' objects>"
        'hasLightOff': None, # (!) real value is "<method 'hasLightOff' of 'panda3d.core.NodePath' objects>"
        'hasLogicOp': None, # (!) real value is "<method 'hasLogicOp' of 'panda3d.core.NodePath' objects>"
        'hasMat': None, # (!) real value is "<method 'hasMat' of 'panda3d.core.NodePath' objects>"
        'hasMaterial': None, # (!) real value is "<method 'hasMaterial' of 'panda3d.core.NodePath' objects>"
        'hasNetPythonTag': None, # (!) real value is "<method 'hasNetPythonTag' of 'panda3d.core.NodePath' objects>"
        'hasNetTag': None, # (!) real value is "<method 'hasNetTag' of 'panda3d.core.NodePath' objects>"
        'hasOccluder': None, # (!) real value is "<method 'hasOccluder' of 'panda3d.core.NodePath' objects>"
        'hasParent': None, # (!) real value is "<method 'hasParent' of 'panda3d.core.NodePath' objects>"
        'hasPythonTag': None, # (!) real value is "<method 'hasPythonTag' of 'panda3d.core.NodePath' objects>"
        'hasRenderMode': None, # (!) real value is "<method 'hasRenderMode' of 'panda3d.core.NodePath' objects>"
        'hasScissor': None, # (!) real value is "<method 'hasScissor' of 'panda3d.core.NodePath' objects>"
        'hasTag': None, # (!) real value is "<method 'hasTag' of 'panda3d.core.NodePath' objects>"
        'hasTexGen': None, # (!) real value is "<method 'hasTexGen' of 'panda3d.core.NodePath' objects>"
        'hasTexProjector': None, # (!) real value is "<method 'hasTexProjector' of 'panda3d.core.NodePath' objects>"
        'hasTexTransform': None, # (!) real value is "<method 'hasTexTransform' of 'panda3d.core.NodePath' objects>"
        'hasTexcoord': None, # (!) real value is "<method 'hasTexcoord' of 'panda3d.core.NodePath' objects>"
        'hasTexture': None, # (!) real value is "<method 'hasTexture' of 'panda3d.core.NodePath' objects>"
        'hasTextureOff': None, # (!) real value is "<method 'hasTextureOff' of 'panda3d.core.NodePath' objects>"
        'hasTransparency': None, # (!) real value is "<method 'hasTransparency' of 'panda3d.core.NodePath' objects>"
        'hasTwoSided': None, # (!) real value is "<method 'hasTwoSided' of 'panda3d.core.NodePath' objects>"
        'hasVertexColumn': None, # (!) real value is "<method 'hasVertexColumn' of 'panda3d.core.NodePath' objects>"
        'has_antialias': None, # (!) real value is "<method 'has_antialias' of 'panda3d.core.NodePath' objects>"
        'has_attrib': None, # (!) real value is "<method 'has_attrib' of 'panda3d.core.NodePath' objects>"
        'has_audio_volume': None, # (!) real value is "<method 'has_audio_volume' of 'panda3d.core.NodePath' objects>"
        'has_billboard': None, # (!) real value is "<method 'has_billboard' of 'panda3d.core.NodePath' objects>"
        'has_bin': None, # (!) real value is "<method 'has_bin' of 'panda3d.core.NodePath' objects>"
        'has_clip_plane': None, # (!) real value is "<method 'has_clip_plane' of 'panda3d.core.NodePath' objects>"
        'has_clip_plane_off': None, # (!) real value is "<method 'has_clip_plane_off' of 'panda3d.core.NodePath' objects>"
        'has_color': None, # (!) real value is "<method 'has_color' of 'panda3d.core.NodePath' objects>"
        'has_color_scale': None, # (!) real value is "<method 'has_color_scale' of 'panda3d.core.NodePath' objects>"
        'has_compass': None, # (!) real value is "<method 'has_compass' of 'panda3d.core.NodePath' objects>"
        'has_depth_offset': None, # (!) real value is "<method 'has_depth_offset' of 'panda3d.core.NodePath' objects>"
        'has_depth_test': None, # (!) real value is "<method 'has_depth_test' of 'panda3d.core.NodePath' objects>"
        'has_depth_write': None, # (!) real value is "<method 'has_depth_write' of 'panda3d.core.NodePath' objects>"
        'has_effect': None, # (!) real value is "<method 'has_effect' of 'panda3d.core.NodePath' objects>"
        'has_fog': None, # (!) real value is "<method 'has_fog' of 'panda3d.core.NodePath' objects>"
        'has_fog_off': None, # (!) real value is "<method 'has_fog_off' of 'panda3d.core.NodePath' objects>"
        'has_light': None, # (!) real value is "<method 'has_light' of 'panda3d.core.NodePath' objects>"
        'has_light_off': None, # (!) real value is "<method 'has_light_off' of 'panda3d.core.NodePath' objects>"
        'has_logic_op': None, # (!) real value is "<method 'has_logic_op' of 'panda3d.core.NodePath' objects>"
        'has_mat': None, # (!) real value is "<method 'has_mat' of 'panda3d.core.NodePath' objects>"
        'has_material': None, # (!) real value is "<method 'has_material' of 'panda3d.core.NodePath' objects>"
        'has_net_python_tag': None, # (!) real value is "<method 'has_net_python_tag' of 'panda3d.core.NodePath' objects>"
        'has_net_tag': None, # (!) real value is "<method 'has_net_tag' of 'panda3d.core.NodePath' objects>"
        'has_occluder': None, # (!) real value is "<method 'has_occluder' of 'panda3d.core.NodePath' objects>"
        'has_parent': None, # (!) real value is "<method 'has_parent' of 'panda3d.core.NodePath' objects>"
        'has_python_tag': None, # (!) real value is "<method 'has_python_tag' of 'panda3d.core.NodePath' objects>"
        'has_render_mode': None, # (!) real value is "<method 'has_render_mode' of 'panda3d.core.NodePath' objects>"
        'has_scissor': None, # (!) real value is "<method 'has_scissor' of 'panda3d.core.NodePath' objects>"
        'has_tag': None, # (!) real value is "<method 'has_tag' of 'panda3d.core.NodePath' objects>"
        'has_tex_gen': None, # (!) real value is "<method 'has_tex_gen' of 'panda3d.core.NodePath' objects>"
        'has_tex_projector': None, # (!) real value is "<method 'has_tex_projector' of 'panda3d.core.NodePath' objects>"
        'has_tex_transform': None, # (!) real value is "<method 'has_tex_transform' of 'panda3d.core.NodePath' objects>"
        'has_texcoord': None, # (!) real value is "<method 'has_texcoord' of 'panda3d.core.NodePath' objects>"
        'has_texture': None, # (!) real value is "<method 'has_texture' of 'panda3d.core.NodePath' objects>"
        'has_texture_off': None, # (!) real value is "<method 'has_texture_off' of 'panda3d.core.NodePath' objects>"
        'has_transparency': None, # (!) real value is "<method 'has_transparency' of 'panda3d.core.NodePath' objects>"
        'has_two_sided': None, # (!) real value is "<method 'has_two_sided' of 'panda3d.core.NodePath' objects>"
        'has_vertex_column': None, # (!) real value is "<method 'has_vertex_column' of 'panda3d.core.NodePath' objects>"
        'headsUp': None, # (!) real value is "<method 'headsUp' of 'panda3d.core.NodePath' objects>"
        'heads_up': None, # (!) real value is "<method 'heads_up' of 'panda3d.core.NodePath' objects>"
        'hide': None, # (!) real value is "<method 'hide' of 'panda3d.core.NodePath' objects>"
        'hideBounds': None, # (!) real value is "<method 'hideBounds' of 'panda3d.core.NodePath' objects>"
        'hide_bounds': None, # (!) real value is "<method 'hide_bounds' of 'panda3d.core.NodePath' objects>"
        'instanceTo': None, # (!) real value is "<method 'instanceTo' of 'panda3d.core.NodePath' objects>"
        'instanceUnderNode': None, # (!) real value is "<method 'instanceUnderNode' of 'panda3d.core.NodePath' objects>"
        'instance_to': None, # (!) real value is "<method 'instance_to' of 'panda3d.core.NodePath' objects>"
        'instance_under_node': None, # (!) real value is "<method 'instance_under_node' of 'panda3d.core.NodePath' objects>"
        'isAncestorOf': None, # (!) real value is "<method 'isAncestorOf' of 'panda3d.core.NodePath' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.core.NodePath' objects>"
        'isHidden': None, # (!) real value is "<method 'isHidden' of 'panda3d.core.NodePath' objects>"
        'isSameGraph': None, # (!) real value is "<method 'isSameGraph' of 'panda3d.core.NodePath' objects>"
        'isSingleton': None, # (!) real value is "<method 'isSingleton' of 'panda3d.core.NodePath' objects>"
        'isStashed': None, # (!) real value is "<method 'isStashed' of 'panda3d.core.NodePath' objects>"
        'is_ancestor_of': None, # (!) real value is "<method 'is_ancestor_of' of 'panda3d.core.NodePath' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.core.NodePath' objects>"
        'is_hidden': None, # (!) real value is "<method 'is_hidden' of 'panda3d.core.NodePath' objects>"
        'is_same_graph': None, # (!) real value is "<method 'is_same_graph' of 'panda3d.core.NodePath' objects>"
        'is_singleton': None, # (!) real value is "<method 'is_singleton' of 'panda3d.core.NodePath' objects>"
        'is_stashed': None, # (!) real value is "<method 'is_stashed' of 'panda3d.core.NodePath' objects>"
        'listTags': None, # (!) real value is "<method 'listTags' of 'panda3d.core.NodePath' objects>"
        'list_tags': None, # (!) real value is "<method 'list_tags' of 'panda3d.core.NodePath' objects>"
        'lookAt': None, # (!) real value is "<method 'lookAt' of 'panda3d.core.NodePath' objects>"
        'look_at': None, # (!) real value is "<method 'look_at' of 'panda3d.core.NodePath' objects>"
        'ls': None, # (!) real value is "<method 'ls' of 'panda3d.core.NodePath' objects>"
        'name': None, # (!) real value is "<attribute 'name' of 'panda3d.core.NodePath' objects>"
        'net_tags': None, # (!) real value is "<attribute 'net_tags' of 'panda3d.core.NodePath' objects>"
        'node': None, # (!) real value is "<method 'node' of 'panda3d.core.NodePath' objects>"
        'nodes': None, # (!) real value is "<attribute 'nodes' of 'panda3d.core.NodePath' objects>"
        'notFound': None, # (!) real value is '<staticmethod(<built-in method notFound of type object at 0x00007FFCFE293A70>)>'
        'not_found': None, # (!) real value is '<staticmethod(<built-in method not_found of type object at 0x00007FFCFE293A70>)>'
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.NodePath' objects>"
        'parent': None, # (!) real value is "<attribute 'parent' of 'panda3d.core.NodePath' objects>"
        'premungeScene': None, # (!) real value is "<method 'premungeScene' of 'panda3d.core.NodePath' objects>"
        'premunge_scene': None, # (!) real value is "<method 'premunge_scene' of 'panda3d.core.NodePath' objects>"
        'prepareScene': None, # (!) real value is "<method 'prepareScene' of 'panda3d.core.NodePath' objects>"
        'prepare_scene': None, # (!) real value is "<method 'prepare_scene' of 'panda3d.core.NodePath' objects>"
        'projectTexture': None, # (!) real value is "<method 'projectTexture' of 'panda3d.core.NodePath' objects>"
        'project_texture': None, # (!) real value is "<method 'project_texture' of 'panda3d.core.NodePath' objects>"
        'python_tags': None, # (!) real value is "<attribute 'python_tags' of 'panda3d.core.NodePath' objects>"
        'removeNode': None, # (!) real value is "<method 'removeNode' of 'panda3d.core.NodePath' objects>"
        'remove_node': None, # (!) real value is "<method 'remove_node' of 'panda3d.core.NodePath' objects>"
        'removed': None, # (!) real value is '<staticmethod(<built-in method removed of type object at 0x00007FFCFE293A70>)>'
        'reparentTo': None, # (!) real value is "<method 'reparentTo' of 'panda3d.core.NodePath' objects>"
        'reparent_to': None, # (!) real value is "<method 'reparent_to' of 'panda3d.core.NodePath' objects>"
        'replaceMaterial': None, # (!) real value is "<method 'replaceMaterial' of 'panda3d.core.NodePath' objects>"
        'replaceTexture': None, # (!) real value is "<method 'replaceTexture' of 'panda3d.core.NodePath' objects>"
        'replace_material': None, # (!) real value is "<method 'replace_material' of 'panda3d.core.NodePath' objects>"
        'replace_texture': None, # (!) real value is "<method 'replace_texture' of 'panda3d.core.NodePath' objects>"
        'reverseLs': None, # (!) real value is "<method 'reverseLs' of 'panda3d.core.NodePath' objects>"
        'reverse_ls': None, # (!) real value is "<method 'reverse_ls' of 'panda3d.core.NodePath' objects>"
        'setAllColorScale': None, # (!) real value is "<method 'setAllColorScale' of 'panda3d.core.NodePath' objects>"
        'setAlphaScale': None, # (!) real value is "<method 'setAlphaScale' of 'panda3d.core.NodePath' objects>"
        'setAntialias': None, # (!) real value is "<method 'setAntialias' of 'panda3d.core.NodePath' objects>"
        'setAttrib': None, # (!) real value is "<method 'setAttrib' of 'panda3d.core.NodePath' objects>"
        'setAudioVolume': None, # (!) real value is "<method 'setAudioVolume' of 'panda3d.core.NodePath' objects>"
        'setAudioVolumeOff': None, # (!) real value is "<method 'setAudioVolumeOff' of 'panda3d.core.NodePath' objects>"
        'setBillboardAxis': None, # (!) real value is "<method 'setBillboardAxis' of 'panda3d.core.NodePath' objects>"
        'setBillboardPointEye': None, # (!) real value is "<method 'setBillboardPointEye' of 'panda3d.core.NodePath' objects>"
        'setBillboardPointWorld': None, # (!) real value is "<method 'setBillboardPointWorld' of 'panda3d.core.NodePath' objects>"
        'setBin': None, # (!) real value is "<method 'setBin' of 'panda3d.core.NodePath' objects>"
        'setClipPlane': None, # (!) real value is "<method 'setClipPlane' of 'panda3d.core.NodePath' objects>"
        'setClipPlaneOff': None, # (!) real value is "<method 'setClipPlaneOff' of 'panda3d.core.NodePath' objects>"
        'setCollideMask': None, # (!) real value is "<method 'setCollideMask' of 'panda3d.core.NodePath' objects>"
        'setColor': None, # (!) real value is "<method 'setColor' of 'panda3d.core.NodePath' objects>"
        'setColorOff': None, # (!) real value is "<method 'setColorOff' of 'panda3d.core.NodePath' objects>"
        'setColorScale': None, # (!) real value is "<method 'setColorScale' of 'panda3d.core.NodePath' objects>"
        'setColorScaleOff': None, # (!) real value is "<method 'setColorScaleOff' of 'panda3d.core.NodePath' objects>"
        'setCompass': None, # (!) real value is "<method 'setCompass' of 'panda3d.core.NodePath' objects>"
        'setDepthOffset': None, # (!) real value is "<method 'setDepthOffset' of 'panda3d.core.NodePath' objects>"
        'setDepthTest': None, # (!) real value is "<method 'setDepthTest' of 'panda3d.core.NodePath' objects>"
        'setDepthWrite': None, # (!) real value is "<method 'setDepthWrite' of 'panda3d.core.NodePath' objects>"
        'setEffect': None, # (!) real value is "<method 'setEffect' of 'panda3d.core.NodePath' objects>"
        'setEffects': None, # (!) real value is "<method 'setEffects' of 'panda3d.core.NodePath' objects>"
        'setFluidPos': None, # (!) real value is "<method 'setFluidPos' of 'panda3d.core.NodePath' objects>"
        'setFluidX': None, # (!) real value is "<method 'setFluidX' of 'panda3d.core.NodePath' objects>"
        'setFluidY': None, # (!) real value is "<method 'setFluidY' of 'panda3d.core.NodePath' objects>"
        'setFluidZ': None, # (!) real value is "<method 'setFluidZ' of 'panda3d.core.NodePath' objects>"
        'setFog': None, # (!) real value is "<method 'setFog' of 'panda3d.core.NodePath' objects>"
        'setFogOff': None, # (!) real value is "<method 'setFogOff' of 'panda3d.core.NodePath' objects>"
        'setH': None, # (!) real value is "<method 'setH' of 'panda3d.core.NodePath' objects>"
        'setHpr': None, # (!) real value is "<method 'setHpr' of 'panda3d.core.NodePath' objects>"
        'setHprScale': None, # (!) real value is "<method 'setHprScale' of 'panda3d.core.NodePath' objects>"
        'setInstanceCount': None, # (!) real value is "<method 'setInstanceCount' of 'panda3d.core.NodePath' objects>"
        'setLight': None, # (!) real value is "<method 'setLight' of 'panda3d.core.NodePath' objects>"
        'setLightOff': None, # (!) real value is "<method 'setLightOff' of 'panda3d.core.NodePath' objects>"
        'setLogicOp': None, # (!) real value is "<method 'setLogicOp' of 'panda3d.core.NodePath' objects>"
        'setMat': None, # (!) real value is "<method 'setMat' of 'panda3d.core.NodePath' objects>"
        'setMaterial': None, # (!) real value is "<method 'setMaterial' of 'panda3d.core.NodePath' objects>"
        'setMaterialOff': None, # (!) real value is "<method 'setMaterialOff' of 'panda3d.core.NodePath' objects>"
        'setMaxSearchDepth': None, # (!) real value is '<staticmethod(<built-in method setMaxSearchDepth of type object at 0x00007FFCFE293A70>)>'
        'setName': None, # (!) real value is "<method 'setName' of 'panda3d.core.NodePath' objects>"
        'setOccluder': None, # (!) real value is "<method 'setOccluder' of 'panda3d.core.NodePath' objects>"
        'setP': None, # (!) real value is "<method 'setP' of 'panda3d.core.NodePath' objects>"
        'setPos': None, # (!) real value is "<method 'setPos' of 'panda3d.core.NodePath' objects>"
        'setPosHpr': None, # (!) real value is "<method 'setPosHpr' of 'panda3d.core.NodePath' objects>"
        'setPosHprScale': None, # (!) real value is "<method 'setPosHprScale' of 'panda3d.core.NodePath' objects>"
        'setPosHprScaleShear': None, # (!) real value is "<method 'setPosHprScaleShear' of 'panda3d.core.NodePath' objects>"
        'setPosQuat': None, # (!) real value is "<method 'setPosQuat' of 'panda3d.core.NodePath' objects>"
        'setPosQuatScale': None, # (!) real value is "<method 'setPosQuatScale' of 'panda3d.core.NodePath' objects>"
        'setPosQuatScaleShear': None, # (!) real value is "<method 'setPosQuatScaleShear' of 'panda3d.core.NodePath' objects>"
        'setPrevTransform': None, # (!) real value is "<method 'setPrevTransform' of 'panda3d.core.NodePath' objects>"
        'setPythonTag': None, # (!) real value is "<method 'setPythonTag' of 'panda3d.core.NodePath' objects>"
        'setQuat': None, # (!) real value is "<method 'setQuat' of 'panda3d.core.NodePath' objects>"
        'setQuatScale': None, # (!) real value is "<method 'setQuatScale' of 'panda3d.core.NodePath' objects>"
        'setR': None, # (!) real value is "<method 'setR' of 'panda3d.core.NodePath' objects>"
        'setRenderMode': None, # (!) real value is "<method 'setRenderMode' of 'panda3d.core.NodePath' objects>"
        'setRenderModeFilled': None, # (!) real value is "<method 'setRenderModeFilled' of 'panda3d.core.NodePath' objects>"
        'setRenderModeFilledWireframe': None, # (!) real value is "<method 'setRenderModeFilledWireframe' of 'panda3d.core.NodePath' objects>"
        'setRenderModePerspective': None, # (!) real value is "<method 'setRenderModePerspective' of 'panda3d.core.NodePath' objects>"
        'setRenderModeThickness': None, # (!) real value is "<method 'setRenderModeThickness' of 'panda3d.core.NodePath' objects>"
        'setRenderModeWireframe': None, # (!) real value is "<method 'setRenderModeWireframe' of 'panda3d.core.NodePath' objects>"
        'setSa': None, # (!) real value is "<method 'setSa' of 'panda3d.core.NodePath' objects>"
        'setSb': None, # (!) real value is "<method 'setSb' of 'panda3d.core.NodePath' objects>"
        'setScale': None, # (!) real value is "<method 'setScale' of 'panda3d.core.NodePath' objects>"
        'setScissor': None, # (!) real value is "<method 'setScissor' of 'panda3d.core.NodePath' objects>"
        'setSg': None, # (!) real value is "<method 'setSg' of 'panda3d.core.NodePath' objects>"
        'setShader': None, # (!) real value is "<method 'setShader' of 'panda3d.core.NodePath' objects>"
        'setShaderAuto': None, # (!) real value is "<method 'setShaderAuto' of 'panda3d.core.NodePath' objects>"
        'setShaderInput': None, # (!) real value is "<method 'setShaderInput' of 'panda3d.core.NodePath' objects>"
        'setShaderInputs': None, # (!) real value is "<method 'setShaderInputs' of 'panda3d.core.NodePath' objects>"
        'setShaderOff': None, # (!) real value is "<method 'setShaderOff' of 'panda3d.core.NodePath' objects>"
        'setShear': None, # (!) real value is "<method 'setShear' of 'panda3d.core.NodePath' objects>"
        'setShxy': None, # (!) real value is "<method 'setShxy' of 'panda3d.core.NodePath' objects>"
        'setShxz': None, # (!) real value is "<method 'setShxz' of 'panda3d.core.NodePath' objects>"
        'setShyz': None, # (!) real value is "<method 'setShyz' of 'panda3d.core.NodePath' objects>"
        'setSr': None, # (!) real value is "<method 'setSr' of 'panda3d.core.NodePath' objects>"
        'setState': None, # (!) real value is "<method 'setState' of 'panda3d.core.NodePath' objects>"
        'setSx': None, # (!) real value is "<method 'setSx' of 'panda3d.core.NodePath' objects>"
        'setSy': None, # (!) real value is "<method 'setSy' of 'panda3d.core.NodePath' objects>"
        'setSz': None, # (!) real value is "<method 'setSz' of 'panda3d.core.NodePath' objects>"
        'setTag': None, # (!) real value is "<method 'setTag' of 'panda3d.core.NodePath' objects>"
        'setTexGen': None, # (!) real value is "<method 'setTexGen' of 'panda3d.core.NodePath' objects>"
        'setTexHpr': None, # (!) real value is "<method 'setTexHpr' of 'panda3d.core.NodePath' objects>"
        'setTexOffset': None, # (!) real value is "<method 'setTexOffset' of 'panda3d.core.NodePath' objects>"
        'setTexPos': None, # (!) real value is "<method 'setTexPos' of 'panda3d.core.NodePath' objects>"
        'setTexProjector': None, # (!) real value is "<method 'setTexProjector' of 'panda3d.core.NodePath' objects>"
        'setTexRotate': None, # (!) real value is "<method 'setTexRotate' of 'panda3d.core.NodePath' objects>"
        'setTexScale': None, # (!) real value is "<method 'setTexScale' of 'panda3d.core.NodePath' objects>"
        'setTexTransform': None, # (!) real value is "<method 'setTexTransform' of 'panda3d.core.NodePath' objects>"
        'setTexture': None, # (!) real value is "<method 'setTexture' of 'panda3d.core.NodePath' objects>"
        'setTextureOff': None, # (!) real value is "<method 'setTextureOff' of 'panda3d.core.NodePath' objects>"
        'setTransform': None, # (!) real value is "<method 'setTransform' of 'panda3d.core.NodePath' objects>"
        'setTransparency': None, # (!) real value is "<method 'setTransparency' of 'panda3d.core.NodePath' objects>"
        'setTwoSided': None, # (!) real value is "<method 'setTwoSided' of 'panda3d.core.NodePath' objects>"
        'setX': None, # (!) real value is "<method 'setX' of 'panda3d.core.NodePath' objects>"
        'setY': None, # (!) real value is "<method 'setY' of 'panda3d.core.NodePath' objects>"
        'setZ': None, # (!) real value is "<method 'setZ' of 'panda3d.core.NodePath' objects>"
        'set_all_color_scale': None, # (!) real value is "<method 'set_all_color_scale' of 'panda3d.core.NodePath' objects>"
        'set_alpha_scale': None, # (!) real value is "<method 'set_alpha_scale' of 'panda3d.core.NodePath' objects>"
        'set_antialias': None, # (!) real value is "<method 'set_antialias' of 'panda3d.core.NodePath' objects>"
        'set_attrib': None, # (!) real value is "<method 'set_attrib' of 'panda3d.core.NodePath' objects>"
        'set_audio_volume': None, # (!) real value is "<method 'set_audio_volume' of 'panda3d.core.NodePath' objects>"
        'set_audio_volume_off': None, # (!) real value is "<method 'set_audio_volume_off' of 'panda3d.core.NodePath' objects>"
        'set_billboard_axis': None, # (!) real value is "<method 'set_billboard_axis' of 'panda3d.core.NodePath' objects>"
        'set_billboard_point_eye': None, # (!) real value is "<method 'set_billboard_point_eye' of 'panda3d.core.NodePath' objects>"
        'set_billboard_point_world': None, # (!) real value is "<method 'set_billboard_point_world' of 'panda3d.core.NodePath' objects>"
        'set_bin': None, # (!) real value is "<method 'set_bin' of 'panda3d.core.NodePath' objects>"
        'set_clip_plane': None, # (!) real value is "<method 'set_clip_plane' of 'panda3d.core.NodePath' objects>"
        'set_clip_plane_off': None, # (!) real value is "<method 'set_clip_plane_off' of 'panda3d.core.NodePath' objects>"
        'set_collide_mask': None, # (!) real value is "<method 'set_collide_mask' of 'panda3d.core.NodePath' objects>"
        'set_color': None, # (!) real value is "<method 'set_color' of 'panda3d.core.NodePath' objects>"
        'set_color_off': None, # (!) real value is "<method 'set_color_off' of 'panda3d.core.NodePath' objects>"
        'set_color_scale': None, # (!) real value is "<method 'set_color_scale' of 'panda3d.core.NodePath' objects>"
        'set_color_scale_off': None, # (!) real value is "<method 'set_color_scale_off' of 'panda3d.core.NodePath' objects>"
        'set_compass': None, # (!) real value is "<method 'set_compass' of 'panda3d.core.NodePath' objects>"
        'set_depth_offset': None, # (!) real value is "<method 'set_depth_offset' of 'panda3d.core.NodePath' objects>"
        'set_depth_test': None, # (!) real value is "<method 'set_depth_test' of 'panda3d.core.NodePath' objects>"
        'set_depth_write': None, # (!) real value is "<method 'set_depth_write' of 'panda3d.core.NodePath' objects>"
        'set_effect': None, # (!) real value is "<method 'set_effect' of 'panda3d.core.NodePath' objects>"
        'set_effects': None, # (!) real value is "<method 'set_effects' of 'panda3d.core.NodePath' objects>"
        'set_fluid_pos': None, # (!) real value is "<method 'set_fluid_pos' of 'panda3d.core.NodePath' objects>"
        'set_fluid_x': None, # (!) real value is "<method 'set_fluid_x' of 'panda3d.core.NodePath' objects>"
        'set_fluid_y': None, # (!) real value is "<method 'set_fluid_y' of 'panda3d.core.NodePath' objects>"
        'set_fluid_z': None, # (!) real value is "<method 'set_fluid_z' of 'panda3d.core.NodePath' objects>"
        'set_fog': None, # (!) real value is "<method 'set_fog' of 'panda3d.core.NodePath' objects>"
        'set_fog_off': None, # (!) real value is "<method 'set_fog_off' of 'panda3d.core.NodePath' objects>"
        'set_h': None, # (!) real value is "<method 'set_h' of 'panda3d.core.NodePath' objects>"
        'set_hpr': None, # (!) real value is "<method 'set_hpr' of 'panda3d.core.NodePath' objects>"
        'set_hpr_scale': None, # (!) real value is "<method 'set_hpr_scale' of 'panda3d.core.NodePath' objects>"
        'set_instance_count': None, # (!) real value is "<method 'set_instance_count' of 'panda3d.core.NodePath' objects>"
        'set_light': None, # (!) real value is "<method 'set_light' of 'panda3d.core.NodePath' objects>"
        'set_light_off': None, # (!) real value is "<method 'set_light_off' of 'panda3d.core.NodePath' objects>"
        'set_logic_op': None, # (!) real value is "<method 'set_logic_op' of 'panda3d.core.NodePath' objects>"
        'set_mat': None, # (!) real value is "<method 'set_mat' of 'panda3d.core.NodePath' objects>"
        'set_material': None, # (!) real value is "<method 'set_material' of 'panda3d.core.NodePath' objects>"
        'set_material_off': None, # (!) real value is "<method 'set_material_off' of 'panda3d.core.NodePath' objects>"
        'set_max_search_depth': None, # (!) real value is '<staticmethod(<built-in method set_max_search_depth of type object at 0x00007FFCFE293A70>)>'
        'set_name': None, # (!) real value is "<method 'set_name' of 'panda3d.core.NodePath' objects>"
        'set_occluder': None, # (!) real value is "<method 'set_occluder' of 'panda3d.core.NodePath' objects>"
        'set_p': None, # (!) real value is "<method 'set_p' of 'panda3d.core.NodePath' objects>"
        'set_pos': None, # (!) real value is "<method 'set_pos' of 'panda3d.core.NodePath' objects>"
        'set_pos_hpr': None, # (!) real value is "<method 'set_pos_hpr' of 'panda3d.core.NodePath' objects>"
        'set_pos_hpr_scale': None, # (!) real value is "<method 'set_pos_hpr_scale' of 'panda3d.core.NodePath' objects>"
        'set_pos_hpr_scale_shear': None, # (!) real value is "<method 'set_pos_hpr_scale_shear' of 'panda3d.core.NodePath' objects>"
        'set_pos_quat': None, # (!) real value is "<method 'set_pos_quat' of 'panda3d.core.NodePath' objects>"
        'set_pos_quat_scale': None, # (!) real value is "<method 'set_pos_quat_scale' of 'panda3d.core.NodePath' objects>"
        'set_pos_quat_scale_shear': None, # (!) real value is "<method 'set_pos_quat_scale_shear' of 'panda3d.core.NodePath' objects>"
        'set_prev_transform': None, # (!) real value is "<method 'set_prev_transform' of 'panda3d.core.NodePath' objects>"
        'set_python_tag': None, # (!) real value is "<method 'set_python_tag' of 'panda3d.core.NodePath' objects>"
        'set_quat': None, # (!) real value is "<method 'set_quat' of 'panda3d.core.NodePath' objects>"
        'set_quat_scale': None, # (!) real value is "<method 'set_quat_scale' of 'panda3d.core.NodePath' objects>"
        'set_r': None, # (!) real value is "<method 'set_r' of 'panda3d.core.NodePath' objects>"
        'set_render_mode': None, # (!) real value is "<method 'set_render_mode' of 'panda3d.core.NodePath' objects>"
        'set_render_mode_filled': None, # (!) real value is "<method 'set_render_mode_filled' of 'panda3d.core.NodePath' objects>"
        'set_render_mode_filled_wireframe': None, # (!) real value is "<method 'set_render_mode_filled_wireframe' of 'panda3d.core.NodePath' objects>"
        'set_render_mode_perspective': None, # (!) real value is "<method 'set_render_mode_perspective' of 'panda3d.core.NodePath' objects>"
        'set_render_mode_thickness': None, # (!) real value is "<method 'set_render_mode_thickness' of 'panda3d.core.NodePath' objects>"
        'set_render_mode_wireframe': None, # (!) real value is "<method 'set_render_mode_wireframe' of 'panda3d.core.NodePath' objects>"
        'set_sa': None, # (!) real value is "<method 'set_sa' of 'panda3d.core.NodePath' objects>"
        'set_sb': None, # (!) real value is "<method 'set_sb' of 'panda3d.core.NodePath' objects>"
        'set_scale': None, # (!) real value is "<method 'set_scale' of 'panda3d.core.NodePath' objects>"
        'set_scissor': None, # (!) real value is "<method 'set_scissor' of 'panda3d.core.NodePath' objects>"
        'set_sg': None, # (!) real value is "<method 'set_sg' of 'panda3d.core.NodePath' objects>"
        'set_shader': None, # (!) real value is "<method 'set_shader' of 'panda3d.core.NodePath' objects>"
        'set_shader_auto': None, # (!) real value is "<method 'set_shader_auto' of 'panda3d.core.NodePath' objects>"
        'set_shader_input': None, # (!) real value is "<method 'set_shader_input' of 'panda3d.core.NodePath' objects>"
        'set_shader_inputs': None, # (!) real value is "<method 'set_shader_inputs' of 'panda3d.core.NodePath' objects>"
        'set_shader_off': None, # (!) real value is "<method 'set_shader_off' of 'panda3d.core.NodePath' objects>"
        'set_shear': None, # (!) real value is "<method 'set_shear' of 'panda3d.core.NodePath' objects>"
        'set_shxy': None, # (!) real value is "<method 'set_shxy' of 'panda3d.core.NodePath' objects>"
        'set_shxz': None, # (!) real value is "<method 'set_shxz' of 'panda3d.core.NodePath' objects>"
        'set_shyz': None, # (!) real value is "<method 'set_shyz' of 'panda3d.core.NodePath' objects>"
        'set_sr': None, # (!) real value is "<method 'set_sr' of 'panda3d.core.NodePath' objects>"
        'set_state': None, # (!) real value is "<method 'set_state' of 'panda3d.core.NodePath' objects>"
        'set_sx': None, # (!) real value is "<method 'set_sx' of 'panda3d.core.NodePath' objects>"
        'set_sy': None, # (!) real value is "<method 'set_sy' of 'panda3d.core.NodePath' objects>"
        'set_sz': None, # (!) real value is "<method 'set_sz' of 'panda3d.core.NodePath' objects>"
        'set_tag': None, # (!) real value is "<method 'set_tag' of 'panda3d.core.NodePath' objects>"
        'set_tex_gen': None, # (!) real value is "<method 'set_tex_gen' of 'panda3d.core.NodePath' objects>"
        'set_tex_hpr': None, # (!) real value is "<method 'set_tex_hpr' of 'panda3d.core.NodePath' objects>"
        'set_tex_offset': None, # (!) real value is "<method 'set_tex_offset' of 'panda3d.core.NodePath' objects>"
        'set_tex_pos': None, # (!) real value is "<method 'set_tex_pos' of 'panda3d.core.NodePath' objects>"
        'set_tex_projector': None, # (!) real value is "<method 'set_tex_projector' of 'panda3d.core.NodePath' objects>"
        'set_tex_rotate': None, # (!) real value is "<method 'set_tex_rotate' of 'panda3d.core.NodePath' objects>"
        'set_tex_scale': None, # (!) real value is "<method 'set_tex_scale' of 'panda3d.core.NodePath' objects>"
        'set_tex_transform': None, # (!) real value is "<method 'set_tex_transform' of 'panda3d.core.NodePath' objects>"
        'set_texture': None, # (!) real value is "<method 'set_texture' of 'panda3d.core.NodePath' objects>"
        'set_texture_off': None, # (!) real value is "<method 'set_texture_off' of 'panda3d.core.NodePath' objects>"
        'set_transform': None, # (!) real value is "<method 'set_transform' of 'panda3d.core.NodePath' objects>"
        'set_transparency': None, # (!) real value is "<method 'set_transparency' of 'panda3d.core.NodePath' objects>"
        'set_two_sided': None, # (!) real value is "<method 'set_two_sided' of 'panda3d.core.NodePath' objects>"
        'set_x': None, # (!) real value is "<method 'set_x' of 'panda3d.core.NodePath' objects>"
        'set_y': None, # (!) real value is "<method 'set_y' of 'panda3d.core.NodePath' objects>"
        'set_z': None, # (!) real value is "<method 'set_z' of 'panda3d.core.NodePath' objects>"
        'show': None, # (!) real value is "<method 'show' of 'panda3d.core.NodePath' objects>"
        'showBounds': None, # (!) real value is "<method 'showBounds' of 'panda3d.core.NodePath' objects>"
        'showThrough': None, # (!) real value is "<method 'showThrough' of 'panda3d.core.NodePath' objects>"
        'showTightBounds': None, # (!) real value is "<method 'showTightBounds' of 'panda3d.core.NodePath' objects>"
        'show_bounds': None, # (!) real value is "<method 'show_bounds' of 'panda3d.core.NodePath' objects>"
        'show_through': None, # (!) real value is "<method 'show_through' of 'panda3d.core.NodePath' objects>"
        'show_tight_bounds': None, # (!) real value is "<method 'show_tight_bounds' of 'panda3d.core.NodePath' objects>"
        'sort': None, # (!) real value is "<attribute 'sort' of 'panda3d.core.NodePath' objects>"
        'stash': None, # (!) real value is "<method 'stash' of 'panda3d.core.NodePath' objects>"
        'stashTo': None, # (!) real value is "<method 'stashTo' of 'panda3d.core.NodePath' objects>"
        'stash_to': None, # (!) real value is "<method 'stash_to' of 'panda3d.core.NodePath' objects>"
        'stashed_children': None, # (!) real value is "<attribute 'stashed_children' of 'panda3d.core.NodePath' objects>"
        'tags': None, # (!) real value is "<attribute 'tags' of 'panda3d.core.NodePath' objects>"
        'unifyTextureStages': None, # (!) real value is "<method 'unifyTextureStages' of 'panda3d.core.NodePath' objects>"
        'unify_texture_stages': None, # (!) real value is "<method 'unify_texture_stages' of 'panda3d.core.NodePath' objects>"
        'unstash': None, # (!) real value is "<method 'unstash' of 'panda3d.core.NodePath' objects>"
        'unstashAll': None, # (!) real value is "<method 'unstashAll' of 'panda3d.core.NodePath' objects>"
        'unstash_all': None, # (!) real value is "<method 'unstash_all' of 'panda3d.core.NodePath' objects>"
        'verifyComplete': None, # (!) real value is "<method 'verifyComplete' of 'panda3d.core.NodePath' objects>"
        'verify_complete': None, # (!) real value is "<method 'verify_complete' of 'panda3d.core.NodePath' objects>"
        'writeBamFile': None, # (!) real value is "<method 'writeBamFile' of 'panda3d.core.NodePath' objects>"
        'writeBamStream': None, # (!) real value is "<method 'writeBamStream' of 'panda3d.core.NodePath' objects>"
        'writeBounds': None, # (!) real value is "<method 'writeBounds' of 'panda3d.core.NodePath' objects>"
        'write_bam_file': None, # (!) real value is "<method 'write_bam_file' of 'panda3d.core.NodePath' objects>"
        'write_bam_stream': None, # (!) real value is "<method 'write_bam_stream' of 'panda3d.core.NodePath' objects>"
        'write_bounds': None, # (!) real value is "<method 'write_bounds' of 'panda3d.core.NodePath' objects>"
        'wrtReparentTo': None, # (!) real value is "<method 'wrtReparentTo' of 'panda3d.core.NodePath' objects>"
        'wrt_reparent_to': None, # (!) real value is "<method 'wrt_reparent_to' of 'panda3d.core.NodePath' objects>"
    }
    ETFail = 3
    ETNotFound = 1
    ETOk = 0
    ETRemoved = 2
    ET_fail = 3
    ET_not_found = 1
    ET_ok = 0
    ET_removed = 2


