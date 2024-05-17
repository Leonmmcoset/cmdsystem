# encoding: utf-8
# module panda3d.bullet
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\bullet.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .BulletBodyNode import BulletBodyNode

class BulletRigidBodyNode(BulletBodyNode):
    """
    /**
     *
     */
    """
    def applyCentralForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_central_force(const BulletRigidBodyNode self, const LVector3f force)
        
        /**
         *
         */
        """
        pass

    def applyCentralImpulse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_central_impulse(const BulletRigidBodyNode self, const LVector3f impulse)
        
        /**
         *
         */
        """
        pass

    def applyForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_force(const BulletRigidBodyNode self, const LVector3f force, const LPoint3f pos)
        
        /**
         *
         */
        """
        pass

    def applyImpulse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_impulse(const BulletRigidBodyNode self, const LVector3f impulse, const LPoint3f pos)
        
        /**
         *
         */
        """
        pass

    def applyTorque(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_torque(const BulletRigidBodyNode self, const LVector3f torque)
        
        /**
         *
         */
        """
        pass

    def applyTorqueImpulse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_torque_impulse(const BulletRigidBodyNode self, const LVector3f torque)
        
        /**
         *
         */
        """
        pass

    def apply_central_force(self, const_BulletRigidBodyNode_self, const_LVector3f_force): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_central_force(const BulletRigidBodyNode self, const LVector3f force)
        
        /**
         *
         */
        """
        pass

    def apply_central_impulse(self, const_BulletRigidBodyNode_self, const_LVector3f_impulse): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_central_impulse(const BulletRigidBodyNode self, const LVector3f impulse)
        
        /**
         *
         */
        """
        pass

    def apply_force(self, const_BulletRigidBodyNode_self, const_LVector3f_force, const_LPoint3f_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_force(const BulletRigidBodyNode self, const LVector3f force, const LPoint3f pos)
        
        /**
         *
         */
        """
        pass

    def apply_impulse(self, const_BulletRigidBodyNode_self, const_LVector3f_impulse, const_LPoint3f_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_impulse(const BulletRigidBodyNode self, const LVector3f impulse, const LPoint3f pos)
        
        /**
         *
         */
        """
        pass

    def apply_torque(self, const_BulletRigidBodyNode_self, const_LVector3f_torque): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_torque(const BulletRigidBodyNode self, const LVector3f torque)
        
        /**
         *
         */
        """
        pass

    def apply_torque_impulse(self, const_BulletRigidBodyNode_self, const_LVector3f_torque): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_torque_impulse(const BulletRigidBodyNode self, const LVector3f torque)
        
        /**
         *
         */
        """
        pass

    def clearForces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_forces(const BulletRigidBodyNode self)
        
        // Forces
        
        /**
         *
         */
        """
        pass

    def clear_forces(self, const_BulletRigidBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_forces(const BulletRigidBodyNode self)
        
        // Forces
        
        /**
         *
         */
        """
        pass

    def getAngularDamping(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_angular_damping(BulletRigidBodyNode self)
        
        /**
         *
         */
        """
        pass

    def getAngularFactor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_angular_factor(BulletRigidBodyNode self)
        
        /**
         *
         */
        """
        pass

    def getAngularSleepThreshold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_angular_sleep_threshold(BulletRigidBodyNode self)
        
        /**
         *
         */
        """
        pass

    def getAngularVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_angular_velocity(BulletRigidBodyNode self)
        
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

    def getGravity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_gravity(BulletRigidBodyNode self)
        
        /**
         *
         */
        """
        pass

    def getInertia(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_inertia(BulletRigidBodyNode self)
        
        /**
         * Returns the inertia of the rigid body.  Inertia is given as a three
         * component vector.  A component value of zero means infinite inertia along
         * this direction.
         */
        """
        pass

    def getInvInertiaDiagLocal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_inv_inertia_diag_local(BulletRigidBodyNode self)
        
        /**
         *
         */
        """
        pass

    def getInvInertiaTensorWorld(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_inv_inertia_tensor_world(BulletRigidBodyNode self)
        
        /**
         *
         */
        """
        pass

    def getInvMass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_inv_mass(BulletRigidBodyNode self)
        
        /**
         * Returns the inverse mass of a rigid body.
         */
        """
        pass

    def getLinearDamping(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_linear_damping(BulletRigidBodyNode self)
        
        // Damping
        
        // Damping
        
        /**
         *
         */
        """
        pass

    def getLinearFactor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_linear_factor(BulletRigidBodyNode self)
        
        // Restrict movement
        
        // Restrict movement
        
        /**
         *
         */
        """
        pass

    def getLinearSleepThreshold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_linear_sleep_threshold(BulletRigidBodyNode self)
        
        // Deactivation thresholds
        
        // Deactivation thresholds
        
        /**
         *
         */
        """
        pass

    def getLinearVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_linear_velocity(BulletRigidBodyNode self)
        
        // Velocity
        
        // Velocity
        
        /**
         *
         */
        """
        pass

    def getMass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mass(BulletRigidBodyNode self)
        
        /**
         * Returns the total mass of a rigid body.  A value of zero means that the
         * body is staic, i.e.  has an infinite mass.
         */
        """
        pass

    def getTotalForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_total_force(BulletRigidBodyNode self)
        
        /**
         *
         */
        """
        pass

    def getTotalTorque(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_total_torque(BulletRigidBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_angular_damping(self, BulletRigidBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_angular_damping(BulletRigidBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_angular_factor(self, BulletRigidBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_angular_factor(BulletRigidBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_angular_sleep_threshold(self, BulletRigidBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_angular_sleep_threshold(BulletRigidBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_angular_velocity(self, BulletRigidBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_angular_velocity(BulletRigidBodyNode self)
        
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

    def get_gravity(self, BulletRigidBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_gravity(BulletRigidBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_inertia(self, BulletRigidBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_inertia(BulletRigidBodyNode self)
        
        /**
         * Returns the inertia of the rigid body.  Inertia is given as a three
         * component vector.  A component value of zero means infinite inertia along
         * this direction.
         */
        """
        pass

    def get_inv_inertia_diag_local(self, BulletRigidBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_inv_inertia_diag_local(BulletRigidBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_inv_inertia_tensor_world(self, BulletRigidBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_inv_inertia_tensor_world(BulletRigidBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_inv_mass(self, BulletRigidBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_inv_mass(BulletRigidBodyNode self)
        
        /**
         * Returns the inverse mass of a rigid body.
         */
        """
        pass

    def get_linear_damping(self, BulletRigidBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_linear_damping(BulletRigidBodyNode self)
        
        // Damping
        
        // Damping
        
        /**
         *
         */
        """
        pass

    def get_linear_factor(self, BulletRigidBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_linear_factor(BulletRigidBodyNode self)
        
        // Restrict movement
        
        // Restrict movement
        
        /**
         *
         */
        """
        pass

    def get_linear_sleep_threshold(self, BulletRigidBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_linear_sleep_threshold(BulletRigidBodyNode self)
        
        // Deactivation thresholds
        
        // Deactivation thresholds
        
        /**
         *
         */
        """
        pass

    def get_linear_velocity(self, BulletRigidBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_linear_velocity(BulletRigidBodyNode self)
        
        // Velocity
        
        // Velocity
        
        /**
         *
         */
        """
        pass

    def get_mass(self, BulletRigidBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mass(BulletRigidBodyNode self)
        
        /**
         * Returns the total mass of a rigid body.  A value of zero means that the
         * body is staic, i.e.  has an infinite mass.
         */
        """
        pass

    def get_total_force(self, BulletRigidBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_total_force(BulletRigidBodyNode self)
        
        /**
         *
         */
        """
        pass

    def get_total_torque(self, BulletRigidBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_total_torque(BulletRigidBodyNode self)
        
        /**
         *
         */
        """
        pass

    def pickDirtyFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pick_dirty_flag(const BulletRigidBodyNode self)
        
        // Special
        
        /**
         * Returns TRUE if the transform of the rigid body has changed at least once
         * since the last call to this method.
         */
        """
        pass

    def pick_dirty_flag(self, const_BulletRigidBodyNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pick_dirty_flag(const BulletRigidBodyNode self)
        
        // Special
        
        /**
         * Returns TRUE if the transform of the rigid body has changed at least once
         * since the last call to this method.
         */
        """
        pass

    def setAngularDamping(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_angular_damping(const BulletRigidBodyNode self, float value)
        
        /**
         *
         */
        """
        pass

    def setAngularFactor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_angular_factor(const BulletRigidBodyNode self, const LVector3f factor)
        
        /**
         *
         */
        """
        pass

    def setAngularSleepThreshold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_angular_sleep_threshold(const BulletRigidBodyNode self, float threshold)
        
        /**
         *
         */
        """
        pass

    def setAngularVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_angular_velocity(const BulletRigidBodyNode self, const LVector3f velocity)
        
        /**
         *
         */
        """
        pass

    def setGravity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_gravity(const BulletRigidBodyNode self, const LVector3f gravity)
        
        // Gravity
        
        // Gravity
        
        /**
         *
         */
        """
        pass

    def setInertia(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_inertia(const BulletRigidBodyNode self, const LVecBase3f inertia)
        
        /**
         * Sets the inertia of a rigid body.  Inertia is given as a three-component
         * vector.  A component value of zero means infinite inertia along this
         * direction.  Setting the intertia will override the value which is
         * automatically calculated from the rigid bodies shape.  However, it is
         * possible that automatic calculation of intertia is trigger after calling
         * this method, and thus overwriting the explicitly set value again.  This
         * happens when: (a) the mass is set after the inertia.  (b) a shape is added
         * or removed from the body.  (c) the scale of the body changed.
         */
        """
        pass

    def setLinearDamping(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_linear_damping(const BulletRigidBodyNode self, float value)
        
        /**
         *
         */
        """
        pass

    def setLinearFactor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_linear_factor(const BulletRigidBodyNode self, const LVector3f factor)
        
        /**
         *
         */
        """
        pass

    def setLinearSleepThreshold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_linear_sleep_threshold(const BulletRigidBodyNode self, float threshold)
        
        /**
         *
         */
        """
        pass

    def setLinearVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_linear_velocity(const BulletRigidBodyNode self, const LVector3f velocity)
        
        /**
         *
         */
        """
        pass

    def setMass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_mass(const BulletRigidBodyNode self, float mass)
        
        // Mass & inertia
        
        // Mass & inertia
        
        /**
         * Sets the mass of a rigid body.  This also modifies the inertia, which is
         * automatically computed from the shape of the body.  Setting a value of zero
         * for mass will make the body static.  A value of zero can be considered an
         * infinite mass.
         */
        """
        pass

    def set_angular_damping(self, const_BulletRigidBodyNode_self, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_angular_damping(const BulletRigidBodyNode self, float value)
        
        /**
         *
         */
        """
        pass

    def set_angular_factor(self, const_BulletRigidBodyNode_self, const_LVector3f_factor): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_angular_factor(const BulletRigidBodyNode self, const LVector3f factor)
        
        /**
         *
         */
        """
        pass

    def set_angular_sleep_threshold(self, const_BulletRigidBodyNode_self, float_threshold): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_angular_sleep_threshold(const BulletRigidBodyNode self, float threshold)
        
        /**
         *
         */
        """
        pass

    def set_angular_velocity(self, const_BulletRigidBodyNode_self, const_LVector3f_velocity): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_angular_velocity(const BulletRigidBodyNode self, const LVector3f velocity)
        
        /**
         *
         */
        """
        pass

    def set_gravity(self, const_BulletRigidBodyNode_self, const_LVector3f_gravity): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_gravity(const BulletRigidBodyNode self, const LVector3f gravity)
        
        // Gravity
        
        // Gravity
        
        /**
         *
         */
        """
        pass

    def set_inertia(self, const_BulletRigidBodyNode_self, const_LVecBase3f_inertia): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_inertia(const BulletRigidBodyNode self, const LVecBase3f inertia)
        
        /**
         * Sets the inertia of a rigid body.  Inertia is given as a three-component
         * vector.  A component value of zero means infinite inertia along this
         * direction.  Setting the intertia will override the value which is
         * automatically calculated from the rigid bodies shape.  However, it is
         * possible that automatic calculation of intertia is trigger after calling
         * this method, and thus overwriting the explicitly set value again.  This
         * happens when: (a) the mass is set after the inertia.  (b) a shape is added
         * or removed from the body.  (c) the scale of the body changed.
         */
        """
        pass

    def set_linear_damping(self, const_BulletRigidBodyNode_self, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_linear_damping(const BulletRigidBodyNode self, float value)
        
        /**
         *
         */
        """
        pass

    def set_linear_factor(self, const_BulletRigidBodyNode_self, const_LVector3f_factor): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_linear_factor(const BulletRigidBodyNode self, const LVector3f factor)
        
        /**
         *
         */
        """
        pass

    def set_linear_sleep_threshold(self, const_BulletRigidBodyNode_self, float_threshold): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_linear_sleep_threshold(const BulletRigidBodyNode self, float threshold)
        
        /**
         *
         */
        """
        pass

    def set_linear_velocity(self, const_BulletRigidBodyNode_self, const_LVector3f_velocity): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_linear_velocity(const BulletRigidBodyNode self, const LVector3f velocity)
        
        /**
         *
         */
        """
        pass

    def set_mass(self, const_BulletRigidBodyNode_self, float_mass): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_mass(const BulletRigidBodyNode self, float mass)
        
        // Mass & inertia
        
        // Mass & inertia
        
        /**
         * Sets the mass of a rigid body.  This also modifies the inertia, which is
         * automatically computed from the shape of the body.  Setting a value of zero
         * for mass will make the body static.  A value of zero can be considered an
         * infinite mass.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    angular_damping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    angular_factor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    angular_sleep_threshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    angular_velocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gravity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inertia = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inv_inertia_diag_local = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inv_inertia_tensor_world = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inv_mass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    linear_damping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// Damping"""

    linear_factor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// Restrict movement"""

    linear_sleep_threshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// Deactivation thresholds"""

    linear_velocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// Velocity"""

    mass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    total_force = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    total_torque = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CD820>'
        'angular_damping': None, # (!) real value is "<attribute 'angular_damping' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'angular_factor': None, # (!) real value is "<attribute 'angular_factor' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'angular_sleep_threshold': None, # (!) real value is "<attribute 'angular_sleep_threshold' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'angular_velocity': None, # (!) real value is "<attribute 'angular_velocity' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'applyCentralForce': None, # (!) real value is "<method 'applyCentralForce' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'applyCentralImpulse': None, # (!) real value is "<method 'applyCentralImpulse' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'applyForce': None, # (!) real value is "<method 'applyForce' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'applyImpulse': None, # (!) real value is "<method 'applyImpulse' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'applyTorque': None, # (!) real value is "<method 'applyTorque' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'applyTorqueImpulse': None, # (!) real value is "<method 'applyTorqueImpulse' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'apply_central_force': None, # (!) real value is "<method 'apply_central_force' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'apply_central_impulse': None, # (!) real value is "<method 'apply_central_impulse' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'apply_force': None, # (!) real value is "<method 'apply_force' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'apply_impulse': None, # (!) real value is "<method 'apply_impulse' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'apply_torque': None, # (!) real value is "<method 'apply_torque' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'apply_torque_impulse': None, # (!) real value is "<method 'apply_torque_impulse' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'clearForces': None, # (!) real value is "<method 'clearForces' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'clear_forces': None, # (!) real value is "<method 'clear_forces' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'getAngularDamping': None, # (!) real value is "<method 'getAngularDamping' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'getAngularFactor': None, # (!) real value is "<method 'getAngularFactor' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'getAngularSleepThreshold': None, # (!) real value is "<method 'getAngularSleepThreshold' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'getAngularVelocity': None, # (!) real value is "<method 'getAngularVelocity' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CD820>)>'
        'getGravity': None, # (!) real value is "<method 'getGravity' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'getInertia': None, # (!) real value is "<method 'getInertia' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'getInvInertiaDiagLocal': None, # (!) real value is "<method 'getInvInertiaDiagLocal' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'getInvInertiaTensorWorld': None, # (!) real value is "<method 'getInvInertiaTensorWorld' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'getInvMass': None, # (!) real value is "<method 'getInvMass' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'getLinearDamping': None, # (!) real value is "<method 'getLinearDamping' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'getLinearFactor': None, # (!) real value is "<method 'getLinearFactor' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'getLinearSleepThreshold': None, # (!) real value is "<method 'getLinearSleepThreshold' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'getLinearVelocity': None, # (!) real value is "<method 'getLinearVelocity' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'getMass': None, # (!) real value is "<method 'getMass' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'getTotalForce': None, # (!) real value is "<method 'getTotalForce' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'getTotalTorque': None, # (!) real value is "<method 'getTotalTorque' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'get_angular_damping': None, # (!) real value is "<method 'get_angular_damping' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'get_angular_factor': None, # (!) real value is "<method 'get_angular_factor' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'get_angular_sleep_threshold': None, # (!) real value is "<method 'get_angular_sleep_threshold' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'get_angular_velocity': None, # (!) real value is "<method 'get_angular_velocity' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CD820>)>'
        'get_gravity': None, # (!) real value is "<method 'get_gravity' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'get_inertia': None, # (!) real value is "<method 'get_inertia' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'get_inv_inertia_diag_local': None, # (!) real value is "<method 'get_inv_inertia_diag_local' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'get_inv_inertia_tensor_world': None, # (!) real value is "<method 'get_inv_inertia_tensor_world' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'get_inv_mass': None, # (!) real value is "<method 'get_inv_mass' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'get_linear_damping': None, # (!) real value is "<method 'get_linear_damping' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'get_linear_factor': None, # (!) real value is "<method 'get_linear_factor' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'get_linear_sleep_threshold': None, # (!) real value is "<method 'get_linear_sleep_threshold' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'get_linear_velocity': None, # (!) real value is "<method 'get_linear_velocity' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'get_mass': None, # (!) real value is "<method 'get_mass' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'get_total_force': None, # (!) real value is "<method 'get_total_force' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'get_total_torque': None, # (!) real value is "<method 'get_total_torque' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'gravity': None, # (!) real value is "<attribute 'gravity' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'inertia': None, # (!) real value is "<attribute 'inertia' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'inv_inertia_diag_local': None, # (!) real value is "<attribute 'inv_inertia_diag_local' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'inv_inertia_tensor_world': None, # (!) real value is "<attribute 'inv_inertia_tensor_world' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'inv_mass': None, # (!) real value is "<attribute 'inv_mass' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'linear_damping': None, # (!) real value is "<attribute 'linear_damping' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'linear_factor': None, # (!) real value is "<attribute 'linear_factor' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'linear_sleep_threshold': None, # (!) real value is "<attribute 'linear_sleep_threshold' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'linear_velocity': None, # (!) real value is "<attribute 'linear_velocity' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'mass': None, # (!) real value is "<attribute 'mass' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'pickDirtyFlag': None, # (!) real value is "<method 'pickDirtyFlag' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'pick_dirty_flag': None, # (!) real value is "<method 'pick_dirty_flag' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'setAngularDamping': None, # (!) real value is "<method 'setAngularDamping' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'setAngularFactor': None, # (!) real value is "<method 'setAngularFactor' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'setAngularSleepThreshold': None, # (!) real value is "<method 'setAngularSleepThreshold' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'setAngularVelocity': None, # (!) real value is "<method 'setAngularVelocity' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'setGravity': None, # (!) real value is "<method 'setGravity' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'setInertia': None, # (!) real value is "<method 'setInertia' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'setLinearDamping': None, # (!) real value is "<method 'setLinearDamping' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'setLinearFactor': None, # (!) real value is "<method 'setLinearFactor' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'setLinearSleepThreshold': None, # (!) real value is "<method 'setLinearSleepThreshold' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'setLinearVelocity': None, # (!) real value is "<method 'setLinearVelocity' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'setMass': None, # (!) real value is "<method 'setMass' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'set_angular_damping': None, # (!) real value is "<method 'set_angular_damping' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'set_angular_factor': None, # (!) real value is "<method 'set_angular_factor' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'set_angular_sleep_threshold': None, # (!) real value is "<method 'set_angular_sleep_threshold' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'set_angular_velocity': None, # (!) real value is "<method 'set_angular_velocity' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'set_gravity': None, # (!) real value is "<method 'set_gravity' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'set_inertia': None, # (!) real value is "<method 'set_inertia' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'set_linear_damping': None, # (!) real value is "<method 'set_linear_damping' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'set_linear_factor': None, # (!) real value is "<method 'set_linear_factor' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'set_linear_sleep_threshold': None, # (!) real value is "<method 'set_linear_sleep_threshold' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'set_linear_velocity': None, # (!) real value is "<method 'set_linear_velocity' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'set_mass': None, # (!) real value is "<method 'set_mass' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'total_force': None, # (!) real value is "<attribute 'total_force' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
        'total_torque': None, # (!) real value is "<attribute 'total_torque' of 'panda3d.bullet.BulletRigidBodyNode' objects>"
    }


