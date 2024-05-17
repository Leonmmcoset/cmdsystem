# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PartGroup import PartGroup

class PartBundle(PartGroup):
    """
    /**
     * This is the root of a MovingPart hierarchy.  It defines the hierarchy of
     * moving parts that make up an animatable object.
     */
    """
    def applyTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_transform(const PartBundle self, const TransformState transform)
        
        /**
         * Returns a PartBundle that is a duplicate of this one, but with the
         * indicated transform applied.  If this is called multiple times with the
         * same TransformState pointer, it returns the same PartBundle each time.
         */
        """
        pass

    def apply_transform(self, const_PartBundle_self, const_TransformState_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_transform(const PartBundle self, const TransformState transform)
        
        /**
         * Returns a PartBundle that is a duplicate of this one, but with the
         * indicated transform applied.  If this is called multiple times with the
         * same TransformState pointer, it returns the same PartBundle each time.
         */
        """
        pass

    def bindAnim(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        bind_anim(const PartBundle self, AnimBundle anim, int hierarchy_match_flags, const PartSubset subset)
        
        /**
         * Binds the animation to the bundle, if possible, and returns a new
         * AnimControl that can be used to start and stop the animation.  If the anim
         * hierarchy does not match the part hierarchy, returns NULL.
         *
         * If hierarchy_match_flags is 0, only an exact match is accepted; otherwise,
         * it may contain a union of PartGroup::HierarchyMatchFlags values indicating
         * conditions that will be tolerated (but warnings will still be issued).
         *
         * If subset is specified, it restricts the binding only to the named subtree
         * of joints.
         *
         * The AnimControl is not stored within the PartBundle; it is the user's
         * responsibility to maintain the pointer.  The animation will automatically
         * unbind itself when the AnimControl destructs (i.e.  its reference count
         * goes to zero).
         */
        """
        pass

    def bind_anim(self, const_PartBundle_self, AnimBundle_anim, int_hierarchy_match_flags, const_PartSubset_subset): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        bind_anim(const PartBundle self, AnimBundle anim, int hierarchy_match_flags, const PartSubset subset)
        
        /**
         * Binds the animation to the bundle, if possible, and returns a new
         * AnimControl that can be used to start and stop the animation.  If the anim
         * hierarchy does not match the part hierarchy, returns NULL.
         *
         * If hierarchy_match_flags is 0, only an exact match is accepted; otherwise,
         * it may contain a union of PartGroup::HierarchyMatchFlags values indicating
         * conditions that will be tolerated (but warnings will still be issued).
         *
         * If subset is specified, it restricts the binding only to the named subtree
         * of joints.
         *
         * The AnimControl is not stored within the PartBundle; it is the user's
         * responsibility to maintain the pointer.  The animation will automatically
         * unbind itself when the AnimControl destructs (i.e.  its reference count
         * goes to zero).
         */
        """
        pass

    def clearAnimPreload(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_anim_preload(const PartBundle self)
        
        /**
         * Removes any AnimPreloadTable associated with the PartBundle.
         */
        """
        pass

    def clearControlEffects(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_control_effects(const PartBundle self)
        
        /**
         * Sets the control effect of all AnimControls to zero (but does not "stop"
         * the AnimControls).  The character will no longer be affected by any
         * animation, and will return to its default pose (unless restore-initial-pose
         * is false).
         *
         * The AnimControls which are no longer associated will not be using any CPU
         * cycles, but they may still be in the "playing" state; if they are later
         * reassociated with the PartBundle they will resume at their current frame as
         * if they'd been running all along.
         */
        """
        pass

    def clear_anim_preload(self, const_PartBundle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_anim_preload(const PartBundle self)
        
        /**
         * Removes any AnimPreloadTable associated with the PartBundle.
         */
        """
        pass

    def clear_control_effects(self, const_PartBundle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_control_effects(const PartBundle self)
        
        /**
         * Sets the control effect of all AnimControls to zero (but does not "stop"
         * the AnimControls).  The character will no longer be affected by any
         * animation, and will return to its default pose (unless restore-initial-pose
         * is false).
         *
         * The AnimControls which are no longer associated will not be using any CPU
         * cycles, but they may still be in the "playing" state; if they are later
         * reassociated with the PartBundle they will resume at their current frame as
         * if they'd been running all along.
         */
        """
        pass

    def controlJoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        control_joint(const PartBundle self, str joint_name, PandaNode node)
        
        /**
         * Specifies that the joint with the indicated name should be animated with
         * the transform on the indicated node.  It will henceforth always follow the
         * node's transform, regardless of any animations that may subsequently be
         * bound to the joint.
         *
         * Returns true if the joint is successfully controlled, or false if the named
         * child is not a joint (or slider) or does not exist.
         */
        """
        pass

    def control_joint(self, const_PartBundle_self, str_joint_name, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        control_joint(const PartBundle self, str joint_name, PandaNode node)
        
        /**
         * Specifies that the joint with the indicated name should be animated with
         * the transform on the indicated node.  It will henceforth always follow the
         * node's transform, regardless of any animations that may subsequently be
         * bound to the joint.
         *
         * Returns true if the joint is successfully controlled, or false if the named
         * child is not a joint (or slider) or does not exist.
         */
        """
        pass

    def forceUpdate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        force_update(const PartBundle self)
        
        /**
         * Updates all the parts in the bundle to reflect the data for the current
         * frame, whether we believe it needs it or not.
         */
        """
        pass

    def force_update(self, const_PartBundle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        force_update(const PartBundle self)
        
        /**
         * Updates all the parts in the bundle to reflect the data for the current
         * frame, whether we believe it needs it or not.
         */
        """
        pass

    def freezeJoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        freeze_joint(const PartBundle self, str joint_name, const TransformState transform)
        freeze_joint(const PartBundle self, str joint_name, float value)
        freeze_joint(const PartBundle self, str joint_name, const LVecBase3f pos, const LVecBase3f hpr, const LVecBase3f scale)
        
        /**
         * Specifies that the joint with the indicated name should be frozen with the
         * specified transform.  It will henceforth always hold this fixed transform,
         * regardless of any animations that may subsequently be bound to the joint.
         *
         * Returns true if the joint is successfully frozen, or false if the named
         * child is not a joint (or slider) or does not exist.
         */
        
        /**
         * Specifies that the joint with the indicated name should be frozen with the
         * specified transform.  It will henceforth always hold this fixed transform,
         * regardless of any animations that may subsequently be bound to the joint.
         *
         * Returns true if the joint is successfully frozen, or false if the named
         * child is not a joint (or slider) or does not exist.
         */
        
        /**
         * Specifies that the joint with the indicated name should be frozen with the
         * specified transform.  It will henceforth always hold this fixed transform,
         * regardless of any animations that may subsequently be bound to the joint.
         *
         * Returns true if the joint is successfully frozen, or false if the named
         * child is not a joint (or slider) or does not exist.
         */
        """
        pass

    def freeze_joint(self, const_PartBundle_self, str_joint_name, const_TransformState_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        freeze_joint(const PartBundle self, str joint_name, const TransformState transform)
        freeze_joint(const PartBundle self, str joint_name, float value)
        freeze_joint(const PartBundle self, str joint_name, const LVecBase3f pos, const LVecBase3f hpr, const LVecBase3f scale)
        
        /**
         * Specifies that the joint with the indicated name should be frozen with the
         * specified transform.  It will henceforth always hold this fixed transform,
         * regardless of any animations that may subsequently be bound to the joint.
         *
         * Returns true if the joint is successfully frozen, or false if the named
         * child is not a joint (or slider) or does not exist.
         */
        
        /**
         * Specifies that the joint with the indicated name should be frozen with the
         * specified transform.  It will henceforth always hold this fixed transform,
         * regardless of any animations that may subsequently be bound to the joint.
         *
         * Returns true if the joint is successfully frozen, or false if the named
         * child is not a joint (or slider) or does not exist.
         */
        
        /**
         * Specifies that the joint with the indicated name should be frozen with the
         * specified transform.  It will henceforth always hold this fixed transform,
         * regardless of any animations that may subsequently be bound to the joint.
         *
         * Returns true if the joint is successfully frozen, or false if the named
         * child is not a joint (or slider) or does not exist.
         */
        """
        pass

    def getAnimBlendFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_anim_blend_flag(PartBundle self)
        
        /**
         * Returns whether the character allows multiple different animations to be
         * bound simultaneously.  See set_anim_blend_flag().
         */
        """
        pass

    def getAnimPreload(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_anim_preload(PartBundle self)
        
        /**
         * Returns the AnimPreloadTable associated with the PartBundle.  This table,
         * if present, can be used for the benefit of load_bind_anim() to allow
         * asynchronous binding.
         */
        """
        pass

    def getBlendType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_blend_type(PartBundle self)
        
        /**
         * Returns the algorithm that is used when blending multiple frames or
         * multiple animations together, when either anim_blend_flag or
         * frame_blend_flag is set to true.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getControlEffect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_control_effect(PartBundle self, AnimControl control)
        
        /**
         * Returns the amount by which the character is affected by the indicated
         * AnimControl and its associated animation.  See set_control_effect().
         */
        """
        pass

    def getFrameBlendFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_blend_flag(PartBundle self)
        
        /**
         * Returns whether the character interpolates (blends) between two sequential
         * animation frames, or whether it holds the current frame until the next one
         * is ready.  See set_frame_blend_flag().
         */
        """
        pass

    def getNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node(PartBundle self, int n)
        
        /**
         * Returns the nth PartBundleNode associated with this PartBundle.
         */
        """
        pass

    def getNodes(self, *args, **kwargs): # real signature unknown
        pass

    def getNumNodes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_nodes(PartBundle self)
        
        /**
         * Returns the number of PartBundleNodes that contain a pointer to this
         * PartBundle.
         */
        """
        pass

    def getRootXform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_root_xform(PartBundle self)
        
        /**
         * Returns the transform matrix which is implicitly applied at the root of the
         * animated hierarchy.
         */
        """
        pass

    def get_anim_blend_flag(self, PartBundle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_anim_blend_flag(PartBundle self)
        
        /**
         * Returns whether the character allows multiple different animations to be
         * bound simultaneously.  See set_anim_blend_flag().
         */
        """
        pass

    def get_anim_preload(self, PartBundle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_anim_preload(PartBundle self)
        
        /**
         * Returns the AnimPreloadTable associated with the PartBundle.  This table,
         * if present, can be used for the benefit of load_bind_anim() to allow
         * asynchronous binding.
         */
        """
        pass

    def get_blend_type(self, PartBundle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_blend_type(PartBundle self)
        
        /**
         * Returns the algorithm that is used when blending multiple frames or
         * multiple animations together, when either anim_blend_flag or
         * frame_blend_flag is set to true.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_control_effect(self, PartBundle_self, AnimControl_control): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_control_effect(PartBundle self, AnimControl control)
        
        /**
         * Returns the amount by which the character is affected by the indicated
         * AnimControl and its associated animation.  See set_control_effect().
         */
        """
        pass

    def get_frame_blend_flag(self, PartBundle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_blend_flag(PartBundle self)
        
        /**
         * Returns whether the character interpolates (blends) between two sequential
         * animation frames, or whether it holds the current frame until the next one
         * is ready.  See set_frame_blend_flag().
         */
        """
        pass

    def get_node(self, PartBundle_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node(PartBundle self, int n)
        
        /**
         * Returns the nth PartBundleNode associated with this PartBundle.
         */
        """
        pass

    def get_nodes(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_nodes(self, PartBundle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_nodes(PartBundle self)
        
        /**
         * Returns the number of PartBundleNodes that contain a pointer to this
         * PartBundle.
         */
        """
        pass

    def get_root_xform(self, PartBundle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_root_xform(PartBundle self)
        
        /**
         * Returns the transform matrix which is implicitly applied at the root of the
         * animated hierarchy.
         */
        """
        pass

    def loadBindAnim(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_bind_anim(const PartBundle self, Loader loader, const Filename filename, int hierarchy_match_flags, const PartSubset subset, bool allow_async)
        
        /**
         * Binds an animation to the bundle.  The animation is loaded from the disk
         * via the indicated Loader object.  In other respects, this behaves similarly
         * to bind_anim(), with the addition of asynchronous support.
         *
         * If allow_aysnc is true, the load will be asynchronous if possible.  This
         * requires that the animation basename can be found in the PartBundle's
         * preload table (see get_anim_preload()).
         *
         * In an asynchronous load, the animation file will be loaded and bound in a
         * sub-thread.  This means that the animation will not necessarily be
         * available at the time this method returns.  You may still use the returned
         * AnimControl immediately, though, but no visible effect will occur until the
         * animation eventually becomes available.
         *
         * You can test AnimControl::is_pending() to see if the animation has been
         * loaded yet, or wait for it to finish with AnimControl::wait_pending() or
         * even PartBundle::wait_pending().  You can also set an event to be triggered
         * when the animation finishes loading with
         * AnimControl::set_pending_done_event().
         */
        """
        pass

    def load_bind_anim(self, const_PartBundle_self, Loader_loader, const_Filename_filename, int_hierarchy_match_flags, const_PartSubset_subset, bool_allow_async): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_bind_anim(const PartBundle self, Loader loader, const Filename filename, int hierarchy_match_flags, const PartSubset subset, bool allow_async)
        
        /**
         * Binds an animation to the bundle.  The animation is loaded from the disk
         * via the indicated Loader object.  In other respects, this behaves similarly
         * to bind_anim(), with the addition of asynchronous support.
         *
         * If allow_aysnc is true, the load will be asynchronous if possible.  This
         * requires that the animation basename can be found in the PartBundle's
         * preload table (see get_anim_preload()).
         *
         * In an asynchronous load, the animation file will be loaded and bound in a
         * sub-thread.  This means that the animation will not necessarily be
         * available at the time this method returns.  You may still use the returned
         * AnimControl immediately, though, but no visible effect will occur until the
         * animation eventually becomes available.
         *
         * You can test AnimControl::is_pending() to see if the animation has been
         * loaded yet, or wait for it to finish with AnimControl::wait_pending() or
         * even PartBundle::wait_pending().  You can also set an event to be triggered
         * when the animation finishes loading with
         * AnimControl::set_pending_done_event().
         */
        """
        pass

    def mergeAnimPreloads(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        merge_anim_preloads(const PartBundle self, const PartBundle other)
        
        /**
         * Copies the contents of the other PartBundle's preload table into this one.
         */
        """
        pass

    def merge_anim_preloads(self, const_PartBundle_self, const_PartBundle_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        merge_anim_preloads(const PartBundle self, const PartBundle other)
        
        /**
         * Copies the contents of the other PartBundle's preload table into this one.
         */
        """
        pass

    def modifyAnimPreload(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_anim_preload(const PartBundle self)
        
        /**
         * Returns a modifiable pointer to the AnimPreloadTable associated with the
         * PartBundle, if any.
         */
        """
        pass

    def modify_anim_preload(self, const_PartBundle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_anim_preload(const PartBundle self)
        
        /**
         * Returns a modifiable pointer to the AnimPreloadTable associated with the
         * PartBundle, if any.
         */
        """
        pass

    def output(self, PartBundle_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(PartBundle self, ostream out)
        
        /**
         * Writes a one-line description of the bundle.
         */
        """
        pass

    def releaseJoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_joint(const PartBundle self, str joint_name)
        
        /**
         * Releases the named joint from the effects of a previous call to
         * freeze_joint() or control_joint(). It will henceforth once again follow
         * whatever transforms are dictated by the animation.
         *
         * Returns true if the joint is released, or false if the named child was not
         * previously controlled or frozen, or it does not exist.
         */
        """
        pass

    def release_joint(self, const_PartBundle_self, str_joint_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_joint(const PartBundle self, str joint_name)
        
        /**
         * Releases the named joint from the effects of a previous call to
         * freeze_joint() or control_joint(). It will henceforth once again follow
         * whatever transforms are dictated by the animation.
         *
         * Returns true if the joint is released, or false if the named child was not
         * previously controlled or frozen, or it does not exist.
         */
        """
        pass

    def setAnimBlendFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_anim_blend_flag(const PartBundle self, bool anim_blend_flag)
        
        /**
         * Defines the way the character responds to multiple calls to
         * set_control_effect()).  By default, this flag is set false, which disallows
         * multiple animations.  When this flag is false, it is not necessary to
         * explicitly set the control_effect when starting an animation; starting the
         * animation will implicitly remove the control_effect from the previous
         * animation and set it on the current one.
         *
         * However, if this flag is set true, the control_effect must be explicitly
         * set via set_control_effect() whenever an animation is to affect the
         * character.
         */
        """
        pass

    def setAnimPreload(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_anim_preload(const PartBundle self, AnimPreloadTable table)
        
        /**
         * Replaces the AnimPreloadTable associated with the PartBundle.
         */
        """
        pass

    def setBlendType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_blend_type(const PartBundle self, int bt)
        
        /**
         * Defines the algorithm that is used when blending multiple frames or
         * multiple animations together, when either anim_blend_flag or
         * frame_blend_flag is set to true.
         *
         * See partBundle.h for a description of the meaning of each of the BlendType
         * values.
         */
        """
        pass

    def setControlEffect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_control_effect(const PartBundle self, AnimControl control, float effect)
        
        /**
         * Sets the amount by which the character is affected by the indicated
         * AnimControl (and its associated animation).  Normally, this will only be
         * zero or one.  Zero indicates the animation does not affect the character,
         * and one means it does.
         *
         * If the _anim_blend_flag is not false (see set_anim_blend_flag()), it is
         * possible to have multiple AnimControls in effect simultaneously.  In this
         * case, the effect is a weight that indicates the relative importance of each
         * AnimControl to the final animation.
         */
        """
        pass

    def setFrameBlendFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame_blend_flag(const PartBundle self, bool frame_blend_flag)
        
        /**
         * Specifies whether the character interpolates (blends) between two
         * sequential frames of an active animation, showing a smooth intra-frame
         * motion, or whether it holds each frame until the next frame is ready,
         * showing precisely the specified animation.
         *
         * When this value is false, the character holds each frame until the next is
         * ready.  When this is true, the character will interpolate between two
         * consecutive frames of animation for each frame the animation is onscreen,
         * according to the amount of time elapsed between the frames.
         *
         * The default value of this flag is determined by the interpolate-frames
         * Config.prc variable.
         *
         * Use set_blend_type() to change the algorithm that the character uses to
         * interpolate matrix positions.
         */
        """
        pass

    def setRootXform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_root_xform(const PartBundle self, const LMatrix4f root_xform)
        
        /**
         * Specifies the transform matrix which is implicitly applied at the root of
         * the animated hierarchy.
         */
        """
        pass

    def set_anim_blend_flag(self, const_PartBundle_self, bool_anim_blend_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_anim_blend_flag(const PartBundle self, bool anim_blend_flag)
        
        /**
         * Defines the way the character responds to multiple calls to
         * set_control_effect()).  By default, this flag is set false, which disallows
         * multiple animations.  When this flag is false, it is not necessary to
         * explicitly set the control_effect when starting an animation; starting the
         * animation will implicitly remove the control_effect from the previous
         * animation and set it on the current one.
         *
         * However, if this flag is set true, the control_effect must be explicitly
         * set via set_control_effect() whenever an animation is to affect the
         * character.
         */
        """
        pass

    def set_anim_preload(self, const_PartBundle_self, AnimPreloadTable_table): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_anim_preload(const PartBundle self, AnimPreloadTable table)
        
        /**
         * Replaces the AnimPreloadTable associated with the PartBundle.
         */
        """
        pass

    def set_blend_type(self, const_PartBundle_self, int_bt): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_blend_type(const PartBundle self, int bt)
        
        /**
         * Defines the algorithm that is used when blending multiple frames or
         * multiple animations together, when either anim_blend_flag or
         * frame_blend_flag is set to true.
         *
         * See partBundle.h for a description of the meaning of each of the BlendType
         * values.
         */
        """
        pass

    def set_control_effect(self, const_PartBundle_self, AnimControl_control, float_effect): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_control_effect(const PartBundle self, AnimControl control, float effect)
        
        /**
         * Sets the amount by which the character is affected by the indicated
         * AnimControl (and its associated animation).  Normally, this will only be
         * zero or one.  Zero indicates the animation does not affect the character,
         * and one means it does.
         *
         * If the _anim_blend_flag is not false (see set_anim_blend_flag()), it is
         * possible to have multiple AnimControls in effect simultaneously.  In this
         * case, the effect is a weight that indicates the relative importance of each
         * AnimControl to the final animation.
         */
        """
        pass

    def set_frame_blend_flag(self, const_PartBundle_self, bool_frame_blend_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame_blend_flag(const PartBundle self, bool frame_blend_flag)
        
        /**
         * Specifies whether the character interpolates (blends) between two
         * sequential frames of an active animation, showing a smooth intra-frame
         * motion, or whether it holds each frame until the next frame is ready,
         * showing precisely the specified animation.
         *
         * When this value is false, the character holds each frame until the next is
         * ready.  When this is true, the character will interpolate between two
         * consecutive frames of animation for each frame the animation is onscreen,
         * according to the amount of time elapsed between the frames.
         *
         * The default value of this flag is determined by the interpolate-frames
         * Config.prc variable.
         *
         * Use set_blend_type() to change the algorithm that the character uses to
         * interpolate matrix positions.
         */
        """
        pass

    def set_root_xform(self, const_PartBundle_self, const_LMatrix4f_root_xform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_root_xform(const PartBundle self, const LMatrix4f root_xform)
        
        /**
         * Specifies the transform matrix which is implicitly applied at the root of
         * the animated hierarchy.
         */
        """
        pass

    def update(self, const_PartBundle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update(const PartBundle self)
        
        /**
         * Updates all the parts in the bundle to reflect the data for the current
         * frame (as set in each of the AnimControls).
         *
         * Returns true if any part has changed as a result of this, or false
         * otherwise.
         */
        """
        pass

    def waitPending(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        wait_pending(const PartBundle self)
        
        /**
         * Blocks the current thread until all currently-pending AnimControls, with a
         * nonzero control effect, have been loaded and are properly bound.
         */
        """
        pass

    def wait_pending(self, const_PartBundle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        wait_pending(const PartBundle self)
        
        /**
         * Blocks the current thread until all currently-pending AnimControls, with a
         * nonzero control effect, have been loaded and are properly bound.
         */
        """
        pass

    def xform(self, const_PartBundle_self, const_LMatrix4f_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform(const PartBundle self, const LMatrix4f mat)
        
        /**
         * Applies the indicated transform to the root of the animated hierarchy.
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

    anim_blend_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blend_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame_blend_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    root_xform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    BTComponentwise = 2
    BTComponentwiseQuat = 3
    BTLinear = 0
    BTNormalizedLinear = 1
    BT_componentwise = 2
    BT_componentwise_quat = 3
    BT_linear = 0
    BT_normalized_linear = 1
    DtoolClassDict = {
        'BTComponentwise': 2,
        'BTComponentwiseQuat': 3,
        'BTLinear': 0,
        'BTNormalizedLinear': 1,
        'BT_componentwise': 2,
        'BT_componentwise_quat': 3,
        'BT_linear': 0,
        'BT_normalized_linear': 1,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This is the root of a MovingPart hierarchy.  It defines the hierarchy of\n * moving parts that make up an animatable object.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PartBundle' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2C4770>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.PartBundle' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.PartBundle' objects>"
        'anim_blend_flag': None, # (!) real value is "<attribute 'anim_blend_flag' of 'panda3d.core.PartBundle' objects>"
        'applyTransform': None, # (!) real value is "<method 'applyTransform' of 'panda3d.core.PartBundle' objects>"
        'apply_transform': None, # (!) real value is "<method 'apply_transform' of 'panda3d.core.PartBundle' objects>"
        'bindAnim': None, # (!) real value is "<method 'bindAnim' of 'panda3d.core.PartBundle' objects>"
        'bind_anim': None, # (!) real value is "<method 'bind_anim' of 'panda3d.core.PartBundle' objects>"
        'blend_type': None, # (!) real value is "<attribute 'blend_type' of 'panda3d.core.PartBundle' objects>"
        'clearAnimPreload': None, # (!) real value is "<method 'clearAnimPreload' of 'panda3d.core.PartBundle' objects>"
        'clearControlEffects': None, # (!) real value is "<method 'clearControlEffects' of 'panda3d.core.PartBundle' objects>"
        'clear_anim_preload': None, # (!) real value is "<method 'clear_anim_preload' of 'panda3d.core.PartBundle' objects>"
        'clear_control_effects': None, # (!) real value is "<method 'clear_control_effects' of 'panda3d.core.PartBundle' objects>"
        'controlJoint': None, # (!) real value is "<method 'controlJoint' of 'panda3d.core.PartBundle' objects>"
        'control_joint': None, # (!) real value is "<method 'control_joint' of 'panda3d.core.PartBundle' objects>"
        'forceUpdate': None, # (!) real value is "<method 'forceUpdate' of 'panda3d.core.PartBundle' objects>"
        'force_update': None, # (!) real value is "<method 'force_update' of 'panda3d.core.PartBundle' objects>"
        'frame_blend_flag': None, # (!) real value is "<attribute 'frame_blend_flag' of 'panda3d.core.PartBundle' objects>"
        'freezeJoint': None, # (!) real value is "<method 'freezeJoint' of 'panda3d.core.PartBundle' objects>"
        'freeze_joint': None, # (!) real value is "<method 'freeze_joint' of 'panda3d.core.PartBundle' objects>"
        'getAnimBlendFlag': None, # (!) real value is "<method 'getAnimBlendFlag' of 'panda3d.core.PartBundle' objects>"
        'getAnimPreload': None, # (!) real value is "<method 'getAnimPreload' of 'panda3d.core.PartBundle' objects>"
        'getBlendType': None, # (!) real value is "<method 'getBlendType' of 'panda3d.core.PartBundle' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2C4770>)>'
        'getControlEffect': None, # (!) real value is "<method 'getControlEffect' of 'panda3d.core.PartBundle' objects>"
        'getFrameBlendFlag': None, # (!) real value is "<method 'getFrameBlendFlag' of 'panda3d.core.PartBundle' objects>"
        'getNode': None, # (!) real value is "<method 'getNode' of 'panda3d.core.PartBundle' objects>"
        'getNodes': None, # (!) real value is "<method 'getNodes' of 'panda3d.core.PartBundle' objects>"
        'getNumNodes': None, # (!) real value is "<method 'getNumNodes' of 'panda3d.core.PartBundle' objects>"
        'getRootXform': None, # (!) real value is "<method 'getRootXform' of 'panda3d.core.PartBundle' objects>"
        'get_anim_blend_flag': None, # (!) real value is "<method 'get_anim_blend_flag' of 'panda3d.core.PartBundle' objects>"
        'get_anim_preload': None, # (!) real value is "<method 'get_anim_preload' of 'panda3d.core.PartBundle' objects>"
        'get_blend_type': None, # (!) real value is "<method 'get_blend_type' of 'panda3d.core.PartBundle' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2C4770>)>'
        'get_control_effect': None, # (!) real value is "<method 'get_control_effect' of 'panda3d.core.PartBundle' objects>"
        'get_frame_blend_flag': None, # (!) real value is "<method 'get_frame_blend_flag' of 'panda3d.core.PartBundle' objects>"
        'get_node': None, # (!) real value is "<method 'get_node' of 'panda3d.core.PartBundle' objects>"
        'get_nodes': None, # (!) real value is "<method 'get_nodes' of 'panda3d.core.PartBundle' objects>"
        'get_num_nodes': None, # (!) real value is "<method 'get_num_nodes' of 'panda3d.core.PartBundle' objects>"
        'get_root_xform': None, # (!) real value is "<method 'get_root_xform' of 'panda3d.core.PartBundle' objects>"
        'loadBindAnim': None, # (!) real value is "<method 'loadBindAnim' of 'panda3d.core.PartBundle' objects>"
        'load_bind_anim': None, # (!) real value is "<method 'load_bind_anim' of 'panda3d.core.PartBundle' objects>"
        'mergeAnimPreloads': None, # (!) real value is "<method 'mergeAnimPreloads' of 'panda3d.core.PartBundle' objects>"
        'merge_anim_preloads': None, # (!) real value is "<method 'merge_anim_preloads' of 'panda3d.core.PartBundle' objects>"
        'modifyAnimPreload': None, # (!) real value is "<method 'modifyAnimPreload' of 'panda3d.core.PartBundle' objects>"
        'modify_anim_preload': None, # (!) real value is "<method 'modify_anim_preload' of 'panda3d.core.PartBundle' objects>"
        'nodes': None, # (!) real value is "<attribute 'nodes' of 'panda3d.core.PartBundle' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.PartBundle' objects>"
        'releaseJoint': None, # (!) real value is "<method 'releaseJoint' of 'panda3d.core.PartBundle' objects>"
        'release_joint': None, # (!) real value is "<method 'release_joint' of 'panda3d.core.PartBundle' objects>"
        'root_xform': None, # (!) real value is "<attribute 'root_xform' of 'panda3d.core.PartBundle' objects>"
        'setAnimBlendFlag': None, # (!) real value is "<method 'setAnimBlendFlag' of 'panda3d.core.PartBundle' objects>"
        'setAnimPreload': None, # (!) real value is "<method 'setAnimPreload' of 'panda3d.core.PartBundle' objects>"
        'setBlendType': None, # (!) real value is "<method 'setBlendType' of 'panda3d.core.PartBundle' objects>"
        'setControlEffect': None, # (!) real value is "<method 'setControlEffect' of 'panda3d.core.PartBundle' objects>"
        'setFrameBlendFlag': None, # (!) real value is "<method 'setFrameBlendFlag' of 'panda3d.core.PartBundle' objects>"
        'setRootXform': None, # (!) real value is "<method 'setRootXform' of 'panda3d.core.PartBundle' objects>"
        'set_anim_blend_flag': None, # (!) real value is "<method 'set_anim_blend_flag' of 'panda3d.core.PartBundle' objects>"
        'set_anim_preload': None, # (!) real value is "<method 'set_anim_preload' of 'panda3d.core.PartBundle' objects>"
        'set_blend_type': None, # (!) real value is "<method 'set_blend_type' of 'panda3d.core.PartBundle' objects>"
        'set_control_effect': None, # (!) real value is "<method 'set_control_effect' of 'panda3d.core.PartBundle' objects>"
        'set_frame_blend_flag': None, # (!) real value is "<method 'set_frame_blend_flag' of 'panda3d.core.PartBundle' objects>"
        'set_root_xform': None, # (!) real value is "<method 'set_root_xform' of 'panda3d.core.PartBundle' objects>"
        'update': None, # (!) real value is "<method 'update' of 'panda3d.core.PartBundle' objects>"
        'waitPending': None, # (!) real value is "<method 'waitPending' of 'panda3d.core.PartBundle' objects>"
        'wait_pending': None, # (!) real value is "<method 'wait_pending' of 'panda3d.core.PartBundle' objects>"
        'xform': None, # (!) real value is "<method 'xform' of 'panda3d.core.PartBundle' objects>"
    }


