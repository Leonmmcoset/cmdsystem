# encoding: utf-8
# module panda3d.bullet
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\bullet.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class BulletVehicle(__panda3d_core.TypedReferenceCount):
    """
    /**
     * Simulates a raycast vehicle which casts a ray per wheel at the ground as a
     * cheap replacement for complex suspension simulation.  The suspension can be
     * tuned in various ways.  It is possible to add a (probably) arbitrary number
     * of wheels.
     */
    """
    def applyEngineForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_engine_force(const BulletVehicle self, float force, int idx)
        
        /**
         * Applies force at the wheel with index idx for acceleration.
         */
        """
        pass

    def apply_engine_force(self, const_BulletVehicle_self, float_force, int_idx): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_engine_force(const BulletVehicle self, float force, int idx)
        
        /**
         * Applies force at the wheel with index idx for acceleration.
         */
        """
        pass

    def createWheel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        create_wheel(const BulletVehicle self)
        
        // Wheels
        
        /**
         * Factory method for creating wheels for this vehicle instance.
         */
        """
        pass

    def create_wheel(self, const_BulletVehicle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        create_wheel(const BulletVehicle self)
        
        // Wheels
        
        /**
         * Factory method for creating wheels for this vehicle instance.
         */
        """
        pass

    def getChassis(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_chassis(const BulletVehicle self)
        
        /**
         * Returns the chassis of this vehicle.  The chassis is a rigid body node.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCurrentSpeedKmHour(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_speed_km_hour(BulletVehicle self)
        
        /**
         * Returns the current speed in kilometers per hour.  Convert to miles using:
         * km/h * 0.62 = mph
         */
        """
        pass

    def getForwardVector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_forward_vector(BulletVehicle self)
        
        /**
         * Returns the forward vector representing the car's actual direction of
         * movement.  The forward vetcor is given in global coordinates.
         */
        """
        pass

    def getNumWheels(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_wheels(BulletVehicle self)
        
        /**
         * Returns the number of wheels this vehicle has.
         */
        """
        pass

    def getSteeringValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_steering_value(BulletVehicle self, int idx)
        
        /**
         * Returns the steering angle of the wheel with index idx in degrees.
         */
        """
        pass

    def getTuning(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tuning(const BulletVehicle self)
        
        // Tuning
        
        // Tuning
        
        /**
         * Returns a reference to the BulletVehicleTuning object of this vehicle which
         * offers various vehicle-global tuning options.  Make sure to configure this
         * before adding wheels!
         */
        """
        pass

    def getWheel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wheel(BulletVehicle self, int idx)
        
        /**
         * Returns the BulletWheel with index idx.  Causes an AssertionError if idx is
         * equal or larger than the number of wheels.
         */
        """
        pass

    def getWheels(self, *args, **kwargs): # real signature unknown
        pass

    def get_chassis(self, const_BulletVehicle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_chassis(const BulletVehicle self)
        
        /**
         * Returns the chassis of this vehicle.  The chassis is a rigid body node.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_current_speed_km_hour(self, BulletVehicle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_speed_km_hour(BulletVehicle self)
        
        /**
         * Returns the current speed in kilometers per hour.  Convert to miles using:
         * km/h * 0.62 = mph
         */
        """
        pass

    def get_forward_vector(self, BulletVehicle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_forward_vector(BulletVehicle self)
        
        /**
         * Returns the forward vector representing the car's actual direction of
         * movement.  The forward vetcor is given in global coordinates.
         */
        """
        pass

    def get_num_wheels(self, BulletVehicle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_wheels(BulletVehicle self)
        
        /**
         * Returns the number of wheels this vehicle has.
         */
        """
        pass

    def get_steering_value(self, BulletVehicle_self, int_idx): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_steering_value(BulletVehicle self, int idx)
        
        /**
         * Returns the steering angle of the wheel with index idx in degrees.
         */
        """
        pass

    def get_tuning(self, const_BulletVehicle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tuning(const BulletVehicle self)
        
        // Tuning
        
        // Tuning
        
        /**
         * Returns a reference to the BulletVehicleTuning object of this vehicle which
         * offers various vehicle-global tuning options.  Make sure to configure this
         * before adding wheels!
         */
        """
        pass

    def get_wheel(self, BulletVehicle_self, int_idx): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wheel(BulletVehicle self, int idx)
        
        /**
         * Returns the BulletWheel with index idx.  Causes an AssertionError if idx is
         * equal or larger than the number of wheels.
         */
        """
        pass

    def get_wheels(self, *args, **kwargs): # real signature unknown
        pass

    def resetSuspension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reset_suspension(const BulletVehicle self)
        
        /**
         * Resets the vehicle's suspension.
         */
        """
        pass

    def reset_suspension(self, const_BulletVehicle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset_suspension(const BulletVehicle self)
        
        /**
         * Resets the vehicle's suspension.
         */
        """
        pass

    def setBrake(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_brake(const BulletVehicle self, float brake, int idx)
        
        /**
         * Applies braking force to the wheel with index idx.
         */
        """
        pass

    def setCoordinateSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_coordinate_system(const BulletVehicle self, int up)
        
        /**
         * Specifies which axis is "up". Nessecary for the vehicle's suspension to
         * work properly!
         */
        """
        pass

    def setPitchControl(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pitch_control(const BulletVehicle self, float pitch)
        
        /**
         *
         */
        """
        pass

    def setSteeringValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_steering_value(const BulletVehicle self, float steering, int idx)
        
        /**
         * Sets the steering value (in degrees) of the wheel with index idx.
         */
        """
        pass

    def set_brake(self, const_BulletVehicle_self, float_brake, int_idx): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_brake(const BulletVehicle self, float brake, int idx)
        
        /**
         * Applies braking force to the wheel with index idx.
         */
        """
        pass

    def set_coordinate_system(self, const_BulletVehicle_self, int_up): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_coordinate_system(const BulletVehicle self, int up)
        
        /**
         * Specifies which axis is "up". Nessecary for the vehicle's suspension to
         * work properly!
         */
        """
        pass

    def set_pitch_control(self, const_BulletVehicle_self, float_pitch): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pitch_control(const BulletVehicle self, float pitch)
        
        /**
         *
         */
        """
        pass

    def set_steering_value(self, const_BulletVehicle_self, float_steering, int_idx): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_steering_value(const BulletVehicle self, float steering, int idx)
        
        /**
         * Sets the steering value (in degrees) of the wheel with index idx.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    chassis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    current_speed_km_hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forward_vector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tuning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// Tuning"""

    wheels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * Simulates a raycast vehicle which casts a ray per wheel at the ground as a\n * cheap replacement for complex suspension simulation.  The suspension can be\n * tuned in various ways.  It is possible to add a (probably) arbitrary number\n * of wheels.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.bullet.BulletVehicle' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CF180>'
        'applyEngineForce': None, # (!) real value is "<method 'applyEngineForce' of 'panda3d.bullet.BulletVehicle' objects>"
        'apply_engine_force': None, # (!) real value is "<method 'apply_engine_force' of 'panda3d.bullet.BulletVehicle' objects>"
        'chassis': None, # (!) real value is "<attribute 'chassis' of 'panda3d.bullet.BulletVehicle' objects>"
        'createWheel': None, # (!) real value is "<method 'createWheel' of 'panda3d.bullet.BulletVehicle' objects>"
        'create_wheel': None, # (!) real value is "<method 'create_wheel' of 'panda3d.bullet.BulletVehicle' objects>"
        'current_speed_km_hour': None, # (!) real value is "<attribute 'current_speed_km_hour' of 'panda3d.bullet.BulletVehicle' objects>"
        'forward_vector': None, # (!) real value is "<attribute 'forward_vector' of 'panda3d.bullet.BulletVehicle' objects>"
        'getChassis': None, # (!) real value is "<method 'getChassis' of 'panda3d.bullet.BulletVehicle' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CF180>)>'
        'getCurrentSpeedKmHour': None, # (!) real value is "<method 'getCurrentSpeedKmHour' of 'panda3d.bullet.BulletVehicle' objects>"
        'getForwardVector': None, # (!) real value is "<method 'getForwardVector' of 'panda3d.bullet.BulletVehicle' objects>"
        'getNumWheels': None, # (!) real value is "<method 'getNumWheels' of 'panda3d.bullet.BulletVehicle' objects>"
        'getSteeringValue': None, # (!) real value is "<method 'getSteeringValue' of 'panda3d.bullet.BulletVehicle' objects>"
        'getTuning': None, # (!) real value is "<method 'getTuning' of 'panda3d.bullet.BulletVehicle' objects>"
        'getWheel': None, # (!) real value is "<method 'getWheel' of 'panda3d.bullet.BulletVehicle' objects>"
        'getWheels': None, # (!) real value is "<method 'getWheels' of 'panda3d.bullet.BulletVehicle' objects>"
        'get_chassis': None, # (!) real value is "<method 'get_chassis' of 'panda3d.bullet.BulletVehicle' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CF180>)>'
        'get_current_speed_km_hour': None, # (!) real value is "<method 'get_current_speed_km_hour' of 'panda3d.bullet.BulletVehicle' objects>"
        'get_forward_vector': None, # (!) real value is "<method 'get_forward_vector' of 'panda3d.bullet.BulletVehicle' objects>"
        'get_num_wheels': None, # (!) real value is "<method 'get_num_wheels' of 'panda3d.bullet.BulletVehicle' objects>"
        'get_steering_value': None, # (!) real value is "<method 'get_steering_value' of 'panda3d.bullet.BulletVehicle' objects>"
        'get_tuning': None, # (!) real value is "<method 'get_tuning' of 'panda3d.bullet.BulletVehicle' objects>"
        'get_wheel': None, # (!) real value is "<method 'get_wheel' of 'panda3d.bullet.BulletVehicle' objects>"
        'get_wheels': None, # (!) real value is "<method 'get_wheels' of 'panda3d.bullet.BulletVehicle' objects>"
        'resetSuspension': None, # (!) real value is "<method 'resetSuspension' of 'panda3d.bullet.BulletVehicle' objects>"
        'reset_suspension': None, # (!) real value is "<method 'reset_suspension' of 'panda3d.bullet.BulletVehicle' objects>"
        'setBrake': None, # (!) real value is "<method 'setBrake' of 'panda3d.bullet.BulletVehicle' objects>"
        'setCoordinateSystem': None, # (!) real value is "<method 'setCoordinateSystem' of 'panda3d.bullet.BulletVehicle' objects>"
        'setPitchControl': None, # (!) real value is "<method 'setPitchControl' of 'panda3d.bullet.BulletVehicle' objects>"
        'setSteeringValue': None, # (!) real value is "<method 'setSteeringValue' of 'panda3d.bullet.BulletVehicle' objects>"
        'set_brake': None, # (!) real value is "<method 'set_brake' of 'panda3d.bullet.BulletVehicle' objects>"
        'set_coordinate_system': None, # (!) real value is "<method 'set_coordinate_system' of 'panda3d.bullet.BulletVehicle' objects>"
        'set_pitch_control': None, # (!) real value is "<method 'set_pitch_control' of 'panda3d.bullet.BulletVehicle' objects>"
        'set_steering_value': None, # (!) real value is "<method 'set_steering_value' of 'panda3d.bullet.BulletVehicle' objects>"
        'tuning': None, # (!) real value is "<attribute 'tuning' of 'panda3d.bullet.BulletVehicle' objects>"
        'wheels': None, # (!) real value is "<attribute 'wheels' of 'panda3d.bullet.BulletVehicle' objects>"
    }


