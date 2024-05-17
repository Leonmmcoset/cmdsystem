# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class CullTraverser(TypedReferenceCount):
    """
    /**
     * This object performs a depth-first traversal of the scene graph, with
     * optional view-frustum culling, collecting CullState and searching for
     * GeomNodes.  Each renderable Geom encountered is passed along with its
     * associated RenderState to the CullHandler object.
     */
    """
    def drawBoundingVolume(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        draw_bounding_volume(CullTraverser self, const BoundingVolume vol, const TransformState internal_transform)
        
        /**
         * Draws an appropriate visualization of the indicated bounding volume.
         */
        """
        pass

    def draw_bounding_volume(self, CullTraverser_self, const_BoundingVolume_vol, const_TransformState_internal_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        draw_bounding_volume(CullTraverser self, const BoundingVolume vol, const TransformState internal_transform)
        
        /**
         * Draws an appropriate visualization of the indicated bounding volume.
         */
        """
        pass

    def endTraverse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        end_traverse(const CullTraverser self)
        
        /**
         * Should be called when the traverser has finished traversing its scene, this
         * gives it a chance to do any necessary finalization.
         */
        """
        pass

    def end_traverse(self, const_CullTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        end_traverse(const CullTraverser self)
        
        /**
         * Should be called when the traverser has finished traversing its scene, this
         * gives it a chance to do any necessary finalization.
         */
        """
        pass

    def flushLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        flush_level()
        
        /**
         * Flushes the PStatCollectors used during traversal.
         */
        """
        pass

    def flush_level(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flush_level()
        
        /**
         * Flushes the PStatCollectors used during traversal.
         */
        """
        pass

    def getCameraMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_camera_mask(CullTraverser self)
        
        /**
         * Returns the visibility mask from the camera viewing the scene.
         */
        """
        pass

    def getCameraTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_camera_transform(CullTraverser self)
        
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

    def getCurrentThread(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_thread(CullTraverser self)
        
        /**
         * Returns the currently-executing thread object, as passed to the
         * CullTraverser constructor.
         */
        """
        pass

    def getDepthOffsetDecals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_depth_offset_decals(CullTraverser self)
        
        /**
         * Returns true, as depth offsets are the only way that we implement decals
         * nowadays.
         */
        """
        pass

    def getEffectiveIncompleteRender(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_effective_incomplete_render(CullTraverser self)
        
        /**
         * Returns true if the cull traversal is effectively in incomplete_render
         * state, considering both the GSG's incomplete_render and the current
         * DisplayRegion's incomplete_render flags.  This returns the flag during the
         * cull traversal; see GSG::get_effective_incomplete_render() for this same
         * flag during the draw traversal.
         */
        """
        pass

    def getGsg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_gsg(CullTraverser self)
        
        /**
         * Returns the GraphicsStateGuardian in effect.
         */
        """
        pass

    def getInitialState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_initial_state(CullTraverser self)
        
        /**
         * Returns the initial RenderState at the top of the scene graph we are
         * traversing, or the empty state if the initial state was never set.
         */
        """
        pass

    def getScene(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scene(CullTraverser self)
        
        /**
         * Returns the SceneSetup object.
         */
        """
        pass

    def getTagStateKey(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tag_state_key(CullTraverser self)
        
        /**
         * Returns the tag state key that has been specified for the scene's camera,
         * if any.
         */
        """
        pass

    def getViewFrustum(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_view_frustum(CullTraverser self)
        
        /**
         * Returns the bounding volume that corresponds to the view frustum, or NULL
         * if the view frustum is not in use or has not been set.
         *
         * Note that the view frustum returned here is always in the coordinate space
         * of the starting node, not the current node, even if it is sampled during a
         * traversal.  To get the view frustum in the current node's coordinate space,
         * check in the current CullTraverserData.
         */
        """
        pass

    def getWorldTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_world_transform(CullTraverser self)
        
        /**
         * Returns the position of the starting node relative to the camera.  This is
         * the inverse of the camera transform.
         *
         * Note that this value is always the position of the starting node, not the
         * current node, even if it is sampled during a traversal.  To get the
         * transform of the current node use
         * CullTraverserData::get_modelview_transform().
         */
        """
        pass

    def get_camera_mask(self, CullTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_camera_mask(CullTraverser self)
        
        /**
         * Returns the visibility mask from the camera viewing the scene.
         */
        """
        pass

    def get_camera_transform(self, CullTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_camera_transform(CullTraverser self)
        
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

    def get_current_thread(self, CullTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_thread(CullTraverser self)
        
        /**
         * Returns the currently-executing thread object, as passed to the
         * CullTraverser constructor.
         */
        """
        pass

    def get_depth_offset_decals(self, CullTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_depth_offset_decals(CullTraverser self)
        
        /**
         * Returns true, as depth offsets are the only way that we implement decals
         * nowadays.
         */
        """
        pass

    def get_effective_incomplete_render(self, CullTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_effective_incomplete_render(CullTraverser self)
        
        /**
         * Returns true if the cull traversal is effectively in incomplete_render
         * state, considering both the GSG's incomplete_render and the current
         * DisplayRegion's incomplete_render flags.  This returns the flag during the
         * cull traversal; see GSG::get_effective_incomplete_render() for this same
         * flag during the draw traversal.
         */
        """
        pass

    def get_gsg(self, CullTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_gsg(CullTraverser self)
        
        /**
         * Returns the GraphicsStateGuardian in effect.
         */
        """
        pass

    def get_initial_state(self, CullTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_initial_state(CullTraverser self)
        
        /**
         * Returns the initial RenderState at the top of the scene graph we are
         * traversing, or the empty state if the initial state was never set.
         */
        """
        pass

    def get_scene(self, CullTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scene(CullTraverser self)
        
        /**
         * Returns the SceneSetup object.
         */
        """
        pass

    def get_tag_state_key(self, CullTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tag_state_key(CullTraverser self)
        
        /**
         * Returns the tag state key that has been specified for the scene's camera,
         * if any.
         */
        """
        pass

    def get_view_frustum(self, CullTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_view_frustum(CullTraverser self)
        
        /**
         * Returns the bounding volume that corresponds to the view frustum, or NULL
         * if the view frustum is not in use or has not been set.
         *
         * Note that the view frustum returned here is always in the coordinate space
         * of the starting node, not the current node, even if it is sampled during a
         * traversal.  To get the view frustum in the current node's coordinate space,
         * check in the current CullTraverserData.
         */
        """
        pass

    def get_world_transform(self, CullTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_world_transform(CullTraverser self)
        
        /**
         * Returns the position of the starting node relative to the camera.  This is
         * the inverse of the camera transform.
         *
         * Note that this value is always the position of the starting node, not the
         * current node, even if it is sampled during a traversal.  To get the
         * transform of the current node use
         * CullTraverserData::get_modelview_transform().
         */
        """
        pass

    def hasTagStateKey(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_tag_state_key(CullTraverser self)
        
        /**
         * Returns true if a nonempty tag state key has been specified for the scene's
         * camera, false otherwise.
         */
        """
        pass

    def has_tag_state_key(self, CullTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_tag_state_key(CullTraverser self)
        
        /**
         * Returns true if a nonempty tag state key has been specified for the scene's
         * camera, false otherwise.
         */
        """
        pass

    def setCameraMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_camera_mask(const CullTraverser self, const BitMask camera_mask)
        
        /**
         * Changes the visibility mask for the camera viewing the scene.  This is
         * normally set automatically at the time setup_scene() is called; you should
         * change this only if you want to render some set of objects different from
         * what the camera normally would draw.
         */
        """
        pass

    def setScene(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scene(const CullTraverser self, SceneSetup scene_setup, GraphicsStateGuardianBase gsg, bool dr_incomplete_render)
        
        /**
         * Sets the SceneSetup object that indicates the initial camera position, etc.
         * This must be called before traversal begins.
         */
        """
        pass

    def setViewFrustum(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_view_frustum(const CullTraverser self, GeometricBoundingVolume view_frustum)
        
        /**
         * Specifies the bounding volume that corresponds to the view frustum.  Any
         * primitives that fall entirely outside of this volume are not drawn.
         */
        """
        pass

    def set_camera_mask(self, const_CullTraverser_self, const_BitMask_camera_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_camera_mask(const CullTraverser self, const BitMask camera_mask)
        
        /**
         * Changes the visibility mask for the camera viewing the scene.  This is
         * normally set automatically at the time setup_scene() is called; you should
         * change this only if you want to render some set of objects different from
         * what the camera normally would draw.
         */
        """
        pass

    def set_scene(self, const_CullTraverser_self, SceneSetup_scene_setup, GraphicsStateGuardianBase_gsg, bool_dr_incomplete_render): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scene(const CullTraverser self, SceneSetup scene_setup, GraphicsStateGuardianBase gsg, bool dr_incomplete_render)
        
        /**
         * Sets the SceneSetup object that indicates the initial camera position, etc.
         * This must be called before traversal begins.
         */
        """
        pass

    def set_view_frustum(self, const_CullTraverser_self, GeometricBoundingVolume_view_frustum): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_view_frustum(const CullTraverser self, GeometricBoundingVolume view_frustum)
        
        /**
         * Specifies the bounding volume that corresponds to the view frustum.  Any
         * primitives that fall entirely outside of this volume are not drawn.
         */
        """
        pass

    def traverse(self, const_CullTraverser_self, CullTraverserData_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        traverse(const CullTraverser self, CullTraverserData data)
        traverse(const CullTraverser self, const NodePath root)
        
        /**
         * Begins the traversal from the indicated node.
         */
        
        /**
         * Traverses from the next node with the given data, which has been
         * constructed with the node but has not yet been converted into the node's
         * space.
         */
        """
        pass

    def traverseBelow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        traverse_below(const CullTraverser self, CullTraverserData data)
        
        /**
         * Traverses all the children of the indicated node, with the given data,
         * which has been converted into the node's space.
         */
        """
        pass

    def traverse_below(self, const_CullTraverser_self, CullTraverserData_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        traverse_below(const CullTraverser self, CullTraverserData data)
        
        /**
         * Traverses all the children of the indicated node, with the given data,
         * which has been converted into the node's space.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.CullTraverser' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.CullTraverser' objects>"
        '__doc__': '/**\n * This object performs a depth-first traversal of the scene graph, with\n * optional view-frustum culling, collecting CullState and searching for\n * GeomNodes.  Each renderable Geom encountered is passed along with its\n * associated RenderState to the CullHandler object.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CullTraverser' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE296D30>'
        'drawBoundingVolume': None, # (!) real value is "<method 'drawBoundingVolume' of 'panda3d.core.CullTraverser' objects>"
        'draw_bounding_volume': None, # (!) real value is "<method 'draw_bounding_volume' of 'panda3d.core.CullTraverser' objects>"
        'endTraverse': None, # (!) real value is "<method 'endTraverse' of 'panda3d.core.CullTraverser' objects>"
        'end_traverse': None, # (!) real value is "<method 'end_traverse' of 'panda3d.core.CullTraverser' objects>"
        'flushLevel': None, # (!) real value is '<staticmethod(<built-in method flushLevel of type object at 0x00007FFCFE296D30>)>'
        'flush_level': None, # (!) real value is '<staticmethod(<built-in method flush_level of type object at 0x00007FFCFE296D30>)>'
        'getCameraMask': None, # (!) real value is "<method 'getCameraMask' of 'panda3d.core.CullTraverser' objects>"
        'getCameraTransform': None, # (!) real value is "<method 'getCameraTransform' of 'panda3d.core.CullTraverser' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE296D30>)>'
        'getCurrentThread': None, # (!) real value is "<method 'getCurrentThread' of 'panda3d.core.CullTraverser' objects>"
        'getDepthOffsetDecals': None, # (!) real value is "<method 'getDepthOffsetDecals' of 'panda3d.core.CullTraverser' objects>"
        'getEffectiveIncompleteRender': None, # (!) real value is "<method 'getEffectiveIncompleteRender' of 'panda3d.core.CullTraverser' objects>"
        'getGsg': None, # (!) real value is "<method 'getGsg' of 'panda3d.core.CullTraverser' objects>"
        'getInitialState': None, # (!) real value is "<method 'getInitialState' of 'panda3d.core.CullTraverser' objects>"
        'getScene': None, # (!) real value is "<method 'getScene' of 'panda3d.core.CullTraverser' objects>"
        'getTagStateKey': None, # (!) real value is "<method 'getTagStateKey' of 'panda3d.core.CullTraverser' objects>"
        'getViewFrustum': None, # (!) real value is "<method 'getViewFrustum' of 'panda3d.core.CullTraverser' objects>"
        'getWorldTransform': None, # (!) real value is "<method 'getWorldTransform' of 'panda3d.core.CullTraverser' objects>"
        'get_camera_mask': None, # (!) real value is "<method 'get_camera_mask' of 'panda3d.core.CullTraverser' objects>"
        'get_camera_transform': None, # (!) real value is "<method 'get_camera_transform' of 'panda3d.core.CullTraverser' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE296D30>)>'
        'get_current_thread': None, # (!) real value is "<method 'get_current_thread' of 'panda3d.core.CullTraverser' objects>"
        'get_depth_offset_decals': None, # (!) real value is "<method 'get_depth_offset_decals' of 'panda3d.core.CullTraverser' objects>"
        'get_effective_incomplete_render': None, # (!) real value is "<method 'get_effective_incomplete_render' of 'panda3d.core.CullTraverser' objects>"
        'get_gsg': None, # (!) real value is "<method 'get_gsg' of 'panda3d.core.CullTraverser' objects>"
        'get_initial_state': None, # (!) real value is "<method 'get_initial_state' of 'panda3d.core.CullTraverser' objects>"
        'get_scene': None, # (!) real value is "<method 'get_scene' of 'panda3d.core.CullTraverser' objects>"
        'get_tag_state_key': None, # (!) real value is "<method 'get_tag_state_key' of 'panda3d.core.CullTraverser' objects>"
        'get_view_frustum': None, # (!) real value is "<method 'get_view_frustum' of 'panda3d.core.CullTraverser' objects>"
        'get_world_transform': None, # (!) real value is "<method 'get_world_transform' of 'panda3d.core.CullTraverser' objects>"
        'hasTagStateKey': None, # (!) real value is "<method 'hasTagStateKey' of 'panda3d.core.CullTraverser' objects>"
        'has_tag_state_key': None, # (!) real value is "<method 'has_tag_state_key' of 'panda3d.core.CullTraverser' objects>"
        'setCameraMask': None, # (!) real value is "<method 'setCameraMask' of 'panda3d.core.CullTraverser' objects>"
        'setScene': None, # (!) real value is "<method 'setScene' of 'panda3d.core.CullTraverser' objects>"
        'setViewFrustum': None, # (!) real value is "<method 'setViewFrustum' of 'panda3d.core.CullTraverser' objects>"
        'set_camera_mask': None, # (!) real value is "<method 'set_camera_mask' of 'panda3d.core.CullTraverser' objects>"
        'set_scene': None, # (!) real value is "<method 'set_scene' of 'panda3d.core.CullTraverser' objects>"
        'set_view_frustum': None, # (!) real value is "<method 'set_view_frustum' of 'panda3d.core.CullTraverser' objects>"
        'traverse': None, # (!) real value is "<method 'traverse' of 'panda3d.core.CullTraverser' objects>"
        'traverseBelow': None, # (!) real value is "<method 'traverseBelow' of 'panda3d.core.CullTraverser' objects>"
        'traverse_below': None, # (!) real value is "<method 'traverse_below' of 'panda3d.core.CullTraverser' objects>"
    }


