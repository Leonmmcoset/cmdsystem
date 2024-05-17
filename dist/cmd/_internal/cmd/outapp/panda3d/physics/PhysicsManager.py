# encoding: utf-8
# module panda3d.physics
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\physics.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class PhysicsManager(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * Physics don't get much higher-level than this.  Attach as many Physicals
     * (particle systems, etc..) as you want, pick an integrator and go.
     */
    """
    def addAngularForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_angular_force(const PhysicsManager self, AngularForce f)
        
        /**
         * Adds a global angular force to the physics manager
         */
        """
        pass

    def addLinearForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_linear_force(const PhysicsManager self, LinearForce f)
        
        /**
         * Adds a global linear force to the physics manager
         */
        """
        pass

    def add_angular_force(self, const_PhysicsManager_self, AngularForce_f): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_angular_force(const PhysicsManager self, AngularForce f)
        
        /**
         * Adds a global angular force to the physics manager
         */
        """
        pass

    def add_linear_force(self, const_PhysicsManager_self, LinearForce_f): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_linear_force(const PhysicsManager self, LinearForce f)
        
        /**
         * Adds a global linear force to the physics manager
         */
        """
        pass

    def attachAngularIntegrator(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        attach_angular_integrator(const PhysicsManager self, AngularIntegrator i)
        
        /**
         * Hooks an angular integrator into the manager
         */
        """
        pass

    def attachLinearIntegrator(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        attach_linear_integrator(const PhysicsManager self, LinearIntegrator i)
        
        /**
         * Hooks a linear integrator into the manager
         */
        """
        pass

    def attachPhysical(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        attach_physical(const PhysicsManager self, Physical p)
        
        /**
         * Registers a Physical class with the manager
         */
        """
        pass

    def attachPhysicalnode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        attach_physicalnode(const PhysicsManager self, PhysicalNode p)
        
        // use attach_physical_node instead.
        
        /**
         * Please call attach_physical_node instead.
         */
        """
        pass

    def attachPhysicalNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        attach_physical_node(const PhysicsManager self, PhysicalNode p)
        
        // use attach_physical_node instead.
        
        /**
         * Registers a physicalnode with the manager
         */
        """
        pass

    def attach_angular_integrator(self, const_PhysicsManager_self, AngularIntegrator_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        attach_angular_integrator(const PhysicsManager self, AngularIntegrator i)
        
        /**
         * Hooks an angular integrator into the manager
         */
        """
        pass

    def attach_linear_integrator(self, const_PhysicsManager_self, LinearIntegrator_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        attach_linear_integrator(const PhysicsManager self, LinearIntegrator i)
        
        /**
         * Hooks a linear integrator into the manager
         */
        """
        pass

    def attach_physical(self, const_PhysicsManager_self, Physical_p): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        attach_physical(const PhysicsManager self, Physical p)
        
        /**
         * Registers a Physical class with the manager
         */
        """
        pass

    def attach_physicalnode(self, const_PhysicsManager_self, PhysicalNode_p): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        attach_physicalnode(const PhysicsManager self, PhysicalNode p)
        
        // use attach_physical_node instead.
        
        /**
         * Please call attach_physical_node instead.
         */
        """
        pass

    def attach_physical_node(self, const_PhysicsManager_self, PhysicalNode_p): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        attach_physical_node(const PhysicsManager self, PhysicalNode p)
        
        // use attach_physical_node instead.
        
        /**
         * Registers a physicalnode with the manager
         */
        """
        pass

    def clearAngularForces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_angular_forces(const PhysicsManager self)
        
        /**
         * Resets the physics manager force vector
         */
        """
        pass

    def clearLinearForces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_linear_forces(const PhysicsManager self)
        
        /**
         * Resets the physics manager force vector
         */
        """
        pass

    def clearPhysicals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_physicals(const PhysicsManager self)
        
        /**
         * Resets the physics manager objects vector
         */
        """
        pass

    def clear_angular_forces(self, const_PhysicsManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_angular_forces(const PhysicsManager self)
        
        /**
         * Resets the physics manager force vector
         */
        """
        pass

    def clear_linear_forces(self, const_PhysicsManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_linear_forces(const PhysicsManager self)
        
        /**
         * Resets the physics manager force vector
         */
        """
        pass

    def clear_physicals(self, const_PhysicsManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_physicals(const PhysicsManager self)
        
        /**
         * Resets the physics manager objects vector
         */
        """
        pass

    def debugOutput(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        debug_output(PhysicsManager self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def debug_output(self, PhysicsManager_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        debug_output(PhysicsManager self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def doPhysics(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        do_physics(const PhysicsManager self, float dt)
        do_physics(const PhysicsManager self, float dt, Physical p)
        
        /**
         * This is the main high-level API call.  Performs integration on every
         * attached Physical.
         */
        
        /**
         * This is the main high-level API call.  Performs integration on a single
         * physical.  Make sure its associated forces are active.
         */
        """
        pass

    def do_physics(self, const_PhysicsManager_self, float_dt): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        do_physics(const PhysicsManager self, float dt)
        do_physics(const PhysicsManager self, float dt, Physical p)
        
        /**
         * This is the main high-level API call.  Performs integration on every
         * attached Physical.
         */
        
        /**
         * This is the main high-level API call.  Performs integration on a single
         * physical.  Make sure its associated forces are active.
         */
        """
        pass

    def getViscosity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_viscosity(PhysicsManager self)
        
        /**
         * Get the global viscosity.
         */
        """
        pass

    def get_viscosity(self, PhysicsManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_viscosity(PhysicsManager self)
        
        /**
         * Get the global viscosity.
         */
        """
        pass

    def initRandomSeed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        init_random_seed(const PhysicsManager self)
        
        /**
         * One-time config function, sets up the random seed used by the physics and
         * particle systems.  For synchronizing across distributed computers
         */
        """
        pass

    def init_random_seed(self, const_PhysicsManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        init_random_seed(const PhysicsManager self)
        
        /**
         * One-time config function, sets up the random seed used by the physics and
         * particle systems.  For synchronizing across distributed computers
         */
        """
        pass

    def output(self, PhysicsManager_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(PhysicsManager self, ostream out)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def removeAngularForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_angular_force(const PhysicsManager self, AngularForce f)
        
        /**
         * takes an angular force out of the physics list
         */
        """
        pass

    def removeLinearForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_linear_force(const PhysicsManager self, LinearForce f)
        
        /**
         * takes a linear force out of the physics list
         */
        """
        pass

    def removePhysical(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_physical(const PhysicsManager self, Physical p)
        
        /**
         * takes a physical out of the object list
         */
        """
        pass

    def removePhysicalNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_physical_node(const PhysicsManager self, PhysicalNode p)
        
        /**
         * Removes a physicalnode from the manager
         */
        """
        pass

    def remove_angular_force(self, const_PhysicsManager_self, AngularForce_f): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_angular_force(const PhysicsManager self, AngularForce f)
        
        /**
         * takes an angular force out of the physics list
         */
        """
        pass

    def remove_linear_force(self, const_PhysicsManager_self, LinearForce_f): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_linear_force(const PhysicsManager self, LinearForce f)
        
        /**
         * takes a linear force out of the physics list
         */
        """
        pass

    def remove_physical(self, const_PhysicsManager_self, Physical_p): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_physical(const PhysicsManager self, Physical p)
        
        /**
         * takes a physical out of the object list
         */
        """
        pass

    def remove_physical_node(self, const_PhysicsManager_self, PhysicalNode_p): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_physical_node(const PhysicsManager self, PhysicalNode p)
        
        /**
         * Removes a physicalnode from the manager
         */
        """
        pass

    def setViscosity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_viscosity(const PhysicsManager self, float viscosity)
        
        /**
         * Set the global viscosity.
         */
        """
        pass

    def set_viscosity(self, const_PhysicsManager_self, float_viscosity): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_viscosity(const PhysicsManager self, float viscosity)
        
        /**
         * Set the global viscosity.
         */
        """
        pass

    def write(self, PhysicsManager_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(PhysicsManager self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def writeAngularForces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_angular_forces(PhysicsManager self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def writeLinearForces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_linear_forces(PhysicsManager self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def writePhysicals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_physicals(PhysicsManager self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def write_angular_forces(self, PhysicsManager_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_angular_forces(PhysicsManager self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def write_linear_forces(self, PhysicsManager_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_linear_forces(PhysicsManager self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def write_physicals(self, PhysicsManager_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_physicals(PhysicsManager self, ostream out, int indent)
        
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.physics.PhysicsManager' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.physics.PhysicsManager' objects>"
        '__doc__': "/**\n * Physics don't get much higher-level than this.  Attach as many Physicals\n * (particle systems, etc..) as you want, pick an integrator and go.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.physics.PhysicsManager' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DEE4D0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.physics.PhysicsManager' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.physics.PhysicsManager' objects>"
        'addAngularForce': None, # (!) real value is "<method 'addAngularForce' of 'panda3d.physics.PhysicsManager' objects>"
        'addLinearForce': None, # (!) real value is "<method 'addLinearForce' of 'panda3d.physics.PhysicsManager' objects>"
        'add_angular_force': None, # (!) real value is "<method 'add_angular_force' of 'panda3d.physics.PhysicsManager' objects>"
        'add_linear_force': None, # (!) real value is "<method 'add_linear_force' of 'panda3d.physics.PhysicsManager' objects>"
        'attachAngularIntegrator': None, # (!) real value is "<method 'attachAngularIntegrator' of 'panda3d.physics.PhysicsManager' objects>"
        'attachLinearIntegrator': None, # (!) real value is "<method 'attachLinearIntegrator' of 'panda3d.physics.PhysicsManager' objects>"
        'attachPhysical': None, # (!) real value is "<method 'attachPhysical' of 'panda3d.physics.PhysicsManager' objects>"
        'attachPhysicalNode': None, # (!) real value is "<method 'attachPhysicalNode' of 'panda3d.physics.PhysicsManager' objects>"
        'attachPhysicalnode': None, # (!) real value is "<method 'attachPhysicalnode' of 'panda3d.physics.PhysicsManager' objects>"
        'attach_angular_integrator': None, # (!) real value is "<method 'attach_angular_integrator' of 'panda3d.physics.PhysicsManager' objects>"
        'attach_linear_integrator': None, # (!) real value is "<method 'attach_linear_integrator' of 'panda3d.physics.PhysicsManager' objects>"
        'attach_physical': None, # (!) real value is "<method 'attach_physical' of 'panda3d.physics.PhysicsManager' objects>"
        'attach_physical_node': None, # (!) real value is "<method 'attach_physical_node' of 'panda3d.physics.PhysicsManager' objects>"
        'attach_physicalnode': None, # (!) real value is "<method 'attach_physicalnode' of 'panda3d.physics.PhysicsManager' objects>"
        'clearAngularForces': None, # (!) real value is "<method 'clearAngularForces' of 'panda3d.physics.PhysicsManager' objects>"
        'clearLinearForces': None, # (!) real value is "<method 'clearLinearForces' of 'panda3d.physics.PhysicsManager' objects>"
        'clearPhysicals': None, # (!) real value is "<method 'clearPhysicals' of 'panda3d.physics.PhysicsManager' objects>"
        'clear_angular_forces': None, # (!) real value is "<method 'clear_angular_forces' of 'panda3d.physics.PhysicsManager' objects>"
        'clear_linear_forces': None, # (!) real value is "<method 'clear_linear_forces' of 'panda3d.physics.PhysicsManager' objects>"
        'clear_physicals': None, # (!) real value is "<method 'clear_physicals' of 'panda3d.physics.PhysicsManager' objects>"
        'debugOutput': None, # (!) real value is "<method 'debugOutput' of 'panda3d.physics.PhysicsManager' objects>"
        'debug_output': None, # (!) real value is "<method 'debug_output' of 'panda3d.physics.PhysicsManager' objects>"
        'doPhysics': None, # (!) real value is "<method 'doPhysics' of 'panda3d.physics.PhysicsManager' objects>"
        'do_physics': None, # (!) real value is "<method 'do_physics' of 'panda3d.physics.PhysicsManager' objects>"
        'getViscosity': None, # (!) real value is "<method 'getViscosity' of 'panda3d.physics.PhysicsManager' objects>"
        'get_viscosity': None, # (!) real value is "<method 'get_viscosity' of 'panda3d.physics.PhysicsManager' objects>"
        'initRandomSeed': None, # (!) real value is "<method 'initRandomSeed' of 'panda3d.physics.PhysicsManager' objects>"
        'init_random_seed': None, # (!) real value is "<method 'init_random_seed' of 'panda3d.physics.PhysicsManager' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.physics.PhysicsManager' objects>"
        'removeAngularForce': None, # (!) real value is "<method 'removeAngularForce' of 'panda3d.physics.PhysicsManager' objects>"
        'removeLinearForce': None, # (!) real value is "<method 'removeLinearForce' of 'panda3d.physics.PhysicsManager' objects>"
        'removePhysical': None, # (!) real value is "<method 'removePhysical' of 'panda3d.physics.PhysicsManager' objects>"
        'removePhysicalNode': None, # (!) real value is "<method 'removePhysicalNode' of 'panda3d.physics.PhysicsManager' objects>"
        'remove_angular_force': None, # (!) real value is "<method 'remove_angular_force' of 'panda3d.physics.PhysicsManager' objects>"
        'remove_linear_force': None, # (!) real value is "<method 'remove_linear_force' of 'panda3d.physics.PhysicsManager' objects>"
        'remove_physical': None, # (!) real value is "<method 'remove_physical' of 'panda3d.physics.PhysicsManager' objects>"
        'remove_physical_node': None, # (!) real value is "<method 'remove_physical_node' of 'panda3d.physics.PhysicsManager' objects>"
        'setViscosity': None, # (!) real value is "<method 'setViscosity' of 'panda3d.physics.PhysicsManager' objects>"
        'set_viscosity': None, # (!) real value is "<method 'set_viscosity' of 'panda3d.physics.PhysicsManager' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.physics.PhysicsManager' objects>"
        'writeAngularForces': None, # (!) real value is "<method 'writeAngularForces' of 'panda3d.physics.PhysicsManager' objects>"
        'writeLinearForces': None, # (!) real value is "<method 'writeLinearForces' of 'panda3d.physics.PhysicsManager' objects>"
        'writePhysicals': None, # (!) real value is "<method 'writePhysicals' of 'panda3d.physics.PhysicsManager' objects>"
        'write_angular_forces': None, # (!) real value is "<method 'write_angular_forces' of 'panda3d.physics.PhysicsManager' objects>"
        'write_linear_forces': None, # (!) real value is "<method 'write_linear_forces' of 'panda3d.physics.PhysicsManager' objects>"
        'write_physicals': None, # (!) real value is "<method 'write_physicals' of 'panda3d.physics.PhysicsManager' objects>"
    }


