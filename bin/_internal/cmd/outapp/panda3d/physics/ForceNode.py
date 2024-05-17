# encoding: utf-8
# module panda3d.physics
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\physics.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class ForceNode(__panda3d_core.PandaNode):
    """
    /**
     * A force that lives in the scene graph and is therefore subject to local
     * coordinate systems.  An example of this would be simulating gravity in a
     * rotating space station.  or something.
     */
    """
    def addForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_force(const ForceNode self, BaseForce force)
        
        /**
        
         */
        """
        pass

    def addForcesFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_forces_from(const ForceNode self, const ForceNode other)
        
        /**
         * append operation
         */
        """
        pass

    def add_force(self, const_ForceNode_self, BaseForce_force): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_force(const ForceNode self, BaseForce force)
        
        /**
        
         */
        """
        pass

    def add_forces_from(self, const_ForceNode_self, const_ForceNode_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_forces_from(const ForceNode self, const ForceNode other)
        
        /**
         * append operation
         */
        """
        pass

    def clear(self, const_ForceNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const ForceNode self)
        
        /**
        
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_force(ForceNode self, int index)
        
        /**
        
         */
        """
        pass

    def getForces(self, *args, **kwargs): # real signature unknown
        pass

    def getNumForces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_forces(ForceNode self)
        
        /**
        
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_force(self, ForceNode_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_force(ForceNode self, int index)
        
        /**
        
         */
        """
        pass

    def get_forces(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_forces(self, ForceNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_forces(ForceNode self)
        
        /**
        
         */
        """
        pass

    def insertForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        insert_force(const ForceNode self, int index, BaseForce force)
        
        /**
         * insert operation
         */
        """
        pass

    def insert_force(self, const_ForceNode_self, int_index, BaseForce_force): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        insert_force(const ForceNode self, int index, BaseForce force)
        
        /**
         * insert operation
         */
        """
        pass

    def removeForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_force(const ForceNode self, BaseForce force)
        remove_force(const ForceNode self, int index)
        
        /**
         * remove operation
         */
        
        /**
         * remove operation
         */
        """
        pass

    def remove_force(self, const_ForceNode_self, BaseForce_force): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_force(const ForceNode self, BaseForce force)
        remove_force(const ForceNode self, int index)
        
        /**
         * remove operation
         */
        
        /**
         * remove operation
         */
        """
        pass

    def setForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_force(const ForceNode self, int index, BaseForce force)
        
        /**
         * replace operation
         */
        """
        pass

    def set_force(self, const_ForceNode_self, int_index, BaseForce_force): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_force(const ForceNode self, int index, BaseForce force)
        
        /**
         * replace operation
         */
        """
        pass

    def writeForces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_forces(ForceNode self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def write_forces(self, ForceNode_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_forces(ForceNode self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    forces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A force that lives in the scene graph and is therefore subject to local\n * coordinate systems.  An example of this would be simulating gravity in a\n * rotating space station.  or something.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.physics.ForceNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DEC9A0>'
        'addForce': None, # (!) real value is "<method 'addForce' of 'panda3d.physics.ForceNode' objects>"
        'addForcesFrom': None, # (!) real value is "<method 'addForcesFrom' of 'panda3d.physics.ForceNode' objects>"
        'add_force': None, # (!) real value is "<method 'add_force' of 'panda3d.physics.ForceNode' objects>"
        'add_forces_from': None, # (!) real value is "<method 'add_forces_from' of 'panda3d.physics.ForceNode' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.physics.ForceNode' objects>"
        'forces': None, # (!) real value is "<attribute 'forces' of 'panda3d.physics.ForceNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC9DEC9A0>)>'
        'getForce': None, # (!) real value is "<method 'getForce' of 'panda3d.physics.ForceNode' objects>"
        'getForces': None, # (!) real value is "<method 'getForces' of 'panda3d.physics.ForceNode' objects>"
        'getNumForces': None, # (!) real value is "<method 'getNumForces' of 'panda3d.physics.ForceNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC9DEC9A0>)>'
        'get_force': None, # (!) real value is "<method 'get_force' of 'panda3d.physics.ForceNode' objects>"
        'get_forces': None, # (!) real value is "<method 'get_forces' of 'panda3d.physics.ForceNode' objects>"
        'get_num_forces': None, # (!) real value is "<method 'get_num_forces' of 'panda3d.physics.ForceNode' objects>"
        'insertForce': None, # (!) real value is "<method 'insertForce' of 'panda3d.physics.ForceNode' objects>"
        'insert_force': None, # (!) real value is "<method 'insert_force' of 'panda3d.physics.ForceNode' objects>"
        'removeForce': None, # (!) real value is "<method 'removeForce' of 'panda3d.physics.ForceNode' objects>"
        'remove_force': None, # (!) real value is "<method 'remove_force' of 'panda3d.physics.ForceNode' objects>"
        'setForce': None, # (!) real value is "<method 'setForce' of 'panda3d.physics.ForceNode' objects>"
        'set_force': None, # (!) real value is "<method 'set_force' of 'panda3d.physics.ForceNode' objects>"
        'writeForces': None, # (!) real value is "<method 'writeForces' of 'panda3d.physics.ForceNode' objects>"
        'write_forces': None, # (!) real value is "<method 'write_forces' of 'panda3d.physics.ForceNode' objects>"
    }


