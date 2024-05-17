# encoding: utf-8
# module panda3d.physics
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\physics.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class Physical(__panda3d_core.TypedReferenceCount):
    """
    /**
     * Defines a set of physically modeled attributes.  If you want physics
     * applied to your class, derive it from this.
     */
    """
    def addAngularForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_angular_force(const Physical self, AngularForce f)
        
        /**
         * Adds an angular force to the force list
         */
        """
        pass

    def addLinearForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_linear_force(const Physical self, LinearForce f)
        
        /**
         * Adds a linear force to the force list
         */
        """
        pass

    def addPhysicsObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_physics_object(const Physical self, PhysicsObject po)
        
        /**
         * Adds an object to the physics object vector
         */
        """
        pass

    def add_angular_force(self, const_Physical_self, AngularForce_f): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_angular_force(const Physical self, AngularForce f)
        
        /**
         * Adds an angular force to the force list
         */
        """
        pass

    def add_linear_force(self, const_Physical_self, LinearForce_f): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_linear_force(const Physical self, LinearForce f)
        
        /**
         * Adds a linear force to the force list
         */
        """
        pass

    def add_physics_object(self, const_Physical_self, PhysicsObject_po): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_physics_object(const Physical self, PhysicsObject po)
        
        /**
         * Adds an object to the physics object vector
         */
        """
        pass

    def clearAngularForces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_angular_forces(const Physical self)
        
        /**
         * Erases the angular force list
         */
        """
        pass

    def clearLinearForces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_linear_forces(const Physical self)
        
        /**
         * Erases the linear force list
         */
        """
        pass

    def clearPhysicsObjects(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_physics_objects(const Physical self)
        
        /**
         * Erases the object list
         */
        """
        pass

    def clear_angular_forces(self, const_Physical_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_angular_forces(const Physical self)
        
        /**
         * Erases the angular force list
         */
        """
        pass

    def clear_linear_forces(self, const_Physical_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_linear_forces(const Physical self)
        
        /**
         * Erases the linear force list
         */
        """
        pass

    def clear_physics_objects(self, const_Physical_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_physics_objects(const Physical self)
        
        /**
         * Erases the object list
         */
        """
        pass

    def getAngularForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_angular_force(Physical self, int index)
        
        /**
        
         */
        """
        pass

    def getAngularForces(self, *args, **kwargs): # real signature unknown
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getLinearForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_linear_force(Physical self, int index)
        
        /**
        
         */
        """
        pass

    def getLinearForces(self, *args, **kwargs): # real signature unknown
        pass

    def getNumAngularForces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_angular_forces(Physical self)
        
        /**
        
         */
        """
        pass

    def getNumLinearForces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_linear_forces(Physical self)
        
        /**
        
         */
        """
        pass

    def getObjects(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_objects(Physical self)
        
        /**
        
         */
        """
        pass

    def getPhysBody(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_phys_body(Physical self)
        
        /**
        
         */
        """
        pass

    def getPhysicalNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_physical_node(Physical self)
        
        /**
        
         */
        """
        pass

    def getPhysicalNodePath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_physical_node_path(Physical self)
        
        /**
        
         */
        """
        pass

    def getPhysicsManager(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_physics_manager(Physical self)
        
        // helpers
        
        /**
        
         */
        """
        pass

    def getViscosity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_viscosity(Physical self)
        
        /**
         * Get the local viscosity.
         */
        """
        pass

    def get_angular_force(self, Physical_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_angular_force(Physical self, int index)
        
        /**
        
         */
        """
        pass

    def get_angular_forces(self, *args, **kwargs): # real signature unknown
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_linear_force(self, Physical_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_linear_force(Physical self, int index)
        
        /**
        
         */
        """
        pass

    def get_linear_forces(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_angular_forces(self, Physical_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_angular_forces(Physical self)
        
        /**
        
         */
        """
        pass

    def get_num_linear_forces(self, Physical_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_linear_forces(Physical self)
        
        /**
        
         */
        """
        pass

    def get_objects(self, Physical_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_objects(Physical self)
        
        /**
        
         */
        """
        pass

    def get_physical_node(self, Physical_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_physical_node(Physical self)
        
        /**
        
         */
        """
        pass

    def get_physical_node_path(self, Physical_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_physical_node_path(Physical self)
        
        /**
        
         */
        """
        pass

    def get_physics_manager(self, Physical_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_physics_manager(Physical self)
        
        // helpers
        
        /**
        
         */
        """
        pass

    def get_phys_body(self, Physical_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_phys_body(Physical self)
        
        /**
        
         */
        """
        pass

    def get_viscosity(self, Physical_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_viscosity(Physical self)
        
        /**
         * Get the local viscosity.
         */
        """
        pass

    def output(self, Physical_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(Physical self, ostream out)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def removeAngularForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_angular_force(const Physical self, AngularForce f)
        
        /**
         * removes an angular force from the force list
         */
        """
        pass

    def removeLinearForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_linear_force(const Physical self, LinearForce f)
        
        /**
         * removes a linear force from the force list
         */
        """
        pass

    def remove_angular_force(self, const_Physical_self, AngularForce_f): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_angular_force(const Physical self, AngularForce f)
        
        /**
         * removes an angular force from the force list
         */
        """
        pass

    def remove_linear_force(self, const_Physical_self, LinearForce_f): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_linear_force(const Physical self, LinearForce f)
        
        /**
         * removes a linear force from the force list
         */
        """
        pass

    def setViscosity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_viscosity(const Physical self, float viscosity)
        
        /**
         * Set the local viscosity.
         */
        """
        pass

    def set_viscosity(self, const_Physical_self, float_viscosity): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_viscosity(const Physical self, float viscosity)
        
        /**
         * Set the local viscosity.
         */
        """
        pass

    def write(self, Physical_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(Physical self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def writeAngularForces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_angular_forces(Physical self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def writeLinearForces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_linear_forces(Physical self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def writePhysicsObjects(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_physics_objects(Physical self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def write_angular_forces(self, Physical_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_angular_forces(Physical self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def write_linear_forces(self, Physical_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_linear_forces(Physical self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def write_physics_objects(self, Physical_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_physics_objects(Physical self, ostream out, int indent)
        
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

    angular_forces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    linear_forces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    viscosity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.physics.Physical' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.physics.Physical' objects>"
        '__doc__': '/**\n * Defines a set of physically modeled attributes.  If you want physics\n * applied to your class, derive it from this.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.physics.Physical' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DEBCF0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.physics.Physical' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.physics.Physical' objects>"
        'addAngularForce': None, # (!) real value is "<method 'addAngularForce' of 'panda3d.physics.Physical' objects>"
        'addLinearForce': None, # (!) real value is "<method 'addLinearForce' of 'panda3d.physics.Physical' objects>"
        'addPhysicsObject': None, # (!) real value is "<method 'addPhysicsObject' of 'panda3d.physics.Physical' objects>"
        'add_angular_force': None, # (!) real value is "<method 'add_angular_force' of 'panda3d.physics.Physical' objects>"
        'add_linear_force': None, # (!) real value is "<method 'add_linear_force' of 'panda3d.physics.Physical' objects>"
        'add_physics_object': None, # (!) real value is "<method 'add_physics_object' of 'panda3d.physics.Physical' objects>"
        'angular_forces': None, # (!) real value is "<attribute 'angular_forces' of 'panda3d.physics.Physical' objects>"
        'clearAngularForces': None, # (!) real value is "<method 'clearAngularForces' of 'panda3d.physics.Physical' objects>"
        'clearLinearForces': None, # (!) real value is "<method 'clearLinearForces' of 'panda3d.physics.Physical' objects>"
        'clearPhysicsObjects': None, # (!) real value is "<method 'clearPhysicsObjects' of 'panda3d.physics.Physical' objects>"
        'clear_angular_forces': None, # (!) real value is "<method 'clear_angular_forces' of 'panda3d.physics.Physical' objects>"
        'clear_linear_forces': None, # (!) real value is "<method 'clear_linear_forces' of 'panda3d.physics.Physical' objects>"
        'clear_physics_objects': None, # (!) real value is "<method 'clear_physics_objects' of 'panda3d.physics.Physical' objects>"
        'getAngularForce': None, # (!) real value is "<method 'getAngularForce' of 'panda3d.physics.Physical' objects>"
        'getAngularForces': None, # (!) real value is "<method 'getAngularForces' of 'panda3d.physics.Physical' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC9DEBCF0>)>'
        'getLinearForce': None, # (!) real value is "<method 'getLinearForce' of 'panda3d.physics.Physical' objects>"
        'getLinearForces': None, # (!) real value is "<method 'getLinearForces' of 'panda3d.physics.Physical' objects>"
        'getNumAngularForces': None, # (!) real value is "<method 'getNumAngularForces' of 'panda3d.physics.Physical' objects>"
        'getNumLinearForces': None, # (!) real value is "<method 'getNumLinearForces' of 'panda3d.physics.Physical' objects>"
        'getObjects': None, # (!) real value is "<method 'getObjects' of 'panda3d.physics.Physical' objects>"
        'getPhysBody': None, # (!) real value is "<method 'getPhysBody' of 'panda3d.physics.Physical' objects>"
        'getPhysicalNode': None, # (!) real value is "<method 'getPhysicalNode' of 'panda3d.physics.Physical' objects>"
        'getPhysicalNodePath': None, # (!) real value is "<method 'getPhysicalNodePath' of 'panda3d.physics.Physical' objects>"
        'getPhysicsManager': None, # (!) real value is "<method 'getPhysicsManager' of 'panda3d.physics.Physical' objects>"
        'getViscosity': None, # (!) real value is "<method 'getViscosity' of 'panda3d.physics.Physical' objects>"
        'get_angular_force': None, # (!) real value is "<method 'get_angular_force' of 'panda3d.physics.Physical' objects>"
        'get_angular_forces': None, # (!) real value is "<method 'get_angular_forces' of 'panda3d.physics.Physical' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC9DEBCF0>)>'
        'get_linear_force': None, # (!) real value is "<method 'get_linear_force' of 'panda3d.physics.Physical' objects>"
        'get_linear_forces': None, # (!) real value is "<method 'get_linear_forces' of 'panda3d.physics.Physical' objects>"
        'get_num_angular_forces': None, # (!) real value is "<method 'get_num_angular_forces' of 'panda3d.physics.Physical' objects>"
        'get_num_linear_forces': None, # (!) real value is "<method 'get_num_linear_forces' of 'panda3d.physics.Physical' objects>"
        'get_objects': None, # (!) real value is "<method 'get_objects' of 'panda3d.physics.Physical' objects>"
        'get_phys_body': None, # (!) real value is "<method 'get_phys_body' of 'panda3d.physics.Physical' objects>"
        'get_physical_node': None, # (!) real value is "<method 'get_physical_node' of 'panda3d.physics.Physical' objects>"
        'get_physical_node_path': None, # (!) real value is "<method 'get_physical_node_path' of 'panda3d.physics.Physical' objects>"
        'get_physics_manager': None, # (!) real value is "<method 'get_physics_manager' of 'panda3d.physics.Physical' objects>"
        'get_viscosity': None, # (!) real value is "<method 'get_viscosity' of 'panda3d.physics.Physical' objects>"
        'linear_forces': None, # (!) real value is "<attribute 'linear_forces' of 'panda3d.physics.Physical' objects>"
        'objects': None, # (!) real value is "<attribute 'objects' of 'panda3d.physics.Physical' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.physics.Physical' objects>"
        'removeAngularForce': None, # (!) real value is "<method 'removeAngularForce' of 'panda3d.physics.Physical' objects>"
        'removeLinearForce': None, # (!) real value is "<method 'removeLinearForce' of 'panda3d.physics.Physical' objects>"
        'remove_angular_force': None, # (!) real value is "<method 'remove_angular_force' of 'panda3d.physics.Physical' objects>"
        'remove_linear_force': None, # (!) real value is "<method 'remove_linear_force' of 'panda3d.physics.Physical' objects>"
        'setViscosity': None, # (!) real value is "<method 'setViscosity' of 'panda3d.physics.Physical' objects>"
        'set_viscosity': None, # (!) real value is "<method 'set_viscosity' of 'panda3d.physics.Physical' objects>"
        'viscosity': None, # (!) real value is "<attribute 'viscosity' of 'panda3d.physics.Physical' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.physics.Physical' objects>"
        'writeAngularForces': None, # (!) real value is "<method 'writeAngularForces' of 'panda3d.physics.Physical' objects>"
        'writeLinearForces': None, # (!) real value is "<method 'writeLinearForces' of 'panda3d.physics.Physical' objects>"
        'writePhysicsObjects': None, # (!) real value is "<method 'writePhysicsObjects' of 'panda3d.physics.Physical' objects>"
        'write_angular_forces': None, # (!) real value is "<method 'write_angular_forces' of 'panda3d.physics.Physical' objects>"
        'write_linear_forces': None, # (!) real value is "<method 'write_linear_forces' of 'panda3d.physics.Physical' objects>"
        'write_physics_objects': None, # (!) real value is "<method 'write_physics_objects' of 'panda3d.physics.Physical' objects>"
    }


