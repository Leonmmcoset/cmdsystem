# encoding: utf-8
# module panda3d.physics
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\physics.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class PhysicsObject(__panda3d_core.TypedReferenceCount):
    """
    /**
     * A body on which physics will be applied.  If you're looking to add physical
     * motion to your class, do NOT derive from this.  Derive from Physical
     * instead.
     */
    """
    def addImpact(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_impact(const PhysicsObject self, const LPoint3f offset_from_center_of_mass, const LVector3f impulse)
        
        /**
         * Adds an impulse and/or torque (i.e.  an instantanious change in velocity)
         * based on how well the offset and impulse align with the center of mass (aka
         * position). If you wanted to immitate this function you could work out the
         * impulse and torque and call add_impulse and add_torque respectively.
         * offset and force are in global (or parent) coordinates.
         */
        """
        pass

    def addImpulse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_impulse(const PhysicsObject self, const LVector3f impulse)
        
        /**
         * Adds an impulse force (i.e.  an instantanious change in velocity).  This is
         * a quicker way to get the velocity, add a vector to it and set that value to
         * be the new velocity.
         */
        """
        pass

    def addLocalImpact(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_local_impact(const PhysicsObject self, const LPoint3f offset_from_center_of_mass, const LVector3f impulse)
        
        /**
         * Adds an impulse and/or torque (i.e.  an instantanious change in velocity)
         * based on how well the offset and impulse align with the center of mass (aka
         * position). If you wanted to immitate this function you could work out the
         * impulse and torque and call add_impulse and add_torque respectively.
         * offset and force are in local coordinates.
         */
        """
        pass

    def addLocalImpulse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_local_impulse(const PhysicsObject self, const LVector3f impulse)
        
        /**
         * Adds an impulse force (i.e.  an instantanious change in velocity).  This is
         * a quicker way to get the velocity, add a vector to it and set that value to
         * be the new velocity.
         */
        """
        pass

    def addLocalTorque(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_local_torque(const PhysicsObject self, const LRotationf torque)
        
        // Local instantanious forces
        
        /**
         * Adds an torque force (i.e.  an instantanious change in velocity).  This is
         * a quicker way to get the angular velocity, add a vector to it and set that
         * value to be the new angular velocity.
         */
        """
        pass

    def addTorque(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_torque(const PhysicsObject self, const LRotationf torque)
        
        // Global instantanious forces
        
        /**
         * Adds an torque force (i.e.  an instantanious change in velocity).  This is
         * a quicker way to get the angular velocity, add a vector to it and set that
         * value to be the new angular velocity.
         */
        """
        pass

    def add_impact(self, const_PhysicsObject_self, const_LPoint3f_offset_from_center_of_mass, const_LVector3f_impulse): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_impact(const PhysicsObject self, const LPoint3f offset_from_center_of_mass, const LVector3f impulse)
        
        /**
         * Adds an impulse and/or torque (i.e.  an instantanious change in velocity)
         * based on how well the offset and impulse align with the center of mass (aka
         * position). If you wanted to immitate this function you could work out the
         * impulse and torque and call add_impulse and add_torque respectively.
         * offset and force are in global (or parent) coordinates.
         */
        """
        pass

    def add_impulse(self, const_PhysicsObject_self, const_LVector3f_impulse): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_impulse(const PhysicsObject self, const LVector3f impulse)
        
        /**
         * Adds an impulse force (i.e.  an instantanious change in velocity).  This is
         * a quicker way to get the velocity, add a vector to it and set that value to
         * be the new velocity.
         */
        """
        pass

    def add_local_impact(self, const_PhysicsObject_self, const_LPoint3f_offset_from_center_of_mass, const_LVector3f_impulse): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_local_impact(const PhysicsObject self, const LPoint3f offset_from_center_of_mass, const LVector3f impulse)
        
        /**
         * Adds an impulse and/or torque (i.e.  an instantanious change in velocity)
         * based on how well the offset and impulse align with the center of mass (aka
         * position). If you wanted to immitate this function you could work out the
         * impulse and torque and call add_impulse and add_torque respectively.
         * offset and force are in local coordinates.
         */
        """
        pass

    def add_local_impulse(self, const_PhysicsObject_self, const_LVector3f_impulse): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_local_impulse(const PhysicsObject self, const LVector3f impulse)
        
        /**
         * Adds an impulse force (i.e.  an instantanious change in velocity).  This is
         * a quicker way to get the velocity, add a vector to it and set that value to
         * be the new velocity.
         */
        """
        pass

    def add_local_torque(self, const_PhysicsObject_self, const_LRotationf_torque): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_local_torque(const PhysicsObject self, const LRotationf torque)
        
        // Local instantanious forces
        
        /**
         * Adds an torque force (i.e.  an instantanious change in velocity).  This is
         * a quicker way to get the angular velocity, add a vector to it and set that
         * value to be the new angular velocity.
         */
        """
        pass

    def add_torque(self, const_PhysicsObject_self, const_LRotationf_torque): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_torque(const PhysicsObject self, const LRotationf torque)
        
        // Global instantanious forces
        
        /**
         * Adds an torque force (i.e.  an instantanious change in velocity).  This is
         * a quicker way to get the angular velocity, add a vector to it and set that
         * value to be the new angular velocity.
         */
        """
        pass

    def assign(self, const_PhysicsObject_self, const_PhysicsObject_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const PhysicsObject self, const PhysicsObject other)
        
        /**
         *
         */
        """
        pass

    def getActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_active(PhysicsObject self)
        
        /**
         * Process Flag Query
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getImplicitVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_implicit_velocity(PhysicsObject self)
        
        /**
         * Velocity Query over the last dt
         */
        """
        pass

    def getInertialTensor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_inertial_tensor(PhysicsObject self)
        
        /**
         * returns a transform matrix that represents the object's willingness to be
         * forced.
         */
        """
        pass

    def getLastPosition(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_last_position(PhysicsObject self)
        
        /**
         * Get the position of the physics object at the start of the most recent
         * do_physics.
         */
        """
        pass

    def getLcs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lcs(PhysicsObject self)
        
        /**
         * returns a transform matrix to this object's local coordinate system.
         */
        """
        pass

    def getMass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mass(PhysicsObject self)
        
        /**
         * Get the mass in slugs (or kilograms).
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(const PhysicsObject self)
        """
        pass

    def getOrientation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_orientation(PhysicsObject self)
        
        /**
         * get current orientation.
         */
        """
        pass

    def getOriented(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_oriented(PhysicsObject self)
        
        /**
         * See set_oriented().
         */
        """
        pass

    def getPosition(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_position(PhysicsObject self)
        
        /**
         * Position Query
         */
        """
        pass

    def getRotation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_rotation(PhysicsObject self)
        
        /**
         * get rotation per second.
         */
        """
        pass

    def getTerminalVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_terminal_velocity(PhysicsObject self)
        
        /**
         * tv query
         */
        """
        pass

    def getVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_velocity(PhysicsObject self)
        
        /**
         * Velocity Query per second
         */
        """
        pass

    def get_active(self, PhysicsObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_active(PhysicsObject self)
        
        /**
         * Process Flag Query
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_implicit_velocity(self, PhysicsObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_implicit_velocity(PhysicsObject self)
        
        /**
         * Velocity Query over the last dt
         */
        """
        pass

    def get_inertial_tensor(self, PhysicsObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_inertial_tensor(PhysicsObject self)
        
        /**
         * returns a transform matrix that represents the object's willingness to be
         * forced.
         */
        """
        pass

    def get_last_position(self, PhysicsObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_last_position(PhysicsObject self)
        
        /**
         * Get the position of the physics object at the start of the most recent
         * do_physics.
         */
        """
        pass

    def get_lcs(self, PhysicsObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lcs(PhysicsObject self)
        
        /**
         * returns a transform matrix to this object's local coordinate system.
         */
        """
        pass

    def get_mass(self, PhysicsObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mass(PhysicsObject self)
        
        /**
         * Get the mass in slugs (or kilograms).
         */
        """
        pass

    def get_name(self, const_PhysicsObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(const PhysicsObject self)
        """
        pass

    def get_orientation(self, PhysicsObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_orientation(PhysicsObject self)
        
        /**
         * get current orientation.
         */
        """
        pass

    def get_oriented(self, PhysicsObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_oriented(PhysicsObject self)
        
        /**
         * See set_oriented().
         */
        """
        pass

    def get_position(self, PhysicsObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_position(PhysicsObject self)
        
        /**
         * Position Query
         */
        """
        pass

    def get_rotation(self, PhysicsObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_rotation(PhysicsObject self)
        
        /**
         * get rotation per second.
         */
        """
        pass

    def get_terminal_velocity(self, PhysicsObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_terminal_velocity(PhysicsObject self)
        
        /**
         * tv query
         */
        """
        pass

    def get_velocity(self, PhysicsObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_velocity(PhysicsObject self)
        
        /**
         * Velocity Query per second
         */
        """
        pass

    def makeCopy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_copy(PhysicsObject self)
        
        /**
         * dynamic copy.
         */
        """
        pass

    def make_copy(self, PhysicsObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_copy(PhysicsObject self)
        
        /**
         * dynamic copy.
         */
        """
        pass

    def output(self, PhysicsObject_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(PhysicsObject self, ostream out)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def resetOrientation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reset_orientation(const PhysicsObject self, const LOrientationf orientation)
        
        /**
         * set the orientation while clearing the rotation velocity.
         */
        """
        pass

    def resetPosition(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reset_position(const PhysicsObject self, const LPoint3f pos)
        
        /**
         * use this to place an object in a completely new position, that has nothing
         * to do with its last position.
         */
        """
        pass

    def reset_orientation(self, const_PhysicsObject_self, const_LOrientationf_orientation): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset_orientation(const PhysicsObject self, const LOrientationf orientation)
        
        /**
         * set the orientation while clearing the rotation velocity.
         */
        """
        pass

    def reset_position(self, const_PhysicsObject_self, const_LPoint3f_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset_position(const PhysicsObject self, const LPoint3f pos)
        
        /**
         * use this to place an object in a completely new position, that has nothing
         * to do with its last position.
         */
        """
        pass

    def setActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_active(const PhysicsObject self, bool flag)
        
        /**
         * Process Flag assignment
         */
        """
        pass

    def setLastPosition(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_last_position(const PhysicsObject self, const LPoint3f pos)
        
        /**
         * Last position assignment
         */
        """
        pass

    def setMass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_mass(const PhysicsObject self, float param0)
        
        /**
         * Set the mass in slugs (or kilograms).
         */
        """
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_name(const PhysicsObject self, str name)
        """
        pass

    def setOrientation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_orientation(const PhysicsObject self, const LOrientationf orientation)
        
        /**
         *
         */
        """
        pass

    def setOriented(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_oriented(const PhysicsObject self, bool flag)
        
        /**
         * Set flag to determine whether this object should do any rotation or
         * orientation calculations.  Optimization.
         */
        """
        pass

    def setPosition(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_position(const PhysicsObject self, const LPoint3f pos)
        set_position(const PhysicsObject self, float x, float y, float z)
        
        // INLINE void set_center_of_mass(const LPoint3 &pos); use set_position.
        
        // INLINE void set_center_of_mass(const LPoint3 &pos); use set_position.
        
        /**
         * Vector position assignment.  This is also used as the center of mass.
         */
        
        /**
         * Piecewise position assignment
         */
        """
        pass

    def setRotation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_rotation(const PhysicsObject self, const LRotationf rotation)
        
        /**
         * set rotation as a quaternion delta per second.
         */
        """
        pass

    def setTerminalVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_terminal_velocity(const PhysicsObject self, float tv)
        
        /**
         * tv assignment
         */
        """
        pass

    def setVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_velocity(const PhysicsObject self, const LVector3f vel)
        set_velocity(const PhysicsObject self, float x, float y, float z)
        
        /**
         * Vector velocity assignment
         */
        
        /**
         * Piecewise velocity assignment
         */
        """
        pass

    def set_active(self, const_PhysicsObject_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_active(const PhysicsObject self, bool flag)
        
        /**
         * Process Flag assignment
         */
        """
        pass

    def set_last_position(self, const_PhysicsObject_self, const_LPoint3f_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_last_position(const PhysicsObject self, const LPoint3f pos)
        
        /**
         * Last position assignment
         */
        """
        pass

    def set_mass(self, const_PhysicsObject_self, float_param0): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_mass(const PhysicsObject self, float param0)
        
        /**
         * Set the mass in slugs (or kilograms).
         */
        """
        pass

    def set_name(self, const_PhysicsObject_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_name(const PhysicsObject self, str name)
        """
        pass

    def set_orientation(self, const_PhysicsObject_self, const_LOrientationf_orientation): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_orientation(const PhysicsObject self, const LOrientationf orientation)
        
        /**
         *
         */
        """
        pass

    def set_oriented(self, const_PhysicsObject_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_oriented(const PhysicsObject self, bool flag)
        
        /**
         * Set flag to determine whether this object should do any rotation or
         * orientation calculations.  Optimization.
         */
        """
        pass

    def set_position(self, const_PhysicsObject_self, const_LPoint3f_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_position(const PhysicsObject self, const LPoint3f pos)
        set_position(const PhysicsObject self, float x, float y, float z)
        
        // INLINE void set_center_of_mass(const LPoint3 &pos); use set_position.
        
        // INLINE void set_center_of_mass(const LPoint3 &pos); use set_position.
        
        /**
         * Vector position assignment.  This is also used as the center of mass.
         */
        
        /**
         * Piecewise position assignment
         */
        """
        pass

    def set_rotation(self, const_PhysicsObject_self, const_LRotationf_rotation): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_rotation(const PhysicsObject self, const LRotationf rotation)
        
        /**
         * set rotation as a quaternion delta per second.
         */
        """
        pass

    def set_terminal_velocity(self, const_PhysicsObject_self, float_tv): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_terminal_velocity(const PhysicsObject self, float tv)
        
        /**
         * tv assignment
         */
        """
        pass

    def set_velocity(self, const_PhysicsObject_self, const_LVector3f_vel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_velocity(const PhysicsObject self, const LVector3f vel)
        set_velocity(const PhysicsObject self, float x, float y, float z)
        
        /**
         * Vector velocity assignment
         */
        
        /**
         * Piecewise velocity assignment
         */
        """
        pass

    def write(self, PhysicsObject_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(PhysicsObject self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    implicit_velocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    orientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    oriented = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    terminal_velocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    velocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.physics.PhysicsObject' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.physics.PhysicsObject' objects>"
        '__doc__': "/**\n * A body on which physics will be applied.  If you're looking to add physical\n * motion to your class, do NOT derive from this.  Derive from Physical\n * instead.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.physics.PhysicsObject' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DEB3E0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.physics.PhysicsObject' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.physics.PhysicsObject' objects>"
        'active': None, # (!) real value is "<attribute 'active' of 'panda3d.physics.PhysicsObject' objects>"
        'addImpact': None, # (!) real value is "<method 'addImpact' of 'panda3d.physics.PhysicsObject' objects>"
        'addImpulse': None, # (!) real value is "<method 'addImpulse' of 'panda3d.physics.PhysicsObject' objects>"
        'addLocalImpact': None, # (!) real value is "<method 'addLocalImpact' of 'panda3d.physics.PhysicsObject' objects>"
        'addLocalImpulse': None, # (!) real value is "<method 'addLocalImpulse' of 'panda3d.physics.PhysicsObject' objects>"
        'addLocalTorque': None, # (!) real value is "<method 'addLocalTorque' of 'panda3d.physics.PhysicsObject' objects>"
        'addTorque': None, # (!) real value is "<method 'addTorque' of 'panda3d.physics.PhysicsObject' objects>"
        'add_impact': None, # (!) real value is "<method 'add_impact' of 'panda3d.physics.PhysicsObject' objects>"
        'add_impulse': None, # (!) real value is "<method 'add_impulse' of 'panda3d.physics.PhysicsObject' objects>"
        'add_local_impact': None, # (!) real value is "<method 'add_local_impact' of 'panda3d.physics.PhysicsObject' objects>"
        'add_local_impulse': None, # (!) real value is "<method 'add_local_impulse' of 'panda3d.physics.PhysicsObject' objects>"
        'add_local_torque': None, # (!) real value is "<method 'add_local_torque' of 'panda3d.physics.PhysicsObject' objects>"
        'add_torque': None, # (!) real value is "<method 'add_torque' of 'panda3d.physics.PhysicsObject' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.physics.PhysicsObject' objects>"
        'getActive': None, # (!) real value is "<method 'getActive' of 'panda3d.physics.PhysicsObject' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC9DEB3E0>)>'
        'getImplicitVelocity': None, # (!) real value is "<method 'getImplicitVelocity' of 'panda3d.physics.PhysicsObject' objects>"
        'getInertialTensor': None, # (!) real value is "<method 'getInertialTensor' of 'panda3d.physics.PhysicsObject' objects>"
        'getLastPosition': None, # (!) real value is "<method 'getLastPosition' of 'panda3d.physics.PhysicsObject' objects>"
        'getLcs': None, # (!) real value is "<method 'getLcs' of 'panda3d.physics.PhysicsObject' objects>"
        'getMass': None, # (!) real value is "<method 'getMass' of 'panda3d.physics.PhysicsObject' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.physics.PhysicsObject' objects>"
        'getOrientation': None, # (!) real value is "<method 'getOrientation' of 'panda3d.physics.PhysicsObject' objects>"
        'getOriented': None, # (!) real value is "<method 'getOriented' of 'panda3d.physics.PhysicsObject' objects>"
        'getPosition': None, # (!) real value is "<method 'getPosition' of 'panda3d.physics.PhysicsObject' objects>"
        'getRotation': None, # (!) real value is "<method 'getRotation' of 'panda3d.physics.PhysicsObject' objects>"
        'getTerminalVelocity': None, # (!) real value is "<method 'getTerminalVelocity' of 'panda3d.physics.PhysicsObject' objects>"
        'getVelocity': None, # (!) real value is "<method 'getVelocity' of 'panda3d.physics.PhysicsObject' objects>"
        'get_active': None, # (!) real value is "<method 'get_active' of 'panda3d.physics.PhysicsObject' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC9DEB3E0>)>'
        'get_implicit_velocity': None, # (!) real value is "<method 'get_implicit_velocity' of 'panda3d.physics.PhysicsObject' objects>"
        'get_inertial_tensor': None, # (!) real value is "<method 'get_inertial_tensor' of 'panda3d.physics.PhysicsObject' objects>"
        'get_last_position': None, # (!) real value is "<method 'get_last_position' of 'panda3d.physics.PhysicsObject' objects>"
        'get_lcs': None, # (!) real value is "<method 'get_lcs' of 'panda3d.physics.PhysicsObject' objects>"
        'get_mass': None, # (!) real value is "<method 'get_mass' of 'panda3d.physics.PhysicsObject' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.physics.PhysicsObject' objects>"
        'get_orientation': None, # (!) real value is "<method 'get_orientation' of 'panda3d.physics.PhysicsObject' objects>"
        'get_oriented': None, # (!) real value is "<method 'get_oriented' of 'panda3d.physics.PhysicsObject' objects>"
        'get_position': None, # (!) real value is "<method 'get_position' of 'panda3d.physics.PhysicsObject' objects>"
        'get_rotation': None, # (!) real value is "<method 'get_rotation' of 'panda3d.physics.PhysicsObject' objects>"
        'get_terminal_velocity': None, # (!) real value is "<method 'get_terminal_velocity' of 'panda3d.physics.PhysicsObject' objects>"
        'get_velocity': None, # (!) real value is "<method 'get_velocity' of 'panda3d.physics.PhysicsObject' objects>"
        'implicit_velocity': None, # (!) real value is "<attribute 'implicit_velocity' of 'panda3d.physics.PhysicsObject' objects>"
        'last_position': None, # (!) real value is "<attribute 'last_position' of 'panda3d.physics.PhysicsObject' objects>"
        'makeCopy': None, # (!) real value is "<method 'makeCopy' of 'panda3d.physics.PhysicsObject' objects>"
        'make_copy': None, # (!) real value is "<method 'make_copy' of 'panda3d.physics.PhysicsObject' objects>"
        'mass': None, # (!) real value is "<attribute 'mass' of 'panda3d.physics.PhysicsObject' objects>"
        'orientation': None, # (!) real value is "<attribute 'orientation' of 'panda3d.physics.PhysicsObject' objects>"
        'oriented': None, # (!) real value is "<attribute 'oriented' of 'panda3d.physics.PhysicsObject' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.physics.PhysicsObject' objects>"
        'position': None, # (!) real value is "<attribute 'position' of 'panda3d.physics.PhysicsObject' objects>"
        'resetOrientation': None, # (!) real value is "<method 'resetOrientation' of 'panda3d.physics.PhysicsObject' objects>"
        'resetPosition': None, # (!) real value is "<method 'resetPosition' of 'panda3d.physics.PhysicsObject' objects>"
        'reset_orientation': None, # (!) real value is "<method 'reset_orientation' of 'panda3d.physics.PhysicsObject' objects>"
        'reset_position': None, # (!) real value is "<method 'reset_position' of 'panda3d.physics.PhysicsObject' objects>"
        'rotation': None, # (!) real value is "<attribute 'rotation' of 'panda3d.physics.PhysicsObject' objects>"
        'setActive': None, # (!) real value is "<method 'setActive' of 'panda3d.physics.PhysicsObject' objects>"
        'setLastPosition': None, # (!) real value is "<method 'setLastPosition' of 'panda3d.physics.PhysicsObject' objects>"
        'setMass': None, # (!) real value is "<method 'setMass' of 'panda3d.physics.PhysicsObject' objects>"
        'setName': None, # (!) real value is "<method 'setName' of 'panda3d.physics.PhysicsObject' objects>"
        'setOrientation': None, # (!) real value is "<method 'setOrientation' of 'panda3d.physics.PhysicsObject' objects>"
        'setOriented': None, # (!) real value is "<method 'setOriented' of 'panda3d.physics.PhysicsObject' objects>"
        'setPosition': None, # (!) real value is "<method 'setPosition' of 'panda3d.physics.PhysicsObject' objects>"
        'setRotation': None, # (!) real value is "<method 'setRotation' of 'panda3d.physics.PhysicsObject' objects>"
        'setTerminalVelocity': None, # (!) real value is "<method 'setTerminalVelocity' of 'panda3d.physics.PhysicsObject' objects>"
        'setVelocity': None, # (!) real value is "<method 'setVelocity' of 'panda3d.physics.PhysicsObject' objects>"
        'set_active': None, # (!) real value is "<method 'set_active' of 'panda3d.physics.PhysicsObject' objects>"
        'set_last_position': None, # (!) real value is "<method 'set_last_position' of 'panda3d.physics.PhysicsObject' objects>"
        'set_mass': None, # (!) real value is "<method 'set_mass' of 'panda3d.physics.PhysicsObject' objects>"
        'set_name': None, # (!) real value is "<method 'set_name' of 'panda3d.physics.PhysicsObject' objects>"
        'set_orientation': None, # (!) real value is "<method 'set_orientation' of 'panda3d.physics.PhysicsObject' objects>"
        'set_oriented': None, # (!) real value is "<method 'set_oriented' of 'panda3d.physics.PhysicsObject' objects>"
        'set_position': None, # (!) real value is "<method 'set_position' of 'panda3d.physics.PhysicsObject' objects>"
        'set_rotation': None, # (!) real value is "<method 'set_rotation' of 'panda3d.physics.PhysicsObject' objects>"
        'set_terminal_velocity': None, # (!) real value is "<method 'set_terminal_velocity' of 'panda3d.physics.PhysicsObject' objects>"
        'set_velocity': None, # (!) real value is "<method 'set_velocity' of 'panda3d.physics.PhysicsObject' objects>"
        'terminal_velocity': None, # (!) real value is "<attribute 'terminal_velocity' of 'panda3d.physics.PhysicsObject' objects>"
        'velocity': None, # (!) real value is "<attribute 'velocity' of 'panda3d.physics.PhysicsObject' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.physics.PhysicsObject' objects>"
    }


