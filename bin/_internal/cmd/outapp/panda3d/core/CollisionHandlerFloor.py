# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CollisionHandlerPhysical import CollisionHandlerPhysical

class CollisionHandlerFloor(CollisionHandlerPhysical):
    """
    /**
     * A specialized kind of CollisionHandler that sets the Z height of the
     * collider to a fixed linear offset from the highest detected collision point
     * each frame.  It's intended to implement walking around on a floor of
     * varying height by casting a ray down from the avatar's head.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getMaxVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_velocity(CollisionHandlerFloor self)
        
        /**
         * Retrieves the maximum speed at which the object will be allowed to descend
         * towards a floor below it, in units per second.  See set_max_velocity().
         */
        """
        pass

    def getOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_offset(CollisionHandlerFloor self)
        
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
        get_reach(CollisionHandlerFloor self)
        
        /**
         * Returns the reach to add to (or subtract from) the highest collision point
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_max_velocity(self, CollisionHandlerFloor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_velocity(CollisionHandlerFloor self)
        
        /**
         * Retrieves the maximum speed at which the object will be allowed to descend
         * towards a floor below it, in units per second.  See set_max_velocity().
         */
        """
        pass

    def get_offset(self, CollisionHandlerFloor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_offset(CollisionHandlerFloor self)
        
        /**
         * Returns the linear offset to add to (or subtract from) the highest detected
         * collision point to determine the actual height at which to set the
         * collider.
         */
        """
        pass

    def get_reach(self, CollisionHandlerFloor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_reach(CollisionHandlerFloor self)
        
        /**
         * Returns the reach to add to (or subtract from) the highest collision point
         */
        """
        pass

    def readDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_datagram(const CollisionHandlerFloor self, DatagramIterator source)
        
        /**
         * Restores the object state from the given datagram, previously obtained using
         * __getstate__.
         */
        """
        pass

    def read_datagram(self, const_CollisionHandlerFloor_self, DatagramIterator_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_datagram(const CollisionHandlerFloor self, DatagramIterator source)
        
        /**
         * Restores the object state from the given datagram, previously obtained using
         * __getstate__.
         */
        """
        pass

    def setMaxVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_velocity(const CollisionHandlerFloor self, float max_vel)
        
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
        set_offset(const CollisionHandlerFloor self, float offset)
        
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
        set_reach(const CollisionHandlerFloor self, float reach)
        
        /**
         * Sets the reach to add to (or subtract from) the highest collision point
         */
        """
        pass

    def set_max_velocity(self, const_CollisionHandlerFloor_self, float_max_vel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_velocity(const CollisionHandlerFloor self, float max_vel)
        
        /**
         * Sets the maximum speed at which the object will be allowed to descend
         * towards a floor below it, in units per second.  Set this to zero to allow
         * it to instantly teleport any distance.
         */
        """
        pass

    def set_offset(self, const_CollisionHandlerFloor_self, float_offset): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_offset(const CollisionHandlerFloor self, float offset)
        
        /**
         * Sets the linear offset to add to (or subtract from) the highest detected
         * collision point to determine the actual height at which to set the
         * collider.
         */
        """
        pass

    def set_reach(self, const_CollisionHandlerFloor_self, float_reach): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_reach(const CollisionHandlerFloor self, float reach)
        
        /**
         * Sets the reach to add to (or subtract from) the highest collision point
         */
        """
        pass

    def writeDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_datagram(CollisionHandlerFloor self, Datagram destination)
        
        /**
         * Serializes this object, to implement pickle support.
         */
        """
        pass

    def write_datagram(self, CollisionHandlerFloor_self, Datagram_destination): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_datagram(CollisionHandlerFloor self, Datagram destination)
        
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

    max_velocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reach = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * A specialized kind of CollisionHandler that sets the Z height of the\n * collider to a fixed linear offset from the highest detected collision point\n * each frame.  It's intended to implement walking around on a floor of\n * varying height by casting a ray down from the avatar's head.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CollisionHandlerFloor' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2CF340>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2CF340>)>'
        'getMaxVelocity': None, # (!) real value is "<method 'getMaxVelocity' of 'panda3d.core.CollisionHandlerFloor' objects>"
        'getOffset': None, # (!) real value is "<method 'getOffset' of 'panda3d.core.CollisionHandlerFloor' objects>"
        'getReach': None, # (!) real value is "<method 'getReach' of 'panda3d.core.CollisionHandlerFloor' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2CF340>)>'
        'get_max_velocity': None, # (!) real value is "<method 'get_max_velocity' of 'panda3d.core.CollisionHandlerFloor' objects>"
        'get_offset': None, # (!) real value is "<method 'get_offset' of 'panda3d.core.CollisionHandlerFloor' objects>"
        'get_reach': None, # (!) real value is "<method 'get_reach' of 'panda3d.core.CollisionHandlerFloor' objects>"
        'max_velocity': None, # (!) real value is "<attribute 'max_velocity' of 'panda3d.core.CollisionHandlerFloor' objects>"
        'offset': None, # (!) real value is "<attribute 'offset' of 'panda3d.core.CollisionHandlerFloor' objects>"
        'reach': None, # (!) real value is "<attribute 'reach' of 'panda3d.core.CollisionHandlerFloor' objects>"
        'readDatagram': None, # (!) real value is "<method 'readDatagram' of 'panda3d.core.CollisionHandlerFloor' objects>"
        'read_datagram': None, # (!) real value is "<method 'read_datagram' of 'panda3d.core.CollisionHandlerFloor' objects>"
        'setMaxVelocity': None, # (!) real value is "<method 'setMaxVelocity' of 'panda3d.core.CollisionHandlerFloor' objects>"
        'setOffset': None, # (!) real value is "<method 'setOffset' of 'panda3d.core.CollisionHandlerFloor' objects>"
        'setReach': None, # (!) real value is "<method 'setReach' of 'panda3d.core.CollisionHandlerFloor' objects>"
        'set_max_velocity': None, # (!) real value is "<method 'set_max_velocity' of 'panda3d.core.CollisionHandlerFloor' objects>"
        'set_offset': None, # (!) real value is "<method 'set_offset' of 'panda3d.core.CollisionHandlerFloor' objects>"
        'set_reach': None, # (!) real value is "<method 'set_reach' of 'panda3d.core.CollisionHandlerFloor' objects>"
        'writeDatagram': None, # (!) real value is "<method 'writeDatagram' of 'panda3d.core.CollisionHandlerFloor' objects>"
        'write_datagram': None, # (!) real value is "<method 'write_datagram' of 'panda3d.core.CollisionHandlerFloor' objects>"
    }


