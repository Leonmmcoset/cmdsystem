# encoding: utf-8
# module panda3d.bullet
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\bullet.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class BulletBodyNode(__panda3d_core.PandaNode):
    """
    /**
     *
     */
    """
    def addShape(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_shape(const BulletBodyNode self, BulletShape shape, const TransformState xform)
        
        // Shapes
        
        /**
         *
         */
        """
        pass

    def addShapesFromCollisionSolids(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_shapes_from_collision_solids(const BulletBodyNode self, CollisionNode cnode)
        
        /**
         *
         */
        """
        pass

    def add_shape(self, const_BulletBodyNode_self, BulletShape_shape, const_TransformState_xform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_shape(const BulletBodyNode self, BulletShape shape, const TransformState xform)
        
        // Shapes
        
        /**
         *
         */
        """
        pass

    def add_shapes_from_collision_solids(self, const_BulletBodyNode_self, CollisionNode_cnode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_shapes_from_collision_solids(const BulletBodyNode self, CollisionNode cnode)
        
        /**
         *
         */
        """
        pass

    def checkCollisionWith(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        check_collision_with(const BulletBodyNode self, PandaNode node)
        
        /**
         *
         */
        """
        pass

    def check_collision_with(self, const_BulletBodyNode_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        check_collision_with(const BulletBodyNode self, PandaNode node)
        
        /**
         *
         */
        """
        pass

    def forceActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        force_active(const BulletBodyNode self, bool active)
        
        /**
         *
         */
        """
        pass

    def force_active(self, const_BulletBodyNode_self, bool_active): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        force_active(const BulletBodyNode self, bool active)
        
        /**
         *
         */
        """
        pass

    def getAnisotropicFriction(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_anisotropic_friction(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def getCcdMotionThreshold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ccd_motion_threshold(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def getCcdSweptSphereRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ccd_swept_sphere_radius(BulletBodyNode self)
        
        // CCD
        
        // CCD
        
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

    def getCollisionResponse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collision_response(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def getContactProcessingThreshold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_contact_processing_threshold(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def getDeactivationTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_deactivation_time(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def getFriction(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_friction(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def getNumShapes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_shapes(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def getRestitution(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_restitution(BulletBodyNode self)
        
        // Friction and Restitution
        
        // Friction and Restitution
        
        /**
         *
         */
        """
        pass

    def getShape(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shape(BulletBodyNode self, int idx)
        
        /**
         *
         */
        """
        pass

    def getShapeBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shape_bounds(BulletBodyNode self)
        
        /**
         * Returns the current bounds of all collision shapes owned by this body.
         */
        """
        pass

    def getShapeMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shape_mat(BulletBodyNode self, int idx)
        
        /**
         *
         */
        """
        pass

    def getShapePos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shape_pos(BulletBodyNode self, int idx)
        
        /**
         *
         */
        """
        pass

    def getShapes(self, *args, **kwargs): # real signature unknown
        pass

    def getShapeTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shape_transform(BulletBodyNode self, int idx)
        
        /**
         *
         */
        """
        pass

    def get_anisotropic_friction(self, BulletBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_anisotropic_friction(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_ccd_motion_threshold(self, BulletBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ccd_motion_threshold(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_ccd_swept_sphere_radius(self, BulletBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ccd_swept_sphere_radius(BulletBodyNode self)
        
        // CCD
        
        // CCD
        
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

    def get_collision_response(self, BulletBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collision_response(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_contact_processing_threshold(self, BulletBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_contact_processing_threshold(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_deactivation_time(self, BulletBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_deactivation_time(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_friction(self, BulletBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_friction(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_num_shapes(self, BulletBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_shapes(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_restitution(self, BulletBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_restitution(BulletBodyNode self)
        
        // Friction and Restitution
        
        // Friction and Restitution
        
        /**
         *
         */
        """
        pass

    def get_shape(self, BulletBodyNode_self, int_idx): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shape(BulletBodyNode self, int idx)
        
        /**
         *
         */
        """
        pass

    def get_shapes(self, *args, **kwargs): # real signature unknown
        pass

    def get_shape_bounds(self, BulletBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shape_bounds(BulletBodyNode self)
        
        /**
         * Returns the current bounds of all collision shapes owned by this body.
         */
        """
        pass

    def get_shape_mat(self, BulletBodyNode_self, int_idx): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shape_mat(BulletBodyNode self, int idx)
        
        /**
         *
         */
        """
        pass

    def get_shape_pos(self, BulletBodyNode_self, int_idx): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shape_pos(BulletBodyNode self, int idx)
        
        /**
         *
         */
        """
        pass

    def get_shape_transform(self, BulletBodyNode_self, int_idx): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shape_transform(BulletBodyNode self, int idx)
        
        /**
         *
         */
        """
        pass

    def hasAnisotropicFriction(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_anisotropic_friction(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def hasContactResponse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_contact_response(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def has_anisotropic_friction(self, BulletBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_anisotropic_friction(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def has_contact_response(self, BulletBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_contact_response(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def isActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_active(BulletBodyNode self)
        
        // Deactivation
        
        // Deactivation
        
        /**
         *
         */
        """
        pass

    def isDeactivationEnabled(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_deactivation_enabled(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def isDebugEnabled(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_debug_enabled(BulletBodyNode self)
        
        /**
         * Returns TRUE if the debug visualisation is enabled for this collision
         * object, and FALSE if the debug visualisation is disabled.
         */
        """
        pass

    def isKinematic(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_kinematic(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def isStatic(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_static(BulletBodyNode self)
        
        // Static and kinematic
        
        // Static and kinematic
        
        /**
         *
         */
        """
        pass

    def is_active(self, BulletBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_active(BulletBodyNode self)
        
        // Deactivation
        
        // Deactivation
        
        /**
         *
         */
        """
        pass

    def is_deactivation_enabled(self, BulletBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_deactivation_enabled(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def is_debug_enabled(self, BulletBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_debug_enabled(BulletBodyNode self)
        
        /**
         * Returns TRUE if the debug visualisation is enabled for this collision
         * object, and FALSE if the debug visualisation is disabled.
         */
        """
        pass

    def is_kinematic(self, BulletBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_kinematic(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def is_static(self, BulletBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_static(BulletBodyNode self)
        
        // Static and kinematic
        
        // Static and kinematic
        
        /**
         *
         */
        """
        pass

    def notifiesCollisions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        notifies_collisions(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def notifies_collisions(self, BulletBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        notifies_collisions(BulletBodyNode self)
        
        /**
         *
         */
        """
        pass

    def notifyCollisions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        notify_collisions(const BulletBodyNode self, bool value)
        
        /**
         *
         */
        """
        pass

    def notify_collisions(self, const_BulletBodyNode_self, bool_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        notify_collisions(const BulletBodyNode self, bool value)
        
        /**
         *
         */
        """
        pass

    def removeShape(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_shape(const BulletBodyNode self, BulletShape shape)
        
        /**
         *
         */
        """
        pass

    def remove_shape(self, const_BulletBodyNode_self, BulletShape_shape): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_shape(const BulletBodyNode self, BulletShape shape)
        
        /**
         *
         */
        """
        pass

    def setActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_active(const BulletBodyNode self, bool active, bool force)
        
        /**
         *
         */
        """
        pass

    def setAnisotropicFriction(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_anisotropic_friction(const BulletBodyNode self, const LVecBase3f friction)
        
        /**
         *
         */
        """
        pass

    def setCcdMotionThreshold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_ccd_motion_threshold(const BulletBodyNode self, float threshold)
        
        /**
         *
         */
        """
        pass

    def setCcdSweptSphereRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_ccd_swept_sphere_radius(const BulletBodyNode self, float radius)
        
        /**
         *
         */
        """
        pass

    def setCollisionResponse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_collision_response(const BulletBodyNode self, bool value)
        
        /**
         *
         */
        """
        pass

    def setContactProcessingThreshold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_contact_processing_threshold(const BulletBodyNode self, float threshold)
        
        /**
         * The constraint solver can discard solving contacts, if the distance is
         * above this threshold.
         */
        """
        pass

    def setDeactivationEnabled(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_deactivation_enabled(const BulletBodyNode self, bool enabled)
        
        /**
         * If true, this object will be deactivated after a certain amount of time has
         * passed without movement.  If false, the object will always remain active.
         */
        """
        pass

    def setDeactivationTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_deactivation_time(const BulletBodyNode self, float dt)
        
        /**
         *
         */
        """
        pass

    def setDebugEnabled(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_debug_enabled(const BulletBodyNode self, bool enabled)
        
        // Debug Visualisation
        
        // Debug Visualisation
        
        /**
         * Enables or disables the debug visualisation for this collision object.  By
         * default the debug visualisation is enabled.
         */
        """
        pass

    def setFriction(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_friction(const BulletBodyNode self, float friction)
        
        /**
         *
         */
        """
        pass

    def setIntoCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_into_collide_mask(const BulletBodyNode self, BitMask mask)
        
        // Contacts
        
        /**
         *
         */
        """
        pass

    def setKinematic(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_kinematic(const BulletBodyNode self, bool value)
        
        /**
         *
         */
        """
        pass

    def setRestitution(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_restitution(const BulletBodyNode self, float restitution)
        
        /**
         *
         */
        """
        pass

    def setStatic(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_static(const BulletBodyNode self, bool value)
        
        /**
         *
         */
        """
        pass

    def setTransformDirty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_transform_dirty(const BulletBodyNode self)
        
        // Special
        
        /**
         * This method enforces an update of the Bullet transform, that is copies the
         * scene graph transform to the Bullet transform.  This is achieved by alling
         * the protected PandaNode hook 'transform_changed'.
         */
        """
        pass

    def set_active(self, const_BulletBodyNode_self, bool_active, bool_force): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_active(const BulletBodyNode self, bool active, bool force)
        
        /**
         *
         */
        """
        pass

    def set_anisotropic_friction(self, const_BulletBodyNode_self, const_LVecBase3f_friction): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_anisotropic_friction(const BulletBodyNode self, const LVecBase3f friction)
        
        /**
         *
         */
        """
        pass

    def set_ccd_motion_threshold(self, const_BulletBodyNode_self, float_threshold): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_ccd_motion_threshold(const BulletBodyNode self, float threshold)
        
        /**
         *
         */
        """
        pass

    def set_ccd_swept_sphere_radius(self, const_BulletBodyNode_self, float_radius): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_ccd_swept_sphere_radius(const BulletBodyNode self, float radius)
        
        /**
         *
         */
        """
        pass

    def set_collision_response(self, const_BulletBodyNode_self, bool_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_collision_response(const BulletBodyNode self, bool value)
        
        /**
         *
         */
        """
        pass

    def set_contact_processing_threshold(self, const_BulletBodyNode_self, float_threshold): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_contact_processing_threshold(const BulletBodyNode self, float threshold)
        
        /**
         * The constraint solver can discard solving contacts, if the distance is
         * above this threshold.
         */
        """
        pass

    def set_deactivation_enabled(self, const_BulletBodyNode_self, bool_enabled): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_deactivation_enabled(const BulletBodyNode self, bool enabled)
        
        /**
         * If true, this object will be deactivated after a certain amount of time has
         * passed without movement.  If false, the object will always remain active.
         */
        """
        pass

    def set_deactivation_time(self, const_BulletBodyNode_self, float_dt): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_deactivation_time(const BulletBodyNode self, float dt)
        
        /**
         *
         */
        """
        pass

    def set_debug_enabled(self, const_BulletBodyNode_self, bool_enabled): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_debug_enabled(const BulletBodyNode self, bool enabled)
        
        // Debug Visualisation
        
        // Debug Visualisation
        
        /**
         * Enables or disables the debug visualisation for this collision object.  By
         * default the debug visualisation is enabled.
         */
        """
        pass

    def set_friction(self, const_BulletBodyNode_self, float_friction): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_friction(const BulletBodyNode self, float friction)
        
        /**
         *
         */
        """
        pass

    def set_into_collide_mask(self, const_BulletBodyNode_self, BitMask_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_into_collide_mask(const BulletBodyNode self, BitMask mask)
        
        // Contacts
        
        /**
         *
         */
        """
        pass

    def set_kinematic(self, const_BulletBodyNode_self, bool_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_kinematic(const BulletBodyNode self, bool value)
        
        /**
         *
         */
        """
        pass

    def set_restitution(self, const_BulletBodyNode_self, float_restitution): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_restitution(const BulletBodyNode self, float restitution)
        
        /**
         *
         */
        """
        pass

    def set_static(self, const_BulletBodyNode_self, bool_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_static(const BulletBodyNode self, bool value)
        
        /**
         *
         */
        """
        pass

    def set_transform_dirty(self, const_BulletBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_transform_dirty(const BulletBodyNode self)
        
        // Special
        
        /**
         * This method enforces an update of the Bullet transform, that is copies the
         * scene graph transform to the Bullet transform.  This is achieved by alling
         * the protected PandaNode hook 'transform_changed'.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// Deactivation"""

    anisotropic_friction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ccd_motion_threshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ccd_swept_sphere_radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// CCD"""

    collision_notification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collision_response = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    contact_processing_threshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    contact_response = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    deactivation_enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    deactivation_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    debug_enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    friction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kinematic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    restitution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// Friction and Restitution"""

    shapes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shape_bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shape_mat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shape_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shape_transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    static = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// Static and kinematic"""


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.bullet.BulletBodyNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CC9A0>'
        'active': None, # (!) real value is "<attribute 'active' of 'panda3d.bullet.BulletBodyNode' objects>"
        'addShape': None, # (!) real value is "<method 'addShape' of 'panda3d.bullet.BulletBodyNode' objects>"
        'addShapesFromCollisionSolids': None, # (!) real value is "<method 'addShapesFromCollisionSolids' of 'panda3d.bullet.BulletBodyNode' objects>"
        'add_shape': None, # (!) real value is "<method 'add_shape' of 'panda3d.bullet.BulletBodyNode' objects>"
        'add_shapes_from_collision_solids': None, # (!) real value is "<method 'add_shapes_from_collision_solids' of 'panda3d.bullet.BulletBodyNode' objects>"
        'anisotropic_friction': None, # (!) real value is "<attribute 'anisotropic_friction' of 'panda3d.bullet.BulletBodyNode' objects>"
        'ccd_motion_threshold': None, # (!) real value is "<attribute 'ccd_motion_threshold' of 'panda3d.bullet.BulletBodyNode' objects>"
        'ccd_swept_sphere_radius': None, # (!) real value is "<attribute 'ccd_swept_sphere_radius' of 'panda3d.bullet.BulletBodyNode' objects>"
        'checkCollisionWith': None, # (!) real value is "<method 'checkCollisionWith' of 'panda3d.bullet.BulletBodyNode' objects>"
        'check_collision_with': None, # (!) real value is "<method 'check_collision_with' of 'panda3d.bullet.BulletBodyNode' objects>"
        'collision_notification': None, # (!) real value is "<attribute 'collision_notification' of 'panda3d.bullet.BulletBodyNode' objects>"
        'collision_response': None, # (!) real value is "<attribute 'collision_response' of 'panda3d.bullet.BulletBodyNode' objects>"
        'contact_processing_threshold': None, # (!) real value is "<attribute 'contact_processing_threshold' of 'panda3d.bullet.BulletBodyNode' objects>"
        'contact_response': None, # (!) real value is "<attribute 'contact_response' of 'panda3d.bullet.BulletBodyNode' objects>"
        'deactivation_enabled': None, # (!) real value is "<attribute 'deactivation_enabled' of 'panda3d.bullet.BulletBodyNode' objects>"
        'deactivation_time': None, # (!) real value is "<attribute 'deactivation_time' of 'panda3d.bullet.BulletBodyNode' objects>"
        'debug_enabled': None, # (!) real value is "<attribute 'debug_enabled' of 'panda3d.bullet.BulletBodyNode' objects>"
        'forceActive': None, # (!) real value is "<method 'forceActive' of 'panda3d.bullet.BulletBodyNode' objects>"
        'force_active': None, # (!) real value is "<method 'force_active' of 'panda3d.bullet.BulletBodyNode' objects>"
        'friction': None, # (!) real value is "<attribute 'friction' of 'panda3d.bullet.BulletBodyNode' objects>"
        'getAnisotropicFriction': None, # (!) real value is "<method 'getAnisotropicFriction' of 'panda3d.bullet.BulletBodyNode' objects>"
        'getCcdMotionThreshold': None, # (!) real value is "<method 'getCcdMotionThreshold' of 'panda3d.bullet.BulletBodyNode' objects>"
        'getCcdSweptSphereRadius': None, # (!) real value is "<method 'getCcdSweptSphereRadius' of 'panda3d.bullet.BulletBodyNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CC9A0>)>'
        'getCollisionResponse': None, # (!) real value is "<method 'getCollisionResponse' of 'panda3d.bullet.BulletBodyNode' objects>"
        'getContactProcessingThreshold': None, # (!) real value is "<method 'getContactProcessingThreshold' of 'panda3d.bullet.BulletBodyNode' objects>"
        'getDeactivationTime': None, # (!) real value is "<method 'getDeactivationTime' of 'panda3d.bullet.BulletBodyNode' objects>"
        'getFriction': None, # (!) real value is "<method 'getFriction' of 'panda3d.bullet.BulletBodyNode' objects>"
        'getNumShapes': None, # (!) real value is "<method 'getNumShapes' of 'panda3d.bullet.BulletBodyNode' objects>"
        'getRestitution': None, # (!) real value is "<method 'getRestitution' of 'panda3d.bullet.BulletBodyNode' objects>"
        'getShape': None, # (!) real value is "<method 'getShape' of 'panda3d.bullet.BulletBodyNode' objects>"
        'getShapeBounds': None, # (!) real value is "<method 'getShapeBounds' of 'panda3d.bullet.BulletBodyNode' objects>"
        'getShapeMat': None, # (!) real value is "<method 'getShapeMat' of 'panda3d.bullet.BulletBodyNode' objects>"
        'getShapePos': None, # (!) real value is "<method 'getShapePos' of 'panda3d.bullet.BulletBodyNode' objects>"
        'getShapeTransform': None, # (!) real value is "<method 'getShapeTransform' of 'panda3d.bullet.BulletBodyNode' objects>"
        'getShapes': None, # (!) real value is "<method 'getShapes' of 'panda3d.bullet.BulletBodyNode' objects>"
        'get_anisotropic_friction': None, # (!) real value is "<method 'get_anisotropic_friction' of 'panda3d.bullet.BulletBodyNode' objects>"
        'get_ccd_motion_threshold': None, # (!) real value is "<method 'get_ccd_motion_threshold' of 'panda3d.bullet.BulletBodyNode' objects>"
        'get_ccd_swept_sphere_radius': None, # (!) real value is "<method 'get_ccd_swept_sphere_radius' of 'panda3d.bullet.BulletBodyNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CC9A0>)>'
        'get_collision_response': None, # (!) real value is "<method 'get_collision_response' of 'panda3d.bullet.BulletBodyNode' objects>"
        'get_contact_processing_threshold': None, # (!) real value is "<method 'get_contact_processing_threshold' of 'panda3d.bullet.BulletBodyNode' objects>"
        'get_deactivation_time': None, # (!) real value is "<method 'get_deactivation_time' of 'panda3d.bullet.BulletBodyNode' objects>"
        'get_friction': None, # (!) real value is "<method 'get_friction' of 'panda3d.bullet.BulletBodyNode' objects>"
        'get_num_shapes': None, # (!) real value is "<method 'get_num_shapes' of 'panda3d.bullet.BulletBodyNode' objects>"
        'get_restitution': None, # (!) real value is "<method 'get_restitution' of 'panda3d.bullet.BulletBodyNode' objects>"
        'get_shape': None, # (!) real value is "<method 'get_shape' of 'panda3d.bullet.BulletBodyNode' objects>"
        'get_shape_bounds': None, # (!) real value is "<method 'get_shape_bounds' of 'panda3d.bullet.BulletBodyNode' objects>"
        'get_shape_mat': None, # (!) real value is "<method 'get_shape_mat' of 'panda3d.bullet.BulletBodyNode' objects>"
        'get_shape_pos': None, # (!) real value is "<method 'get_shape_pos' of 'panda3d.bullet.BulletBodyNode' objects>"
        'get_shape_transform': None, # (!) real value is "<method 'get_shape_transform' of 'panda3d.bullet.BulletBodyNode' objects>"
        'get_shapes': None, # (!) real value is "<method 'get_shapes' of 'panda3d.bullet.BulletBodyNode' objects>"
        'hasAnisotropicFriction': None, # (!) real value is "<method 'hasAnisotropicFriction' of 'panda3d.bullet.BulletBodyNode' objects>"
        'hasContactResponse': None, # (!) real value is "<method 'hasContactResponse' of 'panda3d.bullet.BulletBodyNode' objects>"
        'has_anisotropic_friction': None, # (!) real value is "<method 'has_anisotropic_friction' of 'panda3d.bullet.BulletBodyNode' objects>"
        'has_contact_response': None, # (!) real value is "<method 'has_contact_response' of 'panda3d.bullet.BulletBodyNode' objects>"
        'isActive': None, # (!) real value is "<method 'isActive' of 'panda3d.bullet.BulletBodyNode' objects>"
        'isDeactivationEnabled': None, # (!) real value is "<method 'isDeactivationEnabled' of 'panda3d.bullet.BulletBodyNode' objects>"
        'isDebugEnabled': None, # (!) real value is "<method 'isDebugEnabled' of 'panda3d.bullet.BulletBodyNode' objects>"
        'isKinematic': None, # (!) real value is "<method 'isKinematic' of 'panda3d.bullet.BulletBodyNode' objects>"
        'isStatic': None, # (!) real value is "<method 'isStatic' of 'panda3d.bullet.BulletBodyNode' objects>"
        'is_active': None, # (!) real value is "<method 'is_active' of 'panda3d.bullet.BulletBodyNode' objects>"
        'is_deactivation_enabled': None, # (!) real value is "<method 'is_deactivation_enabled' of 'panda3d.bullet.BulletBodyNode' objects>"
        'is_debug_enabled': None, # (!) real value is "<method 'is_debug_enabled' of 'panda3d.bullet.BulletBodyNode' objects>"
        'is_kinematic': None, # (!) real value is "<method 'is_kinematic' of 'panda3d.bullet.BulletBodyNode' objects>"
        'is_static': None, # (!) real value is "<method 'is_static' of 'panda3d.bullet.BulletBodyNode' objects>"
        'kinematic': None, # (!) real value is "<attribute 'kinematic' of 'panda3d.bullet.BulletBodyNode' objects>"
        'notifiesCollisions': None, # (!) real value is "<method 'notifiesCollisions' of 'panda3d.bullet.BulletBodyNode' objects>"
        'notifies_collisions': None, # (!) real value is "<method 'notifies_collisions' of 'panda3d.bullet.BulletBodyNode' objects>"
        'notifyCollisions': None, # (!) real value is "<method 'notifyCollisions' of 'panda3d.bullet.BulletBodyNode' objects>"
        'notify_collisions': None, # (!) real value is "<method 'notify_collisions' of 'panda3d.bullet.BulletBodyNode' objects>"
        'removeShape': None, # (!) real value is "<method 'removeShape' of 'panda3d.bullet.BulletBodyNode' objects>"
        'remove_shape': None, # (!) real value is "<method 'remove_shape' of 'panda3d.bullet.BulletBodyNode' objects>"
        'restitution': None, # (!) real value is "<attribute 'restitution' of 'panda3d.bullet.BulletBodyNode' objects>"
        'setActive': None, # (!) real value is "<method 'setActive' of 'panda3d.bullet.BulletBodyNode' objects>"
        'setAnisotropicFriction': None, # (!) real value is "<method 'setAnisotropicFriction' of 'panda3d.bullet.BulletBodyNode' objects>"
        'setCcdMotionThreshold': None, # (!) real value is "<method 'setCcdMotionThreshold' of 'panda3d.bullet.BulletBodyNode' objects>"
        'setCcdSweptSphereRadius': None, # (!) real value is "<method 'setCcdSweptSphereRadius' of 'panda3d.bullet.BulletBodyNode' objects>"
        'setCollisionResponse': None, # (!) real value is "<method 'setCollisionResponse' of 'panda3d.bullet.BulletBodyNode' objects>"
        'setContactProcessingThreshold': None, # (!) real value is "<method 'setContactProcessingThreshold' of 'panda3d.bullet.BulletBodyNode' objects>"
        'setDeactivationEnabled': None, # (!) real value is "<method 'setDeactivationEnabled' of 'panda3d.bullet.BulletBodyNode' objects>"
        'setDeactivationTime': None, # (!) real value is "<method 'setDeactivationTime' of 'panda3d.bullet.BulletBodyNode' objects>"
        'setDebugEnabled': None, # (!) real value is "<method 'setDebugEnabled' of 'panda3d.bullet.BulletBodyNode' objects>"
        'setFriction': None, # (!) real value is "<method 'setFriction' of 'panda3d.bullet.BulletBodyNode' objects>"
        'setIntoCollideMask': None, # (!) real value is "<method 'setIntoCollideMask' of 'panda3d.bullet.BulletBodyNode' objects>"
        'setKinematic': None, # (!) real value is "<method 'setKinematic' of 'panda3d.bullet.BulletBodyNode' objects>"
        'setRestitution': None, # (!) real value is "<method 'setRestitution' of 'panda3d.bullet.BulletBodyNode' objects>"
        'setStatic': None, # (!) real value is "<method 'setStatic' of 'panda3d.bullet.BulletBodyNode' objects>"
        'setTransformDirty': None, # (!) real value is "<method 'setTransformDirty' of 'panda3d.bullet.BulletBodyNode' objects>"
        'set_active': None, # (!) real value is "<method 'set_active' of 'panda3d.bullet.BulletBodyNode' objects>"
        'set_anisotropic_friction': None, # (!) real value is "<method 'set_anisotropic_friction' of 'panda3d.bullet.BulletBodyNode' objects>"
        'set_ccd_motion_threshold': None, # (!) real value is "<method 'set_ccd_motion_threshold' of 'panda3d.bullet.BulletBodyNode' objects>"
        'set_ccd_swept_sphere_radius': None, # (!) real value is "<method 'set_ccd_swept_sphere_radius' of 'panda3d.bullet.BulletBodyNode' objects>"
        'set_collision_response': None, # (!) real value is "<method 'set_collision_response' of 'panda3d.bullet.BulletBodyNode' objects>"
        'set_contact_processing_threshold': None, # (!) real value is "<method 'set_contact_processing_threshold' of 'panda3d.bullet.BulletBodyNode' objects>"
        'set_deactivation_enabled': None, # (!) real value is "<method 'set_deactivation_enabled' of 'panda3d.bullet.BulletBodyNode' objects>"
        'set_deactivation_time': None, # (!) real value is "<method 'set_deactivation_time' of 'panda3d.bullet.BulletBodyNode' objects>"
        'set_debug_enabled': None, # (!) real value is "<method 'set_debug_enabled' of 'panda3d.bullet.BulletBodyNode' objects>"
        'set_friction': None, # (!) real value is "<method 'set_friction' of 'panda3d.bullet.BulletBodyNode' objects>"
        'set_into_collide_mask': None, # (!) real value is "<method 'set_into_collide_mask' of 'panda3d.bullet.BulletBodyNode' objects>"
        'set_kinematic': None, # (!) real value is "<method 'set_kinematic' of 'panda3d.bullet.BulletBodyNode' objects>"
        'set_restitution': None, # (!) real value is "<method 'set_restitution' of 'panda3d.bullet.BulletBodyNode' objects>"
        'set_static': None, # (!) real value is "<method 'set_static' of 'panda3d.bullet.BulletBodyNode' objects>"
        'set_transform_dirty': None, # (!) real value is "<method 'set_transform_dirty' of 'panda3d.bullet.BulletBodyNode' objects>"
        'shape_bounds': None, # (!) real value is "<attribute 'shape_bounds' of 'panda3d.bullet.BulletBodyNode' objects>"
        'shape_mat': None, # (!) real value is "<attribute 'shape_mat' of 'panda3d.bullet.BulletBodyNode' objects>"
        'shape_pos': None, # (!) real value is "<attribute 'shape_pos' of 'panda3d.bullet.BulletBodyNode' objects>"
        'shape_transform': None, # (!) real value is "<attribute 'shape_transform' of 'panda3d.bullet.BulletBodyNode' objects>"
        'shapes': None, # (!) real value is "<attribute 'shapes' of 'panda3d.bullet.BulletBodyNode' objects>"
        'static': None, # (!) real value is "<attribute 'static' of 'panda3d.bullet.BulletBodyNode' objects>"
    }


