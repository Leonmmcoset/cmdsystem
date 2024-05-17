# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class SceneSetup(TypedReferenceCount):
    """
    /**
     * This object holds the camera position, etc., and other general setup
     * information for rendering a particular scene.
     */
    """
    def getCameraNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_camera_node(SceneSetup self)
        
        /**
         * Returns the camera used to render the scene.
         */
        """
        pass

    def getCameraPath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_camera_path(SceneSetup self)
        
        /**
         * Returns the NodePath to the camera.
         */
        """
        pass

    def getCameraTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_camera_transform(SceneSetup self)
        
        /**
         * Returns the position of the camera relative to the starting node.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCsTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cs_transform(SceneSetup self)
        
        /**
         * Returns the transform from the camera's coordinate system to the GSG's
         * internal coordinate system.
         */
        """
        pass

    def getCsWorldTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cs_world_transform(SceneSetup self)
        
        /**
         * Returns the position from the starting node relative to the camera, in the
         * GSG's internal coordinate system.
         */
        """
        pass

    def getCullBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cull_bounds(SceneSetup self)
        
        /**
         * Returns the bounding volume that should be used to perform view-frustum
         * culling (in the space of get_cull_center()).  This is normally the current
         * lens' bounding volume, but it may be overridden with
         * Camera::set_cull_bounds().
         */
        """
        pass

    def getCullCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cull_center(SceneSetup self)
        
        /**
         * Returns the point from which the culling operations will be performed.
         * This is normally the camera, but if camera->set_cull_center() has been
         * specified, it will be that special node instead.
         */
        """
        pass

    def getDisplayRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_display_region(SceneSetup self)
        
        /**
         * Returns the display region for the scene.
         */
        """
        pass

    def getInitialState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_initial_state(SceneSetup self)
        
        /**
         * Returns the initial state as set by a previous call to set_initial_state().
         */
        """
        pass

    def getInverted(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_inverted(SceneSetup self)
        
        /**
         * Returns the current setting of the inverted flag.  When this is true, the
         * scene is rendered into the window upside-down, flipped like a mirror along
         * the X axis.
         */
        """
        pass

    def getLens(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lens(SceneSetup self)
        
        /**
         * Returns the particular Lens used for rendering.
         */
        """
        pass

    def getSceneRoot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scene_root(SceneSetup self)
        
        /**
         * Returns the root node of the scene.
         */
        """
        pass

    def getViewportHeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_viewport_height(SceneSetup self)
        
        /**
         * Returns the height of the viewport (display region) in pixels.
         */
        """
        pass

    def getViewportWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_viewport_width(SceneSetup self)
        
        /**
         * Returns the width of the viewport (display region) in pixels.
         */
        """
        pass

    def getWorldTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_world_transform(SceneSetup self)
        
        /**
         * Returns the position of the starting node relative to the camera.  This is
         * the inverse of the camera transform.
         */
        """
        pass

    def get_camera_node(self, SceneSetup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_camera_node(SceneSetup self)
        
        /**
         * Returns the camera used to render the scene.
         */
        """
        pass

    def get_camera_path(self, SceneSetup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_camera_path(SceneSetup self)
        
        /**
         * Returns the NodePath to the camera.
         */
        """
        pass

    def get_camera_transform(self, SceneSetup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_camera_transform(SceneSetup self)
        
        /**
         * Returns the position of the camera relative to the starting node.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_cs_transform(self, SceneSetup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cs_transform(SceneSetup self)
        
        /**
         * Returns the transform from the camera's coordinate system to the GSG's
         * internal coordinate system.
         */
        """
        pass

    def get_cs_world_transform(self, SceneSetup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cs_world_transform(SceneSetup self)
        
        /**
         * Returns the position from the starting node relative to the camera, in the
         * GSG's internal coordinate system.
         */
        """
        pass

    def get_cull_bounds(self, SceneSetup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cull_bounds(SceneSetup self)
        
        /**
         * Returns the bounding volume that should be used to perform view-frustum
         * culling (in the space of get_cull_center()).  This is normally the current
         * lens' bounding volume, but it may be overridden with
         * Camera::set_cull_bounds().
         */
        """
        pass

    def get_cull_center(self, SceneSetup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cull_center(SceneSetup self)
        
        /**
         * Returns the point from which the culling operations will be performed.
         * This is normally the camera, but if camera->set_cull_center() has been
         * specified, it will be that special node instead.
         */
        """
        pass

    def get_display_region(self, SceneSetup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_display_region(SceneSetup self)
        
        /**
         * Returns the display region for the scene.
         */
        """
        pass

    def get_initial_state(self, SceneSetup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_initial_state(SceneSetup self)
        
        /**
         * Returns the initial state as set by a previous call to set_initial_state().
         */
        """
        pass

    def get_inverted(self, SceneSetup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_inverted(SceneSetup self)
        
        /**
         * Returns the current setting of the inverted flag.  When this is true, the
         * scene is rendered into the window upside-down, flipped like a mirror along
         * the X axis.
         */
        """
        pass

    def get_lens(self, SceneSetup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lens(SceneSetup self)
        
        /**
         * Returns the particular Lens used for rendering.
         */
        """
        pass

    def get_scene_root(self, SceneSetup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scene_root(SceneSetup self)
        
        /**
         * Returns the root node of the scene.
         */
        """
        pass

    def get_viewport_height(self, SceneSetup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_viewport_height(SceneSetup self)
        
        /**
         * Returns the height of the viewport (display region) in pixels.
         */
        """
        pass

    def get_viewport_width(self, SceneSetup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_viewport_width(SceneSetup self)
        
        /**
         * Returns the width of the viewport (display region) in pixels.
         */
        """
        pass

    def get_world_transform(self, SceneSetup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_world_transform(SceneSetup self)
        
        /**
         * Returns the position of the starting node relative to the camera.  This is
         * the inverse of the camera transform.
         */
        """
        pass

    def setCameraNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_camera_node(const SceneSetup self, Camera camera_node)
        
        /**
         * Specifies the camera used to render the scene.
         */
        """
        pass

    def setCameraPath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_camera_path(const SceneSetup self, const NodePath camera_path)
        
        /**
         * Specifies the NodePath to the camera.
         */
        """
        pass

    def setCameraTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_camera_transform(const SceneSetup self, const TransformState camera_transform)
        
        /**
         * Specifies the position of the camera relative to the starting node.
         */
        """
        pass

    def setCsTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cs_transform(const SceneSetup self, const TransformState cs_transform)
        
        /**
         * Specifies the transform from the camera's coordinate system to the GSG's
         * internal coordinate system.
         */
        """
        pass

    def setCsWorldTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cs_world_transform(const SceneSetup self, const TransformState cs_world_transform)
        
        /**
         * Specifies the position from the starting node relative to the camera, in
         * the GSG's internal coordinate system.
         */
        """
        pass

    def setDisplayRegion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_display_region(const SceneSetup self, DisplayRegion display_region)
        
        /**
         * Specifies the display region for the scene.
         */
        """
        pass

    def setInitialState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_initial_state(const SceneSetup self, const RenderState initial_state)
        
        /**
         * Sets the initial state which is applied to all nodes in the scene, as if it
         * were set at the top of the scene graph.
         */
        """
        pass

    def setInverted(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_inverted(const SceneSetup self, bool inverted)
        
        /**
         * Changes the current setting of the inverted flag.  When this is true, the
         * scene is rendered into the window upside-down and backwards, that is,
         * inverted as if viewed through a mirror placed on the floor.
         */
        """
        pass

    def setLens(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_lens(const SceneSetup self, const Lens lens)
        
        /**
         * Indicates the particular Lens used for rendering.
         */
        """
        pass

    def setSceneRoot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scene_root(const SceneSetup self, const NodePath scene_root)
        
        /**
         * Specifies the root node of the scene.
         */
        """
        pass

    def setViewportSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_viewport_size(const SceneSetup self, int width, int height)
        
        /**
         * Specifies the size of the viewport (display region), in pixels.
         */
        """
        pass

    def setWorldTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_world_transform(const SceneSetup self, const TransformState world_transform)
        
        /**
         * Specifies the position of the starting node relative to the camera.  This
         * is the inverse of the camera transform.
         */
        """
        pass

    def set_camera_node(self, const_SceneSetup_self, Camera_camera_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_camera_node(const SceneSetup self, Camera camera_node)
        
        /**
         * Specifies the camera used to render the scene.
         */
        """
        pass

    def set_camera_path(self, const_SceneSetup_self, const_NodePath_camera_path): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_camera_path(const SceneSetup self, const NodePath camera_path)
        
        /**
         * Specifies the NodePath to the camera.
         */
        """
        pass

    def set_camera_transform(self, const_SceneSetup_self, const_TransformState_camera_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_camera_transform(const SceneSetup self, const TransformState camera_transform)
        
        /**
         * Specifies the position of the camera relative to the starting node.
         */
        """
        pass

    def set_cs_transform(self, const_SceneSetup_self, const_TransformState_cs_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cs_transform(const SceneSetup self, const TransformState cs_transform)
        
        /**
         * Specifies the transform from the camera's coordinate system to the GSG's
         * internal coordinate system.
         */
        """
        pass

    def set_cs_world_transform(self, const_SceneSetup_self, const_TransformState_cs_world_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cs_world_transform(const SceneSetup self, const TransformState cs_world_transform)
        
        /**
         * Specifies the position from the starting node relative to the camera, in
         * the GSG's internal coordinate system.
         */
        """
        pass

    def set_display_region(self, const_SceneSetup_self, DisplayRegion_display_region): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_display_region(const SceneSetup self, DisplayRegion display_region)
        
        /**
         * Specifies the display region for the scene.
         */
        """
        pass

    def set_initial_state(self, const_SceneSetup_self, const_RenderState_initial_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_initial_state(const SceneSetup self, const RenderState initial_state)
        
        /**
         * Sets the initial state which is applied to all nodes in the scene, as if it
         * were set at the top of the scene graph.
         */
        """
        pass

    def set_inverted(self, const_SceneSetup_self, bool_inverted): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_inverted(const SceneSetup self, bool inverted)
        
        /**
         * Changes the current setting of the inverted flag.  When this is true, the
         * scene is rendered into the window upside-down and backwards, that is,
         * inverted as if viewed through a mirror placed on the floor.
         */
        """
        pass

    def set_lens(self, const_SceneSetup_self, const_Lens_lens): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_lens(const SceneSetup self, const Lens lens)
        
        /**
         * Indicates the particular Lens used for rendering.
         */
        """
        pass

    def set_scene_root(self, const_SceneSetup_self, const_NodePath_scene_root): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scene_root(const SceneSetup self, const NodePath scene_root)
        
        /**
         * Specifies the root node of the scene.
         */
        """
        pass

    def set_viewport_size(self, const_SceneSetup_self, int_width, int_height): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_viewport_size(const SceneSetup self, int width, int height)
        
        /**
         * Specifies the size of the viewport (display region), in pixels.
         */
        """
        pass

    def set_world_transform(self, const_SceneSetup_self, const_TransformState_world_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_world_transform(const SceneSetup self, const TransformState world_transform)
        
        /**
         * Specifies the position of the starting node relative to the camera.  This
         * is the inverse of the camera transform.
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.SceneSetup' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.SceneSetup' objects>"
        '__doc__': '/**\n * This object holds the camera position, etc., and other general setup\n * information for rendering a particular scene.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SceneSetup' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2967C0>'
        'getCameraNode': None, # (!) real value is "<method 'getCameraNode' of 'panda3d.core.SceneSetup' objects>"
        'getCameraPath': None, # (!) real value is "<method 'getCameraPath' of 'panda3d.core.SceneSetup' objects>"
        'getCameraTransform': None, # (!) real value is "<method 'getCameraTransform' of 'panda3d.core.SceneSetup' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2967C0>)>'
        'getCsTransform': None, # (!) real value is "<method 'getCsTransform' of 'panda3d.core.SceneSetup' objects>"
        'getCsWorldTransform': None, # (!) real value is "<method 'getCsWorldTransform' of 'panda3d.core.SceneSetup' objects>"
        'getCullBounds': None, # (!) real value is "<method 'getCullBounds' of 'panda3d.core.SceneSetup' objects>"
        'getCullCenter': None, # (!) real value is "<method 'getCullCenter' of 'panda3d.core.SceneSetup' objects>"
        'getDisplayRegion': None, # (!) real value is "<method 'getDisplayRegion' of 'panda3d.core.SceneSetup' objects>"
        'getInitialState': None, # (!) real value is "<method 'getInitialState' of 'panda3d.core.SceneSetup' objects>"
        'getInverted': None, # (!) real value is "<method 'getInverted' of 'panda3d.core.SceneSetup' objects>"
        'getLens': None, # (!) real value is "<method 'getLens' of 'panda3d.core.SceneSetup' objects>"
        'getSceneRoot': None, # (!) real value is "<method 'getSceneRoot' of 'panda3d.core.SceneSetup' objects>"
        'getViewportHeight': None, # (!) real value is "<method 'getViewportHeight' of 'panda3d.core.SceneSetup' objects>"
        'getViewportWidth': None, # (!) real value is "<method 'getViewportWidth' of 'panda3d.core.SceneSetup' objects>"
        'getWorldTransform': None, # (!) real value is "<method 'getWorldTransform' of 'panda3d.core.SceneSetup' objects>"
        'get_camera_node': None, # (!) real value is "<method 'get_camera_node' of 'panda3d.core.SceneSetup' objects>"
        'get_camera_path': None, # (!) real value is "<method 'get_camera_path' of 'panda3d.core.SceneSetup' objects>"
        'get_camera_transform': None, # (!) real value is "<method 'get_camera_transform' of 'panda3d.core.SceneSetup' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2967C0>)>'
        'get_cs_transform': None, # (!) real value is "<method 'get_cs_transform' of 'panda3d.core.SceneSetup' objects>"
        'get_cs_world_transform': None, # (!) real value is "<method 'get_cs_world_transform' of 'panda3d.core.SceneSetup' objects>"
        'get_cull_bounds': None, # (!) real value is "<method 'get_cull_bounds' of 'panda3d.core.SceneSetup' objects>"
        'get_cull_center': None, # (!) real value is "<method 'get_cull_center' of 'panda3d.core.SceneSetup' objects>"
        'get_display_region': None, # (!) real value is "<method 'get_display_region' of 'panda3d.core.SceneSetup' objects>"
        'get_initial_state': None, # (!) real value is "<method 'get_initial_state' of 'panda3d.core.SceneSetup' objects>"
        'get_inverted': None, # (!) real value is "<method 'get_inverted' of 'panda3d.core.SceneSetup' objects>"
        'get_lens': None, # (!) real value is "<method 'get_lens' of 'panda3d.core.SceneSetup' objects>"
        'get_scene_root': None, # (!) real value is "<method 'get_scene_root' of 'panda3d.core.SceneSetup' objects>"
        'get_viewport_height': None, # (!) real value is "<method 'get_viewport_height' of 'panda3d.core.SceneSetup' objects>"
        'get_viewport_width': None, # (!) real value is "<method 'get_viewport_width' of 'panda3d.core.SceneSetup' objects>"
        'get_world_transform': None, # (!) real value is "<method 'get_world_transform' of 'panda3d.core.SceneSetup' objects>"
        'setCameraNode': None, # (!) real value is "<method 'setCameraNode' of 'panda3d.core.SceneSetup' objects>"
        'setCameraPath': None, # (!) real value is "<method 'setCameraPath' of 'panda3d.core.SceneSetup' objects>"
        'setCameraTransform': None, # (!) real value is "<method 'setCameraTransform' of 'panda3d.core.SceneSetup' objects>"
        'setCsTransform': None, # (!) real value is "<method 'setCsTransform' of 'panda3d.core.SceneSetup' objects>"
        'setCsWorldTransform': None, # (!) real value is "<method 'setCsWorldTransform' of 'panda3d.core.SceneSetup' objects>"
        'setDisplayRegion': None, # (!) real value is "<method 'setDisplayRegion' of 'panda3d.core.SceneSetup' objects>"
        'setInitialState': None, # (!) real value is "<method 'setInitialState' of 'panda3d.core.SceneSetup' objects>"
        'setInverted': None, # (!) real value is "<method 'setInverted' of 'panda3d.core.SceneSetup' objects>"
        'setLens': None, # (!) real value is "<method 'setLens' of 'panda3d.core.SceneSetup' objects>"
        'setSceneRoot': None, # (!) real value is "<method 'setSceneRoot' of 'panda3d.core.SceneSetup' objects>"
        'setViewportSize': None, # (!) real value is "<method 'setViewportSize' of 'panda3d.core.SceneSetup' objects>"
        'setWorldTransform': None, # (!) real value is "<method 'setWorldTransform' of 'panda3d.core.SceneSetup' objects>"
        'set_camera_node': None, # (!) real value is "<method 'set_camera_node' of 'panda3d.core.SceneSetup' objects>"
        'set_camera_path': None, # (!) real value is "<method 'set_camera_path' of 'panda3d.core.SceneSetup' objects>"
        'set_camera_transform': None, # (!) real value is "<method 'set_camera_transform' of 'panda3d.core.SceneSetup' objects>"
        'set_cs_transform': None, # (!) real value is "<method 'set_cs_transform' of 'panda3d.core.SceneSetup' objects>"
        'set_cs_world_transform': None, # (!) real value is "<method 'set_cs_world_transform' of 'panda3d.core.SceneSetup' objects>"
        'set_display_region': None, # (!) real value is "<method 'set_display_region' of 'panda3d.core.SceneSetup' objects>"
        'set_initial_state': None, # (!) real value is "<method 'set_initial_state' of 'panda3d.core.SceneSetup' objects>"
        'set_inverted': None, # (!) real value is "<method 'set_inverted' of 'panda3d.core.SceneSetup' objects>"
        'set_lens': None, # (!) real value is "<method 'set_lens' of 'panda3d.core.SceneSetup' objects>"
        'set_scene_root': None, # (!) real value is "<method 'set_scene_root' of 'panda3d.core.SceneSetup' objects>"
        'set_viewport_size': None, # (!) real value is "<method 'set_viewport_size' of 'panda3d.core.SceneSetup' objects>"
        'set_world_transform': None, # (!) real value is "<method 'set_world_transform' of 'panda3d.core.SceneSetup' objects>"
    }


