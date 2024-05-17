# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CollisionHandlerPhysical import CollisionHandlerPhysical

class CollisionHandlerGravity(CollisionHandlerPhysical):
    """
    /**
     * A specialized kind of CollisionHandler that sets the Z height of the
     * collider to a fixed linear offset from the highest detected collision point
     * each frame.  It's intended to implement walking around on a floor of
     * varying height by casting a ray down from the avatar's head.
     */
    """
    def addVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_velocity(const CollisionHandlerGravity self, float velocity)
        
        /**
         * Adds the sepcified amount to the current velocity.  This is mostly here
         * allow this common operation to be faster for scripting, but it's also more
         * concise even in cpp.
         */
        """
        pass

    def add_velocity(self, const_CollisionHandlerGravity_self, float_velocity): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_velocity(const CollisionHandlerGravity self, float velocity)
        
        /**
         * Adds the sepcified amount to the current velocity.  This is mostly here
         * allow this common operation to be faster for scripting, but it's also more
         * concise even in cpp.
         */
        """
        pass

    def getAirborneHeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_airborne_height(CollisionHandlerGravity self)
        
        /**
         * Return the height of the object from the ground.
         *
         * The object might not necessarily be at rest.  Use is_on_ground() if you
         * want to know whether the object is on the ground and at rest.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getContactNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_contact_normal(CollisionHandlerGravity self)
        
        /**
         *
         */
        """
        pass

    def getGravity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_gravity(CollisionHandlerGravity self)
        
        /**
         * Gets the linear gravity force (always plumb).
         */
        """
        pass

    def getImpactVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_impact_velocity(CollisionHandlerGravity self)
        
        /**
         * How hard did the object hit the ground.  This value is set on impact with
         * the ground.  You may want to watch (poll) on is_on_ground() and when that is
         * true, call get_impact_velocity(). Normally I avoid polling, but we are
         * calling is_on_ground() frequently anyway.
         */
        """
        pass

    def getLegacyMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_legacy_mode(CollisionHandlerGravity self)
        
        /**
         * returns true if legacy mode is enabled
         */
        """
        pass

    def getMaxVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_velocity(CollisionHandlerGravity self)
        
        /**
         * Retrieves the maximum speed at which the object will be allowed to descend
         * towards a floor below it, in units per second.  See set_max_velocity().
         */
        """
        pass

    def getOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_offset(CollisionHandlerGravity self)
        
        /**
         * Returns the linear offset to add to (or subtract from) the highest detected
         * collision point to determine the actual height at which to set the
         * collider.
         */
        """
        pass

    def getReach(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_reach(CollisionHandlerGravity self)
        
        /**
         * Returns the reach to add to (or subtract from) the highest collision point
         */
        """
        pass

    def getVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_velocity(CollisionHandlerGravity self)
        
        /**
         * Gets the current vertical velocity.
         *
         * Generally, negative values mean the object is in free fall; while postive
         * values mean the object has vertical thrust.
         *
         * A zero value does not necessarily mean the object on the ground, it may
         * also be weightless and/or at the apex of its jump.
         *
         * See Also: is_on_ground() and get_gravity()
         */
        """
        pass

    def get_airborne_height(self, CollisionHandlerGravity_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_airborne_height(CollisionHandlerGravity self)
        
        /**
         * Return the height of the object from the ground.
         *
         * The object might not necessarily be at rest.  Use is_on_ground() if you
         * want to know whether the object is on the ground and at rest.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_contact_normal(self, CollisionHandlerGravity_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_contact_normal(CollisionHandlerGravity self)
        
        /**
         *
         */
        """
        pass

    def get_gravity(self, CollisionHandlerGravity_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_gravity(CollisionHandlerGravity self)
        
        /**
         * Gets the linear gravity force (always plumb).
         */
        """
        pass

    def get_impact_velocity(self, CollisionHandlerGravity_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_impact_velocity(CollisionHandlerGravity self)
        
        /**
         * How hard did the object hit the ground.  This value is set on impact with
         * the ground.  You may want to watch (poll) on is_on_ground() and when that is
         * true, call get_impact_velocity(). Normally I avoid polling, but we are
         * calling is_on_ground() frequently anyway.
         */
        """
        pass

    def get_legacy_mode(self, CollisionHandlerGravity_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_legacy_mode(CollisionHandlerGravity self)
        
        /**
         * returns true if legacy mode is enabled
         */
        """
        pass

    def get_max_velocity(self, CollisionHandlerGravity_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_velocity(CollisionHandlerGravity self)
        
        /**
         * Retrieves the maximum speed at which the object will be allowed to descend
         * towards a floor below it, in units per second.  See set_max_velocity().
         */
        """
        pass

    def get_offset(self, CollisionHandlerGravity_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_offset(CollisionHandlerGravity self)
        
        /**
         * Returns the linear offset to add to (or subtract from) the highest detected
         * collision point to determine the actual height at which to set the
         * collider.
         */
        """
        pass

    def get_reach(self, CollisionHandlerGravity_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_reach(CollisionHandlerGravity self)
        
        /**
         * Returns the reach to add to (or subtract from) the highest collision point
         */
        """
        pass

    def get_velocity(self, CollisionHandlerGravity_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_velocity(CollisionHandlerGravity self)
        
        /**
         * Gets the current vertical velocity.
         *
         * Generally, negative values mean the object is in free fall; while postive
         * values mean the object has vertical thrust.
         *
         * A zero value does not necessarily mean the object on the ground, it may
         * also be weightless and/or at the apex of its jump.
         *
         * See Also: is_on_ground() and get_gravity()
         */
        """
        pass

    def isOnGround(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_on_ground(CollisionHandlerGravity self)
        
        /**
         * Is the object at rest?
         */
        """
        pass

    def is_on_ground(self, CollisionHandlerGravity_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_on_ground(CollisionHandlerGravity self)
        
        /**
         * Is the object at rest?
         */
        """
        pass

    def readDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_datagram(const CollisionHandlerGravity self, DatagramIterator source)
        
        /**
         * Restores the object state from the given datagram, previously obtained using
         * __getstate__.
         */
        """
        pass

    def read_datagram(self, const_CollisionHandlerGravity_self, DatagramIterator_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_datagram(const CollisionHandlerGravity self, DatagramIterator source)
        
        /**
         * Restores the object state from the given datagram, previously obtained using
         * __getstate__.
         */
        """
        pass

    def setGravity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_gravity(const CollisionHandlerGravity self, float gravity)
        
        /**
         * Sets the linear gravity force (always plumb).
         */
        """
        pass

    def setLegacyMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_legacy_mode(const CollisionHandlerGravity self, bool legacy_mode)
        
        /**
         * Enables old behavior required by Toontown (Sellbot Factory lava room is
         * good test case, lava and conveyor belt specifically). Behavior is to throw
         * enter/exit events only for floor that the toon is in contact with
         */
        """
        pass

    def setMaxVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_velocity(const CollisionHandlerGravity self, float max_vel)
        
        /**
         * Sets the maximum speed at which the object will be allowed to descend
         * towards a floor below it, in units per second.  Set this to zero to allow
         * it to instantly teleport any distance.
         */
        """
        pass

    def setOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_offset(const CollisionHandlerGravity self, float offset)
        
        /**
         * Sets the linear offset to add to (or subtract from) the highest detected
         * collision point to determine the actual height at which to set the
         * collider.
         */
        """
        pass

    def setReach(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_reach(const CollisionHandlerGravity self, float reach)
        
        /**
         * Sets the reach to add to (or subtract from) the highest collision point
         */
        """
        pass

    def setVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_velocity(const CollisionHandlerGravity self, float velocity)
        
        /**
         * Sets the current vertical velocity.
         */
        """
        pass

    def set_gravity(self, const_CollisionHandlerGravity_self, float_gravity): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_gravity(const CollisionHandlerGravity self, float gravity)
        
        /**
         * Sets the linear gravity force (always plumb).
         */
        """
        pass

    def set_legacy_mode(self, const_CollisionHandlerGravity_self, bool_legacy_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_legacy_mode(const CollisionHandlerGravity self, bool legacy_mode)
        
        /**
         * Enables old behavior required by Toontown (Sellbot Factory lava room is
         * good test case, lava and conveyor belt specifically). Behavior is to throw
         * enter/exit events only for floor that the toon is in contact with
         */
        """
        pass

    def set_max_velocity(self, const_CollisionHandlerGravity_self, float_max_vel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_velocity(const CollisionHandlerGravity self, float max_vel)
        
        /**
         * Sets the maximum speed at which the object will be allowed to descend
         * towards a floor below it, in units per second.  Set this to zero to allow
         * it to instantly teleport any distance.
         */
        """
        pass

    def set_offset(self, const_CollisionHandlerGravity_self, float_offset): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_offset(const CollisionHandlerGravity self, float offset)
        
        /**
         * Sets the linear offset to add to (or subtract from) the highest detected
         * collision point to determine the actual height at which to set the
         * collider.
         */
        """
        pass

    def set_reach(self, const_CollisionHandlerGravity_self, float_reach): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_reach(const CollisionHandlerGravity self, float reach)
        
        /**
         * Sets the reach to add to (or subtract from) the highest collision point
         */
        """
        pass

    def set_velocity(self, const_CollisionHandlerGravity_self, float_velocity): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_velocity(const CollisionHandlerGravity self, float velocity)
        
        /**
         * Sets the current vertical velocity.
         */
        """
        pass

    def writeDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_datagram(CollisionHandlerGravity self, Datagram destination)
        
        /**
         * Serializes this object, to implement pickle support.
         */
        """
        pass

    def write_datagram(self, CollisionHandlerGravity_self, Datagram_destination): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_datagram(CollisionHandlerGravity self, Datagram destination)
        
        /**
         * Serializes this object, to implement pickle support.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    airborne_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    contact_normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gravity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    impact_velocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_velocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    on_ground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reach = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    velocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * A specialized kind of CollisionHandler that sets the Z height of the\n * collider to a fixed linear offset from the highest detected collision point\n * each frame.  It's intended to implement walking around on a floor of\n * varying height by casting a ray down from the avatar's head.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CollisionHandlerGravity' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2CF8B0>'
        'addVelocity': None, # (!) real value is "<method 'addVelocity' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'add_velocity': None, # (!) real value is "<method 'add_velocity' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'airborne_height': None, # (!) real value is "<attribute 'airborne_height' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'contact_normal': None, # (!) real value is "<attribute 'contact_normal' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'getAirborneHeight': None, # (!) real value is "<method 'getAirborneHeight' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2CF8B0>)>'
        'getContactNormal': None, # (!) real value is "<method 'getContactNormal' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'getGravity': None, # (!) real value is "<method 'getGravity' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'getImpactVelocity': None, # (!) real value is "<method 'getImpactVelocity' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'getLegacyMode': None, # (!) real value is "<method 'getLegacyMode' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'getMaxVelocity': None, # (!) real value is "<method 'getMaxVelocity' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'getOffset': None, # (!) real value is "<method 'getOffset' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'getReach': None, # (!) real value is "<method 'getReach' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'getVelocity': None, # (!) real value is "<method 'getVelocity' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'get_airborne_height': None, # (!) real value is "<method 'get_airborne_height' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2CF8B0>)>'
        'get_contact_normal': None, # (!) real value is "<method 'get_contact_normal' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'get_gravity': None, # (!) real value is "<method 'get_gravity' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'get_impact_velocity': None, # (!) real value is "<method 'get_impact_velocity' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'get_legacy_mode': None, # (!) real value is "<method 'get_legacy_mode' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'get_max_velocity': None, # (!) real value is "<method 'get_max_velocity' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'get_offset': None, # (!) real value is "<method 'get_offset' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'get_reach': None, # (!) real value is "<method 'get_reach' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'get_velocity': None, # (!) real value is "<method 'get_velocity' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'gravity': None, # (!) real value is "<attribute 'gravity' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'impact_velocity': None, # (!) real value is "<attribute 'impact_velocity' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'isOnGround': None, # (!) real value is "<method 'isOnGround' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'is_on_ground': None, # (!) real value is "<method 'is_on_ground' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'max_velocity': None, # (!) real value is "<attribute 'max_velocity' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'offset': None, # (!) real value is "<attribute 'offset' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'on_ground': None, # (!) real value is "<attribute 'on_ground' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'reach': None, # (!) real value is "<attribute 'reach' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'readDatagram': None, # (!) real value is "<method 'readDatagram' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'read_datagram': None, # (!) real value is "<method 'read_datagram' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'setGravity': None, # (!) real value is "<method 'setGravity' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'setLegacyMode': None, # (!) real value is "<method 'setLegacyMode' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'setMaxVelocity': None, # (!) real value is "<method 'setMaxVelocity' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'setOffset': None, # (!) real value is "<method 'setOffset' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'setReach': None, # (!) real value is "<method 'setReach' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'setVelocity': None, # (!) real value is "<method 'setVelocity' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'set_gravity': None, # (!) real value is "<method 'set_gravity' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'set_legacy_mode': None, # (!) real value is "<method 'set_legacy_mode' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'set_max_velocity': None, # (!) real value is "<method 'set_max_velocity' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'set_offset': None, # (!) real value is "<method 'set_offset' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'set_reach': None, # (!) real value is "<method 'set_reach' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'set_velocity': None, # (!) real value is "<method 'set_velocity' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'velocity': None, # (!) real value is "<attribute 'velocity' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'writeDatagram': None, # (!) real value is "<method 'writeDatagram' of 'panda3d.core.CollisionHandlerGravity' objects>"
        'write_datagram': None, # (!) real value is "<method 'write_datagram' of 'panda3d.core.CollisionHandlerGravity' objects>"
    }


