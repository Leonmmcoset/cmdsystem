# encoding: utf-8
# module panda3d.bullet
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\bullet.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .BulletConstraint import BulletConstraint

class BulletHingeConstraint(BulletConstraint):
    """
    /**
     * The hinge constraint lets two bodies rotate around a given axis while
     * adhering to specified limits.  It's motor can apply angular force to them.
     */
    """
    def enableAngularMotor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        enable_angular_motor(const BulletHingeConstraint self, bool enable, float target_velocity, float max_impulse)
        
        /**
         * Applies an impulse to the constraint so that the angle changes at
         * target_velocity where max_impulse is the maximum impulse that is used for
         * achieving the specified velocity.
         *
         * Note that the target_velocity is in radians/second, not degrees.
         */
        """
        pass

    def enableMotor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        enable_motor(const BulletHingeConstraint self, bool enable)
        
        /**
         *
         */
        """
        pass

    def enable_angular_motor(self, const_BulletHingeConstraint_self, bool_enable, float_target_velocity, float_max_impulse): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        enable_angular_motor(const BulletHingeConstraint self, bool enable, float target_velocity, float max_impulse)
        
        /**
         * Applies an impulse to the constraint so that the angle changes at
         * target_velocity where max_impulse is the maximum impulse that is used for
         * achieving the specified velocity.
         *
         * Note that the target_velocity is in radians/second, not degrees.
         */
        """
        pass

    def enable_motor(self, const_BulletHingeConstraint_self, bool_enable): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        enable_motor(const BulletHingeConstraint self, bool enable)
        
        /**
         *
         */
        """
        pass

    def getAngularOnly(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_angular_only(BulletHingeConstraint self)
        
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

    def getFrameA(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_a(BulletHingeConstraint self)
        
        /**
         *
         */
        """
        pass

    def getFrameB(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_b(BulletHingeConstraint self)
        
        /**
         *
         */
        """
        pass

    def getHingeAngle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hinge_angle(const BulletHingeConstraint self)
        
        /**
         * Returns the angle between node_a and node_b in degrees.
         */
        """
        pass

    def getLowerLimit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lower_limit(BulletHingeConstraint self)
        
        /**
         * Returns the lower angular limit in degrees.
         */
        """
        pass

    def getUpperLimit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_upper_limit(BulletHingeConstraint self)
        
        /**
         * Returns the upper angular limit in degrees.
         */
        """
        pass

    def get_angular_only(self, BulletHingeConstraint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_angular_only(BulletHingeConstraint self)
        
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

    def get_frame_a(self, BulletHingeConstraint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_a(BulletHingeConstraint self)
        
        /**
         *
         */
        """
        pass

    def get_frame_b(self, BulletHingeConstraint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_b(BulletHingeConstraint self)
        
        /**
         *
         */
        """
        pass

    def get_hinge_angle(self, const_BulletHingeConstraint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hinge_angle(const BulletHingeConstraint self)
        
        /**
         * Returns the angle between node_a and node_b in degrees.
         */
        """
        pass

    def get_lower_limit(self, BulletHingeConstraint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lower_limit(BulletHingeConstraint self)
        
        /**
         * Returns the lower angular limit in degrees.
         */
        """
        pass

    def get_upper_limit(self, BulletHingeConstraint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_upper_limit(BulletHingeConstraint self)
        
        /**
         * Returns the upper angular limit in degrees.
         */
        """
        pass

    def setAngularOnly(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_angular_only(const BulletHingeConstraint self, bool value)
        
        /**
         *
         */
        """
        pass

    def setAxis(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_axis(const BulletHingeConstraint self, const LVector3f axis)
        
        /**
         * Sets the hinge's rotation axis in world coordinates.
         */
        """
        pass

    def setFrames(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frames(const BulletHingeConstraint self, const TransformState ts_a, const TransformState ts_b)
        
        /**
         *
         */
        """
        pass

    def setLimit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_limit(const BulletHingeConstraint self, float low, float high, float softness, float bias, float relaxation)
        
        /**
         * Sets the lower and upper rotational limits in degrees.
         */
        """
        pass

    def setMaxMotorImpulse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_motor_impulse(const BulletHingeConstraint self, float max_impulse)
        
        /**
         * Sets the maximum impulse used to achieve the velocity set in
         * enable_angular_motor.
         */
        """
        pass

    def setMotorTarget(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_motor_target(const BulletHingeConstraint self, const LQuaternionf quat, float dt)
        set_motor_target(const BulletHingeConstraint self, float target_angle, float dt)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def set_angular_only(self, const_BulletHingeConstraint_self, bool_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_angular_only(const BulletHingeConstraint self, bool value)
        
        /**
         *
         */
        """
        pass

    def set_axis(self, const_BulletHingeConstraint_self, const_LVector3f_axis): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_axis(const BulletHingeConstraint self, const LVector3f axis)
        
        /**
         * Sets the hinge's rotation axis in world coordinates.
         */
        """
        pass

    def set_frames(self, const_BulletHingeConstraint_self, const_TransformState_ts_a, const_TransformState_ts_b): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frames(const BulletHingeConstraint self, const TransformState ts_a, const TransformState ts_b)
        
        /**
         *
         */
        """
        pass

    def set_limit(self, const_BulletHingeConstraint_self, float_low, float_high, float_softness, float_bias, float_relaxation): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_limit(const BulletHingeConstraint self, float low, float high, float softness, float bias, float relaxation)
        
        /**
         * Sets the lower and upper rotational limits in degrees.
         */
        """
        pass

    def set_max_motor_impulse(self, const_BulletHingeConstraint_self, float_max_impulse): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_motor_impulse(const BulletHingeConstraint self, float max_impulse)
        
        /**
         * Sets the maximum impulse used to achieve the velocity set in
         * enable_angular_motor.
         */
        """
        pass

    def set_motor_target(self, const_BulletHingeConstraint_self, const_LQuaternionf_quat, float_dt): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_motor_target(const BulletHingeConstraint self, const LQuaternionf quat, float dt)
        set_motor_target(const BulletHingeConstraint self, float target_angle, float dt)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    angular_only = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame_a = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame_b = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hinge_angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lower_limit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    upper_limit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * The hinge constraint lets two bodies rotate around a given axis while\n * adhering to specified limits.  It's motor can apply angular force to them.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68D0AE0>'
        'angular_only': None, # (!) real value is "<attribute 'angular_only' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'enableAngularMotor': None, # (!) real value is "<method 'enableAngularMotor' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'enableMotor': None, # (!) real value is "<method 'enableMotor' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'enable_angular_motor': None, # (!) real value is "<method 'enable_angular_motor' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'enable_motor': None, # (!) real value is "<method 'enable_motor' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'frame_a': None, # (!) real value is "<attribute 'frame_a' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'frame_b': None, # (!) real value is "<attribute 'frame_b' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'getAngularOnly': None, # (!) real value is "<method 'getAngularOnly' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68D0AE0>)>'
        'getFrameA': None, # (!) real value is "<method 'getFrameA' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'getFrameB': None, # (!) real value is "<method 'getFrameB' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'getHingeAngle': None, # (!) real value is "<method 'getHingeAngle' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'getLowerLimit': None, # (!) real value is "<method 'getLowerLimit' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'getUpperLimit': None, # (!) real value is "<method 'getUpperLimit' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'get_angular_only': None, # (!) real value is "<method 'get_angular_only' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68D0AE0>)>'
        'get_frame_a': None, # (!) real value is "<method 'get_frame_a' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'get_frame_b': None, # (!) real value is "<method 'get_frame_b' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'get_hinge_angle': None, # (!) real value is "<method 'get_hinge_angle' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'get_lower_limit': None, # (!) real value is "<method 'get_lower_limit' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'get_upper_limit': None, # (!) real value is "<method 'get_upper_limit' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'hinge_angle': None, # (!) real value is "<attribute 'hinge_angle' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'lower_limit': None, # (!) real value is "<attribute 'lower_limit' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'setAngularOnly': None, # (!) real value is "<method 'setAngularOnly' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'setAxis': None, # (!) real value is "<method 'setAxis' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'setFrames': None, # (!) real value is "<method 'setFrames' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'setLimit': None, # (!) real value is "<method 'setLimit' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'setMaxMotorImpulse': None, # (!) real value is "<method 'setMaxMotorImpulse' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'setMotorTarget': None, # (!) real value is "<method 'setMotorTarget' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'set_angular_only': None, # (!) real value is "<method 'set_angular_only' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'set_axis': None, # (!) real value is "<method 'set_axis' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'set_frames': None, # (!) real value is "<method 'set_frames' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'set_limit': None, # (!) real value is "<method 'set_limit' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'set_max_motor_impulse': None, # (!) real value is "<method 'set_max_motor_impulse' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'set_motor_target': None, # (!) real value is "<method 'set_motor_target' of 'panda3d.bullet.BulletHingeConstraint' objects>"
        'upper_limit': None, # (!) real value is "<attribute 'upper_limit' of 'panda3d.bullet.BulletHingeConstraint' objects>"
    }


