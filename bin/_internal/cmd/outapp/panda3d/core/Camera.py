# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .LensNode import LensNode

class Camera(LensNode):
    """
    /**
     * A node that can be positioned around in the scene graph to represent a
     * point of view for rendering a scene.
     */
    """
    def cleanupAuxSceneData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        cleanup_aux_scene_data(const Camera self, Thread current_thread)
        
        /**
         * Walks through the list of currently-assigned AuxSceneData objects and
         * releases any that are past their expiration times.  Returns the number of
         * elements released.
         */
        """
        pass

    def cleanup_aux_scene_data(self, const_Camera_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        cleanup_aux_scene_data(const Camera self, Thread current_thread)
        
        /**
         * Walks through the list of currently-assigned AuxSceneData objects and
         * releases any that are past their expiration times.  Returns the number of
         * elements released.
         */
        """
        pass

    def clearAuxSceneData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_aux_scene_data(const Camera self, const NodePath node_path)
        
        /**
         * Removes the AuxSceneData associated with the indicated NodePath.  Returns
         * true if it is removed successfully, false if it was already gone.
         */
        """
        pass

    def clearTagState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_tag_state(const Camera self, str tag_state)
        
        /**
         * Removes the association established by a previous call to set_tag_state().
         */
        """
        pass

    def clearTagStates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_tag_states(const Camera self)
        
        /**
         * Removes all associations established by previous calls to set_tag_state().
         */
        """
        pass

    def clear_aux_scene_data(self, const_Camera_self, const_NodePath_node_path): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_aux_scene_data(const Camera self, const NodePath node_path)
        
        /**
         * Removes the AuxSceneData associated with the indicated NodePath.  Returns
         * true if it is removed successfully, false if it was already gone.
         */
        """
        pass

    def clear_tag_state(self, const_Camera_self, str_tag_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_tag_state(const Camera self, str tag_state)
        
        /**
         * Removes the association established by a previous call to set_tag_state().
         */
        """
        pass

    def clear_tag_states(self, const_Camera_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_tag_states(const Camera self)
        
        /**
         * Removes all associations established by previous calls to set_tag_state().
         */
        """
        pass

    def getAuxSceneData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_aux_scene_data(Camera self, const NodePath node_path)
        
        /**
         * Returns the AuxSceneData associated with the indicated NodePath, or NULL if
         * nothing is associated.
         */
        """
        pass

    def getCameraMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_camera_mask(Camera self)
        
        /**
         * Returns the set of bits that represent the subset of the scene graph the
         * camera will render.  See set_camera_mask().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCullBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cull_bounds(Camera self)
        
        /**
         * Returns the custom cull volume that was set by set_cull_bounds(), if any,
         * or NULL if no custom cull volume was set.
         */
        """
        pass

    def getCullCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cull_center(Camera self)
        
        /**
         * Returns the point from which the culling operations will be performed, if
         * it was set by set_cull_center(), or the empty NodePath otherwise.
         */
        """
        pass

    def getDisplayRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_display_region(Camera self, int n)
        
        /**
         * Returns the nth display region associated with the camera.
         */
        """
        pass

    def getDisplayRegions(self, *args, **kwargs): # real signature unknown
        pass

    def getInitialState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_initial_state(Camera self)
        
        /**
         * Returns the initial state as set by a previous call to set_initial_state().
         */
        """
        pass

    def getLodCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lod_center(Camera self)
        
        /**
         * Returns the point from which the LOD distances will be measured, if it was
         * set by set_lod_center(), or the empty NodePath otherwise.
         */
        """
        pass

    def getLodScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lod_scale(Camera self)
        
        /**
         * Returns the multiplier for LOD distances.
         */
        """
        pass

    def getNumDisplayRegions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_display_regions(Camera self)
        
        /**
         * Returns the number of display regions associated with the camera.
         */
        """
        pass

    def getScene(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scene(Camera self)
        
        /**
         * Returns the scene that will be rendered by the camera.  See set_scene().
         */
        """
        pass

    def getTagState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tag_state(Camera self, str tag_state)
        
        /**
         * Returns the state associated with the indicated tag state by a previous
         * call to set_tag_state(), or the empty state if nothing has been associated.
         */
        """
        pass

    def getTagStateKey(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tag_state_key(Camera self)
        
        /**
         * Returns the tag key as set by a previous call to set_tag_state_key().
         */
        """
        pass

    def get_aux_scene_data(self, Camera_self, const_NodePath_node_path): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_aux_scene_data(Camera self, const NodePath node_path)
        
        /**
         * Returns the AuxSceneData associated with the indicated NodePath, or NULL if
         * nothing is associated.
         */
        """
        pass

    def get_camera_mask(self, Camera_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_camera_mask(Camera self)
        
        /**
         * Returns the set of bits that represent the subset of the scene graph the
         * camera will render.  See set_camera_mask().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_cull_bounds(self, Camera_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cull_bounds(Camera self)
        
        /**
         * Returns the custom cull volume that was set by set_cull_bounds(), if any,
         * or NULL if no custom cull volume was set.
         */
        """
        pass

    def get_cull_center(self, Camera_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cull_center(Camera self)
        
        /**
         * Returns the point from which the culling operations will be performed, if
         * it was set by set_cull_center(), or the empty NodePath otherwise.
         */
        """
        pass

    def get_display_region(self, Camera_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_display_region(Camera self, int n)
        
        /**
         * Returns the nth display region associated with the camera.
         */
        """
        pass

    def get_display_regions(self, *args, **kwargs): # real signature unknown
        pass

    def get_initial_state(self, Camera_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_initial_state(Camera self)
        
        /**
         * Returns the initial state as set by a previous call to set_initial_state().
         */
        """
        pass

    def get_lod_center(self, Camera_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lod_center(Camera self)
        
        /**
         * Returns the point from which the LOD distances will be measured, if it was
         * set by set_lod_center(), or the empty NodePath otherwise.
         */
        """
        pass

    def get_lod_scale(self, Camera_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lod_scale(Camera self)
        
        /**
         * Returns the multiplier for LOD distances.
         */
        """
        pass

    def get_num_display_regions(self, Camera_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_display_regions(Camera self)
        
        /**
         * Returns the number of display regions associated with the camera.
         */
        """
        pass

    def get_scene(self, Camera_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scene(Camera self)
        
        /**
         * Returns the scene that will be rendered by the camera.  See set_scene().
         */
        """
        pass

    def get_tag_state(self, Camera_self, str_tag_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tag_state(Camera self, str tag_state)
        
        /**
         * Returns the state associated with the indicated tag state by a previous
         * call to set_tag_state(), or the empty state if nothing has been associated.
         */
        """
        pass

    def get_tag_state_key(self, Camera_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tag_state_key(Camera self)
        
        /**
         * Returns the tag key as set by a previous call to set_tag_state_key().
         */
        """
        pass

    def hasTagState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_tag_state(Camera self, str tag_state)
        
        /**
         * Returns true if set_tag_state() has previously been called with the
         * indicated tag state, false otherwise.
         */
        """
        pass

    def has_tag_state(self, Camera_self, str_tag_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_tag_state(Camera self, str tag_state)
        
        /**
         * Returns true if set_tag_state() has previously been called with the
         * indicated tag state, false otherwise.
         */
        """
        pass

    def isActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_active(Camera self)
        
        /**
         * Returns the current setting of the active flag on the camera.
         */
        """
        pass

    def is_active(self, Camera_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_active(Camera self)
        
        /**
         * Returns the current setting of the active flag on the camera.
         */
        """
        pass

    def listAuxSceneData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        list_aux_scene_data(Camera self, ostream out)
        
        /**
         * Outputs all of the NodePaths and AuxSceneDatas in use.
         */
        """
        pass

    def list_aux_scene_data(self, Camera_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        list_aux_scene_data(Camera self, ostream out)
        
        /**
         * Outputs all of the NodePaths and AuxSceneDatas in use.
         */
        """
        pass

    def setActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_active(const Camera self, bool active)
        
        /**
         * Sets the active flag on the camera.  When the camera is not active, nothing
         * will be rendered.
         */
        """
        pass

    def setAuxSceneData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_aux_scene_data(const Camera self, const NodePath node_path, AuxSceneData data)
        
        /**
         * Associates the indicated AuxSceneData object with the given NodePath,
         * possibly replacing a previous data defined for the same NodePath, if any.
         */
        """
        pass

    def setCameraMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_camera_mask(const Camera self, BitMask mask)
        
        /**
         * Changes the set of bits that represent the subset of the scene graph the
         * camera will render.
         *
         * During the cull traversal, a node is not visited if none of its draw mask
         * bits intersect with the camera's camera mask bits.  These masks can be used
         * to selectively hide and show different parts of the scene graph from
         * different cameras that are otherwise viewing the same scene.
         */
        """
        pass

    def setCullBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cull_bounds(const Camera self, BoundingVolume cull_bounds)
        
        /**
         * Specifies the bounding volume that should be used to perform culling from
         * this camera.  Normally, this is the bounding volume returned from the
         * active lens' make_bounds() call, but you may override this to specify a
         * custom volume if you require.  The specified bounding volume will be
         * understood to be in the coordinate space of the get_cull_center() node.
         */
        """
        pass

    def setCullCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cull_center(const Camera self, const NodePath cull_center)
        
        /**
         * Specifies the point from which the culling operations are performed.
         * Normally, this is the same as the camera, and that is the default if this
         * is not specified; but it may sometimes be useful to perform the culling
         * from some other viewpoint, particularly when you are debugging the culling
         * itself.
         */
        """
        pass

    def setInitialState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_initial_state(const Camera self, const RenderState state)
        
        /**
         * Sets the initial state which is applied to all nodes in the scene, as if it
         * were set at the top of the scene graph.
         */
        """
        pass

    def setLodCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_lod_center(const Camera self, const NodePath lod_center)
        
        /**
         * Specifies the point from which the LOD distances are measured.  Normally,
         * this is the same as the camera, and that is the default if this is not
         * specified; but it may sometimes be useful to perform the distance test from
         * some other viewpoint.  This may be used, for instance, to reduce LOD
         * popping when the camera rotates in a small circle about an avatar.
         */
        """
        pass

    def setLodScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_lod_scale(const Camera self, float value)
        
        /**
         * Sets the multiplier for LOD distances.  This value is multiplied with the
         * LOD scale set on LodNodes.
         */
        """
        pass

    def setScene(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scene(const Camera self, const NodePath scene)
        
        /**
         * Sets the scene that will be rendered by the camera.  This is normally the
         * root node of a scene graph, typically a node called 'render', although it
         * could represent the root of any subgraph.
         *
         * Note that the use of this method is now deprecated.  In the absence of an
         * explicit scene set on the camera, the camera will render whatever scene it
         * is parented into.  This is the preferred way to specify the scene, since it
         * is the more intuitive mechanism.
         */
        """
        pass

    def setTagState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tag_state(const Camera self, str tag_state, const RenderState state)
        
        /**
         * Associates a particular state transition with the indicated tag value.
         * When a node is encountered during traversal with the tag key specified by
         * set_tag_state_key(), if the value of that tag matches tag_state, then the
         * indicated state is applied to this node--but only when it is rendered by
         * this camera.
         *
         * This can be used to apply special effects to nodes when they are rendered
         * by certain cameras.  It is particularly useful for multipass rendering, in
         * which specialty cameras might be needed to render the scene with a
         * particular set of effects.
         */
        """
        pass

    def setTagStateKey(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tag_state_key(const Camera self, str tag_state_key)
        
        /**
         * Sets the tag key which, when encountered as a tag on nodes in the scene
         * graph, causes this Camera to apply an arbitrary state transition based on
         * the value of the tag (as specified to set_tag_state()).
         */
        """
        pass

    def set_active(self, const_Camera_self, bool_active): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_active(const Camera self, bool active)
        
        /**
         * Sets the active flag on the camera.  When the camera is not active, nothing
         * will be rendered.
         */
        """
        pass

    def set_aux_scene_data(self, const_Camera_self, const_NodePath_node_path, AuxSceneData_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_aux_scene_data(const Camera self, const NodePath node_path, AuxSceneData data)
        
        /**
         * Associates the indicated AuxSceneData object with the given NodePath,
         * possibly replacing a previous data defined for the same NodePath, if any.
         */
        """
        pass

    def set_camera_mask(self, const_Camera_self, BitMask_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_camera_mask(const Camera self, BitMask mask)
        
        /**
         * Changes the set of bits that represent the subset of the scene graph the
         * camera will render.
         *
         * During the cull traversal, a node is not visited if none of its draw mask
         * bits intersect with the camera's camera mask bits.  These masks can be used
         * to selectively hide and show different parts of the scene graph from
         * different cameras that are otherwise viewing the same scene.
         */
        """
        pass

    def set_cull_bounds(self, const_Camera_self, BoundingVolume_cull_bounds): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cull_bounds(const Camera self, BoundingVolume cull_bounds)
        
        /**
         * Specifies the bounding volume that should be used to perform culling from
         * this camera.  Normally, this is the bounding volume returned from the
         * active lens' make_bounds() call, but you may override this to specify a
         * custom volume if you require.  The specified bounding volume will be
         * understood to be in the coordinate space of the get_cull_center() node.
         */
        """
        pass

    def set_cull_center(self, const_Camera_self, const_NodePath_cull_center): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cull_center(const Camera self, const NodePath cull_center)
        
        /**
         * Specifies the point from which the culling operations are performed.
         * Normally, this is the same as the camera, and that is the default if this
         * is not specified; but it may sometimes be useful to perform the culling
         * from some other viewpoint, particularly when you are debugging the culling
         * itself.
         */
        """
        pass

    def set_initial_state(self, const_Camera_self, const_RenderState_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_initial_state(const Camera self, const RenderState state)
        
        /**
         * Sets the initial state which is applied to all nodes in the scene, as if it
         * were set at the top of the scene graph.
         */
        """
        pass

    def set_lod_center(self, const_Camera_self, const_NodePath_lod_center): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_lod_center(const Camera self, const NodePath lod_center)
        
        /**
         * Specifies the point from which the LOD distances are measured.  Normally,
         * this is the same as the camera, and that is the default if this is not
         * specified; but it may sometimes be useful to perform the distance test from
         * some other viewpoint.  This may be used, for instance, to reduce LOD
         * popping when the camera rotates in a small circle about an avatar.
         */
        """
        pass

    def set_lod_scale(self, const_Camera_self, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_lod_scale(const Camera self, float value)
        
        /**
         * Sets the multiplier for LOD distances.  This value is multiplied with the
         * LOD scale set on LodNodes.
         */
        """
        pass

    def set_scene(self, const_Camera_self, const_NodePath_scene): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scene(const Camera self, const NodePath scene)
        
        /**
         * Sets the scene that will be rendered by the camera.  This is normally the
         * root node of a scene graph, typically a node called 'render', although it
         * could represent the root of any subgraph.
         *
         * Note that the use of this method is now deprecated.  In the absence of an
         * explicit scene set on the camera, the camera will render whatever scene it
         * is parented into.  This is the preferred way to specify the scene, since it
         * is the more intuitive mechanism.
         */
        """
        pass

    def set_tag_state(self, const_Camera_self, str_tag_state, const_RenderState_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tag_state(const Camera self, str tag_state, const RenderState state)
        
        /**
         * Associates a particular state transition with the indicated tag value.
         * When a node is encountered during traversal with the tag key specified by
         * set_tag_state_key(), if the value of that tag matches tag_state, then the
         * indicated state is applied to this node--but only when it is rendered by
         * this camera.
         *
         * This can be used to apply special effects to nodes when they are rendered
         * by certain cameras.  It is particularly useful for multipass rendering, in
         * which specialty cameras might be needed to render the scene with a
         * particular set of effects.
         */
        """
        pass

    def set_tag_state_key(self, const_Camera_self, str_tag_state_key): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tag_state_key(const Camera self, str tag_state_key)
        
        /**
         * Sets the tag key which, when encountered as a tag on nodes in the scene
         * graph, causes this Camera to apply an arbitrary state transition based on
         * the value of the tag (as specified to set_tag_state()).
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

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    aux_scene_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    camera_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cull_bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cull_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    display_regions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lod_center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lod_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scene = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tag_states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tag_state_key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Camera' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Camera' objects>"
        '__doc__': '/**\n * A node that can be positioned around in the scene graph to represent a\n * point of view for rendering a scene.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Camera' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE294C90>'
        'active': None, # (!) real value is "<attribute 'active' of 'panda3d.core.Camera' objects>"
        'aux_scene_data': None, # (!) real value is "<attribute 'aux_scene_data' of 'panda3d.core.Camera' objects>"
        'camera_mask': None, # (!) real value is "<attribute 'camera_mask' of 'panda3d.core.Camera' objects>"
        'cleanupAuxSceneData': None, # (!) real value is "<method 'cleanupAuxSceneData' of 'panda3d.core.Camera' objects>"
        'cleanup_aux_scene_data': None, # (!) real value is "<method 'cleanup_aux_scene_data' of 'panda3d.core.Camera' objects>"
        'clearAuxSceneData': None, # (!) real value is "<method 'clearAuxSceneData' of 'panda3d.core.Camera' objects>"
        'clearTagState': None, # (!) real value is "<method 'clearTagState' of 'panda3d.core.Camera' objects>"
        'clearTagStates': None, # (!) real value is "<method 'clearTagStates' of 'panda3d.core.Camera' objects>"
        'clear_aux_scene_data': None, # (!) real value is "<method 'clear_aux_scene_data' of 'panda3d.core.Camera' objects>"
        'clear_tag_state': None, # (!) real value is "<method 'clear_tag_state' of 'panda3d.core.Camera' objects>"
        'clear_tag_states': None, # (!) real value is "<method 'clear_tag_states' of 'panda3d.core.Camera' objects>"
        'cull_bounds': None, # (!) real value is "<attribute 'cull_bounds' of 'panda3d.core.Camera' objects>"
        'cull_center': None, # (!) real value is "<attribute 'cull_center' of 'panda3d.core.Camera' objects>"
        'display_regions': None, # (!) real value is "<attribute 'display_regions' of 'panda3d.core.Camera' objects>"
        'getAuxSceneData': None, # (!) real value is "<method 'getAuxSceneData' of 'panda3d.core.Camera' objects>"
        'getCameraMask': None, # (!) real value is "<method 'getCameraMask' of 'panda3d.core.Camera' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE294C90>)>'
        'getCullBounds': None, # (!) real value is "<method 'getCullBounds' of 'panda3d.core.Camera' objects>"
        'getCullCenter': None, # (!) real value is "<method 'getCullCenter' of 'panda3d.core.Camera' objects>"
        'getDisplayRegion': None, # (!) real value is "<method 'getDisplayRegion' of 'panda3d.core.Camera' objects>"
        'getDisplayRegions': None, # (!) real value is "<method 'getDisplayRegions' of 'panda3d.core.Camera' objects>"
        'getInitialState': None, # (!) real value is "<method 'getInitialState' of 'panda3d.core.Camera' objects>"
        'getLodCenter': None, # (!) real value is "<method 'getLodCenter' of 'panda3d.core.Camera' objects>"
        'getLodScale': None, # (!) real value is "<method 'getLodScale' of 'panda3d.core.Camera' objects>"
        'getNumDisplayRegions': None, # (!) real value is "<method 'getNumDisplayRegions' of 'panda3d.core.Camera' objects>"
        'getScene': None, # (!) real value is "<method 'getScene' of 'panda3d.core.Camera' objects>"
        'getTagState': None, # (!) real value is "<method 'getTagState' of 'panda3d.core.Camera' objects>"
        'getTagStateKey': None, # (!) real value is "<method 'getTagStateKey' of 'panda3d.core.Camera' objects>"
        'get_aux_scene_data': None, # (!) real value is "<method 'get_aux_scene_data' of 'panda3d.core.Camera' objects>"
        'get_camera_mask': None, # (!) real value is "<method 'get_camera_mask' of 'panda3d.core.Camera' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE294C90>)>'
        'get_cull_bounds': None, # (!) real value is "<method 'get_cull_bounds' of 'panda3d.core.Camera' objects>"
        'get_cull_center': None, # (!) real value is "<method 'get_cull_center' of 'panda3d.core.Camera' objects>"
        'get_display_region': None, # (!) real value is "<method 'get_display_region' of 'panda3d.core.Camera' objects>"
        'get_display_regions': None, # (!) real value is "<method 'get_display_regions' of 'panda3d.core.Camera' objects>"
        'get_initial_state': None, # (!) real value is "<method 'get_initial_state' of 'panda3d.core.Camera' objects>"
        'get_lod_center': None, # (!) real value is "<method 'get_lod_center' of 'panda3d.core.Camera' objects>"
        'get_lod_scale': None, # (!) real value is "<method 'get_lod_scale' of 'panda3d.core.Camera' objects>"
        'get_num_display_regions': None, # (!) real value is "<method 'get_num_display_regions' of 'panda3d.core.Camera' objects>"
        'get_scene': None, # (!) real value is "<method 'get_scene' of 'panda3d.core.Camera' objects>"
        'get_tag_state': None, # (!) real value is "<method 'get_tag_state' of 'panda3d.core.Camera' objects>"
        'get_tag_state_key': None, # (!) real value is "<method 'get_tag_state_key' of 'panda3d.core.Camera' objects>"
        'hasTagState': None, # (!) real value is "<method 'hasTagState' of 'panda3d.core.Camera' objects>"
        'has_tag_state': None, # (!) real value is "<method 'has_tag_state' of 'panda3d.core.Camera' objects>"
        'initial_state': None, # (!) real value is "<attribute 'initial_state' of 'panda3d.core.Camera' objects>"
        'isActive': None, # (!) real value is "<method 'isActive' of 'panda3d.core.Camera' objects>"
        'is_active': None, # (!) real value is "<method 'is_active' of 'panda3d.core.Camera' objects>"
        'listAuxSceneData': None, # (!) real value is "<method 'listAuxSceneData' of 'panda3d.core.Camera' objects>"
        'list_aux_scene_data': None, # (!) real value is "<method 'list_aux_scene_data' of 'panda3d.core.Camera' objects>"
        'lod_center': None, # (!) real value is "<attribute 'lod_center' of 'panda3d.core.Camera' objects>"
        'lod_scale': None, # (!) real value is "<attribute 'lod_scale' of 'panda3d.core.Camera' objects>"
        'scene': None, # (!) real value is "<attribute 'scene' of 'panda3d.core.Camera' objects>"
        'setActive': None, # (!) real value is "<method 'setActive' of 'panda3d.core.Camera' objects>"
        'setAuxSceneData': None, # (!) real value is "<method 'setAuxSceneData' of 'panda3d.core.Camera' objects>"
        'setCameraMask': None, # (!) real value is "<method 'setCameraMask' of 'panda3d.core.Camera' objects>"
        'setCullBounds': None, # (!) real value is "<method 'setCullBounds' of 'panda3d.core.Camera' objects>"
        'setCullCenter': None, # (!) real value is "<method 'setCullCenter' of 'panda3d.core.Camera' objects>"
        'setInitialState': None, # (!) real value is "<method 'setInitialState' of 'panda3d.core.Camera' objects>"
        'setLodCenter': None, # (!) real value is "<method 'setLodCenter' of 'panda3d.core.Camera' objects>"
        'setLodScale': None, # (!) real value is "<method 'setLodScale' of 'panda3d.core.Camera' objects>"
        'setScene': None, # (!) real value is "<method 'setScene' of 'panda3d.core.Camera' objects>"
        'setTagState': None, # (!) real value is "<method 'setTagState' of 'panda3d.core.Camera' objects>"
        'setTagStateKey': None, # (!) real value is "<method 'setTagStateKey' of 'panda3d.core.Camera' objects>"
        'set_active': None, # (!) real value is "<method 'set_active' of 'panda3d.core.Camera' objects>"
        'set_aux_scene_data': None, # (!) real value is "<method 'set_aux_scene_data' of 'panda3d.core.Camera' objects>"
        'set_camera_mask': None, # (!) real value is "<method 'set_camera_mask' of 'panda3d.core.Camera' objects>"
        'set_cull_bounds': None, # (!) real value is "<method 'set_cull_bounds' of 'panda3d.core.Camera' objects>"
        'set_cull_center': None, # (!) real value is "<method 'set_cull_center' of 'panda3d.core.Camera' objects>"
        'set_initial_state': None, # (!) real value is "<method 'set_initial_state' of 'panda3d.core.Camera' objects>"
        'set_lod_center': None, # (!) real value is "<method 'set_lod_center' of 'panda3d.core.Camera' objects>"
        'set_lod_scale': None, # (!) real value is "<method 'set_lod_scale' of 'panda3d.core.Camera' objects>"
        'set_scene': None, # (!) real value is "<method 'set_scene' of 'panda3d.core.Camera' objects>"
        'set_tag_state': None, # (!) real value is "<method 'set_tag_state' of 'panda3d.core.Camera' objects>"
        'set_tag_state_key': None, # (!) real value is "<method 'set_tag_state_key' of 'panda3d.core.Camera' objects>"
        'tag_state_key': None, # (!) real value is "<attribute 'tag_state_key' of 'panda3d.core.Camera' objects>"
        'tag_states': None, # (!) real value is "<attribute 'tag_states' of 'panda3d.core.Camera' objects>"
    }


