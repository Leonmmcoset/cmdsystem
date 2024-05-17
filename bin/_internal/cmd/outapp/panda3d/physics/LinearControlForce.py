# encoding: utf-8
# module panda3d.physics
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\physics.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .LinearForce import LinearForce

class LinearControlForce(LinearForce):
    """
    /**
     * Simple directed vector force.  This force is different from the others in
     * that it can be global and still only affect a single object.  That might
     * not make sense for a physics simulation, but it's very handy for a game.
     * I.e.  this is the force applied by user on the selected object.
     */
    """
    def clearPhysicsObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_physics_object(const LinearControlForce self)
        
        /**
         * encapsulating wrapper
         */
        """
        pass

    def clear_physics_object(self, const_LinearControlForce_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_physics_object(const LinearControlForce self)
        
        /**
         * encapsulating wrapper
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getLocalVector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_local_vector(LinearControlForce self)
        
        /**
         *
         */
        """
        pass

    def getPhysicsObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_physics_object(LinearControlForce self)
        
        /**
         * piecewise encapsulating wrapper
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_local_vector(self, LinearControlForce_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_local_vector(LinearControlForce self)
        
        /**
         *
         */
        """
        pass

    def get_physics_object(self, LinearControlForce_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_physics_object(LinearControlForce self)
        
        /**
         * piecewise encapsulating wrapper
         */
        """
        pass

    def setPhysicsObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_physics_object(const LinearControlForce self, const PhysicsObject po)
        
        /**
         * encapsulating wrapper
         */
        """
        pass

    def setVector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vector(const LinearControlForce self, const LVector3f v)
        set_vector(const LinearControlForce self, float x, float y, float z)
        
        /**
         * encapsulating wrapper
         */
        
        /**
         * piecewise encapsulating wrapper
         */
        """
        pass

    def set_physics_object(self, const_LinearControlForce_self, const_PhysicsObject_po): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_physics_object(const LinearControlForce self, const PhysicsObject po)
        
        /**
         * encapsulating wrapper
         */
        """
        pass

    def set_vector(self, const_LinearControlForce_self, const_LVector3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vector(const LinearControlForce self, const LVector3f v)
        set_vector(const LinearControlForce self, float x, float y, float z)
        
        /**
         * encapsulating wrapper
         */
        
        /**
         * piecewise encapsulating wrapper
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.physics.LinearControlForce' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.physics.LinearControlForce' objects>"
        '__doc__': "/**\n * Simple directed vector force.  This force is different from the others in\n * that it can be global and still only affect a single object.  That might\n * not make sense for a physics simulation, but it's very handy for a game.\n * I.e.  this is the force applied by user on the selected object.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.physics.LinearControlForce' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DECB70>'
        'clearPhysicsObject': None, # (!) real value is "<method 'clearPhysicsObject' of 'panda3d.physics.LinearControlForce' objects>"
        'clear_physics_object': None, # (!) real value is "<method 'clear_physics_object' of 'panda3d.physics.LinearControlForce' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC9DECB70>)>'
        'getLocalVector': None, # (!) real value is "<method 'getLocalVector' of 'panda3d.physics.LinearControlForce' objects>"
        'getPhysicsObject': None, # (!) real value is "<method 'getPhysicsObject' of 'panda3d.physics.LinearControlForce' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC9DECB70>)>'
        'get_local_vector': None, # (!) real value is "<method 'get_local_vector' of 'panda3d.physics.LinearControlForce' objects>"
        'get_physics_object': None, # (!) real value is "<method 'get_physics_object' of 'panda3d.physics.LinearControlForce' objects>"
        'setPhysicsObject': None, # (!) real value is "<method 'setPhysicsObject' of 'panda3d.physics.LinearControlForce' objects>"
        'setVector': None, # (!) real value is "<method 'setVector' of 'panda3d.physics.LinearControlForce' objects>"
        'set_physics_object': None, # (!) real value is "<method 'set_physics_object' of 'panda3d.physics.LinearControlForce' objects>"
        'set_vector': None, # (!) real value is "<method 'set_vector' of 'panda3d.physics.LinearControlForce' objects>"
    }


