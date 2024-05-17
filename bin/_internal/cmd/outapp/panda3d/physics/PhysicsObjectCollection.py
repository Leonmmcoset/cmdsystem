# encoding: utf-8
# module panda3d.physics
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\physics.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class PhysicsObjectCollection(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is a set of zero or more PhysicsObjects.  It's handy for returning
     * from functions that need to return multiple PhysicsObjects.
     */
    """
    def addPhysicsObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_physics_object(const PhysicsObjectCollection self, PhysicsObject physics_object)
        
        /**
         * Adds a new PhysicsObject to the collection.
         */
        """
        pass

    def addPhysicsObjectsFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_physics_objects_from(const PhysicsObjectCollection self, const PhysicsObjectCollection other)
        
        /**
         * Adds all the PhysicsObjects indicated in the other collection to this
         * collection.  The other physics_objects are simply appended to the end of
         * the physics_objects in this list; duplicates are not automatically removed.
         */
        """
        pass

    def add_physics_object(self, const_PhysicsObjectCollection_self, PhysicsObject_physics_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_physics_object(const PhysicsObjectCollection self, PhysicsObject physics_object)
        
        /**
         * Adds a new PhysicsObject to the collection.
         */
        """
        pass

    def add_physics_objects_from(self, const_PhysicsObjectCollection_self, const_PhysicsObjectCollection_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_physics_objects_from(const PhysicsObjectCollection self, const PhysicsObjectCollection other)
        
        /**
         * Adds all the PhysicsObjects indicated in the other collection to this
         * collection.  The other physics_objects are simply appended to the end of
         * the physics_objects in this list; duplicates are not automatically removed.
         */
        """
        pass

    def assign(self, const_PhysicsObjectCollection_self, const_PhysicsObjectCollection_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const PhysicsObjectCollection self, const PhysicsObjectCollection copy)
        """
        pass

    def clear(self, const_PhysicsObjectCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const PhysicsObjectCollection self)
        
        /**
         * Removes all PhysicsObjects from the collection.
         */
        """
        pass

    def getNumPhysicsObjects(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_physics_objects(PhysicsObjectCollection self)
        
        /**
         * Returns the number of PhysicsObjects in the collection.
         */
        """
        pass

    def getPhysicsObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_physics_object(PhysicsObjectCollection self, int index)
        
        /**
         * Returns the nth PhysicsObject in the collection.
         */
        """
        pass

    def getPhysicsObjects(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_physics_objects(self, PhysicsObjectCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_physics_objects(PhysicsObjectCollection self)
        
        /**
         * Returns the number of PhysicsObjects in the collection.
         */
        """
        pass

    def get_physics_object(self, PhysicsObjectCollection_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_physics_object(PhysicsObjectCollection self, int index)
        
        /**
         * Returns the nth PhysicsObject in the collection.
         */
        """
        pass

    def get_physics_objects(self, *args, **kwargs): # real signature unknown
        pass

    def hasPhysicsObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_physics_object(PhysicsObjectCollection self, PhysicsObject physics_object)
        
        /**
         * Returns true if the indicated PhysicsObject appears in this collection,
         * false otherwise.
         */
        """
        pass

    def has_physics_object(self, PhysicsObjectCollection_self, PhysicsObject_physics_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_physics_object(PhysicsObjectCollection self, PhysicsObject physics_object)
        
        /**
         * Returns true if the indicated PhysicsObject appears in this collection,
         * false otherwise.
         */
        """
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(PhysicsObjectCollection self)
        
        /**
         * Returns true if there are no PhysicsObjects in the collection, false
         * otherwise.
         */
        """
        pass

    def is_empty(self, PhysicsObjectCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(PhysicsObjectCollection self)
        
        /**
         * Returns true if there are no PhysicsObjects in the collection, false
         * otherwise.
         */
        """
        pass

    def output(self, PhysicsObjectCollection_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(PhysicsObjectCollection self, ostream out)
        
        /**
         * Writes a brief one-line description of the PhysicsObjectCollection to the
         * indicated output stream.
         */
        """
        pass

    def removeDuplicatePhysicsObjects(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_duplicate_physics_objects(const PhysicsObjectCollection self)
        
        /**
         * Removes any duplicate entries of the same PhysicsObjects on this
         * collection.  If a PhysicsObject appears multiple times, the first
         * appearance is retained; subsequent appearances are removed.
         */
        """
        pass

    def removePhysicsObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_physics_object(const PhysicsObjectCollection self, PhysicsObject physics_object)
        
        /**
         * Removes the indicated PhysicsObject from the collection.  Returns true if
         * the physics_object was removed, false if it was not a member of the
         * collection.
         */
        """
        pass

    def removePhysicsObjectsFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_physics_objects_from(const PhysicsObjectCollection self, const PhysicsObjectCollection other)
        
        /**
         * Removes from this collection all of the PhysicsObjects listed in the other
         * collection.
         */
        """
        pass

    def remove_duplicate_physics_objects(self, const_PhysicsObjectCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_duplicate_physics_objects(const PhysicsObjectCollection self)
        
        /**
         * Removes any duplicate entries of the same PhysicsObjects on this
         * collection.  If a PhysicsObject appears multiple times, the first
         * appearance is retained; subsequent appearances are removed.
         */
        """
        pass

    def remove_physics_object(self, const_PhysicsObjectCollection_self, PhysicsObject_physics_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_physics_object(const PhysicsObjectCollection self, PhysicsObject physics_object)
        
        /**
         * Removes the indicated PhysicsObject from the collection.  Returns true if
         * the physics_object was removed, false if it was not a member of the
         * collection.
         */
        """
        pass

    def remove_physics_objects_from(self, const_PhysicsObjectCollection_self, const_PhysicsObjectCollection_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_physics_objects_from(const PhysicsObjectCollection self, const PhysicsObjectCollection other)
        
        /**
         * Removes from this collection all of the PhysicsObjects listed in the other
         * collection.
         */
        """
        pass

    def write(self, PhysicsObjectCollection_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(PhysicsObjectCollection self, ostream out, int indent_level)
        
        /**
         * Writes a complete multi-line description of the PhysicsObjectCollection to
         * the indicated output stream.
         */
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__add__': None, # (!) real value is "<slot wrapper '__add__' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        '__doc__': "/**\n * This is a set of zero or more PhysicsObjects.  It's handy for returning\n * from functions that need to return multiple PhysicsObjects.\n */",
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        '__iadd__': None, # (!) real value is "<slot wrapper '__iadd__' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        '__len__': None, # (!) real value is "<slot wrapper '__len__' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DEB5B0>'
        '__radd__': None, # (!) real value is "<slot wrapper '__radd__' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'addPhysicsObject': None, # (!) real value is "<method 'addPhysicsObject' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'addPhysicsObjectsFrom': None, # (!) real value is "<method 'addPhysicsObjectsFrom' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'add_physics_object': None, # (!) real value is "<method 'add_physics_object' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'add_physics_objects_from': None, # (!) real value is "<method 'add_physics_objects_from' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'getNumPhysicsObjects': None, # (!) real value is "<method 'getNumPhysicsObjects' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'getPhysicsObject': None, # (!) real value is "<method 'getPhysicsObject' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'getPhysicsObjects': None, # (!) real value is "<method 'getPhysicsObjects' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'get_num_physics_objects': None, # (!) real value is "<method 'get_num_physics_objects' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'get_physics_object': None, # (!) real value is "<method 'get_physics_object' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'get_physics_objects': None, # (!) real value is "<method 'get_physics_objects' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'hasPhysicsObject': None, # (!) real value is "<method 'hasPhysicsObject' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'has_physics_object': None, # (!) real value is "<method 'has_physics_object' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'removeDuplicatePhysicsObjects': None, # (!) real value is "<method 'removeDuplicatePhysicsObjects' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'removePhysicsObject': None, # (!) real value is "<method 'removePhysicsObject' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'removePhysicsObjectsFrom': None, # (!) real value is "<method 'removePhysicsObjectsFrom' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'remove_duplicate_physics_objects': None, # (!) real value is "<method 'remove_duplicate_physics_objects' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'remove_physics_object': None, # (!) real value is "<method 'remove_physics_object' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'remove_physics_objects_from': None, # (!) real value is "<method 'remove_physics_objects_from' of 'panda3d.physics.PhysicsObjectCollection' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.physics.PhysicsObjectCollection' objects>"
    }


