# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggGroupNode import EggGroupNode

from .EggRenderMode import EggRenderMode

from .EggTransform import EggTransform

class EggGroup(EggGroupNode, EggRenderMode, EggTransform):
    """
    /**
     * The main glue of the egg hierarchy, this corresponds to the <Group>,
     * <Instance>, and <Joint> type nodes.
     */
    """
    def addGroupRef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_group_ref(const EggGroup self, EggGroup group)
        
        /**
         * Adds a new <Ref> entry to the group.  This declares an internal reference
         * to another node, and is used to implement scene-graph instancing; it is
         * only valid if the group_type is GT_instance.
         */
        """
        pass

    def addObjectType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_object_type(const EggGroup self, str object_type)
        
        /**
         *
         */
        """
        pass

    def add_group_ref(self, const_EggGroup_self, EggGroup_group): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_group_ref(const EggGroup self, EggGroup group)
        
        /**
         * Adds a new <Ref> entry to the group.  This declares an internal reference
         * to another node, and is used to implement scene-graph instancing; it is
         * only valid if the group_type is GT_instance.
         */
        """
        pass

    def add_object_type(self, const_EggGroup_self, str_object_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_object_type(const EggGroup self, str object_type)
        
        /**
         *
         */
        """
        pass

    def assign(self, const_EggGroup_self, const_EggGroup_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggGroup self, const EggGroup copy)
        
        /**
         *
         */
        """
        pass

    def clearBillboardCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_billboard_center(const EggGroup self)
        
        /**
         *
         */
        """
        pass

    def clearBlendColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_blend_color(const EggGroup self)
        
        /**
         * Removes the blend color specification.
         */
        """
        pass

    def clearCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_collide_mask(const EggGroup self)
        
        /**
         *
         */
        """
        pass

    def clearCollisionName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_collision_name(const EggGroup self)
        
        /**
         *
         */
        """
        pass

    def clearDefaultPose(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_default_pose(const EggGroup self)
        
        /**
         * Removes the initial pose transform.  See set_default_pose().
         */
        """
        pass

    def clearFromCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_from_collide_mask(const EggGroup self)
        
        /**
         *
         */
        """
        pass

    def clearGroupRefs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_group_refs(const EggGroup self)
        
        /**
         * Removes all of the <Ref> entries within this group.  See add_group_ref().
         */
        """
        pass

    def clearIndexedFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_indexed_flag(const EggGroup self)
        
        /**
         *
         */
        """
        pass

    def clearIntoCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_into_collide_mask(const EggGroup self)
        
        /**
         *
         */
        """
        pass

    def clearLod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_lod(const EggGroup self)
        
        /**
         *
         */
        """
        pass

    def clearObjectTypes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_object_types(const EggGroup self)
        
        /**
         *
         */
        """
        pass

    def clearTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_tag(const EggGroup self, str key)
        
        /**
         * Removes the value defined for this key on this particular node.  After a
         * call to clear_tag(), has_tag() will return false for the indicated key.
         */
        """
        pass

    def clear_billboard_center(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_billboard_center(const EggGroup self)
        
        /**
         *
         */
        """
        pass

    def clear_blend_color(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_blend_color(const EggGroup self)
        
        /**
         * Removes the blend color specification.
         */
        """
        pass

    def clear_collide_mask(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_collide_mask(const EggGroup self)
        
        /**
         *
         */
        """
        pass

    def clear_collision_name(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_collision_name(const EggGroup self)
        
        /**
         *
         */
        """
        pass

    def clear_default_pose(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_default_pose(const EggGroup self)
        
        /**
         * Removes the initial pose transform.  See set_default_pose().
         */
        """
        pass

    def clear_from_collide_mask(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_from_collide_mask(const EggGroup self)
        
        /**
         *
         */
        """
        pass

    def clear_group_refs(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_group_refs(const EggGroup self)
        
        /**
         * Removes all of the <Ref> entries within this group.  See add_group_ref().
         */
        """
        pass

    def clear_indexed_flag(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_indexed_flag(const EggGroup self)
        
        /**
         *
         */
        """
        pass

    def clear_into_collide_mask(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_into_collide_mask(const EggGroup self)
        
        /**
         *
         */
        """
        pass

    def clear_lod(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_lod(const EggGroup self)
        
        /**
         *
         */
        """
        pass

    def clear_object_types(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_object_types(const EggGroup self)
        
        /**
         *
         */
        """
        pass

    def clear_tag(self, const_EggGroup_self, str_key): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_tag(const EggGroup self, str key)
        
        /**
         * Removes the value defined for this key on this particular node.  After a
         * call to clear_tag(), has_tag() will return false for the indicated key.
         */
        """
        pass

    def determineAlphaMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_alpha_mode(const EggGroup self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this group that has an alpha_mode
         * other than AM_unspecified.  Returns a valid EggRenderMode pointer if one is
         * found, or NULL otherwise.
         */
        """
        pass

    def determineBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_bin(const EggGroup self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this group that has a bin
         * specified.  Returns a valid EggRenderMode pointer if one is found, or NULL
         * otherwise.
         */
        """
        pass

    def determineDecal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_decal(const EggGroup self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup at this level or above
         * that has the "decal" flag set.  Returns the value of the decal flag if it
         * is found, or false if it is not.
         *
         * In other words, returns true if the "decal" flag is in effect for the
         * indicated node, false otherwise.
         */
        """
        pass

    def determineDepthOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_depth_offset(const EggGroup self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this group that has a depth_offset
         * specified.  Returns a valid EggRenderMode pointer if one is found, or NULL
         * otherwise.
         */
        """
        pass

    def determineDepthTestMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_depth_test_mode(const EggGroup self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this group that has a
         * depth_test_mode other than DTM_unspecified.  Returns a valid EggRenderMode
         * pointer if one is found, or NULL otherwise.
         */
        """
        pass

    def determineDepthWriteMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_depth_write_mode(const EggGroup self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this group that has a
         * depth_write_mode other than DWM_unspecified.  Returns a valid EggRenderMode
         * pointer if one is found, or NULL otherwise.
         */
        """
        pass

    def determineDrawOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_draw_order(const EggGroup self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this group that has a draw_order
         * specified.  Returns a valid EggRenderMode pointer if one is found, or NULL
         * otherwise.
         */
        """
        pass

    def determineIndexed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_indexed(const EggGroup self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup at this level or above
         * that has the "indexed" scalar set.  Returns the value of the indexed scalar
         * if it is found, or false if it is not.
         *
         * In other words, returns true if the "indexed" flag is in effect for the
         * indicated node, false otherwise.
         */
        """
        pass

    def determineVisibilityMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_visibility_mode(const EggGroup self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this group that has a
         * visibility_mode other than VM_unspecified.  Returns a valid EggRenderMode
         * pointer if one is found, or NULL otherwise.
         */
        """
        pass

    def determine_alpha_mode(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_alpha_mode(const EggGroup self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this group that has an alpha_mode
         * other than AM_unspecified.  Returns a valid EggRenderMode pointer if one is
         * found, or NULL otherwise.
         */
        """
        pass

    def determine_bin(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_bin(const EggGroup self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this group that has a bin
         * specified.  Returns a valid EggRenderMode pointer if one is found, or NULL
         * otherwise.
         */
        """
        pass

    def determine_decal(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_decal(const EggGroup self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup at this level or above
         * that has the "decal" flag set.  Returns the value of the decal flag if it
         * is found, or false if it is not.
         *
         * In other words, returns true if the "decal" flag is in effect for the
         * indicated node, false otherwise.
         */
        """
        pass

    def determine_depth_offset(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_depth_offset(const EggGroup self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this group that has a depth_offset
         * specified.  Returns a valid EggRenderMode pointer if one is found, or NULL
         * otherwise.
         */
        """
        pass

    def determine_depth_test_mode(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_depth_test_mode(const EggGroup self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this group that has a
         * depth_test_mode other than DTM_unspecified.  Returns a valid EggRenderMode
         * pointer if one is found, or NULL otherwise.
         */
        """
        pass

    def determine_depth_write_mode(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_depth_write_mode(const EggGroup self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this group that has a
         * depth_write_mode other than DWM_unspecified.  Returns a valid EggRenderMode
         * pointer if one is found, or NULL otherwise.
         */
        """
        pass

    def determine_draw_order(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_draw_order(const EggGroup self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this group that has a draw_order
         * specified.  Returns a valid EggRenderMode pointer if one is found, or NULL
         * otherwise.
         */
        """
        pass

    def determine_indexed(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_indexed(const EggGroup self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup at this level or above
         * that has the "indexed" scalar set.  Returns the value of the indexed scalar
         * if it is found, or false if it is not.
         *
         * In other words, returns true if the "indexed" flag is in effect for the
         * indicated node, false otherwise.
         */
        """
        pass

    def determine_visibility_mode(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_visibility_mode(const EggGroup self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this group that has a
         * visibility_mode other than VM_unspecified.  Returns a valid EggRenderMode
         * pointer if one is found, or NULL otherwise.
         */
        """
        pass

    def getBillboardCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_billboard_center(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getBillboardType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_billboard_type(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getBlendColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_blend_color(EggGroup self)
        
        /**
         * Returns the blend color if one has been specified, or (0, 0, 0, 0) if one
         * has not.
         */
        """
        pass

    def getBlendMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_blend_mode(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getBlendOperandA(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_blend_operand_a(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getBlendOperandB(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_blend_operand_b(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCollideFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collide_flags(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collide_mask(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getCollisionName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collision_name(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getCsType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cs_type(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getDartType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_dart_type(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getDcsType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_dcs_type(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getDecalFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_decal_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getDefaultPose(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_pose(EggGroup self)
        
        /**
         * Returns a read-only accessor to the initial pose transform.  This is the
         * <DefaultPose> entry for a Joint, and defines only the initial transform
         * pose for the unanimated joint; it has nothing to do with the group's
         * <Transform> entry, which defines the (eventual) space of the group's
         * vertices.
         */
        """
        pass

    def getDirectFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_direct_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getFromCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_from_collide_mask(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getGroupRef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_group_ref(EggGroup self, int n)
        
        /**
         * Returns the nth <Ref> entry within this group.  See add_group_ref().
         */
        """
        pass

    def getGroupRefs(self, *args, **kwargs): # real signature unknown
        pass

    def getGroupType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_group_type(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getIndexedFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_indexed_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getIntoCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_into_collide_mask(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getLod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lod(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getModelFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_model_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getNofogFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_nofog_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getNumGroupRefs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_group_refs(EggGroup self)
        
        /**
         * Returns the number of <Ref> entries within this group.  See
         * add_group_ref().
         */
        """
        pass

    def getNumObjectTypes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_object_types(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getObjectType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_object_type(EggGroup self, int index)
        
        /**
         *
         */
        """
        pass

    def getObjectTypes(self, *args, **kwargs): # real signature unknown
        pass

    def getOccluderFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_occluder_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getPolylightFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_polylight_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getPortalFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_portal_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getScrollR(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scroll_r(EggGroup self)
        """
        pass

    def getScrollU(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scroll_u(EggGroup self)
        """
        pass

    def getScrollV(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scroll_v(EggGroup self)
        """
        pass

    def getScrollW(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scroll_w(EggGroup self)
        """
        pass

    def getSwitchFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_switch_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getSwitchFps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_switch_fps(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tag(EggGroup self, str key)
        
        /**
         * Retrieves the user-defined value that was previously set on this node for
         * the particular key, if any.  If no value has been previously set, returns
         * the empty string.
         */
        """
        pass

    def getTexlistFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texlist_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def getVertexMembership(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex_membership(EggGroup self, const EggVertex vert)
        
        /**
         * Returns the amount of membership of the indicated vertex in this group.  If
         * the vertex is not reffed by the group, returns 0.
         */
        """
        pass

    def get_billboard_center(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_billboard_center(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_billboard_type(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_billboard_type(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_blend_color(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_blend_color(EggGroup self)
        
        /**
         * Returns the blend color if one has been specified, or (0, 0, 0, 0) if one
         * has not.
         */
        """
        pass

    def get_blend_mode(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_blend_mode(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_blend_operand_a(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_blend_operand_a(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_blend_operand_b(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_blend_operand_b(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_collide_flags(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collide_flags(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_collide_mask(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collide_mask(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_collision_name(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collision_name(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_cs_type(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cs_type(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_dart_type(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_dart_type(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_dcs_type(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_dcs_type(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_decal_flag(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_decal_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_default_pose(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_pose(EggGroup self)
        
        /**
         * Returns a read-only accessor to the initial pose transform.  This is the
         * <DefaultPose> entry for a Joint, and defines only the initial transform
         * pose for the unanimated joint; it has nothing to do with the group's
         * <Transform> entry, which defines the (eventual) space of the group's
         * vertices.
         */
        """
        pass

    def get_direct_flag(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_direct_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_from_collide_mask(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_from_collide_mask(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_group_ref(self, EggGroup_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_group_ref(EggGroup self, int n)
        
        /**
         * Returns the nth <Ref> entry within this group.  See add_group_ref().
         */
        """
        pass

    def get_group_refs(self, *args, **kwargs): # real signature unknown
        pass

    def get_group_type(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_group_type(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_indexed_flag(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_indexed_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_into_collide_mask(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_into_collide_mask(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_lod(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lod(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_model_flag(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_model_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_nofog_flag(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_nofog_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_num_group_refs(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_group_refs(EggGroup self)
        
        /**
         * Returns the number of <Ref> entries within this group.  See
         * add_group_ref().
         */
        """
        pass

    def get_num_object_types(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_object_types(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_object_type(self, EggGroup_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_object_type(EggGroup self, int index)
        
        /**
         *
         */
        """
        pass

    def get_object_types(self, *args, **kwargs): # real signature unknown
        pass

    def get_occluder_flag(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_occluder_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_polylight_flag(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_polylight_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_portal_flag(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_portal_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_scroll_r(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scroll_r(EggGroup self)
        """
        pass

    def get_scroll_u(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scroll_u(EggGroup self)
        """
        pass

    def get_scroll_v(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scroll_v(EggGroup self)
        """
        pass

    def get_scroll_w(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scroll_w(EggGroup self)
        """
        pass

    def get_switch_flag(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_switch_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_switch_fps(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_switch_fps(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_tag(self, EggGroup_self, str_key): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tag(EggGroup self, str key)
        
        /**
         * Retrieves the user-defined value that was previously set on this node for
         * the particular key, if any.  If no value has been previously set, returns
         * the empty string.
         */
        """
        pass

    def get_texlist_flag(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texlist_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def get_vertex_membership(self, EggGroup_self, const_EggVertex_vert): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex_membership(EggGroup self, const EggVertex vert)
        
        /**
         * Returns the amount of membership of the indicated vertex in this group.  If
         * the vertex is not reffed by the group, returns 0.
         */
        """
        pass

    def hasBillboardCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_billboard_center(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def hasBlendColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_blend_color(EggGroup self)
        
        /**
         * Returns true if the blend color has been specified, false otherwise.
         */
        """
        pass

    def hasCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_collide_mask(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def hasCollisionName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_collision_name(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def hasDcsType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_dcs_type(EggGroup self)
        
        /**
         * Returns true if the specified DCS type is not DC_none and not
         * DC_unspecified.
         */
        """
        pass

    def hasFromCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_from_collide_mask(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def hasIndexedFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_indexed_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def hasIntoCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_into_collide_mask(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def hasLod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_lod(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def hasObjectType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_object_type(EggGroup self, str object_type)
        
        /**
         * Returns true if the indicated object type has been added to the group, or
         * false otherwise.
         */
        """
        pass

    def hasScrollingUvs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_scrolling_uvs(const EggGroup self)
        """
        pass

    def hasTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_tag(EggGroup self, str key)
        
        /**
         * Returns true if a value has been defined on this node for the particular
         * key (even if that value is the empty string), or false if no value has been
         * set.
         */
        """
        pass

    def has_billboard_center(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_billboard_center(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def has_blend_color(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_blend_color(EggGroup self)
        
        /**
         * Returns true if the blend color has been specified, false otherwise.
         */
        """
        pass

    def has_collide_mask(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_collide_mask(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def has_collision_name(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_collision_name(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def has_dcs_type(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_dcs_type(EggGroup self)
        
        /**
         * Returns true if the specified DCS type is not DC_none and not
         * DC_unspecified.
         */
        """
        pass

    def has_from_collide_mask(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_from_collide_mask(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def has_indexed_flag(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_indexed_flag(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def has_into_collide_mask(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_into_collide_mask(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def has_lod(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_lod(EggGroup self)
        
        /**
         *
         */
        """
        pass

    def has_object_type(self, EggGroup_self, str_object_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_object_type(EggGroup self, str object_type)
        
        /**
         * Returns true if the indicated object type has been added to the group, or
         * false otherwise.
         */
        """
        pass

    def has_scrolling_uvs(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_scrolling_uvs(const EggGroup self)
        """
        pass

    def has_tag(self, EggGroup_self, str_key): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_tag(EggGroup self, str key)
        
        /**
         * Returns true if a value has been defined on this node for the particular
         * key (even if that value is the empty string), or false if no value has been
         * set.
         */
        """
        pass

    def isInstanceType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_instance_type(EggGroup self)
        
        /**
         * Returns true if this group is an instance type node; i.e.  it begins the
         * root of a local coordinate space.  This is not related to instancing
         * (multiple copies of a node in a scene graph).
         *
         * This also includes the case of the node including a billboard flag without
         * an explicit center, which implicitly makes the node behave like an
         * instance.
         */
        """
        pass

    def isJoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_joint(EggGroup self)
        
        /**
         * Returns true if this particular node represents a <Joint> entry or not.
         * This is a handy thing to know since Joints are sorted to the end of their
         * sibling list when writing an egg file.  See EggGroupNode::write().
         */
        """
        pass

    def is_instance_type(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_instance_type(EggGroup self)
        
        /**
         * Returns true if this group is an instance type node; i.e.  it begins the
         * root of a local coordinate space.  This is not related to instancing
         * (multiple copies of a node in a scene graph).
         *
         * This also includes the case of the node including a billboard flag without
         * an explicit center, which implicitly makes the node behave like an
         * instance.
         */
        """
        pass

    def is_joint(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_joint(EggGroup self)
        
        /**
         * Returns true if this particular node represents a <Joint> entry or not.
         * This is a handy thing to know since Joints are sorted to the end of their
         * sibling list when writing an egg file.  See EggGroupNode::write().
         */
        """
        pass

    def modifyDefaultPose(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_default_pose(const EggGroup self)
        
        /**
         * Returns a writable accessor to the initial pose transform.  This is the
         * <DefaultPose> entry for a Joint, and defines only the initial transform
         * pose for the unanimated joint; it has nothing to do with the group's
         * <Transform> entry, which defines the (eventual) space of the group's
         * vertices.
         */
        """
        pass

    def modify_default_pose(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_default_pose(const EggGroup self)
        
        /**
         * Returns a writable accessor to the initial pose transform.  This is the
         * <DefaultPose> entry for a Joint, and defines only the initial transform
         * pose for the unanimated joint; it has nothing to do with the group's
         * <Transform> entry, which defines the (eventual) space of the group's
         * vertices.
         */
        """
        pass

    def refVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        ref_vertex(const EggGroup self, EggVertex vert, double membership)
        
        /**
         * Adds the vertex to the set of those referenced by the group, at the
         * indicated membership level.  If the vertex is already being referenced,
         * increases the membership amount by the indicated amount.
         */
        """
        pass

    def ref_vertex(self, const_EggGroup_self, EggVertex_vert, double_membership): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ref_vertex(const EggGroup self, EggVertex vert, double membership)
        
        /**
         * Adds the vertex to the set of those referenced by the group, at the
         * indicated membership level.  If the vertex is already being referenced,
         * increases the membership amount by the indicated amount.
         */
        """
        pass

    def removeGroupRef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_group_ref(const EggGroup self, int n)
        
        /**
         * Removes the nth <Ref> entry within this group.  See add_group_ref().
         */
        """
        pass

    def removeObjectType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_object_type(const EggGroup self, str object_type)
        
        /**
         * Removes the first instance of the indicated object type from the group if
         * it is present.  Returns true if the object type was found and removed,
         * false otherwise.
         */
        """
        pass

    def remove_group_ref(self, const_EggGroup_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_group_ref(const EggGroup self, int n)
        
        /**
         * Removes the nth <Ref> entry within this group.  See add_group_ref().
         */
        """
        pass

    def remove_object_type(self, const_EggGroup_self, str_object_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_object_type(const EggGroup self, str object_type)
        
        /**
         * Removes the first instance of the indicated object type from the group if
         * it is present.  Returns true if the object type was found and removed,
         * false otherwise.
         */
        """
        pass

    def setBillboardCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_billboard_center(const EggGroup self, const LPoint3d billboard_center)
        
        /**
         * Sets the point around which the billboard will rotate, if this node
         * contains a billboard specification.
         *
         * If a billboard type is given but no billboard_center is specified, then the
         * group node is treated as an <Instance>, and the billboard rotates around
         * the origin.  If, however, a billboard_center is specified, then the group
         * node is *not* treated as an <Instance>, and the billboard rotates around
         * the specified point.
         *
         * The point is in the same coordinate system as the vertices of this node:
         * usually global, but possibly local if there is an <Instance> somewhere
         * above.  Specifically, this is the coordinate system defined by
         * get_vertex_frame().
         */
        """
        pass

    def setBillboardType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_billboard_type(const EggGroup self, int type)
        
        /**
         *
         */
        """
        pass

    def setBlendColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_blend_color(const EggGroup self, const LVecBase4f blend_color)
        
        /**
         *
         */
        """
        pass

    def setBlendMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_blend_mode(const EggGroup self, int blend_mode)
        
        /**
         *
         */
        """
        pass

    def setBlendOperandA(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_blend_operand_a(const EggGroup self, int blend_operand_a)
        
        /**
         *
         */
        """
        pass

    def setBlendOperandB(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_blend_operand_b(const EggGroup self, int blend_operand_b)
        
        /**
         *
         */
        """
        pass

    def setCollideFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_collide_flags(const EggGroup self, int flags)
        
        /**
         *
         */
        """
        pass

    def setCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_collide_mask(const EggGroup self, BitMask mask)
        
        /**
         *
         */
        """
        pass

    def setCollisionName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_collision_name(const EggGroup self, str collision_name)
        
        /**
         *
         */
        """
        pass

    def setCsType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cs_type(const EggGroup self, int type)
        
        /**
         *
         */
        """
        pass

    def setDartType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_dart_type(const EggGroup self, int type)
        
        /**
         *
         */
        """
        pass

    def setDcsType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_dcs_type(const EggGroup self, int type)
        
        /**
         *
         */
        """
        pass

    def setDecalFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_decal_flag(const EggGroup self, bool flag)
        
        /**
         *
         */
        """
        pass

    def setDefaultPose(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_default_pose(const EggGroup self, const EggTransform transform)
        
        /**
         * Replaces the initial pose transform.  This is the <DefaultPose> entry for a
         * Joint, and defines only the initial transform pose for the unanimated
         * joint; it has nothing to do with the group's <Transform> entry, which
         * defines the (eventual) space of the group's vertices.
         */
        """
        pass

    def setDirectFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_direct_flag(const EggGroup self, bool flag)
        
        /**
         *
         */
        """
        pass

    def setFromCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_from_collide_mask(const EggGroup self, BitMask mask)
        
        /**
         *
         */
        """
        pass

    def setGroupType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_group_type(const EggGroup self, int type)
        
        /**
         *
         */
        """
        pass

    def setIndexedFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_indexed_flag(const EggGroup self, bool flag)
        
        /**
         * If this flag is true, geometry at this node and below will be generated as
         * indexed geometry.
         */
        """
        pass

    def setIntoCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_into_collide_mask(const EggGroup self, BitMask mask)
        
        /**
         *
         */
        """
        pass

    def setLod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_lod(const EggGroup self, const EggSwitchCondition lod)
        
        /**
         *
         */
        """
        pass

    def setModelFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_model_flag(const EggGroup self, bool flag)
        
        /**
         *
         */
        """
        pass

    def setNofogFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_nofog_flag(const EggGroup self, bool flag)
        
        /**
         *
         */
        """
        pass

    def setOccluderFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_occluder_flag(const EggGroup self, bool flag)
        
        /**
         *
         */
        """
        pass

    def setPolylightFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_polylight_flag(const EggGroup self, bool flag)
        
        /**
         *
         */
        """
        pass

    def setPortalFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_portal_flag(const EggGroup self, bool flag)
        
        /**
         *
         */
        """
        pass

    def setScrollR(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scroll_r(const EggGroup self, double r_speed)
        """
        pass

    def setScrollU(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scroll_u(const EggGroup self, double u_speed)
        """
        pass

    def setScrollV(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scroll_v(const EggGroup self, double v_speed)
        """
        pass

    def setScrollW(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scroll_w(const EggGroup self, double w_speed)
        """
        pass

    def setSwitchFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_switch_flag(const EggGroup self, bool flag)
        
        /**
         *
         */
        """
        pass

    def setSwitchFps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_switch_fps(const EggGroup self, double fps)
        
        /**
         *
         */
        """
        pass

    def setTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tag(const EggGroup self, str key, str value)
        
        /**
         * Associates a user-defined value with a user-defined key which is stored on
         * the node.  This value has no meaning to Panda; but it is stored
         * indefinitely on the node until it is requested again.  This value will be
         * copied to the PandaNode that is created for this particular EggGroup if the
         * egg file is loaded as a scene.
         *
         * Each unique key stores a different string value.  There is no effective
         * limit on the number of different keys that may be stored or on the length
         * of any one key's value.
         */
        """
        pass

    def setTexlistFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_texlist_flag(const EggGroup self, bool flag)
        
        /**
         *
         */
        """
        pass

    def setVertexMembership(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vertex_membership(const EggGroup self, EggVertex vert, double membership)
        
        /**
         * Explicitly sets the net membership of the indicated vertex in this group to
         * the given value.
         */
        """
        pass

    def set_billboard_center(self, const_EggGroup_self, const_LPoint3d_billboard_center): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_billboard_center(const EggGroup self, const LPoint3d billboard_center)
        
        /**
         * Sets the point around which the billboard will rotate, if this node
         * contains a billboard specification.
         *
         * If a billboard type is given but no billboard_center is specified, then the
         * group node is treated as an <Instance>, and the billboard rotates around
         * the origin.  If, however, a billboard_center is specified, then the group
         * node is *not* treated as an <Instance>, and the billboard rotates around
         * the specified point.
         *
         * The point is in the same coordinate system as the vertices of this node:
         * usually global, but possibly local if there is an <Instance> somewhere
         * above.  Specifically, this is the coordinate system defined by
         * get_vertex_frame().
         */
        """
        pass

    def set_billboard_type(self, const_EggGroup_self, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_billboard_type(const EggGroup self, int type)
        
        /**
         *
         */
        """
        pass

    def set_blend_color(self, const_EggGroup_self, const_LVecBase4f_blend_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_blend_color(const EggGroup self, const LVecBase4f blend_color)
        
        /**
         *
         */
        """
        pass

    def set_blend_mode(self, const_EggGroup_self, int_blend_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_blend_mode(const EggGroup self, int blend_mode)
        
        /**
         *
         */
        """
        pass

    def set_blend_operand_a(self, const_EggGroup_self, int_blend_operand_a): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_blend_operand_a(const EggGroup self, int blend_operand_a)
        
        /**
         *
         */
        """
        pass

    def set_blend_operand_b(self, const_EggGroup_self, int_blend_operand_b): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_blend_operand_b(const EggGroup self, int blend_operand_b)
        
        /**
         *
         */
        """
        pass

    def set_collide_flags(self, const_EggGroup_self, int_flags): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_collide_flags(const EggGroup self, int flags)
        
        /**
         *
         */
        """
        pass

    def set_collide_mask(self, const_EggGroup_self, BitMask_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_collide_mask(const EggGroup self, BitMask mask)
        
        /**
         *
         */
        """
        pass

    def set_collision_name(self, const_EggGroup_self, str_collision_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_collision_name(const EggGroup self, str collision_name)
        
        /**
         *
         */
        """
        pass

    def set_cs_type(self, const_EggGroup_self, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cs_type(const EggGroup self, int type)
        
        /**
         *
         */
        """
        pass

    def set_dart_type(self, const_EggGroup_self, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_dart_type(const EggGroup self, int type)
        
        /**
         *
         */
        """
        pass

    def set_dcs_type(self, const_EggGroup_self, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_dcs_type(const EggGroup self, int type)
        
        /**
         *
         */
        """
        pass

    def set_decal_flag(self, const_EggGroup_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_decal_flag(const EggGroup self, bool flag)
        
        /**
         *
         */
        """
        pass

    def set_default_pose(self, const_EggGroup_self, const_EggTransform_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_default_pose(const EggGroup self, const EggTransform transform)
        
        /**
         * Replaces the initial pose transform.  This is the <DefaultPose> entry for a
         * Joint, and defines only the initial transform pose for the unanimated
         * joint; it has nothing to do with the group's <Transform> entry, which
         * defines the (eventual) space of the group's vertices.
         */
        """
        pass

    def set_direct_flag(self, const_EggGroup_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_direct_flag(const EggGroup self, bool flag)
        
        /**
         *
         */
        """
        pass

    def set_from_collide_mask(self, const_EggGroup_self, BitMask_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_from_collide_mask(const EggGroup self, BitMask mask)
        
        /**
         *
         */
        """
        pass

    def set_group_type(self, const_EggGroup_self, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_group_type(const EggGroup self, int type)
        
        /**
         *
         */
        """
        pass

    def set_indexed_flag(self, const_EggGroup_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_indexed_flag(const EggGroup self, bool flag)
        
        /**
         * If this flag is true, geometry at this node and below will be generated as
         * indexed geometry.
         */
        """
        pass

    def set_into_collide_mask(self, const_EggGroup_self, BitMask_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_into_collide_mask(const EggGroup self, BitMask mask)
        
        /**
         *
         */
        """
        pass

    def set_lod(self, const_EggGroup_self, const_EggSwitchCondition_lod): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_lod(const EggGroup self, const EggSwitchCondition lod)
        
        /**
         *
         */
        """
        pass

    def set_model_flag(self, const_EggGroup_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_model_flag(const EggGroup self, bool flag)
        
        /**
         *
         */
        """
        pass

    def set_nofog_flag(self, const_EggGroup_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_nofog_flag(const EggGroup self, bool flag)
        
        /**
         *
         */
        """
        pass

    def set_occluder_flag(self, const_EggGroup_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_occluder_flag(const EggGroup self, bool flag)
        
        /**
         *
         */
        """
        pass

    def set_polylight_flag(self, const_EggGroup_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_polylight_flag(const EggGroup self, bool flag)
        
        /**
         *
         */
        """
        pass

    def set_portal_flag(self, const_EggGroup_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_portal_flag(const EggGroup self, bool flag)
        
        /**
         *
         */
        """
        pass

    def set_scroll_r(self, const_EggGroup_self, double_r_speed): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scroll_r(const EggGroup self, double r_speed)
        """
        pass

    def set_scroll_u(self, const_EggGroup_self, double_u_speed): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scroll_u(const EggGroup self, double u_speed)
        """
        pass

    def set_scroll_v(self, const_EggGroup_self, double_v_speed): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scroll_v(const EggGroup self, double v_speed)
        """
        pass

    def set_scroll_w(self, const_EggGroup_self, double_w_speed): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scroll_w(const EggGroup self, double w_speed)
        """
        pass

    def set_switch_flag(self, const_EggGroup_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_switch_flag(const EggGroup self, bool flag)
        
        /**
         *
         */
        """
        pass

    def set_switch_fps(self, const_EggGroup_self, double_fps): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_switch_fps(const EggGroup self, double fps)
        
        /**
         *
         */
        """
        pass

    def set_tag(self, const_EggGroup_self, str_key, str_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tag(const EggGroup self, str key, str value)
        
        /**
         * Associates a user-defined value with a user-defined key which is stored on
         * the node.  This value has no meaning to Panda; but it is stored
         * indefinitely on the node until it is requested again.  This value will be
         * copied to the PandaNode that is created for this particular EggGroup if the
         * egg file is loaded as a scene.
         *
         * Each unique key stores a different string value.  There is no effective
         * limit on the number of different keys that may be stored or on the length
         * of any one key's value.
         */
        """
        pass

    def set_texlist_flag(self, const_EggGroup_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_texlist_flag(const EggGroup self, bool flag)
        
        /**
         *
         */
        """
        pass

    def set_vertex_membership(self, const_EggGroup_self, EggVertex_vert, double_membership): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vertex_membership(const EggGroup self, EggVertex vert, double membership)
        
        /**
         * Explicitly sets the net membership of the indicated vertex in this group to
         * the given value.
         */
        """
        pass

    def stealVrefs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        steal_vrefs(const EggGroup self, EggGroup other)
        
        /**
         * Moves all of the vertex references from the indicated other group into this
         * one.  If a given vertex was previously shared by both groups, the relative
         * memberships will be summed.
         */
        """
        pass

    def steal_vrefs(self, const_EggGroup_self, EggGroup_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        steal_vrefs(const EggGroup self, EggGroup other)
        
        /**
         * Moves all of the vertex references from the indicated other group into this
         * one.  If a given vertex was previously shared by both groups, the relative
         * memberships will be summed.
         */
        """
        pass

    def stringBillboardType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_billboard_type(str strval)
        
        /**
         * Returns the BillboardType value associated with the given string
         * representation, or BT_none if the string does not match any known
         * BillboardType value.
         */
        """
        pass

    def stringBlendMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_blend_mode(str strval)
        
        /**
         * Returns the BlendMode value associated with the given string
         * representation, or BM_none if the string does not match any known
         * BlendMode.
         */
        """
        pass

    def stringBlendOperand(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_blend_operand(str strval)
        
        /**
         * Returns the BlendOperand value associated with the given string
         * representation, or BO_none if the string does not match any known
         * BlendOperand.
         */
        """
        pass

    def stringCollideFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_collide_flags(str strval)
        
        /**
         * Returns the CollideFlags value associated with the given string
         * representation, or CF_none if the string does not match any known
         * CollideFlags value.  This only recognizes a single keyword; it does not
         * attempt to parse a string of keywords.
         */
        """
        pass

    def stringCsType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_cs_type(str strval)
        
        /**
         * Returns the CollisionSolidType value associated with the given string
         * representation, or CST_none if the string does not match any known
         * CollisionSolidType value.
         */
        """
        pass

    def stringDartType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_dart_type(str strval)
        
        /**
         * Returns the DartType value associated with the given string representation,
         * or DT_none if the string does not match any known DartType value.
         */
        """
        pass

    def stringDcsType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_dcs_type(str strval)
        
        /**
         * Returns the DCSType value associated with the given string representation,
         * or DC_unspecified if the string does not match any known DCSType value.
         */
        """
        pass

    def stringGroupType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_group_type(str strval)
        
        /**
         * Returns the GroupType value associated with the given string
         * representation, or GT_invalid if the string does not match any known
         * GroupType value.
         */
        """
        pass

    def string_billboard_type(self, str_strval): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_billboard_type(str strval)
        
        /**
         * Returns the BillboardType value associated with the given string
         * representation, or BT_none if the string does not match any known
         * BillboardType value.
         */
        """
        pass

    def string_blend_mode(self, str_strval): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_blend_mode(str strval)
        
        /**
         * Returns the BlendMode value associated with the given string
         * representation, or BM_none if the string does not match any known
         * BlendMode.
         */
        """
        pass

    def string_blend_operand(self, str_strval): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_blend_operand(str strval)
        
        /**
         * Returns the BlendOperand value associated with the given string
         * representation, or BO_none if the string does not match any known
         * BlendOperand.
         */
        """
        pass

    def string_collide_flags(self, str_strval): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_collide_flags(str strval)
        
        /**
         * Returns the CollideFlags value associated with the given string
         * representation, or CF_none if the string does not match any known
         * CollideFlags value.  This only recognizes a single keyword; it does not
         * attempt to parse a string of keywords.
         */
        """
        pass

    def string_cs_type(self, str_strval): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_cs_type(str strval)
        
        /**
         * Returns the CollisionSolidType value associated with the given string
         * representation, or CST_none if the string does not match any known
         * CollisionSolidType value.
         */
        """
        pass

    def string_dart_type(self, str_strval): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_dart_type(str strval)
        
        /**
         * Returns the DartType value associated with the given string representation,
         * or DT_none if the string does not match any known DartType value.
         */
        """
        pass

    def string_dcs_type(self, str_strval): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_dcs_type(str strval)
        
        /**
         * Returns the DCSType value associated with the given string representation,
         * or DC_unspecified if the string does not match any known DCSType value.
         */
        """
        pass

    def string_group_type(self, str_strval): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_group_type(str strval)
        
        /**
         * Returns the GroupType value associated with the given string
         * representation, or GT_invalid if the string does not match any known
         * GroupType value.
         */
        """
        pass

    def testVrefIntegrity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        test_vref_integrity(EggGroup self)
        """
        pass

    def test_vref_integrity(self, EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        test_vref_integrity(EggGroup self)
        """
        pass

    def unrefAllVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unref_all_vertices(const EggGroup self)
        
        /**
         * Removes all vertices from the reference list.
         */
        """
        pass

    def unrefVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unref_vertex(const EggGroup self, EggVertex vert)
        
        /**
         * Removes the vertex from the set of those referenced by the group.  Does
         * nothing if the vertex is not already reffed.
         */
        """
        pass

    def unref_all_vertices(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unref_all_vertices(const EggGroup self)
        
        /**
         * Removes all vertices from the reference list.
         */
        """
        pass

    def unref_vertex(self, const_EggGroup_self, EggVertex_vert): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unref_vertex(const EggGroup self, EggVertex vert)
        
        /**
         * Removes the vertex from the set of those referenced by the group.  Does
         * nothing if the vertex is not already reffed.
         */
        """
        pass

    def upcastToEggGroupNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_EggGroupNode(const EggGroup self)
        
        upcast from EggGroup to EggGroupNode
        """
        pass

    def upcastToEggRenderMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_EggRenderMode(const EggGroup self)
        
        upcast from EggGroup to EggRenderMode
        """
        pass

    def upcastToEggTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_EggTransform(const EggGroup self)
        
        upcast from EggGroup to EggTransform
        """
        pass

    def upcast_to_EggGroupNode(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_EggGroupNode(const EggGroup self)
        
        upcast from EggGroup to EggGroupNode
        """
        pass

    def upcast_to_EggRenderMode(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_EggRenderMode(const EggGroup self)
        
        upcast from EggGroup to EggRenderMode
        """
        pass

    def upcast_to_EggTransform(self, const_EggGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_EggTransform(const EggGroup self)
        
        upcast from EggGroup to EggTransform
        """
        pass

    def write(self, EggGroup_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(EggGroup self, ostream out, int indent_level)
        
        /**
         * Writes the group and all of its children to the indicated output stream in
         * Egg format.
         */
        """
        pass

    def writeBillboardFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_billboard_flags(EggGroup self, ostream out, int indent_level)
        
        /**
         * Writes just the <Billboard> entry and related fields to the indicated
         * ostream.
         */
        """
        pass

    def writeCollideFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_collide_flags(EggGroup self, ostream out, int indent_level)
        
        /**
         * Writes just the <Collide> entry and related fields to the indicated
         * ostream.
         */
        """
        pass

    def writeDecalFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_decal_flags(EggGroup self, ostream out, int indent_level)
        
        /**
         * Writes the flags related to decaling, if any.
         */
        """
        pass

    def writeModelFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_model_flags(EggGroup self, ostream out, int indent_level)
        
        /**
         * Writes the <Model> flag and related flags to the indicated ostream.
         */
        """
        pass

    def writeObjectTypes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_object_types(EggGroup self, ostream out, int indent_level)
        
        /**
         * Writes just the <ObjectTypes> entries, if any, to the indicated ostream.
         */
        """
        pass

    def writeRenderMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_render_mode(EggGroup self, ostream out, int indent_level)
        
        /**
         * Writes the flags inherited from EggRenderMode and similar flags that
         * control obscure render effects.
         */
        """
        pass

    def writeSwitchFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_switch_flags(EggGroup self, ostream out, int indent_level)
        
        /**
         * Writes the <Switch> flag and related flags to the indicated ostream.
         */
        """
        pass

    def writeTags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_tags(EggGroup self, ostream out, int indent_level)
        
        /**
         * Writes just the <Tag> entries, if any, to the indicated ostream.
         */
        """
        pass

    def write_billboard_flags(self, EggGroup_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_billboard_flags(EggGroup self, ostream out, int indent_level)
        
        /**
         * Writes just the <Billboard> entry and related fields to the indicated
         * ostream.
         */
        """
        pass

    def write_collide_flags(self, EggGroup_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_collide_flags(EggGroup self, ostream out, int indent_level)
        
        /**
         * Writes just the <Collide> entry and related fields to the indicated
         * ostream.
         */
        """
        pass

    def write_decal_flags(self, EggGroup_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_decal_flags(EggGroup self, ostream out, int indent_level)
        
        /**
         * Writes the flags related to decaling, if any.
         */
        """
        pass

    def write_model_flags(self, EggGroup_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_model_flags(EggGroup self, ostream out, int indent_level)
        
        /**
         * Writes the <Model> flag and related flags to the indicated ostream.
         */
        """
        pass

    def write_object_types(self, EggGroup_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_object_types(EggGroup self, ostream out, int indent_level)
        
        /**
         * Writes just the <ObjectTypes> entries, if any, to the indicated ostream.
         */
        """
        pass

    def write_render_mode(self, EggGroup_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_render_mode(EggGroup self, ostream out, int indent_level)
        
        /**
         * Writes the flags inherited from EggRenderMode and similar flags that
         * control obscure render effects.
         */
        """
        pass

    def write_switch_flags(self, EggGroup_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_switch_flags(EggGroup self, ostream out, int indent_level)
        
        /**
         * Writes the <Switch> flag and related flags to the indicated ostream.
         */
        """
        pass

    def write_tags(self, EggGroup_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_tags(EggGroup self, ostream out, int indent_level)
        
        /**
         * Writes just the <Tag> entries, if any, to the indicated ostream.
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    billboard_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    billboard_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blend_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blend_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blend_operand_a = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blend_operand_b = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collide_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collide_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collision_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cs_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dart_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dcs_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    decal_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    default_pose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    direct_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    from_collide_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    group_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    indexed_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    into_collide_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nofog_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object_types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    occluder_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    portal_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scroll_r = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scroll_u = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scroll_v = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scroll_w = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    switch_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    switch_fps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    texlist_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    BMAdd = 2
    BMInvSubtract = 4
    BMMax = 6
    BMMin = 5
    BMNone = 1
    BMSubtract = 3
    BMUnspecified = 0
    BM_add = 2
    BM_inv_subtract = 4
    BM_max = 6
    BM_min = 5
    BM_none = 1
    BM_subtract = 3
    BM_unspecified = 0
    BOAlphaScale = 18
    BOColorScale = 16
    BOConstantAlpha = 13
    BOConstantColor = 11
    BOFbufferAlpha = 9
    BOFbufferColor = 5
    BOIncomingAlpha = 7
    BOIncomingColor = 3
    BOIncomingColorSaturate = 15
    BOOne = 2
    BOOneMinusAlphaScale = 19
    BOOneMinusColorScale = 17
    BOOneMinusConstantAlpha = 14
    BOOneMinusConstantColor = 12
    BOOneMinusFbufferAlpha = 10
    BOOneMinusFbufferColor = 6
    BOOneMinusIncomingAlpha = 8
    BOOneMinusIncomingColor = 4
    BOUnspecified = 0
    BOZero = 1
    BO_alpha_scale = 18
    BO_color_scale = 16
    BO_constant_alpha = 13
    BO_constant_color = 11
    BO_fbuffer_alpha = 9
    BO_fbuffer_color = 5
    BO_incoming_alpha = 7
    BO_incoming_color = 3
    BO_incoming_color_saturate = 15
    BO_one = 2
    BO_one_minus_alpha_scale = 19
    BO_one_minus_color_scale = 17
    BO_one_minus_constant_alpha = 14
    BO_one_minus_constant_color = 12
    BO_one_minus_fbuffer_alpha = 10
    BO_one_minus_fbuffer_color = 6
    BO_one_minus_incoming_alpha = 8
    BO_one_minus_incoming_color = 4
    BO_unspecified = 0
    BO_zero = 1
    BTAxis = 32
    BTNone = 0
    BTPointCameraRelative = 64
    BTPointWorldRelative = 128
    BT_axis = 32
    BT_none = 0
    BT_point_camera_relative = 64
    BT_point_world_relative = 128
    CFCenter = 16777216
    CFDescend = 1048576
    CFEvent = 2097152
    CFIntangible = 134217728
    CFKeep = 4194304
    CFLevel = 67108864
    CFNone = 0
    CFSolid = 8388608
    CFTurnstile = 33554432
    CF_center = 16777216
    CF_descend = 1048576
    CF_event = 2097152
    CF_intangible = 134217728
    CF_keep = 4194304
    CF_level = 67108864
    CF_none = 0
    CF_solid = 8388608
    CF_turnstile = 33554432
    CSTBox = 458752
    CSTFloorMesh = 524288
    CSTInvSphere = 393216
    CSTNone = 0
    CSTPlane = 65536
    CSTPolygon = 131072
    CSTPolyset = 196608
    CSTSphere = 262144
    CSTTube = 327680
    CST_box = 458752
    CST_floor_mesh = 524288
    CST_inv_sphere = 393216
    CST_none = 0
    CST_plane = 65536
    CST_polygon = 131072
    CST_polyset = 196608
    CST_sphere = 262144
    CST_tube = 327680
    DCDefault = 80
    DCLocal = 32
    DCNet = 48
    DCNone = 16
    DCNoTouch = 64
    DCUnspecified = 0
    DC_default = 80
    DC_local = 32
    DC_net = 48
    DC_none = 16
    DC_no_touch = 64
    DC_unspecified = 0
    DTDefault = 1073741824
    DTNone = 0
    DTNosync = 805306368
    DtoolClassDict = {
        'BMAdd': 2,
        'BMInvSubtract': 4,
        'BMMax': 6,
        'BMMin': 5,
        'BMNone': 1,
        'BMSubtract': 3,
        'BMUnspecified': 0,
        'BM_add': 2,
        'BM_inv_subtract': 4,
        'BM_max': 6,
        'BM_min': 5,
        'BM_none': 1,
        'BM_subtract': 3,
        'BM_unspecified': 0,
        'BOAlphaScale': 18,
        'BOColorScale': 16,
        'BOConstantAlpha': 13,
        'BOConstantColor': 11,
        'BOFbufferAlpha': 9,
        'BOFbufferColor': 5,
        'BOIncomingAlpha': 7,
        'BOIncomingColor': 3,
        'BOIncomingColorSaturate': 15,
        'BOOne': 2,
        'BOOneMinusAlphaScale': 19,
        'BOOneMinusColorScale': 17,
        'BOOneMinusConstantAlpha': 14,
        'BOOneMinusConstantColor': 12,
        'BOOneMinusFbufferAlpha': 10,
        'BOOneMinusFbufferColor': 6,
        'BOOneMinusIncomingAlpha': 8,
        'BOOneMinusIncomingColor': 4,
        'BOUnspecified': 0,
        'BOZero': 1,
        'BO_alpha_scale': 18,
        'BO_color_scale': 16,
        'BO_constant_alpha': 13,
        'BO_constant_color': 11,
        'BO_fbuffer_alpha': 9,
        'BO_fbuffer_color': 5,
        'BO_incoming_alpha': 7,
        'BO_incoming_color': 3,
        'BO_incoming_color_saturate': 15,
        'BO_one': 2,
        'BO_one_minus_alpha_scale': 19,
        'BO_one_minus_color_scale': 17,
        'BO_one_minus_constant_alpha': 14,
        'BO_one_minus_constant_color': 12,
        'BO_one_minus_fbuffer_alpha': 10,
        'BO_one_minus_fbuffer_color': 6,
        'BO_one_minus_incoming_alpha': 8,
        'BO_one_minus_incoming_color': 4,
        'BO_unspecified': 0,
        'BO_zero': 1,
        'BTAxis': 32,
        'BTNone': 0,
        'BTPointCameraRelative': 64,
        'BTPointWorldRelative': 128,
        'BT_axis': 32,
        'BT_none': 0,
        'BT_point_camera_relative': 64,
        'BT_point_world_relative': 128,
        'CFCenter': 16777216,
        'CFDescend': 1048576,
        'CFEvent': 2097152,
        'CFIntangible': 134217728,
        'CFKeep': 4194304,
        'CFLevel': 67108864,
        'CFNone': 0,
        'CFSolid': 8388608,
        'CFTurnstile': 33554432,
        'CF_center': 16777216,
        'CF_descend': 1048576,
        'CF_event': 2097152,
        'CF_intangible': 134217728,
        'CF_keep': 4194304,
        'CF_level': 67108864,
        'CF_none': 0,
        'CF_solid': 8388608,
        'CF_turnstile': 33554432,
        'CSTBox': 458752,
        'CSTFloorMesh': 524288,
        'CSTInvSphere': 393216,
        'CSTNone': 0,
        'CSTPlane': 65536,
        'CSTPolygon': 131072,
        'CSTPolyset': 196608,
        'CSTSphere': 262144,
        'CSTTube': 327680,
        'CST_box': 458752,
        'CST_floor_mesh': 524288,
        'CST_inv_sphere': 393216,
        'CST_none': 0,
        'CST_plane': 65536,
        'CST_polygon': 131072,
        'CST_polyset': 196608,
        'CST_sphere': 262144,
        'CST_tube': 327680,
        'DCDefault': 80,
        'DCLocal': 32,
        'DCNet': 48,
        'DCNoTouch': 64,
        'DCNone': 16,
        'DCUnspecified': 0,
        'DC_default': 80,
        'DC_local': 32,
        'DC_net': 48,
        'DC_no_touch': 64,
        'DC_none': 16,
        'DC_unspecified': 0,
        'DTDefault': 1073741824,
        'DTNone': 0,
        'DTNosync': 805306368,
        'DTStructured': 268435456,
        'DTSync': 536870912,
        'DT_default': 1073741824,
        'DT_none': 0,
        'DT_nosync': 805306368,
        'DT_structured': 268435456,
        'DT_sync': 536870912,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'GTGroup': 0,
        'GTInstance': 1,
        'GTInvalid': -1,
        'GTJoint': 2,
        'GT_group': 0,
        'GT_instance': 1,
        'GT_invalid': -1,
        'GT_joint': 2,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggGroup' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggGroup' objects>"
        '__doc__': '/**\n * The main glue of the egg hierarchy, this corresponds to the <Group>,\n * <Instance>, and <Joint> type nodes.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggGroup' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CE2B0>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.egg.EggGroup' objects>"
        'addGroupRef': None, # (!) real value is "<method 'addGroupRef' of 'panda3d.egg.EggGroup' objects>"
        'addObjectType': None, # (!) real value is "<method 'addObjectType' of 'panda3d.egg.EggGroup' objects>"
        'add_group_ref': None, # (!) real value is "<method 'add_group_ref' of 'panda3d.egg.EggGroup' objects>"
        'add_object_type': None, # (!) real value is "<method 'add_object_type' of 'panda3d.egg.EggGroup' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggGroup' objects>"
        'billboard_center': None, # (!) real value is "<attribute 'billboard_center' of 'panda3d.egg.EggGroup' objects>"
        'billboard_type': None, # (!) real value is "<attribute 'billboard_type' of 'panda3d.egg.EggGroup' objects>"
        'blend_color': None, # (!) real value is "<attribute 'blend_color' of 'panda3d.egg.EggGroup' objects>"
        'blend_mode': None, # (!) real value is "<attribute 'blend_mode' of 'panda3d.egg.EggGroup' objects>"
        'blend_operand_a': None, # (!) real value is "<attribute 'blend_operand_a' of 'panda3d.egg.EggGroup' objects>"
        'blend_operand_b': None, # (!) real value is "<attribute 'blend_operand_b' of 'panda3d.egg.EggGroup' objects>"
        'clearBillboardCenter': None, # (!) real value is "<method 'clearBillboardCenter' of 'panda3d.egg.EggGroup' objects>"
        'clearBlendColor': None, # (!) real value is "<method 'clearBlendColor' of 'panda3d.egg.EggGroup' objects>"
        'clearCollideMask': None, # (!) real value is "<method 'clearCollideMask' of 'panda3d.egg.EggGroup' objects>"
        'clearCollisionName': None, # (!) real value is "<method 'clearCollisionName' of 'panda3d.egg.EggGroup' objects>"
        'clearDefaultPose': None, # (!) real value is "<method 'clearDefaultPose' of 'panda3d.egg.EggGroup' objects>"
        'clearFromCollideMask': None, # (!) real value is "<method 'clearFromCollideMask' of 'panda3d.egg.EggGroup' objects>"
        'clearGroupRefs': None, # (!) real value is "<method 'clearGroupRefs' of 'panda3d.egg.EggGroup' objects>"
        'clearIndexedFlag': None, # (!) real value is "<method 'clearIndexedFlag' of 'panda3d.egg.EggGroup' objects>"
        'clearIntoCollideMask': None, # (!) real value is "<method 'clearIntoCollideMask' of 'panda3d.egg.EggGroup' objects>"
        'clearLod': None, # (!) real value is "<method 'clearLod' of 'panda3d.egg.EggGroup' objects>"
        'clearObjectTypes': None, # (!) real value is "<method 'clearObjectTypes' of 'panda3d.egg.EggGroup' objects>"
        'clearTag': None, # (!) real value is "<method 'clearTag' of 'panda3d.egg.EggGroup' objects>"
        'clear_billboard_center': None, # (!) real value is "<method 'clear_billboard_center' of 'panda3d.egg.EggGroup' objects>"
        'clear_blend_color': None, # (!) real value is "<method 'clear_blend_color' of 'panda3d.egg.EggGroup' objects>"
        'clear_collide_mask': None, # (!) real value is "<method 'clear_collide_mask' of 'panda3d.egg.EggGroup' objects>"
        'clear_collision_name': None, # (!) real value is "<method 'clear_collision_name' of 'panda3d.egg.EggGroup' objects>"
        'clear_default_pose': None, # (!) real value is "<method 'clear_default_pose' of 'panda3d.egg.EggGroup' objects>"
        'clear_from_collide_mask': None, # (!) real value is "<method 'clear_from_collide_mask' of 'panda3d.egg.EggGroup' objects>"
        'clear_group_refs': None, # (!) real value is "<method 'clear_group_refs' of 'panda3d.egg.EggGroup' objects>"
        'clear_indexed_flag': None, # (!) real value is "<method 'clear_indexed_flag' of 'panda3d.egg.EggGroup' objects>"
        'clear_into_collide_mask': None, # (!) real value is "<method 'clear_into_collide_mask' of 'panda3d.egg.EggGroup' objects>"
        'clear_lod': None, # (!) real value is "<method 'clear_lod' of 'panda3d.egg.EggGroup' objects>"
        'clear_object_types': None, # (!) real value is "<method 'clear_object_types' of 'panda3d.egg.EggGroup' objects>"
        'clear_tag': None, # (!) real value is "<method 'clear_tag' of 'panda3d.egg.EggGroup' objects>"
        'collide_flags': None, # (!) real value is "<attribute 'collide_flags' of 'panda3d.egg.EggGroup' objects>"
        'collide_mask': None, # (!) real value is "<attribute 'collide_mask' of 'panda3d.egg.EggGroup' objects>"
        'collision_name': None, # (!) real value is "<attribute 'collision_name' of 'panda3d.egg.EggGroup' objects>"
        'cs_type': None, # (!) real value is "<attribute 'cs_type' of 'panda3d.egg.EggGroup' objects>"
        'dart_type': None, # (!) real value is "<attribute 'dart_type' of 'panda3d.egg.EggGroup' objects>"
        'dcs_type': None, # (!) real value is "<attribute 'dcs_type' of 'panda3d.egg.EggGroup' objects>"
        'decal_flag': None, # (!) real value is "<attribute 'decal_flag' of 'panda3d.egg.EggGroup' objects>"
        'default_pose': None, # (!) real value is "<attribute 'default_pose' of 'panda3d.egg.EggGroup' objects>"
        'determineAlphaMode': None, # (!) real value is "<method 'determineAlphaMode' of 'panda3d.egg.EggGroup' objects>"
        'determineBin': None, # (!) real value is "<method 'determineBin' of 'panda3d.egg.EggGroup' objects>"
        'determineDecal': None, # (!) real value is "<method 'determineDecal' of 'panda3d.egg.EggGroup' objects>"
        'determineDepthOffset': None, # (!) real value is "<method 'determineDepthOffset' of 'panda3d.egg.EggGroup' objects>"
        'determineDepthTestMode': None, # (!) real value is "<method 'determineDepthTestMode' of 'panda3d.egg.EggGroup' objects>"
        'determineDepthWriteMode': None, # (!) real value is "<method 'determineDepthWriteMode' of 'panda3d.egg.EggGroup' objects>"
        'determineDrawOrder': None, # (!) real value is "<method 'determineDrawOrder' of 'panda3d.egg.EggGroup' objects>"
        'determineIndexed': None, # (!) real value is "<method 'determineIndexed' of 'panda3d.egg.EggGroup' objects>"
        'determineVisibilityMode': None, # (!) real value is "<method 'determineVisibilityMode' of 'panda3d.egg.EggGroup' objects>"
        'determine_alpha_mode': None, # (!) real value is "<method 'determine_alpha_mode' of 'panda3d.egg.EggGroup' objects>"
        'determine_bin': None, # (!) real value is "<method 'determine_bin' of 'panda3d.egg.EggGroup' objects>"
        'determine_decal': None, # (!) real value is "<method 'determine_decal' of 'panda3d.egg.EggGroup' objects>"
        'determine_depth_offset': None, # (!) real value is "<method 'determine_depth_offset' of 'panda3d.egg.EggGroup' objects>"
        'determine_depth_test_mode': None, # (!) real value is "<method 'determine_depth_test_mode' of 'panda3d.egg.EggGroup' objects>"
        'determine_depth_write_mode': None, # (!) real value is "<method 'determine_depth_write_mode' of 'panda3d.egg.EggGroup' objects>"
        'determine_draw_order': None, # (!) real value is "<method 'determine_draw_order' of 'panda3d.egg.EggGroup' objects>"
        'determine_indexed': None, # (!) real value is "<method 'determine_indexed' of 'panda3d.egg.EggGroup' objects>"
        'determine_visibility_mode': None, # (!) real value is "<method 'determine_visibility_mode' of 'panda3d.egg.EggGroup' objects>"
        'direct_flag': None, # (!) real value is "<attribute 'direct_flag' of 'panda3d.egg.EggGroup' objects>"
        'from_collide_mask': None, # (!) real value is "<attribute 'from_collide_mask' of 'panda3d.egg.EggGroup' objects>"
        'getBillboardCenter': None, # (!) real value is "<method 'getBillboardCenter' of 'panda3d.egg.EggGroup' objects>"
        'getBillboardType': None, # (!) real value is "<method 'getBillboardType' of 'panda3d.egg.EggGroup' objects>"
        'getBlendColor': None, # (!) real value is "<method 'getBlendColor' of 'panda3d.egg.EggGroup' objects>"
        'getBlendMode': None, # (!) real value is "<method 'getBlendMode' of 'panda3d.egg.EggGroup' objects>"
        'getBlendOperandA': None, # (!) real value is "<method 'getBlendOperandA' of 'panda3d.egg.EggGroup' objects>"
        'getBlendOperandB': None, # (!) real value is "<method 'getBlendOperandB' of 'panda3d.egg.EggGroup' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CE2B0>)>'
        'getCollideFlags': None, # (!) real value is "<method 'getCollideFlags' of 'panda3d.egg.EggGroup' objects>"
        'getCollideMask': None, # (!) real value is "<method 'getCollideMask' of 'panda3d.egg.EggGroup' objects>"
        'getCollisionName': None, # (!) real value is "<method 'getCollisionName' of 'panda3d.egg.EggGroup' objects>"
        'getCsType': None, # (!) real value is "<method 'getCsType' of 'panda3d.egg.EggGroup' objects>"
        'getDartType': None, # (!) real value is "<method 'getDartType' of 'panda3d.egg.EggGroup' objects>"
        'getDcsType': None, # (!) real value is "<method 'getDcsType' of 'panda3d.egg.EggGroup' objects>"
        'getDecalFlag': None, # (!) real value is "<method 'getDecalFlag' of 'panda3d.egg.EggGroup' objects>"
        'getDefaultPose': None, # (!) real value is "<method 'getDefaultPose' of 'panda3d.egg.EggGroup' objects>"
        'getDirectFlag': None, # (!) real value is "<method 'getDirectFlag' of 'panda3d.egg.EggGroup' objects>"
        'getFromCollideMask': None, # (!) real value is "<method 'getFromCollideMask' of 'panda3d.egg.EggGroup' objects>"
        'getGroupRef': None, # (!) real value is "<method 'getGroupRef' of 'panda3d.egg.EggGroup' objects>"
        'getGroupRefs': None, # (!) real value is "<method 'getGroupRefs' of 'panda3d.egg.EggGroup' objects>"
        'getGroupType': None, # (!) real value is "<method 'getGroupType' of 'panda3d.egg.EggGroup' objects>"
        'getIndexedFlag': None, # (!) real value is "<method 'getIndexedFlag' of 'panda3d.egg.EggGroup' objects>"
        'getIntoCollideMask': None, # (!) real value is "<method 'getIntoCollideMask' of 'panda3d.egg.EggGroup' objects>"
        'getLod': None, # (!) real value is "<method 'getLod' of 'panda3d.egg.EggGroup' objects>"
        'getModelFlag': None, # (!) real value is "<method 'getModelFlag' of 'panda3d.egg.EggGroup' objects>"
        'getNofogFlag': None, # (!) real value is "<method 'getNofogFlag' of 'panda3d.egg.EggGroup' objects>"
        'getNumGroupRefs': None, # (!) real value is "<method 'getNumGroupRefs' of 'panda3d.egg.EggGroup' objects>"
        'getNumObjectTypes': None, # (!) real value is "<method 'getNumObjectTypes' of 'panda3d.egg.EggGroup' objects>"
        'getObjectType': None, # (!) real value is "<method 'getObjectType' of 'panda3d.egg.EggGroup' objects>"
        'getObjectTypes': None, # (!) real value is "<method 'getObjectTypes' of 'panda3d.egg.EggGroup' objects>"
        'getOccluderFlag': None, # (!) real value is "<method 'getOccluderFlag' of 'panda3d.egg.EggGroup' objects>"
        'getPolylightFlag': None, # (!) real value is "<method 'getPolylightFlag' of 'panda3d.egg.EggGroup' objects>"
        'getPortalFlag': None, # (!) real value is "<method 'getPortalFlag' of 'panda3d.egg.EggGroup' objects>"
        'getScrollR': None, # (!) real value is "<method 'getScrollR' of 'panda3d.egg.EggGroup' objects>"
        'getScrollU': None, # (!) real value is "<method 'getScrollU' of 'panda3d.egg.EggGroup' objects>"
        'getScrollV': None, # (!) real value is "<method 'getScrollV' of 'panda3d.egg.EggGroup' objects>"
        'getScrollW': None, # (!) real value is "<method 'getScrollW' of 'panda3d.egg.EggGroup' objects>"
        'getSwitchFlag': None, # (!) real value is "<method 'getSwitchFlag' of 'panda3d.egg.EggGroup' objects>"
        'getSwitchFps': None, # (!) real value is "<method 'getSwitchFps' of 'panda3d.egg.EggGroup' objects>"
        'getTag': None, # (!) real value is "<method 'getTag' of 'panda3d.egg.EggGroup' objects>"
        'getTexlistFlag': None, # (!) real value is "<method 'getTexlistFlag' of 'panda3d.egg.EggGroup' objects>"
        'getVertexMembership': None, # (!) real value is "<method 'getVertexMembership' of 'panda3d.egg.EggGroup' objects>"
        'get_billboard_center': None, # (!) real value is "<method 'get_billboard_center' of 'panda3d.egg.EggGroup' objects>"
        'get_billboard_type': None, # (!) real value is "<method 'get_billboard_type' of 'panda3d.egg.EggGroup' objects>"
        'get_blend_color': None, # (!) real value is "<method 'get_blend_color' of 'panda3d.egg.EggGroup' objects>"
        'get_blend_mode': None, # (!) real value is "<method 'get_blend_mode' of 'panda3d.egg.EggGroup' objects>"
        'get_blend_operand_a': None, # (!) real value is "<method 'get_blend_operand_a' of 'panda3d.egg.EggGroup' objects>"
        'get_blend_operand_b': None, # (!) real value is "<method 'get_blend_operand_b' of 'panda3d.egg.EggGroup' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CE2B0>)>'
        'get_collide_flags': None, # (!) real value is "<method 'get_collide_flags' of 'panda3d.egg.EggGroup' objects>"
        'get_collide_mask': None, # (!) real value is "<method 'get_collide_mask' of 'panda3d.egg.EggGroup' objects>"
        'get_collision_name': None, # (!) real value is "<method 'get_collision_name' of 'panda3d.egg.EggGroup' objects>"
        'get_cs_type': None, # (!) real value is "<method 'get_cs_type' of 'panda3d.egg.EggGroup' objects>"
        'get_dart_type': None, # (!) real value is "<method 'get_dart_type' of 'panda3d.egg.EggGroup' objects>"
        'get_dcs_type': None, # (!) real value is "<method 'get_dcs_type' of 'panda3d.egg.EggGroup' objects>"
        'get_decal_flag': None, # (!) real value is "<method 'get_decal_flag' of 'panda3d.egg.EggGroup' objects>"
        'get_default_pose': None, # (!) real value is "<method 'get_default_pose' of 'panda3d.egg.EggGroup' objects>"
        'get_direct_flag': None, # (!) real value is "<method 'get_direct_flag' of 'panda3d.egg.EggGroup' objects>"
        'get_from_collide_mask': None, # (!) real value is "<method 'get_from_collide_mask' of 'panda3d.egg.EggGroup' objects>"
        'get_group_ref': None, # (!) real value is "<method 'get_group_ref' of 'panda3d.egg.EggGroup' objects>"
        'get_group_refs': None, # (!) real value is "<method 'get_group_refs' of 'panda3d.egg.EggGroup' objects>"
        'get_group_type': None, # (!) real value is "<method 'get_group_type' of 'panda3d.egg.EggGroup' objects>"
        'get_indexed_flag': None, # (!) real value is "<method 'get_indexed_flag' of 'panda3d.egg.EggGroup' objects>"
        'get_into_collide_mask': None, # (!) real value is "<method 'get_into_collide_mask' of 'panda3d.egg.EggGroup' objects>"
        'get_lod': None, # (!) real value is "<method 'get_lod' of 'panda3d.egg.EggGroup' objects>"
        'get_model_flag': None, # (!) real value is "<method 'get_model_flag' of 'panda3d.egg.EggGroup' objects>"
        'get_nofog_flag': None, # (!) real value is "<method 'get_nofog_flag' of 'panda3d.egg.EggGroup' objects>"
        'get_num_group_refs': None, # (!) real value is "<method 'get_num_group_refs' of 'panda3d.egg.EggGroup' objects>"
        'get_num_object_types': None, # (!) real value is "<method 'get_num_object_types' of 'panda3d.egg.EggGroup' objects>"
        'get_object_type': None, # (!) real value is "<method 'get_object_type' of 'panda3d.egg.EggGroup' objects>"
        'get_object_types': None, # (!) real value is "<method 'get_object_types' of 'panda3d.egg.EggGroup' objects>"
        'get_occluder_flag': None, # (!) real value is "<method 'get_occluder_flag' of 'panda3d.egg.EggGroup' objects>"
        'get_polylight_flag': None, # (!) real value is "<method 'get_polylight_flag' of 'panda3d.egg.EggGroup' objects>"
        'get_portal_flag': None, # (!) real value is "<method 'get_portal_flag' of 'panda3d.egg.EggGroup' objects>"
        'get_scroll_r': None, # (!) real value is "<method 'get_scroll_r' of 'panda3d.egg.EggGroup' objects>"
        'get_scroll_u': None, # (!) real value is "<method 'get_scroll_u' of 'panda3d.egg.EggGroup' objects>"
        'get_scroll_v': None, # (!) real value is "<method 'get_scroll_v' of 'panda3d.egg.EggGroup' objects>"
        'get_scroll_w': None, # (!) real value is "<method 'get_scroll_w' of 'panda3d.egg.EggGroup' objects>"
        'get_switch_flag': None, # (!) real value is "<method 'get_switch_flag' of 'panda3d.egg.EggGroup' objects>"
        'get_switch_fps': None, # (!) real value is "<method 'get_switch_fps' of 'panda3d.egg.EggGroup' objects>"
        'get_tag': None, # (!) real value is "<method 'get_tag' of 'panda3d.egg.EggGroup' objects>"
        'get_texlist_flag': None, # (!) real value is "<method 'get_texlist_flag' of 'panda3d.egg.EggGroup' objects>"
        'get_vertex_membership': None, # (!) real value is "<method 'get_vertex_membership' of 'panda3d.egg.EggGroup' objects>"
        'group_type': None, # (!) real value is "<attribute 'group_type' of 'panda3d.egg.EggGroup' objects>"
        'hasBillboardCenter': None, # (!) real value is "<method 'hasBillboardCenter' of 'panda3d.egg.EggGroup' objects>"
        'hasBlendColor': None, # (!) real value is "<method 'hasBlendColor' of 'panda3d.egg.EggGroup' objects>"
        'hasCollideMask': None, # (!) real value is "<method 'hasCollideMask' of 'panda3d.egg.EggGroup' objects>"
        'hasCollisionName': None, # (!) real value is "<method 'hasCollisionName' of 'panda3d.egg.EggGroup' objects>"
        'hasDcsType': None, # (!) real value is "<method 'hasDcsType' of 'panda3d.egg.EggGroup' objects>"
        'hasFromCollideMask': None, # (!) real value is "<method 'hasFromCollideMask' of 'panda3d.egg.EggGroup' objects>"
        'hasIndexedFlag': None, # (!) real value is "<method 'hasIndexedFlag' of 'panda3d.egg.EggGroup' objects>"
        'hasIntoCollideMask': None, # (!) real value is "<method 'hasIntoCollideMask' of 'panda3d.egg.EggGroup' objects>"
        'hasLod': None, # (!) real value is "<method 'hasLod' of 'panda3d.egg.EggGroup' objects>"
        'hasObjectType': None, # (!) real value is "<method 'hasObjectType' of 'panda3d.egg.EggGroup' objects>"
        'hasScrollingUvs': None, # (!) real value is "<method 'hasScrollingUvs' of 'panda3d.egg.EggGroup' objects>"
        'hasTag': None, # (!) real value is "<method 'hasTag' of 'panda3d.egg.EggGroup' objects>"
        'has_billboard_center': None, # (!) real value is "<method 'has_billboard_center' of 'panda3d.egg.EggGroup' objects>"
        'has_blend_color': None, # (!) real value is "<method 'has_blend_color' of 'panda3d.egg.EggGroup' objects>"
        'has_collide_mask': None, # (!) real value is "<method 'has_collide_mask' of 'panda3d.egg.EggGroup' objects>"
        'has_collision_name': None, # (!) real value is "<method 'has_collision_name' of 'panda3d.egg.EggGroup' objects>"
        'has_dcs_type': None, # (!) real value is "<method 'has_dcs_type' of 'panda3d.egg.EggGroup' objects>"
        'has_from_collide_mask': None, # (!) real value is "<method 'has_from_collide_mask' of 'panda3d.egg.EggGroup' objects>"
        'has_indexed_flag': None, # (!) real value is "<method 'has_indexed_flag' of 'panda3d.egg.EggGroup' objects>"
        'has_into_collide_mask': None, # (!) real value is "<method 'has_into_collide_mask' of 'panda3d.egg.EggGroup' objects>"
        'has_lod': None, # (!) real value is "<method 'has_lod' of 'panda3d.egg.EggGroup' objects>"
        'has_object_type': None, # (!) real value is "<method 'has_object_type' of 'panda3d.egg.EggGroup' objects>"
        'has_scrolling_uvs': None, # (!) real value is "<method 'has_scrolling_uvs' of 'panda3d.egg.EggGroup' objects>"
        'has_tag': None, # (!) real value is "<method 'has_tag' of 'panda3d.egg.EggGroup' objects>"
        'indexed_flag': None, # (!) real value is "<attribute 'indexed_flag' of 'panda3d.egg.EggGroup' objects>"
        'into_collide_mask': None, # (!) real value is "<attribute 'into_collide_mask' of 'panda3d.egg.EggGroup' objects>"
        'isInstanceType': None, # (!) real value is "<method 'isInstanceType' of 'panda3d.egg.EggGroup' objects>"
        'isJoint': None, # (!) real value is "<method 'isJoint' of 'panda3d.egg.EggGroup' objects>"
        'is_instance_type': None, # (!) real value is "<method 'is_instance_type' of 'panda3d.egg.EggGroup' objects>"
        'is_joint': None, # (!) real value is "<method 'is_joint' of 'panda3d.egg.EggGroup' objects>"
        'lod': None, # (!) real value is "<attribute 'lod' of 'panda3d.egg.EggGroup' objects>"
        'model_flag': None, # (!) real value is "<attribute 'model_flag' of 'panda3d.egg.EggGroup' objects>"
        'modifyDefaultPose': None, # (!) real value is "<method 'modifyDefaultPose' of 'panda3d.egg.EggGroup' objects>"
        'modify_default_pose': None, # (!) real value is "<method 'modify_default_pose' of 'panda3d.egg.EggGroup' objects>"
        'nofog_flag': None, # (!) real value is "<attribute 'nofog_flag' of 'panda3d.egg.EggGroup' objects>"
        'object_types': None, # (!) real value is "<attribute 'object_types' of 'panda3d.egg.EggGroup' objects>"
        'occluder_flag': None, # (!) real value is "<attribute 'occluder_flag' of 'panda3d.egg.EggGroup' objects>"
        'portal_flag': None, # (!) real value is "<attribute 'portal_flag' of 'panda3d.egg.EggGroup' objects>"
        'refVertex': None, # (!) real value is "<method 'refVertex' of 'panda3d.egg.EggGroup' objects>"
        'ref_vertex': None, # (!) real value is "<method 'ref_vertex' of 'panda3d.egg.EggGroup' objects>"
        'removeGroupRef': None, # (!) real value is "<method 'removeGroupRef' of 'panda3d.egg.EggGroup' objects>"
        'removeObjectType': None, # (!) real value is "<method 'removeObjectType' of 'panda3d.egg.EggGroup' objects>"
        'remove_group_ref': None, # (!) real value is "<method 'remove_group_ref' of 'panda3d.egg.EggGroup' objects>"
        'remove_object_type': None, # (!) real value is "<method 'remove_object_type' of 'panda3d.egg.EggGroup' objects>"
        'scroll_r': None, # (!) real value is "<attribute 'scroll_r' of 'panda3d.egg.EggGroup' objects>"
        'scroll_u': None, # (!) real value is "<attribute 'scroll_u' of 'panda3d.egg.EggGroup' objects>"
        'scroll_v': None, # (!) real value is "<attribute 'scroll_v' of 'panda3d.egg.EggGroup' objects>"
        'scroll_w': None, # (!) real value is "<attribute 'scroll_w' of 'panda3d.egg.EggGroup' objects>"
        'setBillboardCenter': None, # (!) real value is "<method 'setBillboardCenter' of 'panda3d.egg.EggGroup' objects>"
        'setBillboardType': None, # (!) real value is "<method 'setBillboardType' of 'panda3d.egg.EggGroup' objects>"
        'setBlendColor': None, # (!) real value is "<method 'setBlendColor' of 'panda3d.egg.EggGroup' objects>"
        'setBlendMode': None, # (!) real value is "<method 'setBlendMode' of 'panda3d.egg.EggGroup' objects>"
        'setBlendOperandA': None, # (!) real value is "<method 'setBlendOperandA' of 'panda3d.egg.EggGroup' objects>"
        'setBlendOperandB': None, # (!) real value is "<method 'setBlendOperandB' of 'panda3d.egg.EggGroup' objects>"
        'setCollideFlags': None, # (!) real value is "<method 'setCollideFlags' of 'panda3d.egg.EggGroup' objects>"
        'setCollideMask': None, # (!) real value is "<method 'setCollideMask' of 'panda3d.egg.EggGroup' objects>"
        'setCollisionName': None, # (!) real value is "<method 'setCollisionName' of 'panda3d.egg.EggGroup' objects>"
        'setCsType': None, # (!) real value is "<method 'setCsType' of 'panda3d.egg.EggGroup' objects>"
        'setDartType': None, # (!) real value is "<method 'setDartType' of 'panda3d.egg.EggGroup' objects>"
        'setDcsType': None, # (!) real value is "<method 'setDcsType' of 'panda3d.egg.EggGroup' objects>"
        'setDecalFlag': None, # (!) real value is "<method 'setDecalFlag' of 'panda3d.egg.EggGroup' objects>"
        'setDefaultPose': None, # (!) real value is "<method 'setDefaultPose' of 'panda3d.egg.EggGroup' objects>"
        'setDirectFlag': None, # (!) real value is "<method 'setDirectFlag' of 'panda3d.egg.EggGroup' objects>"
        'setFromCollideMask': None, # (!) real value is "<method 'setFromCollideMask' of 'panda3d.egg.EggGroup' objects>"
        'setGroupType': None, # (!) real value is "<method 'setGroupType' of 'panda3d.egg.EggGroup' objects>"
        'setIndexedFlag': None, # (!) real value is "<method 'setIndexedFlag' of 'panda3d.egg.EggGroup' objects>"
        'setIntoCollideMask': None, # (!) real value is "<method 'setIntoCollideMask' of 'panda3d.egg.EggGroup' objects>"
        'setLod': None, # (!) real value is "<method 'setLod' of 'panda3d.egg.EggGroup' objects>"
        'setModelFlag': None, # (!) real value is "<method 'setModelFlag' of 'panda3d.egg.EggGroup' objects>"
        'setNofogFlag': None, # (!) real value is "<method 'setNofogFlag' of 'panda3d.egg.EggGroup' objects>"
        'setOccluderFlag': None, # (!) real value is "<method 'setOccluderFlag' of 'panda3d.egg.EggGroup' objects>"
        'setPolylightFlag': None, # (!) real value is "<method 'setPolylightFlag' of 'panda3d.egg.EggGroup' objects>"
        'setPortalFlag': None, # (!) real value is "<method 'setPortalFlag' of 'panda3d.egg.EggGroup' objects>"
        'setScrollR': None, # (!) real value is "<method 'setScrollR' of 'panda3d.egg.EggGroup' objects>"
        'setScrollU': None, # (!) real value is "<method 'setScrollU' of 'panda3d.egg.EggGroup' objects>"
        'setScrollV': None, # (!) real value is "<method 'setScrollV' of 'panda3d.egg.EggGroup' objects>"
        'setScrollW': None, # (!) real value is "<method 'setScrollW' of 'panda3d.egg.EggGroup' objects>"
        'setSwitchFlag': None, # (!) real value is "<method 'setSwitchFlag' of 'panda3d.egg.EggGroup' objects>"
        'setSwitchFps': None, # (!) real value is "<method 'setSwitchFps' of 'panda3d.egg.EggGroup' objects>"
        'setTag': None, # (!) real value is "<method 'setTag' of 'panda3d.egg.EggGroup' objects>"
        'setTexlistFlag': None, # (!) real value is "<method 'setTexlistFlag' of 'panda3d.egg.EggGroup' objects>"
        'setVertexMembership': None, # (!) real value is "<method 'setVertexMembership' of 'panda3d.egg.EggGroup' objects>"
        'set_billboard_center': None, # (!) real value is "<method 'set_billboard_center' of 'panda3d.egg.EggGroup' objects>"
        'set_billboard_type': None, # (!) real value is "<method 'set_billboard_type' of 'panda3d.egg.EggGroup' objects>"
        'set_blend_color': None, # (!) real value is "<method 'set_blend_color' of 'panda3d.egg.EggGroup' objects>"
        'set_blend_mode': None, # (!) real value is "<method 'set_blend_mode' of 'panda3d.egg.EggGroup' objects>"
        'set_blend_operand_a': None, # (!) real value is "<method 'set_blend_operand_a' of 'panda3d.egg.EggGroup' objects>"
        'set_blend_operand_b': None, # (!) real value is "<method 'set_blend_operand_b' of 'panda3d.egg.EggGroup' objects>"
        'set_collide_flags': None, # (!) real value is "<method 'set_collide_flags' of 'panda3d.egg.EggGroup' objects>"
        'set_collide_mask': None, # (!) real value is "<method 'set_collide_mask' of 'panda3d.egg.EggGroup' objects>"
        'set_collision_name': None, # (!) real value is "<method 'set_collision_name' of 'panda3d.egg.EggGroup' objects>"
        'set_cs_type': None, # (!) real value is "<method 'set_cs_type' of 'panda3d.egg.EggGroup' objects>"
        'set_dart_type': None, # (!) real value is "<method 'set_dart_type' of 'panda3d.egg.EggGroup' objects>"
        'set_dcs_type': None, # (!) real value is "<method 'set_dcs_type' of 'panda3d.egg.EggGroup' objects>"
        'set_decal_flag': None, # (!) real value is "<method 'set_decal_flag' of 'panda3d.egg.EggGroup' objects>"
        'set_default_pose': None, # (!) real value is "<method 'set_default_pose' of 'panda3d.egg.EggGroup' objects>"
        'set_direct_flag': None, # (!) real value is "<method 'set_direct_flag' of 'panda3d.egg.EggGroup' objects>"
        'set_from_collide_mask': None, # (!) real value is "<method 'set_from_collide_mask' of 'panda3d.egg.EggGroup' objects>"
        'set_group_type': None, # (!) real value is "<method 'set_group_type' of 'panda3d.egg.EggGroup' objects>"
        'set_indexed_flag': None, # (!) real value is "<method 'set_indexed_flag' of 'panda3d.egg.EggGroup' objects>"
        'set_into_collide_mask': None, # (!) real value is "<method 'set_into_collide_mask' of 'panda3d.egg.EggGroup' objects>"
        'set_lod': None, # (!) real value is "<method 'set_lod' of 'panda3d.egg.EggGroup' objects>"
        'set_model_flag': None, # (!) real value is "<method 'set_model_flag' of 'panda3d.egg.EggGroup' objects>"
        'set_nofog_flag': None, # (!) real value is "<method 'set_nofog_flag' of 'panda3d.egg.EggGroup' objects>"
        'set_occluder_flag': None, # (!) real value is "<method 'set_occluder_flag' of 'panda3d.egg.EggGroup' objects>"
        'set_polylight_flag': None, # (!) real value is "<method 'set_polylight_flag' of 'panda3d.egg.EggGroup' objects>"
        'set_portal_flag': None, # (!) real value is "<method 'set_portal_flag' of 'panda3d.egg.EggGroup' objects>"
        'set_scroll_r': None, # (!) real value is "<method 'set_scroll_r' of 'panda3d.egg.EggGroup' objects>"
        'set_scroll_u': None, # (!) real value is "<method 'set_scroll_u' of 'panda3d.egg.EggGroup' objects>"
        'set_scroll_v': None, # (!) real value is "<method 'set_scroll_v' of 'panda3d.egg.EggGroup' objects>"
        'set_scroll_w': None, # (!) real value is "<method 'set_scroll_w' of 'panda3d.egg.EggGroup' objects>"
        'set_switch_flag': None, # (!) real value is "<method 'set_switch_flag' of 'panda3d.egg.EggGroup' objects>"
        'set_switch_fps': None, # (!) real value is "<method 'set_switch_fps' of 'panda3d.egg.EggGroup' objects>"
        'set_tag': None, # (!) real value is "<method 'set_tag' of 'panda3d.egg.EggGroup' objects>"
        'set_texlist_flag': None, # (!) real value is "<method 'set_texlist_flag' of 'panda3d.egg.EggGroup' objects>"
        'set_vertex_membership': None, # (!) real value is "<method 'set_vertex_membership' of 'panda3d.egg.EggGroup' objects>"
        'stealVrefs': None, # (!) real value is "<method 'stealVrefs' of 'panda3d.egg.EggGroup' objects>"
        'steal_vrefs': None, # (!) real value is "<method 'steal_vrefs' of 'panda3d.egg.EggGroup' objects>"
        'stringBillboardType': None, # (!) real value is '<staticmethod(<built-in method stringBillboardType of type object at 0x00007FFDC68CE2B0>)>'
        'stringBlendMode': None, # (!) real value is '<staticmethod(<built-in method stringBlendMode of type object at 0x00007FFDC68CE2B0>)>'
        'stringBlendOperand': None, # (!) real value is '<staticmethod(<built-in method stringBlendOperand of type object at 0x00007FFDC68CE2B0>)>'
        'stringCollideFlags': None, # (!) real value is '<staticmethod(<built-in method stringCollideFlags of type object at 0x00007FFDC68CE2B0>)>'
        'stringCsType': None, # (!) real value is '<staticmethod(<built-in method stringCsType of type object at 0x00007FFDC68CE2B0>)>'
        'stringDartType': None, # (!) real value is '<staticmethod(<built-in method stringDartType of type object at 0x00007FFDC68CE2B0>)>'
        'stringDcsType': None, # (!) real value is '<staticmethod(<built-in method stringDcsType of type object at 0x00007FFDC68CE2B0>)>'
        'stringGroupType': None, # (!) real value is '<staticmethod(<built-in method stringGroupType of type object at 0x00007FFDC68CE2B0>)>'
        'string_billboard_type': None, # (!) real value is '<staticmethod(<built-in method string_billboard_type of type object at 0x00007FFDC68CE2B0>)>'
        'string_blend_mode': None, # (!) real value is '<staticmethod(<built-in method string_blend_mode of type object at 0x00007FFDC68CE2B0>)>'
        'string_blend_operand': None, # (!) real value is '<staticmethod(<built-in method string_blend_operand of type object at 0x00007FFDC68CE2B0>)>'
        'string_collide_flags': None, # (!) real value is '<staticmethod(<built-in method string_collide_flags of type object at 0x00007FFDC68CE2B0>)>'
        'string_cs_type': None, # (!) real value is '<staticmethod(<built-in method string_cs_type of type object at 0x00007FFDC68CE2B0>)>'
        'string_dart_type': None, # (!) real value is '<staticmethod(<built-in method string_dart_type of type object at 0x00007FFDC68CE2B0>)>'
        'string_dcs_type': None, # (!) real value is '<staticmethod(<built-in method string_dcs_type of type object at 0x00007FFDC68CE2B0>)>'
        'string_group_type': None, # (!) real value is '<staticmethod(<built-in method string_group_type of type object at 0x00007FFDC68CE2B0>)>'
        'switch_flag': None, # (!) real value is "<attribute 'switch_flag' of 'panda3d.egg.EggGroup' objects>"
        'switch_fps': None, # (!) real value is "<attribute 'switch_fps' of 'panda3d.egg.EggGroup' objects>"
        'testVrefIntegrity': None, # (!) real value is "<method 'testVrefIntegrity' of 'panda3d.egg.EggGroup' objects>"
        'test_vref_integrity': None, # (!) real value is "<method 'test_vref_integrity' of 'panda3d.egg.EggGroup' objects>"
        'texlist_flag': None, # (!) real value is "<attribute 'texlist_flag' of 'panda3d.egg.EggGroup' objects>"
        'unrefAllVertices': None, # (!) real value is "<method 'unrefAllVertices' of 'panda3d.egg.EggGroup' objects>"
        'unrefVertex': None, # (!) real value is "<method 'unrefVertex' of 'panda3d.egg.EggGroup' objects>"
        'unref_all_vertices': None, # (!) real value is "<method 'unref_all_vertices' of 'panda3d.egg.EggGroup' objects>"
        'unref_vertex': None, # (!) real value is "<method 'unref_vertex' of 'panda3d.egg.EggGroup' objects>"
        'upcastToEggGroupNode': None, # (!) real value is "<method 'upcastToEggGroupNode' of 'panda3d.egg.EggGroup' objects>"
        'upcastToEggRenderMode': None, # (!) real value is "<method 'upcastToEggRenderMode' of 'panda3d.egg.EggGroup' objects>"
        'upcastToEggTransform': None, # (!) real value is "<method 'upcastToEggTransform' of 'panda3d.egg.EggGroup' objects>"
        'upcast_to_EggGroupNode': None, # (!) real value is "<method 'upcast_to_EggGroupNode' of 'panda3d.egg.EggGroup' objects>"
        'upcast_to_EggRenderMode': None, # (!) real value is "<method 'upcast_to_EggRenderMode' of 'panda3d.egg.EggGroup' objects>"
        'upcast_to_EggTransform': None, # (!) real value is "<method 'upcast_to_EggTransform' of 'panda3d.egg.EggGroup' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.egg.EggGroup' objects>"
        'writeBillboardFlags': None, # (!) real value is "<method 'writeBillboardFlags' of 'panda3d.egg.EggGroup' objects>"
        'writeCollideFlags': None, # (!) real value is "<method 'writeCollideFlags' of 'panda3d.egg.EggGroup' objects>"
        'writeDecalFlags': None, # (!) real value is "<method 'writeDecalFlags' of 'panda3d.egg.EggGroup' objects>"
        'writeModelFlags': None, # (!) real value is "<method 'writeModelFlags' of 'panda3d.egg.EggGroup' objects>"
        'writeObjectTypes': None, # (!) real value is "<method 'writeObjectTypes' of 'panda3d.egg.EggGroup' objects>"
        'writeRenderMode': None, # (!) real value is "<method 'writeRenderMode' of 'panda3d.egg.EggGroup' objects>"
        'writeSwitchFlags': None, # (!) real value is "<method 'writeSwitchFlags' of 'panda3d.egg.EggGroup' objects>"
        'writeTags': None, # (!) real value is "<method 'writeTags' of 'panda3d.egg.EggGroup' objects>"
        'write_billboard_flags': None, # (!) real value is "<method 'write_billboard_flags' of 'panda3d.egg.EggGroup' objects>"
        'write_collide_flags': None, # (!) real value is "<method 'write_collide_flags' of 'panda3d.egg.EggGroup' objects>"
        'write_decal_flags': None, # (!) real value is "<method 'write_decal_flags' of 'panda3d.egg.EggGroup' objects>"
        'write_model_flags': None, # (!) real value is "<method 'write_model_flags' of 'panda3d.egg.EggGroup' objects>"
        'write_object_types': None, # (!) real value is "<method 'write_object_types' of 'panda3d.egg.EggGroup' objects>"
        'write_render_mode': None, # (!) real value is "<method 'write_render_mode' of 'panda3d.egg.EggGroup' objects>"
        'write_switch_flags': None, # (!) real value is "<method 'write_switch_flags' of 'panda3d.egg.EggGroup' objects>"
        'write_tags': None, # (!) real value is "<method 'write_tags' of 'panda3d.egg.EggGroup' objects>"
    }
    DTStructured = 268435456
    DTSync = 536870912
    DT_default = 1073741824
    DT_none = 0
    DT_nosync = 805306368
    DT_structured = 268435456
    DT_sync = 536870912
    GTGroup = 0
    GTInstance = 1
    GTInvalid = -1
    GTJoint = 2
    GT_group = 0
    GT_instance = 1
    GT_invalid = -1
    GT_joint = 2


