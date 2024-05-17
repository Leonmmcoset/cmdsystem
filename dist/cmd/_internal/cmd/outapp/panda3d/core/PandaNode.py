# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

from .Namable import Namable

class PandaNode(TypedWritableReferenceCount, Namable):
    """
    /**
     * A basic node of the scene graph or data graph.  This is the base class of
     * all specialized nodes, and also serves as a generic node with no special
     * properties.
     */
    """
    def addChild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_child(const PandaNode self, PandaNode child_node, int sort, Thread current_thread)
        
        /**
         * Adds a new child to the node.  The child is added in the relative position
         * indicated by sort; if all children have the same sort index, the child is
         * added at the end.
         *
         * If the same child is added to a node more than once, the previous instance
         * is first removed.
         */
        """
        pass

    def addStashed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_stashed(const PandaNode self, PandaNode child_node, int sort, Thread current_thread)
        
        /**
         * Adds a new child to the node, directly as a stashed child.  The child is
         * not added in the normal sense, but will be revealed if unstash_child() is
         * called on it later.
         *
         * If the same child is added to a node more than once, the previous instance
         * is first removed.
         *
         * This can only be called from the top pipeline stage (i.e.  from App).
         */
        """
        pass

    def add_child(self, const_PandaNode_self, PandaNode_child_node, int_sort, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_child(const PandaNode self, PandaNode child_node, int sort, Thread current_thread)
        
        /**
         * Adds a new child to the node.  The child is added in the relative position
         * indicated by sort; if all children have the same sort index, the child is
         * added at the end.
         *
         * If the same child is added to a node more than once, the previous instance
         * is first removed.
         */
        """
        pass

    def add_stashed(self, const_PandaNode_self, PandaNode_child_node, int_sort, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_stashed(const PandaNode self, PandaNode child_node, int sort, Thread current_thread)
        
        /**
         * Adds a new child to the node, directly as a stashed child.  The child is
         * not added in the normal sense, but will be revealed if unstash_child() is
         * called on it later.
         *
         * If the same child is added to a node more than once, the previous instance
         * is first removed.
         *
         * This can only be called from the top pipeline stage (i.e.  from App).
         */
        """
        pass

    def adjustDrawMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        adjust_draw_mask(const PandaNode self, BitMask show_mask, BitMask hide_mask, BitMask clear_mask)
        
        /**
         * Adjusts the hide/show bits of this particular node.
         *
         * These three parameters can be used to adjust the _draw_control_mask and
         * _draw_show_mask independently, which work together to provide per-camera
         * visibility for the node and its descendents.
         *
         * _draw_control_mask indicates the bits in _draw_show_mask that are
         * significant.  Each different bit corresponds to a different camera (and
         * these bits are assigned via Camera::set_camera_mask()).
         *
         * Where _draw_control_mask has a 1 bit, a 1 bit in _draw_show_mask indicates
         * the node is visible to that camera, and a 0 bit indicates the node is
         * hidden to that camera.  Where _draw_control_mask is 0, the node is hidden
         * only if a parent node is hidden.
         *
         * The meaning of the three parameters is as follows:
         *
         * * Wherever show_mask is 1, _draw_show_mask and _draw_control_mask will be
         * set 1.  Thus, show_mask indicates the set of cameras to which the node
         * should be shown.
         *
         * * Wherever hide_mask is 1, _draw_show_mask will be set 0 and
         * _draw_control_mask will be set 1.  Thus, hide_mask indicates the set of
         * cameras from which the node should be hidden.
         *
         * * Wherever clear_mask is 1, _draw_control_mask will be set 0.  Thus,
         * clear_mask indicates the set of cameras from which the hidden state should
         * be inherited from a parent.
         */
        """
        pass

    def adjust_draw_mask(self, const_PandaNode_self, BitMask_show_mask, BitMask_hide_mask, BitMask_clear_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        adjust_draw_mask(const PandaNode self, BitMask show_mask, BitMask hide_mask, BitMask clear_mask)
        
        /**
         * Adjusts the hide/show bits of this particular node.
         *
         * These three parameters can be used to adjust the _draw_control_mask and
         * _draw_show_mask independently, which work together to provide per-camera
         * visibility for the node and its descendents.
         *
         * _draw_control_mask indicates the bits in _draw_show_mask that are
         * significant.  Each different bit corresponds to a different camera (and
         * these bits are assigned via Camera::set_camera_mask()).
         *
         * Where _draw_control_mask has a 1 bit, a 1 bit in _draw_show_mask indicates
         * the node is visible to that camera, and a 0 bit indicates the node is
         * hidden to that camera.  Where _draw_control_mask is 0, the node is hidden
         * only if a parent node is hidden.
         *
         * The meaning of the three parameters is as follows:
         *
         * * Wherever show_mask is 1, _draw_show_mask and _draw_control_mask will be
         * set 1.  Thus, show_mask indicates the set of cameras to which the node
         * should be shown.
         *
         * * Wherever hide_mask is 1, _draw_show_mask will be set 0 and
         * _draw_control_mask will be set 1.  Thus, hide_mask indicates the set of
         * cameras from which the node should be hidden.
         *
         * * Wherever clear_mask is 1, _draw_control_mask will be set 0.  Thus,
         * clear_mask indicates the set of cameras from which the hidden state should
         * be inherited from a parent.
         */
        """
        pass

    def asLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        as_light(const PandaNode self)
        
        /**
         * Cross-casts the node to a Light pointer, if it is one of the four kinds of
         * Light nodes, or returns NULL if it is not.
         */
        """
        pass

    def as_light(self, const_PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        as_light(const PandaNode self)
        
        /**
         * Cross-casts the node to a Light pointer, if it is one of the four kinds of
         * Light nodes, or returns NULL if it is not.
         */
        """
        pass

    def clearAttrib(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_attrib(const PandaNode self, TypeHandle type)
        clear_attrib(const PandaNode self, int slot)
        
        /**
         * Removes the render attribute of the given type from this node.  This node,
         * and the subgraph below, will now inherit the indicated render attribute
         * from the nodes above this one.
         */
        
        /**
         * Removes the render attribute of the given type from this node.  This node,
         * and the subgraph below, will now inherit the indicated render attribute
         * from the nodes above this one.
         */
        """
        pass

    def clearBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_bounds(const PandaNode self)
        
        /**
         * Reverses the effect of a previous call to set_bounds(), and allows the
         * node's bounding volume to be automatically computed once more based on the
         * contents of the node.
         */
        """
        pass

    def clearEffect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_effect(const PandaNode self, TypeHandle type)
        
        /**
         * Removes the render effect of the given type from this node.
         */
        """
        pass

    def clearEffects(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_effects(const PandaNode self, Thread current_thread)
        
        /**
         * Resets this node to have no render effects.
         */
        """
        pass

    def clearPythonTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_python_tag(const PandaNode self, object key)
        """
        pass

    def clearState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_state(const PandaNode self, Thread current_thread)
        
        /**
         * Resets this node to leave the render state alone.  Nodes at this level and
         * below will once again inherit their render state unchanged from the nodes
         * above this level.
         */
        """
        pass

    def clearTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_tag(const PandaNode self, str key, Thread current_thread)
        
        /**
         * Removes the value defined for this key on this particular node.  After a
         * call to clear_tag(), has_tag() will return false for the indicated key.
         */
        """
        pass

    def clearTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_transform(const PandaNode self, Thread current_thread)
        
        /**
         * Resets the transform on this node to the identity transform.
         */
        """
        pass

    def clearUnexpectedChange(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_unexpected_change(const PandaNode self, int flags)
        
        /**
         * Sets one or more of the PandaNode::UnexpectedChange bits off, indicating
         * that the corresponding property may once again change on this node.  See
         * set_unexpected_change().
         *
         * The input parameter is the union of bits that are to be cleared.
         *
         * Since this is a developer debugging tool only, this function does nothing
         * in a production (NDEBUG) build.
         */
        """
        pass

    def clear_attrib(self, const_PandaNode_self, TypeHandle_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_attrib(const PandaNode self, TypeHandle type)
        clear_attrib(const PandaNode self, int slot)
        
        /**
         * Removes the render attribute of the given type from this node.  This node,
         * and the subgraph below, will now inherit the indicated render attribute
         * from the nodes above this one.
         */
        
        /**
         * Removes the render attribute of the given type from this node.  This node,
         * and the subgraph below, will now inherit the indicated render attribute
         * from the nodes above this one.
         */
        """
        pass

    def clear_bounds(self, const_PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_bounds(const PandaNode self)
        
        /**
         * Reverses the effect of a previous call to set_bounds(), and allows the
         * node's bounding volume to be automatically computed once more based on the
         * contents of the node.
         */
        """
        pass

    def clear_effect(self, const_PandaNode_self, TypeHandle_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_effect(const PandaNode self, TypeHandle type)
        
        /**
         * Removes the render effect of the given type from this node.
         */
        """
        pass

    def clear_effects(self, const_PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_effects(const PandaNode self, Thread current_thread)
        
        /**
         * Resets this node to have no render effects.
         */
        """
        pass

    def clear_python_tag(self, const_PandaNode_self, object_key): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_python_tag(const PandaNode self, object key)
        """
        pass

    def clear_state(self, const_PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_state(const PandaNode self, Thread current_thread)
        
        /**
         * Resets this node to leave the render state alone.  Nodes at this level and
         * below will once again inherit their render state unchanged from the nodes
         * above this level.
         */
        """
        pass

    def clear_tag(self, const_PandaNode_self, str_key, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_tag(const PandaNode self, str key, Thread current_thread)
        
        /**
         * Removes the value defined for this key on this particular node.  After a
         * call to clear_tag(), has_tag() will return false for the indicated key.
         */
        """
        pass

    def clear_transform(self, const_PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_transform(const PandaNode self, Thread current_thread)
        
        /**
         * Resets the transform on this node to the identity transform.
         */
        """
        pass

    def clear_unexpected_change(self, const_PandaNode_self, int_flags): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_unexpected_change(const PandaNode self, int flags)
        
        /**
         * Sets one or more of the PandaNode::UnexpectedChange bits off, indicating
         * that the corresponding property may once again change on this node.  See
         * set_unexpected_change().
         *
         * The input parameter is the union of bits that are to be cleared.
         *
         * Since this is a developer debugging tool only, this function does nothing
         * in a production (NDEBUG) build.
         */
        """
        pass

    def combineWith(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        combine_with(const PandaNode self, PandaNode other)
        
        // published so that characters can be combined.
        
        /**
         * Collapses this PandaNode with the other PandaNode, if possible, and returns
         * a pointer to the combined PandaNode, or NULL if the two PandaNodes cannot
         * safely be combined.
         *
         * The return value may be this, other, or a new PandaNode altogether.
         *
         * This function is called from GraphReducer::flatten(), and need not deal
         * with children; its job is just to decide whether to collapse the two
         * PandaNodes and what the collapsed PandaNode should look like.
         */
        """
        pass

    def combine_with(self, const_PandaNode_self, PandaNode_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        combine_with(const PandaNode self, PandaNode other)
        
        // published so that characters can be combined.
        
        /**
         * Collapses this PandaNode with the other PandaNode, if possible, and returns
         * a pointer to the combined PandaNode, or NULL if the two PandaNodes cannot
         * safely be combined.
         *
         * The return value may be this, other, or a new PandaNode altogether.
         *
         * This function is called from GraphReducer::flatten(), and need not deal
         * with children; its job is just to decide whether to collapse the two
         * PandaNodes and what the collapsed PandaNode should look like.
         */
        """
        pass

    def compareTags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_tags(PandaNode self, const PandaNode other)
        
        /**
         * Returns a number less than 0, 0, or greater than 0, to indicate the
         * similarity of tags between this node and the other one.  If this returns 0,
         * the tags are identical.  If it returns other than 0, then the tags are
         * different; and the nodes may be sorted into a consistent (but arbitrary)
         * ordering based on this number.
         */
        """
        pass

    def compare_tags(self, PandaNode_self, const_PandaNode_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_tags(PandaNode self, const PandaNode other)
        
        /**
         * Returns a number less than 0, 0, or greater than 0, to indicate the
         * similarity of tags between this node and the other one.  If this returns 0,
         * the tags are identical.  If it returns other than 0, then the tags are
         * different; and the nodes may be sorted into a consistent (but arbitrary)
         * ordering based on this number.
         */
        """
        pass

    def copyAllProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_all_properties(const PandaNode self, PandaNode other)
        
        /**
         * Copies the TransformState, RenderState, RenderEffects, tags, Python tags,
         * and the show/hide state from the other node onto this one.  Typically this
         * is used to prepare a node to replace another node in the scene graph (also
         * see replace_node()).
         */
        """
        pass

    def copyChildren(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_children(const PandaNode self, PandaNode other, Thread current_thread)
        
        /**
         * Makes another instance of all the children of the other node, copying them
         * to this node.
         */
        """
        pass

    def copySubgraph(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_subgraph(PandaNode self, Thread current_thread)
        
        /**
         * Allocates and returns a complete copy of this PandaNode and the entire
         * scene graph rooted at this PandaNode.  Some data may still be shared from
         * the original (e.g.  vertex index tables), but nothing that will impede
         * normal use of the PandaNode.
         */
        """
        pass

    def copyTags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_tags(const PandaNode self, PandaNode other)
        
        /**
         * Copies all of the tags stored on the other node onto this node.  If a
         * particular tag exists on both nodes, the contents of this node's value is
         * replaced by that of the other.
         */
        """
        pass

    def copy_all_properties(self, const_PandaNode_self, PandaNode_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_all_properties(const PandaNode self, PandaNode other)
        
        /**
         * Copies the TransformState, RenderState, RenderEffects, tags, Python tags,
         * and the show/hide state from the other node onto this one.  Typically this
         * is used to prepare a node to replace another node in the scene graph (also
         * see replace_node()).
         */
        """
        pass

    def copy_children(self, const_PandaNode_self, PandaNode_other, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_children(const PandaNode self, PandaNode other, Thread current_thread)
        
        /**
         * Makes another instance of all the children of the other node, copying them
         * to this node.
         */
        """
        pass

    def copy_subgraph(self, PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_subgraph(PandaNode self, Thread current_thread)
        
        /**
         * Allocates and returns a complete copy of this PandaNode and the entire
         * scene graph rooted at this PandaNode.  Some data may still be shared from
         * the original (e.g.  vertex index tables), but nothing that will impede
         * normal use of the PandaNode.
         */
        """
        pass

    def copy_tags(self, const_PandaNode_self, PandaNode_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_tags(const PandaNode self, PandaNode other)
        
        /**
         * Copies all of the tags stored on the other node onto this node.  If a
         * particular tag exists on both nodes, the contents of this node's value is
         * replaced by that of the other.
         */
        """
        pass

    def countNumDescendants(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        count_num_descendants(PandaNode self)
        
        /**
         * Returns the number of nodes at and below this level.
         */
        """
        pass

    def count_num_descendants(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        count_num_descendants(PandaNode self)
        
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
         * Reads the bytes created by a previous call to encode_to_bam_stream(), and
         * extracts and returns the single object on those bytes.  Returns NULL on
         * error.
         *
         * This method is intended to replace decode_raw_from_bam_stream() when you
         * know the stream in question returns an object of type PandaNode, allowing
         * for easier reference count management.  Note that the caller is still
         * responsible for maintaining the reference count on the return value.
         */
        """
        pass

    def decode_from_bam_stream(self, bytes_data, BamReader_reader): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        decode_from_bam_stream(bytes data, BamReader reader)
        
        /**
         * Reads the bytes created by a previous call to encode_to_bam_stream(), and
         * extracts and returns the single object on those bytes.  Returns NULL on
         * error.
         *
         * This method is intended to replace decode_raw_from_bam_stream() when you
         * know the stream in question returns an object of type PandaNode, allowing
         * for easier reference count management.  Note that the caller is still
         * responsible for maintaining the reference count on the return value.
         */
        """
        pass

    def findChild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_child(PandaNode self, PandaNode node, Thread current_thread)
        
        /**
         * Returns the index of the indicated child node, if it is a child, or -1 if
         * it is not.
         */
        """
        pass

    def findParent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_parent(PandaNode self, PandaNode node, Thread current_thread)
        
        /**
         * Returns the index of the indicated parent node, if it is a parent, or -1 if
         * it is not.
         */
        """
        pass

    def findStashed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_stashed(PandaNode self, PandaNode node, Thread current_thread)
        
        /**
         * Returns the index of the indicated stashed node, if it is a stashed child,
         * or -1 if it is not.
         */
        """
        pass

    def find_child(self, PandaNode_self, PandaNode_node, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_child(PandaNode self, PandaNode node, Thread current_thread)
        
        /**
         * Returns the index of the indicated child node, if it is a child, or -1 if
         * it is not.
         */
        """
        pass

    def find_parent(self, PandaNode_self, PandaNode_node, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_parent(PandaNode self, PandaNode node, Thread current_thread)
        
        /**
         * Returns the index of the indicated parent node, if it is a parent, or -1 if
         * it is not.
         */
        """
        pass

    def find_stashed(self, PandaNode_self, PandaNode_node, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_stashed(PandaNode self, PandaNode node, Thread current_thread)
        
        /**
         * Returns the index of the indicated stashed node, if it is a stashed child,
         * or -1 if it is not.
         */
        """
        pass

    def getAllCameraMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_all_camera_mask()
        
        /**
         * Returns a DrawMask that is appropriate for rendering to all cameras.
         */
        """
        pass

    def getAttrib(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_attrib(PandaNode self, TypeHandle type)
        get_attrib(PandaNode self, int slot)
        
        /**
         * Returns the render attribute of the indicated type, if it is defined on the
         * node, or NULL if it is not.  This checks only what is set on this
         * particular node level, and has nothing to do with what render attributes
         * may be inherited from parent nodes.
         */
        
        /**
         * Returns the render attribute of the indicated type, if it is defined on the
         * node, or NULL if it is not.  This checks only what is set on this
         * particular node level, and has nothing to do with what render attributes
         * may be inherited from parent nodes.
         */
        """
        pass

    def getBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bounds(PandaNode self)
        get_bounds(PandaNode self, UpdateSeq seq, Thread current_thread)
        get_bounds(PandaNode self, Thread current_thread)
        
        /**
         * Returns the external bounding volume of this node: a bounding volume that
         * contains the user bounding volume, the internal bounding volume, and all of
         * the children's bounding volumes.
         */
        
        /**
         * This flavor of get_bounds() return the external bounding volume, and also
         * fills in seq with the bounding volume's current sequence number.  When this
         * sequence number changes, it indicates that the bounding volume might have
         * changed, e.g.  because some nested child's bounding volume has changed.
         *
         * Although this might occasionally increment without changing the bounding
         * volume, the bounding volume will never change without incrementing this
         * counter, so as long as this counter remains unchanged you can be confident
         * the bounding volume is also unchanged.
         */
        """
        pass

    def getBoundsType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bounds_type(PandaNode self)
        
        /**
         * Returns the bounding volume type set with set_bounds_type().
         */
        """
        pass

    def getChild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_child(PandaNode self, int n, Thread current_thread)
        
        /**
         * Returns the nth child node of this node.  See get_num_children().  Also see
         * get_children(), if your intention is to iterate through the complete list
         * of children; get_children() is preferable in this case.
         */
        """
        pass

    def getChildren(self, *args, **kwargs): # real signature unknown
        pass

    def getChildSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_child_sort(PandaNode self, int n, Thread current_thread)
        
        /**
         * Returns the sort index of the nth child node of this node (that is, the
         * number that was passed to add_child()).  See get_num_children().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDrawControlMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_draw_control_mask(PandaNode self)
        
        /**
         * Returns the set of bits in draw_show_mask that are considered meaningful.
         * See adjust_draw_mask().
         */
        """
        pass

    def getDrawShowMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_draw_show_mask(PandaNode self)
        
        /**
         * Returns the hide/show bits of this particular node.  See
         * adjust_draw_mask().
         */
        """
        pass

    def getEffect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_effect(PandaNode self, TypeHandle type)
        
        /**
         * Returns the render effect of the indicated type, if it is defined on the
         * node, or NULL if it is not.
         */
        """
        pass

    def getEffects(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_effects(PandaNode self, Thread current_thread)
        
        /**
         * Returns the complete RenderEffects that will be applied to this node.
         */
        """
        pass

    def getFancyBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fancy_bits(PandaNode self, Thread current_thread)
        
        /**
         * Returns the union of all of the enum FancyBits values corresponding to the
         * various "fancy" attributes that are set on the node.  If this returns 0,
         * the node has nothing interesting about it.  This is intended to speed
         * traversal by quickly skipping past nodes that don't particularly affect the
         * render state.
         */
        """
        pass

    def getInternalBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_internal_bounds(PandaNode self, Thread current_thread)
        
        /**
         * Returns the node's internal bounding volume.  This is the bounding volume
         * around the node alone, without including children.  If the user has called
         * set_bounds(), it will be the specified bounding volume.
         */
        
        /**
         * Returns the node's internal bounding volume.  This is the bounding volume
         * around the node alone, without including children.
         */
        """
        pass

    def getInternalVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_internal_vertices(PandaNode self, Thread current_thread)
        
        /**
         * Returns the total number of vertices that will be rendered by this
         * particular node alone, not accounting for its children.
         *
         * This may not include all vertices for certain dynamic effects.
         */
        
        /**
         * Returns the total number of vertices that will be rendered by this
         * particular node alone, not accounting for its children.
         *
         * This may not include all vertices for certain dynamic effects.
         */
        """
        pass

    def getIntoCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_into_collide_mask(PandaNode self)
        
        /**
         * Returns the "into" collide mask for this node.
         */
        """
        pass

    def getLegalCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_legal_collide_mask(PandaNode self)
        
        /**
         * Returns the subset of CollideMask bits that may be set for this particular
         * type of PandaNode.  For most nodes, this is 0; it doesn't make sense to set
         * a CollideMask for most kinds of nodes.
         *
         * For nodes that can be collided with, such as GeomNode and CollisionNode,
         * this returns all bits on.
         */
        """
        pass

    def getNestedVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_nested_vertices(PandaNode self, Thread current_thread)
        
        /**
         * Returns the total number of vertices that will be rendered by this node and
         * all of its descendents.
         *
         * This is not necessarily an accurate count of vertices that will actually be
         * rendered, since this will include all vertices of all LOD's, and it will
         * also include hidden nodes.  It may also omit or only approximate certain
         * kinds of dynamic geometry.  However, it will not include stashed nodes.
         */
        """
        pass

    def getNetCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_net_collide_mask(PandaNode self, Thread current_thread)
        
        /**
         * Returns the union of all into_collide_mask() values set at CollisionNodes
         * at this level and below.
         */
        """
        pass

    def getNetDrawControlMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_net_draw_control_mask(PandaNode self)
        
        /**
         * Returns the set of bits in get_net_draw_show_mask() that have been
         * explicitly set via adjust_draw_mask(), rather than implicitly inherited.
         *
         * A 1 bit in any position of this mask indicates that (a) this node has
         * renderable children, and (b) some child of this node has made an explicit
         * hide() or show_through() call for the corresponding bit.
         */
        """
        pass

    def getNetDrawShowMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_net_draw_show_mask(PandaNode self)
        
        /**
         * Returns the union of all draw_show_mask values--of renderable nodes only--
         * at this level and below.  If any bit in this mask is 0, there is no reason
         * to traverse below this node for a camera with the corresponding
         * camera_mask.
         *
         * The bits in this mask that do not correspond to a 1 bit in the
         * net_draw_control_mask are meaningless (and will be set to 1).  For bits
         * that *do* correspond to a 1 bit in the net_draw_control_mask, a 1 bit
         * indicates that at least one child should be visible, while a 0 bit
         * indicates that all children are hidden.
         */
        """
        pass

    def getNumChildren(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_children(PandaNode self, Thread current_thread)
        
        /**
         * Returns the number of child nodes this node has.  The order of the child
         * nodes *is* meaningful and is based on the sort number that was passed to
         * add_child(), and also on the order in which the nodes were added.
         */
        """
        pass

    def getNumParents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_parents(PandaNode self, Thread current_thread)
        
        /**
         * Returns the number of parent nodes this node has.  If this number is
         * greater than 1, the node has been multiply instanced.  The order of the
         * parent nodes is not meaningful and is not related to the order in which the
         * node was instanced to them.
         */
        """
        pass

    def getNumStashed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_stashed(PandaNode self, Thread current_thread)
        
        /**
         * Returns the number of stashed nodes this node has.  These are former
         * children of the node that have been moved to the special stashed list via
         * stash_child().
         */
        """
        pass

    def getOffClipPlanes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_off_clip_planes(PandaNode self, Thread current_thread)
        
        /**
         * Returns a ClipPlaneAttrib which represents the union of all of the clip
         * planes that have been turned *off* at this level and below.
         */
        """
        pass

    def getOverallBit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_overall_bit()
        
        /**
         * Returns the special bit that, when specifically cleared in the node's
         * DrawMask, indicates that the node is hidden to all cameras, regardless of
         * the remaining DrawMask bits.
         */
        """
        pass

    def getParent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_parent(PandaNode self, int n, Thread current_thread)
        
        /**
         * Returns the nth parent node of this node.  See get_num_parents().  Also see
         * get_parents(), if your intention is to iterate through the complete list of
         * parents; get_parents() is preferable in this case.
         */
        """
        pass

    def getParents(self, *args, **kwargs): # real signature unknown
        pass

    def getPrevTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_prev_transform(PandaNode self, Thread current_thread)
        
        /**
         * Returns the transform that has been set as this node's "previous" position.
         * See set_prev_transform().
         */
        """
        pass

    def getPythonTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_python_tag(PandaNode self, object key)
        """
        pass

    def getPythonTagKeys(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_python_tag_keys(PandaNode self)
        """
        pass

    def getPythonTags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_python_tags(const PandaNode self)
        """
        pass

    def getStashed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_stashed(PandaNode self)
        get_stashed(PandaNode self, int n, Thread current_thread)
        get_stashed(PandaNode self, Thread current_thread)
        
        /**
         * Returns the nth stashed child of this node.  See get_num_stashed().  Also
         * see get_stashed(), if your intention is to iterate through the complete
         * list of stashed children; get_stashed() is preferable in this case.
         */
        
        /**
         * Returns an object that can be used to walk through the list of children of
         * the node.  When you intend to visit multiple children, using this is
         * slightly faster than calling get_stashed() directly on the PandaNode, since
         * this object avoids reopening the PipelineCycler each time.
         *
         * This object also protects you from self-modifying loops (e.g.  adding or
         * removing children during traversal), since a virtual copy of the children
         * is made ahead of time.  The virtual copy is fast--it is a form of copy-on-
         * write, so the list is not actually copied unless it is modified during the
         * traversal.
         */
        """
        pass

    def getStashedSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_stashed_sort(PandaNode self, int n, Thread current_thread)
        
        /**
         * Returns the sort index of the nth stashed node of this node (that is, the
         * number that was passed to add_child()).  See get_num_stashed().
         */
        """
        pass

    def getState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_state(PandaNode self, Thread current_thread)
        
        /**
         * Returns the complete RenderState that will be applied to all nodes at this
         * level and below, as set on this node.  This returns only the RenderState
         * set on this particular node, and has nothing to do with state that might be
         * inherited from above.
         */
        """
        pass

    def getTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tag(PandaNode self, str key, Thread current_thread)
        
        /**
         * Retrieves the user-defined value that was previously set on this node for
         * the particular key, if any.  If no value has been previously set, returns
         * the empty string.
         */
        """
        pass

    def getTagKeys(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tag_keys(PandaNode self)
        
        /**
         * Fills the given vector up with the list of tags on this PandaNode.
         *
         * It is the user's responsibility to ensure that the keys vector is empty
         * before making this call; otherwise, the new keys will be appended to it.
         */
        """
        pass

    def getTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_transform(PandaNode self, Thread current_thread)
        
        /**
         * Returns the transform that has been set on this particular node.  This is
         * not the net transform from the root, but simply the transform on this
         * particular node.
         */
        """
        pass

    def getUnexpectedChange(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_unexpected_change(PandaNode self, int flags)
        
        /**
         * Returns nonzero if any of the bits in the input parameter are set on this
         * node, or zero if none of them are set.  More specifically, this returns the
         * particular set of bits (masked by the input parameter) that have been set
         * on this node.  See set_unexpected_change().
         *
         * Since this is a developer debugging tool only, this function always returns
         * zero in a production (NDEBUG) build.
         */
        """
        pass

    def get_all_camera_mask(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_all_camera_mask()
        
        /**
         * Returns a DrawMask that is appropriate for rendering to all cameras.
         */
        """
        pass

    def get_attrib(self, PandaNode_self, TypeHandle_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_attrib(PandaNode self, TypeHandle type)
        get_attrib(PandaNode self, int slot)
        
        /**
         * Returns the render attribute of the indicated type, if it is defined on the
         * node, or NULL if it is not.  This checks only what is set on this
         * particular node level, and has nothing to do with what render attributes
         * may be inherited from parent nodes.
         */
        
        /**
         * Returns the render attribute of the indicated type, if it is defined on the
         * node, or NULL if it is not.  This checks only what is set on this
         * particular node level, and has nothing to do with what render attributes
         * may be inherited from parent nodes.
         */
        """
        pass

    def get_bounds(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bounds(PandaNode self)
        get_bounds(PandaNode self, UpdateSeq seq, Thread current_thread)
        get_bounds(PandaNode self, Thread current_thread)
        
        /**
         * Returns the external bounding volume of this node: a bounding volume that
         * contains the user bounding volume, the internal bounding volume, and all of
         * the children's bounding volumes.
         */
        
        /**
         * This flavor of get_bounds() return the external bounding volume, and also
         * fills in seq with the bounding volume's current sequence number.  When this
         * sequence number changes, it indicates that the bounding volume might have
         * changed, e.g.  because some nested child's bounding volume has changed.
         *
         * Although this might occasionally increment without changing the bounding
         * volume, the bounding volume will never change without incrementing this
         * counter, so as long as this counter remains unchanged you can be confident
         * the bounding volume is also unchanged.
         */
        """
        pass

    def get_bounds_type(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bounds_type(PandaNode self)
        
        /**
         * Returns the bounding volume type set with set_bounds_type().
         */
        """
        pass

    def get_child(self, PandaNode_self, int_n, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_child(PandaNode self, int n, Thread current_thread)
        
        /**
         * Returns the nth child node of this node.  See get_num_children().  Also see
         * get_children(), if your intention is to iterate through the complete list
         * of children; get_children() is preferable in this case.
         */
        """
        pass

    def get_children(self, *args, **kwargs): # real signature unknown
        pass

    def get_child_sort(self, PandaNode_self, int_n, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_child_sort(PandaNode self, int n, Thread current_thread)
        
        /**
         * Returns the sort index of the nth child node of this node (that is, the
         * number that was passed to add_child()).  See get_num_children().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_draw_control_mask(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_draw_control_mask(PandaNode self)
        
        /**
         * Returns the set of bits in draw_show_mask that are considered meaningful.
         * See adjust_draw_mask().
         */
        """
        pass

    def get_draw_show_mask(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_draw_show_mask(PandaNode self)
        
        /**
         * Returns the hide/show bits of this particular node.  See
         * adjust_draw_mask().
         */
        """
        pass

    def get_effect(self, PandaNode_self, TypeHandle_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_effect(PandaNode self, TypeHandle type)
        
        /**
         * Returns the render effect of the indicated type, if it is defined on the
         * node, or NULL if it is not.
         */
        """
        pass

    def get_effects(self, PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_effects(PandaNode self, Thread current_thread)
        
        /**
         * Returns the complete RenderEffects that will be applied to this node.
         */
        """
        pass

    def get_fancy_bits(self, PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fancy_bits(PandaNode self, Thread current_thread)
        
        /**
         * Returns the union of all of the enum FancyBits values corresponding to the
         * various "fancy" attributes that are set on the node.  If this returns 0,
         * the node has nothing interesting about it.  This is intended to speed
         * traversal by quickly skipping past nodes that don't particularly affect the
         * render state.
         */
        """
        pass

    def get_internal_bounds(self, PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_internal_bounds(PandaNode self, Thread current_thread)
        
        /**
         * Returns the node's internal bounding volume.  This is the bounding volume
         * around the node alone, without including children.  If the user has called
         * set_bounds(), it will be the specified bounding volume.
         */
        
        /**
         * Returns the node's internal bounding volume.  This is the bounding volume
         * around the node alone, without including children.
         */
        """
        pass

    def get_internal_vertices(self, PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_internal_vertices(PandaNode self, Thread current_thread)
        
        /**
         * Returns the total number of vertices that will be rendered by this
         * particular node alone, not accounting for its children.
         *
         * This may not include all vertices for certain dynamic effects.
         */
        
        /**
         * Returns the total number of vertices that will be rendered by this
         * particular node alone, not accounting for its children.
         *
         * This may not include all vertices for certain dynamic effects.
         */
        """
        pass

    def get_into_collide_mask(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_into_collide_mask(PandaNode self)
        
        /**
         * Returns the "into" collide mask for this node.
         */
        """
        pass

    def get_legal_collide_mask(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_legal_collide_mask(PandaNode self)
        
        /**
         * Returns the subset of CollideMask bits that may be set for this particular
         * type of PandaNode.  For most nodes, this is 0; it doesn't make sense to set
         * a CollideMask for most kinds of nodes.
         *
         * For nodes that can be collided with, such as GeomNode and CollisionNode,
         * this returns all bits on.
         */
        """
        pass

    def get_nested_vertices(self, PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_nested_vertices(PandaNode self, Thread current_thread)
        
        /**
         * Returns the total number of vertices that will be rendered by this node and
         * all of its descendents.
         *
         * This is not necessarily an accurate count of vertices that will actually be
         * rendered, since this will include all vertices of all LOD's, and it will
         * also include hidden nodes.  It may also omit or only approximate certain
         * kinds of dynamic geometry.  However, it will not include stashed nodes.
         */
        """
        pass

    def get_net_collide_mask(self, PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_net_collide_mask(PandaNode self, Thread current_thread)
        
        /**
         * Returns the union of all into_collide_mask() values set at CollisionNodes
         * at this level and below.
         */
        """
        pass

    def get_net_draw_control_mask(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_net_draw_control_mask(PandaNode self)
        
        /**
         * Returns the set of bits in get_net_draw_show_mask() that have been
         * explicitly set via adjust_draw_mask(), rather than implicitly inherited.
         *
         * A 1 bit in any position of this mask indicates that (a) this node has
         * renderable children, and (b) some child of this node has made an explicit
         * hide() or show_through() call for the corresponding bit.
         */
        """
        pass

    def get_net_draw_show_mask(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_net_draw_show_mask(PandaNode self)
        
        /**
         * Returns the union of all draw_show_mask values--of renderable nodes only--
         * at this level and below.  If any bit in this mask is 0, there is no reason
         * to traverse below this node for a camera with the corresponding
         * camera_mask.
         *
         * The bits in this mask that do not correspond to a 1 bit in the
         * net_draw_control_mask are meaningless (and will be set to 1).  For bits
         * that *do* correspond to a 1 bit in the net_draw_control_mask, a 1 bit
         * indicates that at least one child should be visible, while a 0 bit
         * indicates that all children are hidden.
         */
        """
        pass

    def get_num_children(self, PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_children(PandaNode self, Thread current_thread)
        
        /**
         * Returns the number of child nodes this node has.  The order of the child
         * nodes *is* meaningful and is based on the sort number that was passed to
         * add_child(), and also on the order in which the nodes were added.
         */
        """
        pass

    def get_num_parents(self, PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_parents(PandaNode self, Thread current_thread)
        
        /**
         * Returns the number of parent nodes this node has.  If this number is
         * greater than 1, the node has been multiply instanced.  The order of the
         * parent nodes is not meaningful and is not related to the order in which the
         * node was instanced to them.
         */
        """
        pass

    def get_num_stashed(self, PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_stashed(PandaNode self, Thread current_thread)
        
        /**
         * Returns the number of stashed nodes this node has.  These are former
         * children of the node that have been moved to the special stashed list via
         * stash_child().
         */
        """
        pass

    def get_off_clip_planes(self, PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_off_clip_planes(PandaNode self, Thread current_thread)
        
        /**
         * Returns a ClipPlaneAttrib which represents the union of all of the clip
         * planes that have been turned *off* at this level and below.
         */
        """
        pass

    def get_overall_bit(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_overall_bit()
        
        /**
         * Returns the special bit that, when specifically cleared in the node's
         * DrawMask, indicates that the node is hidden to all cameras, regardless of
         * the remaining DrawMask bits.
         */
        """
        pass

    def get_parent(self, PandaNode_self, int_n, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_parent(PandaNode self, int n, Thread current_thread)
        
        /**
         * Returns the nth parent node of this node.  See get_num_parents().  Also see
         * get_parents(), if your intention is to iterate through the complete list of
         * parents; get_parents() is preferable in this case.
         */
        """
        pass

    def get_parents(self, *args, **kwargs): # real signature unknown
        pass

    def get_prev_transform(self, PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_prev_transform(PandaNode self, Thread current_thread)
        
        /**
         * Returns the transform that has been set as this node's "previous" position.
         * See set_prev_transform().
         */
        """
        pass

    def get_python_tag(self, PandaNode_self, object_key): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_python_tag(PandaNode self, object key)
        """
        pass

    def get_python_tags(self, const_PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_python_tags(const PandaNode self)
        """
        pass

    def get_python_tag_keys(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_python_tag_keys(PandaNode self)
        """
        pass

    def get_stashed(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_stashed(PandaNode self)
        get_stashed(PandaNode self, int n, Thread current_thread)
        get_stashed(PandaNode self, Thread current_thread)
        
        /**
         * Returns the nth stashed child of this node.  See get_num_stashed().  Also
         * see get_stashed(), if your intention is to iterate through the complete
         * list of stashed children; get_stashed() is preferable in this case.
         */
        
        /**
         * Returns an object that can be used to walk through the list of children of
         * the node.  When you intend to visit multiple children, using this is
         * slightly faster than calling get_stashed() directly on the PandaNode, since
         * this object avoids reopening the PipelineCycler each time.
         *
         * This object also protects you from self-modifying loops (e.g.  adding or
         * removing children during traversal), since a virtual copy of the children
         * is made ahead of time.  The virtual copy is fast--it is a form of copy-on-
         * write, so the list is not actually copied unless it is modified during the
         * traversal.
         */
        """
        pass

    def get_stashed_sort(self, PandaNode_self, int_n, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_stashed_sort(PandaNode self, int n, Thread current_thread)
        
        /**
         * Returns the sort index of the nth stashed node of this node (that is, the
         * number that was passed to add_child()).  See get_num_stashed().
         */
        """
        pass

    def get_state(self, PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_state(PandaNode self, Thread current_thread)
        
        /**
         * Returns the complete RenderState that will be applied to all nodes at this
         * level and below, as set on this node.  This returns only the RenderState
         * set on this particular node, and has nothing to do with state that might be
         * inherited from above.
         */
        """
        pass

    def get_tag(self, PandaNode_self, str_key, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tag(PandaNode self, str key, Thread current_thread)
        
        /**
         * Retrieves the user-defined value that was previously set on this node for
         * the particular key, if any.  If no value has been previously set, returns
         * the empty string.
         */
        """
        pass

    def get_tag_keys(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tag_keys(PandaNode self)
        
        /**
         * Fills the given vector up with the list of tags on this PandaNode.
         *
         * It is the user's responsibility to ensure that the keys vector is empty
         * before making this call; otherwise, the new keys will be appended to it.
         */
        """
        pass

    def get_transform(self, PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_transform(PandaNode self, Thread current_thread)
        
        /**
         * Returns the transform that has been set on this particular node.  This is
         * not the net transform from the root, but simply the transform on this
         * particular node.
         */
        """
        pass

    def get_unexpected_change(self, PandaNode_self, int_flags): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_unexpected_change(PandaNode self, int flags)
        
        /**
         * Returns nonzero if any of the bits in the input parameter are set on this
         * node, or zero if none of them are set.  More specifically, this returns the
         * particular set of bits (masked by the input parameter) that have been set
         * on this node.  See set_unexpected_change().
         *
         * Since this is a developer debugging tool only, this function always returns
         * zero in a production (NDEBUG) build.
         */
        """
        pass

    def hasAttrib(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_attrib(PandaNode self, TypeHandle type)
        has_attrib(PandaNode self, int slot)
        
        /**
         * Returns true if there is a render attribute of the indicated type defined
         * on this node, or false if there is not.
         */
        
        /**
         * Returns true if there is a render attribute of the indicated type defined
         * on this node, or false if there is not.
         */
        """
        pass

    def hasDirtyPrevTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_dirty_prev_transform(PandaNode self)
        
        /**
         * Returns true if this node has the _dirty_prev_transform flag set, which
         * indicates its _prev_transform is different from its _transform value (in
         * pipeline stage 0).  In this case, the node will be visited by
         * reset_prev_transform().
         */
        """
        pass

    def hasEffect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_effect(PandaNode self, TypeHandle type)
        
        /**
         * Returns true if there is a render effect of the indicated type defined on
         * this node, or false if there is not.
         */
        """
        pass

    def hasPythonTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_python_tag(PandaNode self, object key)
        """
        pass

    def hasTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_tag(PandaNode self, str key, Thread current_thread)
        
        /**
         * Returns true if a value has been defined on this node for the particular
         * key (even if that value is the empty string), or false if no value has been
         * set.
         */
        """
        pass

    def hasTags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_tags(PandaNode self)
        
        /**
         * Returns true if the node has any tags (or any Python tags) at all, false if
         * it has none.
         */
        """
        pass

    def has_attrib(self, PandaNode_self, TypeHandle_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_attrib(PandaNode self, TypeHandle type)
        has_attrib(PandaNode self, int slot)
        
        /**
         * Returns true if there is a render attribute of the indicated type defined
         * on this node, or false if there is not.
         */
        
        /**
         * Returns true if there is a render attribute of the indicated type defined
         * on this node, or false if there is not.
         */
        """
        pass

    def has_dirty_prev_transform(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_dirty_prev_transform(PandaNode self)
        
        /**
         * Returns true if this node has the _dirty_prev_transform flag set, which
         * indicates its _prev_transform is different from its _transform value (in
         * pipeline stage 0).  In this case, the node will be visited by
         * reset_prev_transform().
         */
        """
        pass

    def has_effect(self, PandaNode_self, TypeHandle_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_effect(PandaNode self, TypeHandle type)
        
        /**
         * Returns true if there is a render effect of the indicated type defined on
         * this node, or false if there is not.
         */
        """
        pass

    def has_python_tag(self, PandaNode_self, object_key): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_python_tag(PandaNode self, object key)
        """
        pass

    def has_tag(self, PandaNode_self, str_key, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_tag(PandaNode self, str key, Thread current_thread)
        
        /**
         * Returns true if a value has been defined on this node for the particular
         * key (even if that value is the empty string), or false if no value has been
         * set.
         */
        """
        pass

    def has_tags(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_tags(PandaNode self)
        
        /**
         * Returns true if the node has any tags (or any Python tags) at all, false if
         * it has none.
         */
        """
        pass

    def isAmbientLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_ambient_light(PandaNode self)
        
        /**
         * Returns true if this is an AmbientLight, false if it is not a light, or it
         * is some other kind of light.
         */
        """
        pass

    def isBoundsStale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_bounds_stale(PandaNode self)
        
        /**
         * Returns true if the bounding volume of this node is stale and will be
         * implicitly recomputed at the next call to get_bounds(), or false if it is
         * fresh and need not be recomputed.
         */
        """
        pass

    def isCollisionNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_collision_node(PandaNode self)
        
        /**
         * A simple downcast check.  Returns true if this kind of node happens to
         * inherit from CollisionNode, false otherwise.
         *
         * This is provided as a a faster alternative to calling
         * is_of_type(CollisionNode::get_class_type()).
         */
        """
        pass

    def isFinal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_final(PandaNode self, Thread current_thread)
        
        /**
         * Returns the current state of the "final" flag.  Initially, this flag is off
         * (false), but it may be changed by an explicit call to set_final().  See
         * set_final().
         */
        """
        pass

    def isGeomNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_geom_node(PandaNode self)
        
        /**
         * A simple downcast check.  Returns true if this kind of node happens to
         * inherit from GeomNode, false otherwise.
         *
         * This is provided as a a faster alternative to calling
         * is_of_type(GeomNode::get_class_type()), since this test is so important to
         * rendering.
         */
        """
        pass

    def isLodNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_lod_node(PandaNode self)
        
        /**
         * A simple downcast check.  Returns true if this kind of node happens to
         * inherit from LODNode, false otherwise.
         *
         * This is provided as a a faster alternative to calling
         * is_of_type(LODNode::get_class_type()).
         */
        """
        pass

    def isOverallHidden(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_overall_hidden(PandaNode self)
        
        /**
         * Returns true if the node has been hidden to all cameras by clearing its
         * overall bit.
         */
        """
        pass

    def isSceneRoot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_scene_root(PandaNode self)
        
        /**
         * Returns true if this particular node is known to be the render root of some
         * active DisplayRegion associated with the global GraphicsEngine, false
         * otherwise.
         */
        """
        pass

    def isUnderSceneRoot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_under_scene_root(PandaNode self)
        
        /**
         * Returns true if this particular node is in a live scene graph: that is, it
         * is a child or descendent of a node that is itself a scene root.  If this is
         * true, this node may potentially be traversed by the render traverser.
         * Stashed nodes don't count for this purpose, but hidden nodes do.
         */
        """
        pass

    def is_ambient_light(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_ambient_light(PandaNode self)
        
        /**
         * Returns true if this is an AmbientLight, false if it is not a light, or it
         * is some other kind of light.
         */
        """
        pass

    def is_bounds_stale(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_bounds_stale(PandaNode self)
        
        /**
         * Returns true if the bounding volume of this node is stale and will be
         * implicitly recomputed at the next call to get_bounds(), or false if it is
         * fresh and need not be recomputed.
         */
        """
        pass

    def is_collision_node(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_collision_node(PandaNode self)
        
        /**
         * A simple downcast check.  Returns true if this kind of node happens to
         * inherit from CollisionNode, false otherwise.
         *
         * This is provided as a a faster alternative to calling
         * is_of_type(CollisionNode::get_class_type()).
         */
        """
        pass

    def is_final(self, PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_final(PandaNode self, Thread current_thread)
        
        /**
         * Returns the current state of the "final" flag.  Initially, this flag is off
         * (false), but it may be changed by an explicit call to set_final().  See
         * set_final().
         */
        """
        pass

    def is_geom_node(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_geom_node(PandaNode self)
        
        /**
         * A simple downcast check.  Returns true if this kind of node happens to
         * inherit from GeomNode, false otherwise.
         *
         * This is provided as a a faster alternative to calling
         * is_of_type(GeomNode::get_class_type()), since this test is so important to
         * rendering.
         */
        """
        pass

    def is_lod_node(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_lod_node(PandaNode self)
        
        /**
         * A simple downcast check.  Returns true if this kind of node happens to
         * inherit from LODNode, false otherwise.
         *
         * This is provided as a a faster alternative to calling
         * is_of_type(LODNode::get_class_type()).
         */
        """
        pass

    def is_overall_hidden(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_overall_hidden(PandaNode self)
        
        /**
         * Returns true if the node has been hidden to all cameras by clearing its
         * overall bit.
         */
        """
        pass

    def is_scene_root(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_scene_root(PandaNode self)
        
        /**
         * Returns true if this particular node is known to be the render root of some
         * active DisplayRegion associated with the global GraphicsEngine, false
         * otherwise.
         */
        """
        pass

    def is_under_scene_root(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_under_scene_root(PandaNode self)
        
        /**
         * Returns true if this particular node is in a live scene graph: that is, it
         * is a child or descendent of a node that is itself a scene root.  If this is
         * true, this node may potentially be traversed by the render traverser.
         * Stashed nodes don't count for this purpose, but hidden nodes do.
         */
        """
        pass

    def listTags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        list_tags(PandaNode self, ostream out, str separator)
        
        /**
         * Writes a list of all the tag keys assigned to the node to the indicated
         * stream.  Writes one instance of the separator following each key (but does
         * not write a terminal separator).  The value associated with each key is not
         * written.
         *
         * This is mainly for the benefit of the realtime user, to see the list of all
         * of the associated tag keys.
         */
        """
        pass

    def list_tags(self, PandaNode_self, ostream_out, str_separator): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        list_tags(PandaNode self, ostream out, str separator)
        
        /**
         * Writes a list of all the tag keys assigned to the node to the indicated
         * stream.  Writes one instance of the separator following each key (but does
         * not write a terminal separator).  The value associated with each key is not
         * written.
         *
         * This is mainly for the benefit of the realtime user, to see the list of all
         * of the associated tag keys.
         */
        """
        pass

    def ls(self, PandaNode_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ls(PandaNode self, ostream out, int indent_level)
        
        /**
         * Lists all the nodes at and below the current path hierarchically.
         */
        """
        pass

    def makeCopy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_copy(PandaNode self)
        
        /**
         * Returns a newly-allocated PandaNode that is a shallow copy of this one.  It
         * will be a different pointer, but its internal data may or may not be shared
         * with that of the original PandaNode.  No children will be copied.
         */
        """
        pass

    def make_copy(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_copy(PandaNode self)
        
        /**
         * Returns a newly-allocated PandaNode that is a shallow copy of this one.  It
         * will be a different pointer, but its internal data may or may not be shared
         * with that of the original PandaNode.  No children will be copied.
         */
        """
        pass

    def markBoundsStale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        mark_bounds_stale(PandaNode self, Thread current_thread)
        
        /**
         * Indicates that the bounding volume, or something that influences the
         * bounding volume (or any of the other things stored in CData, like
         * net_collide_mask), may have changed for this node, and that it must be
         * recomputed.
         */
        
        /**
         * Indicates that the bounding volume, or something that influences the
         * bounding volume (or any of the other things stored in CData, like
         * net_collide_mask), may have changed for this node, and that it must be
         * recomputed.
         *
         * With no parameters, this means to iterate through all stages including and
         * upstream of the current pipeline stage.
         *
         * This method is intended for internal use; usually it is not necessary for a
         * user to call this directly.  It will be called automatically by derived
         * classes when appropriate.
         */
        """
        pass

    def markInternalBoundsStale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        mark_internal_bounds_stale(const PandaNode self, Thread current_thread)
        
        /**
         * Should be called by a derived class to mark the internal bounding volume
         * stale, so that recompute_internal_bounds() will be called when the bounding
         * volume is next requested.
         */
        
        /**
         * Should be called by a derived class to mark the internal bounding volume
         * stale, so that compute_internal_bounds() will be called when the bounding
         * volume is next requested.
         *
         * With no parameters, this means to iterate through all stages including and
         * upstream of the current pipeline stage.
         *
         * It is normally not necessary to call this method directly; each node should
         * be responsible for calling it when its internals have changed.
         */
        """
        pass

    def mark_bounds_stale(self, PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        mark_bounds_stale(PandaNode self, Thread current_thread)
        
        /**
         * Indicates that the bounding volume, or something that influences the
         * bounding volume (or any of the other things stored in CData, like
         * net_collide_mask), may have changed for this node, and that it must be
         * recomputed.
         */
        
        /**
         * Indicates that the bounding volume, or something that influences the
         * bounding volume (or any of the other things stored in CData, like
         * net_collide_mask), may have changed for this node, and that it must be
         * recomputed.
         *
         * With no parameters, this means to iterate through all stages including and
         * upstream of the current pipeline stage.
         *
         * This method is intended for internal use; usually it is not necessary for a
         * user to call this directly.  It will be called automatically by derived
         * classes when appropriate.
         */
        """
        pass

    def mark_internal_bounds_stale(self, const_PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        mark_internal_bounds_stale(const PandaNode self, Thread current_thread)
        
        /**
         * Should be called by a derived class to mark the internal bounding volume
         * stale, so that recompute_internal_bounds() will be called when the bounding
         * volume is next requested.
         */
        
        /**
         * Should be called by a derived class to mark the internal bounding volume
         * stale, so that compute_internal_bounds() will be called when the bounding
         * volume is next requested.
         *
         * With no parameters, this means to iterate through all stages including and
         * upstream of the current pipeline stage.
         *
         * It is normally not necessary to call this method directly; each node should
         * be responsible for calling it when its internals have changed.
         */
        """
        pass

    def output(self, PandaNode_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(PandaNode self, ostream out)
        
        /**
         *
         */
        """
        pass

    def prepareScene(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        prepare_scene(const PandaNode self, GraphicsStateGuardianBase gsg, const RenderState node_state)
        
        /**
         * Walks through the scene graph beginning at this node, and does whatever
         * initialization is required to render the scene properly with the indicated
         * GSG.  It is not strictly necessary to call this, since the GSG will
         * initialize itself when the scene is rendered, but this may take some of the
         * overhead away from that process.
         *
         * In particular, this will ensure that textures and vertex buffers within the
         * scene are loaded into graphics memory.
         */
        """
        pass

    def prepare_scene(self, const_PandaNode_self, GraphicsStateGuardianBase_gsg, const_RenderState_node_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare_scene(const PandaNode self, GraphicsStateGuardianBase gsg, const RenderState node_state)
        
        /**
         * Walks through the scene graph beginning at this node, and does whatever
         * initialization is required to render the scene properly with the indicated
         * GSG.  It is not strictly necessary to call this, since the GSG will
         * initialize itself when the scene is rendered, but this may take some of the
         * overhead away from that process.
         *
         * In particular, this will ensure that textures and vertex buffers within the
         * scene are loaded into graphics memory.
         */
        """
        pass

    def removeAllChildren(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_all_children(const PandaNode self, Thread current_thread)
        
        /**
         * Removes all the children from the node at once, including stashed children.
         *
         * This can only be called from the top pipeline stage (i.e.  from App).
         */
        """
        pass

    def removeChild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_child(const PandaNode self, PandaNode child_node, Thread current_thread)
        remove_child(const PandaNode self, int child_index, Thread current_thread)
        
        /**
         * Removes the nth child from the node.
         */
        
        /**
         * Removes the indicated child from the node.  Returns true if the child was
         * removed, false if it was not already a child of the node.  This will also
         * successfully remove the child if it had been stashed.
         */
        """
        pass

    def removeStashed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_stashed(const PandaNode self, int child_index, Thread current_thread)
        
        /**
         * Removes the nth stashed child from the node.
         */
        """
        pass

    def remove_all_children(self, const_PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_all_children(const PandaNode self, Thread current_thread)
        
        /**
         * Removes all the children from the node at once, including stashed children.
         *
         * This can only be called from the top pipeline stage (i.e.  from App).
         */
        """
        pass

    def remove_child(self, const_PandaNode_self, PandaNode_child_node, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_child(const PandaNode self, PandaNode child_node, Thread current_thread)
        remove_child(const PandaNode self, int child_index, Thread current_thread)
        
        /**
         * Removes the nth child from the node.
         */
        
        /**
         * Removes the indicated child from the node.  Returns true if the child was
         * removed, false if it was not already a child of the node.  This will also
         * successfully remove the child if it had been stashed.
         */
        """
        pass

    def remove_stashed(self, const_PandaNode_self, int_child_index, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_stashed(const PandaNode self, int child_index, Thread current_thread)
        
        /**
         * Removes the nth stashed child from the node.
         */
        """
        pass

    def replaceChild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        replace_child(const PandaNode self, PandaNode orig_child, PandaNode new_child, Thread current_thread)
        
        /**
         * Searches for the orig_child node in the node's list of children, and
         * replaces it with the new_child instead.  Returns true if the replacement is
         * made, or false if the node is not a child or if there is some other
         * problem.
         */
        """
        pass

    def replaceNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        replace_node(const PandaNode self, PandaNode other)
        
        /**
         * Inserts this node into the scene graph in place of the other one, and
         * removes the other node.  All scene graph attributes (TransformState,
         * RenderState, etc.) are copied to this node.
         *
         * All children are moved to this node, and removed from the old node.  The
         * new node is left in the same place in the old node's parent's list of
         * children.
         *
         * Even NodePaths that reference the old node are updated in-place to
         * reference the new node instead.
         *
         * This method is intended to be used to replace a node of a given type in the
         * scene graph with a node of a different type.
         */
        """
        pass

    def replace_child(self, const_PandaNode_self, PandaNode_orig_child, PandaNode_new_child, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        replace_child(const PandaNode self, PandaNode orig_child, PandaNode new_child, Thread current_thread)
        
        /**
         * Searches for the orig_child node in the node's list of children, and
         * replaces it with the new_child instead.  Returns true if the replacement is
         * made, or false if the node is not a child or if there is some other
         * problem.
         */
        """
        pass

    def replace_node(self, const_PandaNode_self, PandaNode_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        replace_node(const PandaNode self, PandaNode other)
        
        /**
         * Inserts this node into the scene graph in place of the other one, and
         * removes the other node.  All scene graph attributes (TransformState,
         * RenderState, etc.) are copied to this node.
         *
         * All children are moved to this node, and removed from the old node.  The
         * new node is left in the same place in the old node's parent's list of
         * children.
         *
         * Even NodePaths that reference the old node are updated in-place to
         * reference the new node instead.
         *
         * This method is intended to be used to replace a node of a given type in the
         * scene graph with a node of a different type.
         */
        """
        pass

    def resetAllPrevTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reset_all_prev_transform(Thread current_thread)
        
        /**
         * Visits all nodes in the world with the _dirty_prev_transform flag--that is,
         * all nodes whose _prev_transform is different from the _transform in
         * pipeline stage 0--and resets the _prev_transform to be the same as
         * _transform.
         */
        """
        pass

    def resetPrevTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reset_prev_transform(const PandaNode self, Thread current_thread)
        
        /**
         * Resets the transform that represents this node's "previous" position to the
         * same as the current transform.  This is not the same thing as clearing it
         * to identity.
         */
        """
        pass

    def reset_all_prev_transform(self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset_all_prev_transform(Thread current_thread)
        
        /**
         * Visits all nodes in the world with the _dirty_prev_transform flag--that is,
         * all nodes whose _prev_transform is different from the _transform in
         * pipeline stage 0--and resets the _prev_transform to be the same as
         * _transform.
         */
        """
        pass

    def reset_prev_transform(self, const_PandaNode_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset_prev_transform(const PandaNode self, Thread current_thread)
        
        /**
         * Resets the transform that represents this node's "previous" position to the
         * same as the current transform.  This is not the same thing as clearing it
         * to identity.
         */
        """
        pass

    def setAttrib(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_attrib(const PandaNode self, const RenderAttrib attrib, int override)
        
        /**
         * Adds the indicated render attribute to the scene graph on this node.  This
         * attribute will now apply to this node and everything below.  If there was
         * already an attribute of the same type, it is replaced.
         */
        """
        pass

    def setBound(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bound(const PandaNode self, const BoundingVolume volume)
        
        /**
         * @deprecated Use set_bounds() instead.
         */
        """
        pass

    def setBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bounds(const PandaNode self, const BoundingVolume volume)
        
        /**
         * Resets the bounding volume so that it is the indicated volume.  When it is
         * explicitly set, the bounding volume will no longer be automatically
         * computed according to the contents of the node itself, for nodes like
         * GeomNodes and TextNodes that contain substance (but the bounding volume
         * will still be automatically expanded to include its children).
         *
         * Call clear_bounds() if you would like to return the bounding volume to its
         * default behavior later.
         */
        """
        pass

    def setBoundsType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bounds_type(const PandaNode self, int bounds_type)
        
        // We define set_bounds() and get_bounds() functions so that set_bounds()
        // sets the user bounding volume, while get_bounds() returns the external
        // bounding volume.  Although it might seem strange and confusing to do
        // this, this is actually the natural way the user thinks about nodes and
        // bounding volumes.
        
        // We define set_bounds() and get_bounds() functions so that set_bounds()
        // sets the user bounding volume, while get_bounds() returns the external
        // bounding volume.  Although it might seem strange and confusing to do
        // this, this is actually the natural way the user thinks about nodes and
        // bounding volumes.
        
        /**
         * Specifies the desired type of bounding volume that will be created for this
         * node.  This is normally BoundingVolume::BT_default, which means to set the
         * type according to the config variable "bounds-type".
         *
         * If this is BT_sphere or BT_box, a BoundingSphere or BoundingBox is
         * explicitly created.  If it is BT_best, the appropriate type to best enclose
         * the node's children is created.
         *
         * This affects the bounding volume returned by get_bounds(), which is not
         * exactly the same bounding volume modified by set_bounds(), because a new
         * bounding volume has to be created that includes this node and all of its
         * children.
         */
        """
        pass

    def setEffect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_effect(const PandaNode self, const RenderEffect effect)
        
        /**
         * Adds the indicated render effect to the scene graph on this node.  If there
         * was already an effect of the same type, it is replaced.
         */
        """
        pass

    def setEffects(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_effects(const PandaNode self, const RenderEffects effects, Thread current_thread)
        
        /**
         * Sets the complete RenderEffects that will be applied this node.  This
         * completely replaces whatever has been set on this node via repeated calls
         * to set_attrib().
         */
        """
        pass

    def setFinal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_final(const PandaNode self, bool flag)
        
        /**
         * Sets the "final" flag on this PandaNode.  If this is true, than no bounding
         * volume need be tested below it; a positive intersection with this node's
         * bounding volume is deemed to be a positive intersection with all geometry
         * inside.
         *
         * This is useful to quickly force a larger bounding volume around a node when
         * the GeomNodes themselves are inaccurate for some reason, without forcing a
         * recompute of every nested bounding volume.  It's also helpful when the
         * bounding volume is tricked by some special properties, like billboards,
         * that may move geometry out of its bounding volume otherwise.
         */
        """
        pass

    def setIntoCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_into_collide_mask(const PandaNode self, BitMask mask)
        
        /**
         * Sets the "into" CollideMask.
         *
         * This specifies the set of bits that must be shared with a CollisionNode's
         * "from" CollideMask in order for the CollisionNode to detect a collision
         * with this particular node.
         *
         * The actual CollideMask that will be set is masked by the return value from
         * get_legal_collide_mask(). Thus, the into_collide_mask cannot be set to
         * anything other than nonzero except for those types of nodes that can be
         * collided into, such as CollisionNodes and GeomNodes.
         */
        """
        pass

    def setOverallHidden(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_overall_hidden(const PandaNode self, bool overall_hidden)
        
        /**
         * Sets or clears the hidden flag.  When the hidden flag is true, the node and
         * all of its children are invisible to all cameras, regardless of the setting
         * of any draw masks.  Setting the hidden flag to false restores the previous
         * visibility as established by the draw masks.
         *
         * This actually works by twiddling the reserved _overall_bit in the node's
         * draw mask, which has special meaning.
         */
        """
        pass

    def setPrevTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_prev_transform(const PandaNode self, const TransformState transform, Thread current_thread)
        
        /**
         * Sets the transform that represents this node's "previous" position, one
         * frame ago, for the purposes of detecting motion for accurate collision
         * calculations.
         */
        """
        pass

    def setPythonTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_python_tag(const PandaNode self, object key, object value)
        """
        pass

    def setState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_state(const PandaNode self, const RenderState state, Thread current_thread)
        
        /**
         * Sets the complete RenderState that will be applied to all nodes at this
         * level and below.  (The actual state that will be applied to lower nodes is
         * based on the composition of RenderStates from above this node as well).
         * This completely replaces whatever has been set on this node via repeated
         * calls to set_attrib().
         */
        """
        pass

    def setTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tag(const PandaNode self, str key, str value, Thread current_thread)
        
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

    def setTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_transform(const PandaNode self, const TransformState transform, Thread current_thread)
        
        /**
         * Sets the transform that will be applied to this node and below.  This
         * defines a new coordinate space at this point in the scene graph and below.
         */
        """
        pass

    def setUnexpectedChange(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_unexpected_change(const PandaNode self, int flags)
        
        /**
         * Sets one or more of the PandaNode::UnexpectedChange bits on, indicating
         * that the corresponding property should not change again on this node.  Once
         * one of these bits has been set, if the property changes, an assertion
         * failure will be raised, which is designed to assist the developer in
         * identifying the troublesome code that modified the property unexpectedly.
         *
         * The input parameter is the union of bits that are to be set.  To clear
         * these bits later, use clear_unexpected_change().
         *
         * Since this is a developer debugging tool only, this function does nothing
         * in a production (NDEBUG) build.
         */
        """
        pass

    def set_attrib(self, const_PandaNode_self, const_RenderAttrib_attrib, int_override): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_attrib(const PandaNode self, const RenderAttrib attrib, int override)
        
        /**
         * Adds the indicated render attribute to the scene graph on this node.  This
         * attribute will now apply to this node and everything below.  If there was
         * already an attribute of the same type, it is replaced.
         */
        """
        pass

    def set_bound(self, const_PandaNode_self, const_BoundingVolume_volume): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bound(const PandaNode self, const BoundingVolume volume)
        
        /**
         * @deprecated Use set_bounds() instead.
         */
        """
        pass

    def set_bounds(self, const_PandaNode_self, const_BoundingVolume_volume): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bounds(const PandaNode self, const BoundingVolume volume)
        
        /**
         * Resets the bounding volume so that it is the indicated volume.  When it is
         * explicitly set, the bounding volume will no longer be automatically
         * computed according to the contents of the node itself, for nodes like
         * GeomNodes and TextNodes that contain substance (but the bounding volume
         * will still be automatically expanded to include its children).
         *
         * Call clear_bounds() if you would like to return the bounding volume to its
         * default behavior later.
         */
        """
        pass

    def set_bounds_type(self, const_PandaNode_self, int_bounds_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bounds_type(const PandaNode self, int bounds_type)
        
        // We define set_bounds() and get_bounds() functions so that set_bounds()
        // sets the user bounding volume, while get_bounds() returns the external
        // bounding volume.  Although it might seem strange and confusing to do
        // this, this is actually the natural way the user thinks about nodes and
        // bounding volumes.
        
        // We define set_bounds() and get_bounds() functions so that set_bounds()
        // sets the user bounding volume, while get_bounds() returns the external
        // bounding volume.  Although it might seem strange and confusing to do
        // this, this is actually the natural way the user thinks about nodes and
        // bounding volumes.
        
        /**
         * Specifies the desired type of bounding volume that will be created for this
         * node.  This is normally BoundingVolume::BT_default, which means to set the
         * type according to the config variable "bounds-type".
         *
         * If this is BT_sphere or BT_box, a BoundingSphere or BoundingBox is
         * explicitly created.  If it is BT_best, the appropriate type to best enclose
         * the node's children is created.
         *
         * This affects the bounding volume returned by get_bounds(), which is not
         * exactly the same bounding volume modified by set_bounds(), because a new
         * bounding volume has to be created that includes this node and all of its
         * children.
         */
        """
        pass

    def set_effect(self, const_PandaNode_self, const_RenderEffect_effect): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_effect(const PandaNode self, const RenderEffect effect)
        
        /**
         * Adds the indicated render effect to the scene graph on this node.  If there
         * was already an effect of the same type, it is replaced.
         */
        """
        pass

    def set_effects(self, const_PandaNode_self, const_RenderEffects_effects, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_effects(const PandaNode self, const RenderEffects effects, Thread current_thread)
        
        /**
         * Sets the complete RenderEffects that will be applied this node.  This
         * completely replaces whatever has been set on this node via repeated calls
         * to set_attrib().
         */
        """
        pass

    def set_final(self, const_PandaNode_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_final(const PandaNode self, bool flag)
        
        /**
         * Sets the "final" flag on this PandaNode.  If this is true, than no bounding
         * volume need be tested below it; a positive intersection with this node's
         * bounding volume is deemed to be a positive intersection with all geometry
         * inside.
         *
         * This is useful to quickly force a larger bounding volume around a node when
         * the GeomNodes themselves are inaccurate for some reason, without forcing a
         * recompute of every nested bounding volume.  It's also helpful when the
         * bounding volume is tricked by some special properties, like billboards,
         * that may move geometry out of its bounding volume otherwise.
         */
        """
        pass

    def set_into_collide_mask(self, const_PandaNode_self, BitMask_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_into_collide_mask(const PandaNode self, BitMask mask)
        
        /**
         * Sets the "into" CollideMask.
         *
         * This specifies the set of bits that must be shared with a CollisionNode's
         * "from" CollideMask in order for the CollisionNode to detect a collision
         * with this particular node.
         *
         * The actual CollideMask that will be set is masked by the return value from
         * get_legal_collide_mask(). Thus, the into_collide_mask cannot be set to
         * anything other than nonzero except for those types of nodes that can be
         * collided into, such as CollisionNodes and GeomNodes.
         */
        """
        pass

    def set_overall_hidden(self, const_PandaNode_self, bool_overall_hidden): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_overall_hidden(const PandaNode self, bool overall_hidden)
        
        /**
         * Sets or clears the hidden flag.  When the hidden flag is true, the node and
         * all of its children are invisible to all cameras, regardless of the setting
         * of any draw masks.  Setting the hidden flag to false restores the previous
         * visibility as established by the draw masks.
         *
         * This actually works by twiddling the reserved _overall_bit in the node's
         * draw mask, which has special meaning.
         */
        """
        pass

    def set_prev_transform(self, const_PandaNode_self, const_TransformState_transform, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_prev_transform(const PandaNode self, const TransformState transform, Thread current_thread)
        
        /**
         * Sets the transform that represents this node's "previous" position, one
         * frame ago, for the purposes of detecting motion for accurate collision
         * calculations.
         */
        """
        pass

    def set_python_tag(self, const_PandaNode_self, object_key, object_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_python_tag(const PandaNode self, object key, object value)
        """
        pass

    def set_state(self, const_PandaNode_self, const_RenderState_state, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_state(const PandaNode self, const RenderState state, Thread current_thread)
        
        /**
         * Sets the complete RenderState that will be applied to all nodes at this
         * level and below.  (The actual state that will be applied to lower nodes is
         * based on the composition of RenderStates from above this node as well).
         * This completely replaces whatever has been set on this node via repeated
         * calls to set_attrib().
         */
        """
        pass

    def set_tag(self, const_PandaNode_self, str_key, str_value, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tag(const PandaNode self, str key, str value, Thread current_thread)
        
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

    def set_transform(self, const_PandaNode_self, const_TransformState_transform, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_transform(const PandaNode self, const TransformState transform, Thread current_thread)
        
        /**
         * Sets the transform that will be applied to this node and below.  This
         * defines a new coordinate space at this point in the scene graph and below.
         */
        """
        pass

    def set_unexpected_change(self, const_PandaNode_self, int_flags): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_unexpected_change(const PandaNode self, int flags)
        
        /**
         * Sets one or more of the PandaNode::UnexpectedChange bits on, indicating
         * that the corresponding property should not change again on this node.  Once
         * one of these bits has been set, if the property changes, an assertion
         * failure will be raised, which is designed to assist the developer in
         * identifying the troublesome code that modified the property unexpectedly.
         *
         * The input parameter is the union of bits that are to be set.  To clear
         * these bits later, use clear_unexpected_change().
         *
         * Since this is a developer debugging tool only, this function does nothing
         * in a production (NDEBUG) build.
         */
        """
        pass

    def stashChild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        stash_child(const PandaNode self, PandaNode child_node, Thread current_thread)
        stash_child(const PandaNode self, int child_index, Thread current_thread)
        
        /**
         * Stashes the indicated child node.  This removes the child from the list of
         * active children and puts it on a special list of stashed children.  This
         * child node no longer contributes to the bounding volume of the PandaNode,
         * and is not visited in normal traversals.  It is invisible and uncollidable.
         * The child may later be restored by calling unstash_child().
         *
         * This function returns true if the child node was successfully stashed, or
         * false if it was not a child of the node in the first place (e.g.  it was
         * previously stashed).
         */
        
        /**
         * Stashes the indicated child node.  This removes the child from the list of
         * active children and puts it on a special list of stashed children.  This
         * child node no longer contributes to the bounding volume of the PandaNode,
         * and is not visited in normal traversals.  It is invisible and uncollidable.
         * The child may later be restored by calling unstash_child().
         *
         * This can only be called from the top pipeline stage (i.e.  from App).
         */
        """
        pass

    def stash_child(self, const_PandaNode_self, PandaNode_child_node, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        stash_child(const PandaNode self, PandaNode child_node, Thread current_thread)
        stash_child(const PandaNode self, int child_index, Thread current_thread)
        
        /**
         * Stashes the indicated child node.  This removes the child from the list of
         * active children and puts it on a special list of stashed children.  This
         * child node no longer contributes to the bounding volume of the PandaNode,
         * and is not visited in normal traversals.  It is invisible and uncollidable.
         * The child may later be restored by calling unstash_child().
         *
         * This function returns true if the child node was successfully stashed, or
         * false if it was not a child of the node in the first place (e.g.  it was
         * previously stashed).
         */
        
        /**
         * Stashes the indicated child node.  This removes the child from the list of
         * active children and puts it on a special list of stashed children.  This
         * child node no longer contributes to the bounding volume of the PandaNode,
         * and is not visited in normal traversals.  It is invisible and uncollidable.
         * The child may later be restored by calling unstash_child().
         *
         * This can only be called from the top pipeline stage (i.e.  from App).
         */
        """
        pass

    def stealChildren(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        steal_children(const PandaNode self, PandaNode other, Thread current_thread)
        
        /**
         * Moves all the children from the other node onto this node.
         *
         * Any NodePaths to child nodes of the other node are truncated, rather than
         * moved to the new parent.
         */
        """
        pass

    def steal_children(self, const_PandaNode_self, PandaNode_other, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        steal_children(const PandaNode self, PandaNode other, Thread current_thread)
        
        /**
         * Moves all the children from the other node onto this node.
         *
         * Any NodePaths to child nodes of the other node are truncated, rather than
         * moved to the new parent.
         */
        """
        pass

    def unstashChild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unstash_child(const PandaNode self, PandaNode child_node, Thread current_thread)
        unstash_child(const PandaNode self, int stashed_index, Thread current_thread)
        
        /**
         * Returns the indicated stashed node to normal child status.  This removes
         * the child from the list of stashed children and puts it on the normal list
         * of active children.  This child node once again contributes to the bounding
         * volume of the PandaNode, and will be visited in normal traversals.  It is
         * visible and collidable.
         *
         * This function returns true if the child node was successfully stashed, or
         * false if it was not a child of the node in the first place (e.g.  it was
         * previously stashed).
         */
        
        /**
         * Returns the indicated stashed node to normal child status.  This removes
         * the child from the list of stashed children and puts it on the normal list
         * of active children.  This child node once again contributes to the bounding
         * volume of the PandaNode, and will be visited in normal traversals.  It is
         * visible and collidable.
         *
         * This can only be called from the top pipeline stage (i.e.  from App).
         */
        """
        pass

    def unstash_child(self, const_PandaNode_self, PandaNode_child_node, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unstash_child(const PandaNode self, PandaNode child_node, Thread current_thread)
        unstash_child(const PandaNode self, int stashed_index, Thread current_thread)
        
        /**
         * Returns the indicated stashed node to normal child status.  This removes
         * the child from the list of stashed children and puts it on the normal list
         * of active children.  This child node once again contributes to the bounding
         * volume of the PandaNode, and will be visited in normal traversals.  It is
         * visible and collidable.
         *
         * This function returns true if the child node was successfully stashed, or
         * false if it was not a child of the node in the first place (e.g.  it was
         * previously stashed).
         */
        
        /**
         * Returns the indicated stashed node to normal child status.  This removes
         * the child from the list of stashed children and puts it on the normal list
         * of active children.  This child node once again contributes to the bounding
         * volume of the PandaNode, and will be visited in normal traversals.  It is
         * visible and collidable.
         *
         * This can only be called from the top pipeline stage (i.e.  from App).
         */
        """
        pass

    def upcastToNamable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_Namable(const PandaNode self)
        
        upcast from PandaNode to Namable
        """
        pass

    def upcastToTypedWritableReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const PandaNode self)
        
        upcast from PandaNode to TypedWritableReferenceCount
        """
        pass

    def upcast_to_Namable(self, const_PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Namable(const PandaNode self)
        
        upcast from PandaNode to Namable
        """
        pass

    def upcast_to_TypedWritableReferenceCount(self, const_PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const PandaNode self)
        
        upcast from PandaNode to TypedWritableReferenceCount
        """
        pass

    def write(self, PandaNode_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(PandaNode self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def __copy__(self, PandaNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __copy__(PandaNode self)
        """
        pass

    def __deepcopy__(self, PandaNode_self, object_memo): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __deepcopy__(PandaNode self, object memo)
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

    bounds_stale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bounds_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_control_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_show_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    effects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    final = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    internal_bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    internal_vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    into_collide_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    legal_collide_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nested_vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    overall_hidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prev_transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    python_tags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stashed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    all_camera_mask = None # (!) real value is ' 0111 1111 1111 1111 1111 1111 1111 1111'
    Children = None # (!) real value is "<class 'panda3d.core.Children'>"
    DtoolClassDict = {
        'Children': None, # (!) real value is "<class 'panda3d.core.Children'>"
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'FBCullCallback': 64,
        'FBDrawMask': 32,
        'FBEffects': 4,
        'FBState': 2,
        'FBTag': 16,
        'FBTransform': 1,
        'FB_cull_callback': 64,
        'FB_draw_mask': 32,
        'FB_effects': 4,
        'FB_state': 2,
        'FB_tag': 16,
        'FB_transform': 1,
        'Parents': None, # (!) real value is "<class 'panda3d.core.Parents'>"
        'Stashed': None, # (!) real value is "<class 'panda3d.core.Stashed'>"
        'UCChildren': 2,
        'UCDrawMask': 16,
        'UCParents': 1,
        'UCState': 8,
        'UCTransform': 4,
        'UC_children': 2,
        'UC_draw_mask': 16,
        'UC_parents': 1,
        'UC_state': 8,
        'UC_transform': 4,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.PandaNode' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.PandaNode' objects>"
        '__doc__': '/**\n * A basic node of the scene graph or data graph.  This is the base class of\n * all specialized nodes, and also serves as a generic node with no special\n * properties.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PandaNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE292850>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.PandaNode' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.PandaNode' objects>"
        'addChild': None, # (!) real value is "<method 'addChild' of 'panda3d.core.PandaNode' objects>"
        'addStashed': None, # (!) real value is "<method 'addStashed' of 'panda3d.core.PandaNode' objects>"
        'add_child': None, # (!) real value is "<method 'add_child' of 'panda3d.core.PandaNode' objects>"
        'add_stashed': None, # (!) real value is "<method 'add_stashed' of 'panda3d.core.PandaNode' objects>"
        'adjustDrawMask': None, # (!) real value is "<method 'adjustDrawMask' of 'panda3d.core.PandaNode' objects>"
        'adjust_draw_mask': None, # (!) real value is "<method 'adjust_draw_mask' of 'panda3d.core.PandaNode' objects>"
        'all_camera_mask': None, # (!) real value is "<attribute 'all_camera_mask' of 'panda3d.core.PandaNode'>"
        'asLight': None, # (!) real value is "<method 'asLight' of 'panda3d.core.PandaNode' objects>"
        'as_light': None, # (!) real value is "<method 'as_light' of 'panda3d.core.PandaNode' objects>"
        'bounds_stale': None, # (!) real value is "<attribute 'bounds_stale' of 'panda3d.core.PandaNode' objects>"
        'bounds_type': None, # (!) real value is "<attribute 'bounds_type' of 'panda3d.core.PandaNode' objects>"
        'children': None, # (!) real value is "<attribute 'children' of 'panda3d.core.PandaNode' objects>"
        'clearAttrib': None, # (!) real value is "<method 'clearAttrib' of 'panda3d.core.PandaNode' objects>"
        'clearBounds': None, # (!) real value is "<method 'clearBounds' of 'panda3d.core.PandaNode' objects>"
        'clearEffect': None, # (!) real value is "<method 'clearEffect' of 'panda3d.core.PandaNode' objects>"
        'clearEffects': None, # (!) real value is "<method 'clearEffects' of 'panda3d.core.PandaNode' objects>"
        'clearPythonTag': None, # (!) real value is "<method 'clearPythonTag' of 'panda3d.core.PandaNode' objects>"
        'clearState': None, # (!) real value is "<method 'clearState' of 'panda3d.core.PandaNode' objects>"
        'clearTag': None, # (!) real value is "<method 'clearTag' of 'panda3d.core.PandaNode' objects>"
        'clearTransform': None, # (!) real value is "<method 'clearTransform' of 'panda3d.core.PandaNode' objects>"
        'clearUnexpectedChange': None, # (!) real value is "<method 'clearUnexpectedChange' of 'panda3d.core.PandaNode' objects>"
        'clear_attrib': None, # (!) real value is "<method 'clear_attrib' of 'panda3d.core.PandaNode' objects>"
        'clear_bounds': None, # (!) real value is "<method 'clear_bounds' of 'panda3d.core.PandaNode' objects>"
        'clear_effect': None, # (!) real value is "<method 'clear_effect' of 'panda3d.core.PandaNode' objects>"
        'clear_effects': None, # (!) real value is "<method 'clear_effects' of 'panda3d.core.PandaNode' objects>"
        'clear_python_tag': None, # (!) real value is "<method 'clear_python_tag' of 'panda3d.core.PandaNode' objects>"
        'clear_state': None, # (!) real value is "<method 'clear_state' of 'panda3d.core.PandaNode' objects>"
        'clear_tag': None, # (!) real value is "<method 'clear_tag' of 'panda3d.core.PandaNode' objects>"
        'clear_transform': None, # (!) real value is "<method 'clear_transform' of 'panda3d.core.PandaNode' objects>"
        'clear_unexpected_change': None, # (!) real value is "<method 'clear_unexpected_change' of 'panda3d.core.PandaNode' objects>"
        'combineWith': None, # (!) real value is "<method 'combineWith' of 'panda3d.core.PandaNode' objects>"
        'combine_with': None, # (!) real value is "<method 'combine_with' of 'panda3d.core.PandaNode' objects>"
        'compareTags': None, # (!) real value is "<method 'compareTags' of 'panda3d.core.PandaNode' objects>"
        'compare_tags': None, # (!) real value is "<method 'compare_tags' of 'panda3d.core.PandaNode' objects>"
        'copyAllProperties': None, # (!) real value is "<method 'copyAllProperties' of 'panda3d.core.PandaNode' objects>"
        'copyChildren': None, # (!) real value is "<method 'copyChildren' of 'panda3d.core.PandaNode' objects>"
        'copySubgraph': None, # (!) real value is "<method 'copySubgraph' of 'panda3d.core.PandaNode' objects>"
        'copyTags': None, # (!) real value is "<method 'copyTags' of 'panda3d.core.PandaNode' objects>"
        'copy_all_properties': None, # (!) real value is "<method 'copy_all_properties' of 'panda3d.core.PandaNode' objects>"
        'copy_children': None, # (!) real value is "<method 'copy_children' of 'panda3d.core.PandaNode' objects>"
        'copy_subgraph': None, # (!) real value is "<method 'copy_subgraph' of 'panda3d.core.PandaNode' objects>"
        'copy_tags': None, # (!) real value is "<method 'copy_tags' of 'panda3d.core.PandaNode' objects>"
        'countNumDescendants': None, # (!) real value is "<method 'countNumDescendants' of 'panda3d.core.PandaNode' objects>"
        'count_num_descendants': None, # (!) real value is "<method 'count_num_descendants' of 'panda3d.core.PandaNode' objects>"
        'decodeFromBamStream': None, # (!) real value is '<staticmethod(<built-in method decodeFromBamStream of type object at 0x00007FFCFE292850>)>'
        'decode_from_bam_stream': None, # (!) real value is '<staticmethod(<built-in method decode_from_bam_stream of type object at 0x00007FFCFE292850>)>'
        'draw_control_mask': None, # (!) real value is "<attribute 'draw_control_mask' of 'panda3d.core.PandaNode' objects>"
        'draw_show_mask': None, # (!) real value is "<attribute 'draw_show_mask' of 'panda3d.core.PandaNode' objects>"
        'effects': None, # (!) real value is "<attribute 'effects' of 'panda3d.core.PandaNode' objects>"
        'final': None, # (!) real value is "<attribute 'final' of 'panda3d.core.PandaNode' objects>"
        'findChild': None, # (!) real value is "<method 'findChild' of 'panda3d.core.PandaNode' objects>"
        'findParent': None, # (!) real value is "<method 'findParent' of 'panda3d.core.PandaNode' objects>"
        'findStashed': None, # (!) real value is "<method 'findStashed' of 'panda3d.core.PandaNode' objects>"
        'find_child': None, # (!) real value is "<method 'find_child' of 'panda3d.core.PandaNode' objects>"
        'find_parent': None, # (!) real value is "<method 'find_parent' of 'panda3d.core.PandaNode' objects>"
        'find_stashed': None, # (!) real value is "<method 'find_stashed' of 'panda3d.core.PandaNode' objects>"
        'getAllCameraMask': None, # (!) real value is '<staticmethod(<built-in method getAllCameraMask of type object at 0x00007FFCFE292850>)>'
        'getAttrib': None, # (!) real value is "<method 'getAttrib' of 'panda3d.core.PandaNode' objects>"
        'getBounds': None, # (!) real value is "<method 'getBounds' of 'panda3d.core.PandaNode' objects>"
        'getBoundsType': None, # (!) real value is "<method 'getBoundsType' of 'panda3d.core.PandaNode' objects>"
        'getChild': None, # (!) real value is "<method 'getChild' of 'panda3d.core.PandaNode' objects>"
        'getChildSort': None, # (!) real value is "<method 'getChildSort' of 'panda3d.core.PandaNode' objects>"
        'getChildren': None, # (!) real value is "<method 'getChildren' of 'panda3d.core.PandaNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE292850>)>'
        'getDrawControlMask': None, # (!) real value is "<method 'getDrawControlMask' of 'panda3d.core.PandaNode' objects>"
        'getDrawShowMask': None, # (!) real value is "<method 'getDrawShowMask' of 'panda3d.core.PandaNode' objects>"
        'getEffect': None, # (!) real value is "<method 'getEffect' of 'panda3d.core.PandaNode' objects>"
        'getEffects': None, # (!) real value is "<method 'getEffects' of 'panda3d.core.PandaNode' objects>"
        'getFancyBits': None, # (!) real value is "<method 'getFancyBits' of 'panda3d.core.PandaNode' objects>"
        'getInternalBounds': None, # (!) real value is "<method 'getInternalBounds' of 'panda3d.core.PandaNode' objects>"
        'getInternalVertices': None, # (!) real value is "<method 'getInternalVertices' of 'panda3d.core.PandaNode' objects>"
        'getIntoCollideMask': None, # (!) real value is "<method 'getIntoCollideMask' of 'panda3d.core.PandaNode' objects>"
        'getLegalCollideMask': None, # (!) real value is "<method 'getLegalCollideMask' of 'panda3d.core.PandaNode' objects>"
        'getNestedVertices': None, # (!) real value is "<method 'getNestedVertices' of 'panda3d.core.PandaNode' objects>"
        'getNetCollideMask': None, # (!) real value is "<method 'getNetCollideMask' of 'panda3d.core.PandaNode' objects>"
        'getNetDrawControlMask': None, # (!) real value is "<method 'getNetDrawControlMask' of 'panda3d.core.PandaNode' objects>"
        'getNetDrawShowMask': None, # (!) real value is "<method 'getNetDrawShowMask' of 'panda3d.core.PandaNode' objects>"
        'getNumChildren': None, # (!) real value is "<method 'getNumChildren' of 'panda3d.core.PandaNode' objects>"
        'getNumParents': None, # (!) real value is "<method 'getNumParents' of 'panda3d.core.PandaNode' objects>"
        'getNumStashed': None, # (!) real value is "<method 'getNumStashed' of 'panda3d.core.PandaNode' objects>"
        'getOffClipPlanes': None, # (!) real value is "<method 'getOffClipPlanes' of 'panda3d.core.PandaNode' objects>"
        'getOverallBit': None, # (!) real value is '<staticmethod(<built-in method getOverallBit of type object at 0x00007FFCFE292850>)>'
        'getParent': None, # (!) real value is "<method 'getParent' of 'panda3d.core.PandaNode' objects>"
        'getParents': None, # (!) real value is "<method 'getParents' of 'panda3d.core.PandaNode' objects>"
        'getPrevTransform': None, # (!) real value is "<method 'getPrevTransform' of 'panda3d.core.PandaNode' objects>"
        'getPythonTag': None, # (!) real value is "<method 'getPythonTag' of 'panda3d.core.PandaNode' objects>"
        'getPythonTagKeys': None, # (!) real value is "<method 'getPythonTagKeys' of 'panda3d.core.PandaNode' objects>"
        'getPythonTags': None, # (!) real value is "<method 'getPythonTags' of 'panda3d.core.PandaNode' objects>"
        'getStashed': None, # (!) real value is "<method 'getStashed' of 'panda3d.core.PandaNode' objects>"
        'getStashedSort': None, # (!) real value is "<method 'getStashedSort' of 'panda3d.core.PandaNode' objects>"
        'getState': None, # (!) real value is "<method 'getState' of 'panda3d.core.PandaNode' objects>"
        'getTag': None, # (!) real value is "<method 'getTag' of 'panda3d.core.PandaNode' objects>"
        'getTagKeys': None, # (!) real value is "<method 'getTagKeys' of 'panda3d.core.PandaNode' objects>"
        'getTransform': None, # (!) real value is "<method 'getTransform' of 'panda3d.core.PandaNode' objects>"
        'getUnexpectedChange': None, # (!) real value is "<method 'getUnexpectedChange' of 'panda3d.core.PandaNode' objects>"
        'get_all_camera_mask': None, # (!) real value is '<staticmethod(<built-in method get_all_camera_mask of type object at 0x00007FFCFE292850>)>'
        'get_attrib': None, # (!) real value is "<method 'get_attrib' of 'panda3d.core.PandaNode' objects>"
        'get_bounds': None, # (!) real value is "<method 'get_bounds' of 'panda3d.core.PandaNode' objects>"
        'get_bounds_type': None, # (!) real value is "<method 'get_bounds_type' of 'panda3d.core.PandaNode' objects>"
        'get_child': None, # (!) real value is "<method 'get_child' of 'panda3d.core.PandaNode' objects>"
        'get_child_sort': None, # (!) real value is "<method 'get_child_sort' of 'panda3d.core.PandaNode' objects>"
        'get_children': None, # (!) real value is "<method 'get_children' of 'panda3d.core.PandaNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE292850>)>'
        'get_draw_control_mask': None, # (!) real value is "<method 'get_draw_control_mask' of 'panda3d.core.PandaNode' objects>"
        'get_draw_show_mask': None, # (!) real value is "<method 'get_draw_show_mask' of 'panda3d.core.PandaNode' objects>"
        'get_effect': None, # (!) real value is "<method 'get_effect' of 'panda3d.core.PandaNode' objects>"
        'get_effects': None, # (!) real value is "<method 'get_effects' of 'panda3d.core.PandaNode' objects>"
        'get_fancy_bits': None, # (!) real value is "<method 'get_fancy_bits' of 'panda3d.core.PandaNode' objects>"
        'get_internal_bounds': None, # (!) real value is "<method 'get_internal_bounds' of 'panda3d.core.PandaNode' objects>"
        'get_internal_vertices': None, # (!) real value is "<method 'get_internal_vertices' of 'panda3d.core.PandaNode' objects>"
        'get_into_collide_mask': None, # (!) real value is "<method 'get_into_collide_mask' of 'panda3d.core.PandaNode' objects>"
        'get_legal_collide_mask': None, # (!) real value is "<method 'get_legal_collide_mask' of 'panda3d.core.PandaNode' objects>"
        'get_nested_vertices': None, # (!) real value is "<method 'get_nested_vertices' of 'panda3d.core.PandaNode' objects>"
        'get_net_collide_mask': None, # (!) real value is "<method 'get_net_collide_mask' of 'panda3d.core.PandaNode' objects>"
        'get_net_draw_control_mask': None, # (!) real value is "<method 'get_net_draw_control_mask' of 'panda3d.core.PandaNode' objects>"
        'get_net_draw_show_mask': None, # (!) real value is "<method 'get_net_draw_show_mask' of 'panda3d.core.PandaNode' objects>"
        'get_num_children': None, # (!) real value is "<method 'get_num_children' of 'panda3d.core.PandaNode' objects>"
        'get_num_parents': None, # (!) real value is "<method 'get_num_parents' of 'panda3d.core.PandaNode' objects>"
        'get_num_stashed': None, # (!) real value is "<method 'get_num_stashed' of 'panda3d.core.PandaNode' objects>"
        'get_off_clip_planes': None, # (!) real value is "<method 'get_off_clip_planes' of 'panda3d.core.PandaNode' objects>"
        'get_overall_bit': None, # (!) real value is '<staticmethod(<built-in method get_overall_bit of type object at 0x00007FFCFE292850>)>'
        'get_parent': None, # (!) real value is "<method 'get_parent' of 'panda3d.core.PandaNode' objects>"
        'get_parents': None, # (!) real value is "<method 'get_parents' of 'panda3d.core.PandaNode' objects>"
        'get_prev_transform': None, # (!) real value is "<method 'get_prev_transform' of 'panda3d.core.PandaNode' objects>"
        'get_python_tag': None, # (!) real value is "<method 'get_python_tag' of 'panda3d.core.PandaNode' objects>"
        'get_python_tag_keys': None, # (!) real value is "<method 'get_python_tag_keys' of 'panda3d.core.PandaNode' objects>"
        'get_python_tags': None, # (!) real value is "<method 'get_python_tags' of 'panda3d.core.PandaNode' objects>"
        'get_stashed': None, # (!) real value is "<method 'get_stashed' of 'panda3d.core.PandaNode' objects>"
        'get_stashed_sort': None, # (!) real value is "<method 'get_stashed_sort' of 'panda3d.core.PandaNode' objects>"
        'get_state': None, # (!) real value is "<method 'get_state' of 'panda3d.core.PandaNode' objects>"
        'get_tag': None, # (!) real value is "<method 'get_tag' of 'panda3d.core.PandaNode' objects>"
        'get_tag_keys': None, # (!) real value is "<method 'get_tag_keys' of 'panda3d.core.PandaNode' objects>"
        'get_transform': None, # (!) real value is "<method 'get_transform' of 'panda3d.core.PandaNode' objects>"
        'get_unexpected_change': None, # (!) real value is "<method 'get_unexpected_change' of 'panda3d.core.PandaNode' objects>"
        'hasAttrib': None, # (!) real value is "<method 'hasAttrib' of 'panda3d.core.PandaNode' objects>"
        'hasDirtyPrevTransform': None, # (!) real value is "<method 'hasDirtyPrevTransform' of 'panda3d.core.PandaNode' objects>"
        'hasEffect': None, # (!) real value is "<method 'hasEffect' of 'panda3d.core.PandaNode' objects>"
        'hasPythonTag': None, # (!) real value is "<method 'hasPythonTag' of 'panda3d.core.PandaNode' objects>"
        'hasTag': None, # (!) real value is "<method 'hasTag' of 'panda3d.core.PandaNode' objects>"
        'hasTags': None, # (!) real value is "<method 'hasTags' of 'panda3d.core.PandaNode' objects>"
        'has_attrib': None, # (!) real value is "<method 'has_attrib' of 'panda3d.core.PandaNode' objects>"
        'has_dirty_prev_transform': None, # (!) real value is "<method 'has_dirty_prev_transform' of 'panda3d.core.PandaNode' objects>"
        'has_effect': None, # (!) real value is "<method 'has_effect' of 'panda3d.core.PandaNode' objects>"
        'has_python_tag': None, # (!) real value is "<method 'has_python_tag' of 'panda3d.core.PandaNode' objects>"
        'has_tag': None, # (!) real value is "<method 'has_tag' of 'panda3d.core.PandaNode' objects>"
        'has_tags': None, # (!) real value is "<method 'has_tags' of 'panda3d.core.PandaNode' objects>"
        'internal_bounds': None, # (!) real value is "<attribute 'internal_bounds' of 'panda3d.core.PandaNode' objects>"
        'internal_vertices': None, # (!) real value is "<attribute 'internal_vertices' of 'panda3d.core.PandaNode' objects>"
        'into_collide_mask': None, # (!) real value is "<attribute 'into_collide_mask' of 'panda3d.core.PandaNode' objects>"
        'isAmbientLight': None, # (!) real value is "<method 'isAmbientLight' of 'panda3d.core.PandaNode' objects>"
        'isBoundsStale': None, # (!) real value is "<method 'isBoundsStale' of 'panda3d.core.PandaNode' objects>"
        'isCollisionNode': None, # (!) real value is "<method 'isCollisionNode' of 'panda3d.core.PandaNode' objects>"
        'isFinal': None, # (!) real value is "<method 'isFinal' of 'panda3d.core.PandaNode' objects>"
        'isGeomNode': None, # (!) real value is "<method 'isGeomNode' of 'panda3d.core.PandaNode' objects>"
        'isLodNode': None, # (!) real value is "<method 'isLodNode' of 'panda3d.core.PandaNode' objects>"
        'isOverallHidden': None, # (!) real value is "<method 'isOverallHidden' of 'panda3d.core.PandaNode' objects>"
        'isSceneRoot': None, # (!) real value is "<method 'isSceneRoot' of 'panda3d.core.PandaNode' objects>"
        'isUnderSceneRoot': None, # (!) real value is "<method 'isUnderSceneRoot' of 'panda3d.core.PandaNode' objects>"
        'is_ambient_light': None, # (!) real value is "<method 'is_ambient_light' of 'panda3d.core.PandaNode' objects>"
        'is_bounds_stale': None, # (!) real value is "<method 'is_bounds_stale' of 'panda3d.core.PandaNode' objects>"
        'is_collision_node': None, # (!) real value is "<method 'is_collision_node' of 'panda3d.core.PandaNode' objects>"
        'is_final': None, # (!) real value is "<method 'is_final' of 'panda3d.core.PandaNode' objects>"
        'is_geom_node': None, # (!) real value is "<method 'is_geom_node' of 'panda3d.core.PandaNode' objects>"
        'is_lod_node': None, # (!) real value is "<method 'is_lod_node' of 'panda3d.core.PandaNode' objects>"
        'is_overall_hidden': None, # (!) real value is "<method 'is_overall_hidden' of 'panda3d.core.PandaNode' objects>"
        'is_scene_root': None, # (!) real value is "<method 'is_scene_root' of 'panda3d.core.PandaNode' objects>"
        'is_under_scene_root': None, # (!) real value is "<method 'is_under_scene_root' of 'panda3d.core.PandaNode' objects>"
        'legal_collide_mask': None, # (!) real value is "<attribute 'legal_collide_mask' of 'panda3d.core.PandaNode' objects>"
        'listTags': None, # (!) real value is "<method 'listTags' of 'panda3d.core.PandaNode' objects>"
        'list_tags': None, # (!) real value is "<method 'list_tags' of 'panda3d.core.PandaNode' objects>"
        'ls': None, # (!) real value is "<method 'ls' of 'panda3d.core.PandaNode' objects>"
        'makeCopy': None, # (!) real value is "<method 'makeCopy' of 'panda3d.core.PandaNode' objects>"
        'make_copy': None, # (!) real value is "<method 'make_copy' of 'panda3d.core.PandaNode' objects>"
        'markBoundsStale': None, # (!) real value is "<method 'markBoundsStale' of 'panda3d.core.PandaNode' objects>"
        'markInternalBoundsStale': None, # (!) real value is "<method 'markInternalBoundsStale' of 'panda3d.core.PandaNode' objects>"
        'mark_bounds_stale': None, # (!) real value is "<method 'mark_bounds_stale' of 'panda3d.core.PandaNode' objects>"
        'mark_internal_bounds_stale': None, # (!) real value is "<method 'mark_internal_bounds_stale' of 'panda3d.core.PandaNode' objects>"
        'nested_vertices': None, # (!) real value is "<attribute 'nested_vertices' of 'panda3d.core.PandaNode' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.PandaNode' objects>"
        'overall_bit': None, # (!) real value is "<attribute 'overall_bit' of 'panda3d.core.PandaNode'>"
        'overall_hidden': None, # (!) real value is "<attribute 'overall_hidden' of 'panda3d.core.PandaNode' objects>"
        'parents': None, # (!) real value is "<attribute 'parents' of 'panda3d.core.PandaNode' objects>"
        'prepareScene': None, # (!) real value is "<method 'prepareScene' of 'panda3d.core.PandaNode' objects>"
        'prepare_scene': None, # (!) real value is "<method 'prepare_scene' of 'panda3d.core.PandaNode' objects>"
        'prev_transform': None, # (!) real value is "<attribute 'prev_transform' of 'panda3d.core.PandaNode' objects>"
        'python_tags': None, # (!) real value is "<attribute 'python_tags' of 'panda3d.core.PandaNode' objects>"
        'removeAllChildren': None, # (!) real value is "<method 'removeAllChildren' of 'panda3d.core.PandaNode' objects>"
        'removeChild': None, # (!) real value is "<method 'removeChild' of 'panda3d.core.PandaNode' objects>"
        'removeStashed': None, # (!) real value is "<method 'removeStashed' of 'panda3d.core.PandaNode' objects>"
        'remove_all_children': None, # (!) real value is "<method 'remove_all_children' of 'panda3d.core.PandaNode' objects>"
        'remove_child': None, # (!) real value is "<method 'remove_child' of 'panda3d.core.PandaNode' objects>"
        'remove_stashed': None, # (!) real value is "<method 'remove_stashed' of 'panda3d.core.PandaNode' objects>"
        'replaceChild': None, # (!) real value is "<method 'replaceChild' of 'panda3d.core.PandaNode' objects>"
        'replaceNode': None, # (!) real value is "<method 'replaceNode' of 'panda3d.core.PandaNode' objects>"
        'replace_child': None, # (!) real value is "<method 'replace_child' of 'panda3d.core.PandaNode' objects>"
        'replace_node': None, # (!) real value is "<method 'replace_node' of 'panda3d.core.PandaNode' objects>"
        'resetAllPrevTransform': None, # (!) real value is '<staticmethod(<built-in method resetAllPrevTransform of type object at 0x00007FFCFE292850>)>'
        'resetPrevTransform': None, # (!) real value is "<method 'resetPrevTransform' of 'panda3d.core.PandaNode' objects>"
        'reset_all_prev_transform': None, # (!) real value is '<staticmethod(<built-in method reset_all_prev_transform of type object at 0x00007FFCFE292850>)>'
        'reset_prev_transform': None, # (!) real value is "<method 'reset_prev_transform' of 'panda3d.core.PandaNode' objects>"
        'setAttrib': None, # (!) real value is "<method 'setAttrib' of 'panda3d.core.PandaNode' objects>"
        'setBound': None, # (!) real value is "<method 'setBound' of 'panda3d.core.PandaNode' objects>"
        'setBounds': None, # (!) real value is "<method 'setBounds' of 'panda3d.core.PandaNode' objects>"
        'setBoundsType': None, # (!) real value is "<method 'setBoundsType' of 'panda3d.core.PandaNode' objects>"
        'setEffect': None, # (!) real value is "<method 'setEffect' of 'panda3d.core.PandaNode' objects>"
        'setEffects': None, # (!) real value is "<method 'setEffects' of 'panda3d.core.PandaNode' objects>"
        'setFinal': None, # (!) real value is "<method 'setFinal' of 'panda3d.core.PandaNode' objects>"
        'setIntoCollideMask': None, # (!) real value is "<method 'setIntoCollideMask' of 'panda3d.core.PandaNode' objects>"
        'setOverallHidden': None, # (!) real value is "<method 'setOverallHidden' of 'panda3d.core.PandaNode' objects>"
        'setPrevTransform': None, # (!) real value is "<method 'setPrevTransform' of 'panda3d.core.PandaNode' objects>"
        'setPythonTag': None, # (!) real value is "<method 'setPythonTag' of 'panda3d.core.PandaNode' objects>"
        'setState': None, # (!) real value is "<method 'setState' of 'panda3d.core.PandaNode' objects>"
        'setTag': None, # (!) real value is "<method 'setTag' of 'panda3d.core.PandaNode' objects>"
        'setTransform': None, # (!) real value is "<method 'setTransform' of 'panda3d.core.PandaNode' objects>"
        'setUnexpectedChange': None, # (!) real value is "<method 'setUnexpectedChange' of 'panda3d.core.PandaNode' objects>"
        'set_attrib': None, # (!) real value is "<method 'set_attrib' of 'panda3d.core.PandaNode' objects>"
        'set_bound': None, # (!) real value is "<method 'set_bound' of 'panda3d.core.PandaNode' objects>"
        'set_bounds': None, # (!) real value is "<method 'set_bounds' of 'panda3d.core.PandaNode' objects>"
        'set_bounds_type': None, # (!) real value is "<method 'set_bounds_type' of 'panda3d.core.PandaNode' objects>"
        'set_effect': None, # (!) real value is "<method 'set_effect' of 'panda3d.core.PandaNode' objects>"
        'set_effects': None, # (!) real value is "<method 'set_effects' of 'panda3d.core.PandaNode' objects>"
        'set_final': None, # (!) real value is "<method 'set_final' of 'panda3d.core.PandaNode' objects>"
        'set_into_collide_mask': None, # (!) real value is "<method 'set_into_collide_mask' of 'panda3d.core.PandaNode' objects>"
        'set_overall_hidden': None, # (!) real value is "<method 'set_overall_hidden' of 'panda3d.core.PandaNode' objects>"
        'set_prev_transform': None, # (!) real value is "<method 'set_prev_transform' of 'panda3d.core.PandaNode' objects>"
        'set_python_tag': None, # (!) real value is "<method 'set_python_tag' of 'panda3d.core.PandaNode' objects>"
        'set_state': None, # (!) real value is "<method 'set_state' of 'panda3d.core.PandaNode' objects>"
        'set_tag': None, # (!) real value is "<method 'set_tag' of 'panda3d.core.PandaNode' objects>"
        'set_transform': None, # (!) real value is "<method 'set_transform' of 'panda3d.core.PandaNode' objects>"
        'set_unexpected_change': None, # (!) real value is "<method 'set_unexpected_change' of 'panda3d.core.PandaNode' objects>"
        'stashChild': None, # (!) real value is "<method 'stashChild' of 'panda3d.core.PandaNode' objects>"
        'stash_child': None, # (!) real value is "<method 'stash_child' of 'panda3d.core.PandaNode' objects>"
        'stashed': None, # (!) real value is "<attribute 'stashed' of 'panda3d.core.PandaNode' objects>"
        'state': None, # (!) real value is "<attribute 'state' of 'panda3d.core.PandaNode' objects>"
        'stealChildren': None, # (!) real value is "<method 'stealChildren' of 'panda3d.core.PandaNode' objects>"
        'steal_children': None, # (!) real value is "<method 'steal_children' of 'panda3d.core.PandaNode' objects>"
        'tags': None, # (!) real value is "<attribute 'tags' of 'panda3d.core.PandaNode' objects>"
        'transform': None, # (!) real value is "<attribute 'transform' of 'panda3d.core.PandaNode' objects>"
        'unstashChild': None, # (!) real value is "<method 'unstashChild' of 'panda3d.core.PandaNode' objects>"
        'unstash_child': None, # (!) real value is "<method 'unstash_child' of 'panda3d.core.PandaNode' objects>"
        'upcastToNamable': None, # (!) real value is "<method 'upcastToNamable' of 'panda3d.core.PandaNode' objects>"
        'upcastToTypedWritableReferenceCount': None, # (!) real value is "<method 'upcastToTypedWritableReferenceCount' of 'panda3d.core.PandaNode' objects>"
        'upcast_to_Namable': None, # (!) real value is "<method 'upcast_to_Namable' of 'panda3d.core.PandaNode' objects>"
        'upcast_to_TypedWritableReferenceCount': None, # (!) real value is "<method 'upcast_to_TypedWritableReferenceCount' of 'panda3d.core.PandaNode' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.PandaNode' objects>"
    }
    FBCullCallback = 64
    FBDrawMask = 32
    FBEffects = 4
    FBState = 2
    FBTag = 16
    FBTransform = 1
    FB_cull_callback = 64
    FB_draw_mask = 32
    FB_effects = 4
    FB_state = 2
    FB_tag = 16
    FB_transform = 1
    overall_bit = None # (!) real value is ' 1000 0000 0000 0000 0000 0000 0000 0000'
    Parents = None # (!) real value is "<class 'panda3d.core.Parents'>"
    Stashed = None # (!) real value is "<class 'panda3d.core.Stashed'>"
    UCChildren = 2
    UCDrawMask = 16
    UCParents = 1
    UCState = 8
    UCTransform = 4
    UC_children = 2
    UC_draw_mask = 16
    UC_parents = 1
    UC_state = 8
    UC_transform = 4


