# encoding: utf-8
# module panda3d.physics
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\physics.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class PhysicalNode(__panda3d_core.PandaNode):
    """
    /**
     * Graph node that encapsulated a series of physical objects
     */
    """
    def addPhysical(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_physical(const PhysicalNode self, Physical physical)
        
        /**
         * Adds a Physical to this PhysicalNode.  If it is already added to this node,
         * does nothing.  It is an error to add a Physical to multiple PhysicalNodes.
         */
        """
        pass

    def addPhysicalsFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_physicals_from(const PhysicalNode self, const PhysicalNode other)
        
        /**
         * append operation
         */
        """
        pass

    def add_physical(self, const_PhysicalNode_self, Physical_physical): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_physical(const PhysicalNode self, Physical physical)
        
        /**
         * Adds a Physical to this PhysicalNode.  If it is already added to this node,
         * does nothing.  It is an error to add a Physical to multiple PhysicalNodes.
         */
        """
        pass

    def add_physicals_from(self, const_PhysicalNode_self, const_PhysicalNode_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_physicals_from(const PhysicalNode self, const PhysicalNode other)
        
        /**
         * append operation
         */
        """
        pass

    def clear(self, const_PhysicalNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const PhysicalNode self)
        
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

    def getNumPhysicals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_physicals(PhysicalNode self)
        
        /**
        
         */
        """
        pass

    def getPhysical(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_physical(PhysicalNode self, int index)
        
        /**
        
         */
        """
        pass

    def getPhysicals(self, *args, **kwargs): # real signature unknown
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_physicals(self, PhysicalNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_physicals(PhysicalNode self)
        
        /**
        
         */
        """
        pass

    def get_physical(self, PhysicalNode_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_physical(PhysicalNode self, int index)
        
        /**
        
         */
        """
        pass

    def get_physicals(self, *args, **kwargs): # real signature unknown
        pass

    def insertPhysical(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        insert_physical(const PhysicalNode self, int index, Physical physical)
        
        /**
         * insert operation
         */
        """
        pass

    def insert_physical(self, const_PhysicalNode_self, int_index, Physical_physical): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        insert_physical(const PhysicalNode self, int index, Physical physical)
        
        /**
         * insert operation
         */
        """
        pass

    def removePhysical(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_physical(const PhysicalNode self, Physical physical)
        remove_physical(const PhysicalNode self, int index)
        
        /**
         * remove operation
         */
        
        /**
         * remove operation
         */
        """
        pass

    def remove_physical(self, const_PhysicalNode_self, Physical_physical): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_physical(const PhysicalNode self, Physical physical)
        remove_physical(const PhysicalNode self, int index)
        
        /**
         * remove operation
         */
        
        /**
         * remove operation
         */
        """
        pass

    def setPhysical(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_physical(const PhysicalNode self, int index, Physical physical)
        
        /**
         * replace operation
         */
        """
        pass

    def set_physical(self, const_PhysicalNode_self, int_index, Physical_physical): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_physical(const PhysicalNode self, int index, Physical physical)
        
        /**
         * replace operation
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    physicals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * Graph node that encapsulated a series of physical objects\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.physics.PhysicalNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DEBEC0>'
        'addPhysical': None, # (!) real value is "<method 'addPhysical' of 'panda3d.physics.PhysicalNode' objects>"
        'addPhysicalsFrom': None, # (!) real value is "<method 'addPhysicalsFrom' of 'panda3d.physics.PhysicalNode' objects>"
        'add_physical': None, # (!) real value is "<method 'add_physical' of 'panda3d.physics.PhysicalNode' objects>"
        'add_physicals_from': None, # (!) real value is "<method 'add_physicals_from' of 'panda3d.physics.PhysicalNode' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.physics.PhysicalNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC9DEBEC0>)>'
        'getNumPhysicals': None, # (!) real value is "<method 'getNumPhysicals' of 'panda3d.physics.PhysicalNode' objects>"
        'getPhysical': None, # (!) real value is "<method 'getPhysical' of 'panda3d.physics.PhysicalNode' objects>"
        'getPhysicals': None, # (!) real value is "<method 'getPhysicals' of 'panda3d.physics.PhysicalNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC9DEBEC0>)>'
        'get_num_physicals': None, # (!) real value is "<method 'get_num_physicals' of 'panda3d.physics.PhysicalNode' objects>"
        'get_physical': None, # (!) real value is "<method 'get_physical' of 'panda3d.physics.PhysicalNode' objects>"
        'get_physicals': None, # (!) real value is "<method 'get_physicals' of 'panda3d.physics.PhysicalNode' objects>"
        'insertPhysical': None, # (!) real value is "<method 'insertPhysical' of 'panda3d.physics.PhysicalNode' objects>"
        'insert_physical': None, # (!) real value is "<method 'insert_physical' of 'panda3d.physics.PhysicalNode' objects>"
        'physicals': None, # (!) real value is "<attribute 'physicals' of 'panda3d.physics.PhysicalNode' objects>"
        'removePhysical': None, # (!) real value is "<method 'removePhysical' of 'panda3d.physics.PhysicalNode' objects>"
        'remove_physical': None, # (!) real value is "<method 'remove_physical' of 'panda3d.physics.PhysicalNode' objects>"
        'setPhysical': None, # (!) real value is "<method 'setPhysical' of 'panda3d.physics.PhysicalNode' objects>"
        'set_physical': None, # (!) real value is "<method 'set_physical' of 'panda3d.physics.PhysicalNode' objects>"
    }


