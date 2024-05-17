# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class TypeHandle(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * TypeHandle is the identifier used to differentiate C++ class types.  Any
     * C++ classes that inherit from some base class, and must be differentiated
     * at run time, should store a static TypeHandle object that can be queried
     * through a static member function named get_class_type().  Most of the time,
     * it is also desirable to inherit from TypedObject, which provides some
     * virtual functions to return the TypeHandle for a particular instance.
     *
     * At its essence, a TypeHandle is simply a unique identifier that is assigned
     * by the TypeRegistry.  The TypeRegistry stores a tree of TypeHandles, so
     * that ancestry of a particular type may be queried, and the type name may be
     * retrieved for run-time display.
     */
    """
    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(TypeHandle self, const TypeHandle other)
        
        /**
         * Sorts TypeHandles arbitrarily (according to <, >, etc.).  Returns a number
         * less than 0 if this type sorts before the other one, greater than zero if
         * it sorts after, 0 if they are equivalent.
         */
        """
        pass

    def compare_to(self, TypeHandle_self, const_TypeHandle_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(TypeHandle self, const TypeHandle other)
        
        /**
         * Sorts TypeHandles arbitrarily (according to <, >, etc.).  Returns a number
         * less than 0 if this type sorts before the other one, greater than zero if
         * it sorts after, 0 if they are equivalent.
         */
        """
        pass

    def decMemoryUsage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        dec_memory_usage(const TypeHandle self, int memory_class, int size)
        
        /**
         * Subtracts the indicated amount from the record for the total allocated
         * memory for objects of this type.
         */
        """
        pass

    def dec_memory_usage(self, const_TypeHandle_self, int_memory_class, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        dec_memory_usage(const TypeHandle self, int memory_class, int size)
        
        /**
         * Subtracts the indicated amount from the record for the total allocated
         * memory for objects of this type.
         */
        """
        pass

    def getChildClass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_child_class(TypeHandle self, int index)
        
        /**
         * Returns the nth child class of this type.  The index should be in the range
         * 0 <= index < get_num_child_classes().
         */
        """
        pass

    def getHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hash(TypeHandle self)
        
        /**
         * Returns a hash code suitable for phash_map.
         */
        """
        pass

    def getIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_index(TypeHandle self)
        
        /**
         * Returns the integer index associated with this TypeHandle.  Each different
         * TypeHandle will have a different index.  However, you probably shouldn't be
         * using this method; you should just treat the TypeHandles as opaque classes.
         * This is provided for the convenience of non-C++ scripting languages to
         * build a hashtable of TypeHandles.
         */
        """
        pass

    def getMemoryUsage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_memory_usage(TypeHandle self, int memory_class)
        
        /**
         * Returns the total allocated memory used by objects of this type, for the
         * indicated memory class.  This is only updated if track-memory-usage is set
         * true in your Config.prc file.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(TypeHandle self, TypedObject object)
        
        /**
         * Returns the name of the type.
         *
         * The "object" pointer is an optional pointer to the TypedObject class that
         * owns this TypeHandle.  It is only used in case the TypeHandle is
         * inadvertantly undefined.
         */
        """
        pass

    def getNumChildClasses(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_child_classes(TypeHandle self, TypedObject object)
        
        /**
         * Returns the number of child classes that this type is known to have.  This
         * may then be used to index into get_child_class().
         *
         * The "object" pointer is an optional pointer to the TypedObject class that
         * owns this TypeHandle.  It is only used in case the TypeHandle is
         * inadvertantly undefined.
         */
        """
        pass

    def getNumParentClasses(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_parent_classes(TypeHandle self, TypedObject object)
        
        /**
         * Returns the number of parent classes that this type is known to have.  This
         * may then be used to index into get_parent_class().  The result will be 0 if
         * this class does not inherit from any other classes, 1 if normal, single
         * inheritance is in effect, or greater than one if multiple inheritance is in
         * effect.
         *
         * The "object" pointer is an optional pointer to the TypedObject class that
         * owns this TypeHandle.  It is only used in case the TypeHandle is
         * inadvertantly undefined.
         */
        """
        pass

    def getParentClass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_parent_class(TypeHandle self, int index)
        
        /**
         * Returns the nth parent class of this type.  The index should be in the
         * range 0 <= index < get_num_parent_classes().
         */
        """
        pass

    def getParentTowards(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_parent_towards(TypeHandle self, TypeHandle ancestor, TypedObject object)
        
        /**
         * Returns the parent class that is in a direct line of inheritance to the
         * indicated ancestor class.  This is useful in the presence of multiple
         * inheritance to try to determine what properties an unknown type may have.
         *
         * The return value is TypeHandle::none() if the type does not inherit from
         * the ancestor.  If ancestor is the same as this type, the return value is
         * this type.
         *
         * The "object" pointer is an optional pointer to the TypedObject class that
         * owns this TypeHandle.  It is only used in case the TypeHandle is
         * inadvertantly undefined.
         */
        """
        pass

    def get_child_class(self, TypeHandle_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_child_class(TypeHandle self, int index)
        
        /**
         * Returns the nth child class of this type.  The index should be in the range
         * 0 <= index < get_num_child_classes().
         */
        """
        pass

    def get_hash(self, TypeHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hash(TypeHandle self)
        
        /**
         * Returns a hash code suitable for phash_map.
         */
        """
        pass

    def get_index(self, TypeHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_index(TypeHandle self)
        
        /**
         * Returns the integer index associated with this TypeHandle.  Each different
         * TypeHandle will have a different index.  However, you probably shouldn't be
         * using this method; you should just treat the TypeHandles as opaque classes.
         * This is provided for the convenience of non-C++ scripting languages to
         * build a hashtable of TypeHandles.
         */
        """
        pass

    def get_memory_usage(self, TypeHandle_self, int_memory_class): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_memory_usage(TypeHandle self, int memory_class)
        
        /**
         * Returns the total allocated memory used by objects of this type, for the
         * indicated memory class.  This is only updated if track-memory-usage is set
         * true in your Config.prc file.
         */
        """
        pass

    def get_name(self, TypeHandle_self, TypedObject_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(TypeHandle self, TypedObject object)
        
        /**
         * Returns the name of the type.
         *
         * The "object" pointer is an optional pointer to the TypedObject class that
         * owns this TypeHandle.  It is only used in case the TypeHandle is
         * inadvertantly undefined.
         */
        """
        pass

    def get_num_child_classes(self, TypeHandle_self, TypedObject_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_child_classes(TypeHandle self, TypedObject object)
        
        /**
         * Returns the number of child classes that this type is known to have.  This
         * may then be used to index into get_child_class().
         *
         * The "object" pointer is an optional pointer to the TypedObject class that
         * owns this TypeHandle.  It is only used in case the TypeHandle is
         * inadvertantly undefined.
         */
        """
        pass

    def get_num_parent_classes(self, TypeHandle_self, TypedObject_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_parent_classes(TypeHandle self, TypedObject object)
        
        /**
         * Returns the number of parent classes that this type is known to have.  This
         * may then be used to index into get_parent_class().  The result will be 0 if
         * this class does not inherit from any other classes, 1 if normal, single
         * inheritance is in effect, or greater than one if multiple inheritance is in
         * effect.
         *
         * The "object" pointer is an optional pointer to the TypedObject class that
         * owns this TypeHandle.  It is only used in case the TypeHandle is
         * inadvertantly undefined.
         */
        """
        pass

    def get_parent_class(self, TypeHandle_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_parent_class(TypeHandle self, int index)
        
        /**
         * Returns the nth parent class of this type.  The index should be in the
         * range 0 <= index < get_num_parent_classes().
         */
        """
        pass

    def get_parent_towards(self, TypeHandle_self, TypeHandle_ancestor, TypedObject_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_parent_towards(TypeHandle self, TypeHandle ancestor, TypedObject object)
        
        /**
         * Returns the parent class that is in a direct line of inheritance to the
         * indicated ancestor class.  This is useful in the presence of multiple
         * inheritance to try to determine what properties an unknown type may have.
         *
         * The return value is TypeHandle::none() if the type does not inherit from
         * the ancestor.  If ancestor is the same as this type, the return value is
         * this type.
         *
         * The "object" pointer is an optional pointer to the TypedObject class that
         * owns this TypeHandle.  It is only used in case the TypeHandle is
         * inadvertantly undefined.
         */
        """
        pass

    def incMemoryUsage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        inc_memory_usage(const TypeHandle self, int memory_class, int size)
        
        /**
         * Adds the indicated amount to the record for the total allocated memory for
         * objects of this type.
         */
        """
        pass

    def inc_memory_usage(self, const_TypeHandle_self, int_memory_class, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        inc_memory_usage(const TypeHandle self, int memory_class, int size)
        
        /**
         * Adds the indicated amount to the record for the total allocated memory for
         * objects of this type.
         */
        """
        pass

    def isDerivedFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_derived_from(TypeHandle self, TypeHandle parent, TypedObject object)
        
        /**
         * Returns true if this type is derived from the indicated type, false
         * otherwise.
         *
         * The "object" pointer is an optional pointer to the TypedObject class that
         * owns this TypeHandle.  It is only used in case the TypeHandle is
         * inadvertantly undefined.
         */
        """
        pass

    def is_derived_from(self, TypeHandle_self, TypeHandle_parent, TypedObject_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_derived_from(TypeHandle self, TypeHandle parent, TypedObject object)
        
        /**
         * Returns true if this type is derived from the indicated type, false
         * otherwise.
         *
         * The "object" pointer is an optional pointer to the TypedObject class that
         * owns this TypeHandle.  It is only used in case the TypeHandle is
         * inadvertantly undefined.
         */
        """
        pass

    def make(self, type_classobj): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(type classobj)
        """
        pass

    def none(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        none()
        """
        pass

    def output(self, TypeHandle_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(TypeHandle self, ostream out)
        
        /**
         *
         */
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    child_classes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_classes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'MCArray': 1,
        'MCDeletedChainActive': 2,
        'MCDeletedChainInactive': 3,
        'MCLimit': 4,
        'MCSingleton': 0,
        'MC_array': 1,
        'MC_deleted_chain_active': 2,
        'MC_deleted_chain_inactive': 3,
        'MC_limit': 4,
        'MC_singleton': 0,
        '__bool__': None, # (!) real value is "<slot wrapper '__bool__' of 'panda3d.core.TypeHandle' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TypeHandle' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TypeHandle' objects>"
        '__doc__': '/**\n * TypeHandle is the identifier used to differentiate C++ class types.  Any\n * C++ classes that inherit from some base class, and must be differentiated\n * at run time, should store a static TypeHandle object that can be queried\n * through a static member function named get_class_type().  Most of the time,\n * it is also desirable to inherit from TypedObject, which provides some\n * virtual functions to return the TypeHandle for a particular instance.\n *\n * At its essence, a TypeHandle is simply a unique identifier that is assigned\n * by the TypeRegistry.  The TypeRegistry stores a tree of TypeHandles, so\n * that ancestry of a particular type may be queried, and the type name may be\n * retrieved for run-time display.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.TypeHandle' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.TypeHandle' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.TypeHandle' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.TypeHandle' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TypeHandle' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.TypeHandle' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.TypeHandle' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.TypeHandle' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE258680>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.TypeHandle' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.TypeHandle' objects>"
        'child_classes': None, # (!) real value is "<attribute 'child_classes' of 'panda3d.core.TypeHandle' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.TypeHandle' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.TypeHandle' objects>"
        'decMemoryUsage': None, # (!) real value is "<method 'decMemoryUsage' of 'panda3d.core.TypeHandle' objects>"
        'dec_memory_usage': None, # (!) real value is "<method 'dec_memory_usage' of 'panda3d.core.TypeHandle' objects>"
        'getChildClass': None, # (!) real value is "<method 'getChildClass' of 'panda3d.core.TypeHandle' objects>"
        'getHash': None, # (!) real value is "<method 'getHash' of 'panda3d.core.TypeHandle' objects>"
        'getIndex': None, # (!) real value is "<method 'getIndex' of 'panda3d.core.TypeHandle' objects>"
        'getMemoryUsage': None, # (!) real value is "<method 'getMemoryUsage' of 'panda3d.core.TypeHandle' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.TypeHandle' objects>"
        'getNumChildClasses': None, # (!) real value is "<method 'getNumChildClasses' of 'panda3d.core.TypeHandle' objects>"
        'getNumParentClasses': None, # (!) real value is "<method 'getNumParentClasses' of 'panda3d.core.TypeHandle' objects>"
        'getParentClass': None, # (!) real value is "<method 'getParentClass' of 'panda3d.core.TypeHandle' objects>"
        'getParentTowards': None, # (!) real value is "<method 'getParentTowards' of 'panda3d.core.TypeHandle' objects>"
        'get_child_class': None, # (!) real value is "<method 'get_child_class' of 'panda3d.core.TypeHandle' objects>"
        'get_hash': None, # (!) real value is "<method 'get_hash' of 'panda3d.core.TypeHandle' objects>"
        'get_index': None, # (!) real value is "<method 'get_index' of 'panda3d.core.TypeHandle' objects>"
        'get_memory_usage': None, # (!) real value is "<method 'get_memory_usage' of 'panda3d.core.TypeHandle' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.TypeHandle' objects>"
        'get_num_child_classes': None, # (!) real value is "<method 'get_num_child_classes' of 'panda3d.core.TypeHandle' objects>"
        'get_num_parent_classes': None, # (!) real value is "<method 'get_num_parent_classes' of 'panda3d.core.TypeHandle' objects>"
        'get_parent_class': None, # (!) real value is "<method 'get_parent_class' of 'panda3d.core.TypeHandle' objects>"
        'get_parent_towards': None, # (!) real value is "<method 'get_parent_towards' of 'panda3d.core.TypeHandle' objects>"
        'incMemoryUsage': None, # (!) real value is "<method 'incMemoryUsage' of 'panda3d.core.TypeHandle' objects>"
        'inc_memory_usage': None, # (!) real value is "<method 'inc_memory_usage' of 'panda3d.core.TypeHandle' objects>"
        'index': None, # (!) real value is "<attribute 'index' of 'panda3d.core.TypeHandle' objects>"
        'isDerivedFrom': None, # (!) real value is "<method 'isDerivedFrom' of 'panda3d.core.TypeHandle' objects>"
        'is_derived_from': None, # (!) real value is "<method 'is_derived_from' of 'panda3d.core.TypeHandle' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE258680>)>'
        'name': None, # (!) real value is "<attribute 'name' of 'panda3d.core.TypeHandle' objects>"
        'none': None, # (!) real value is '<staticmethod(<built-in method none of type object at 0x00007FFCFE258680>)>'
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.TypeHandle' objects>"
        'parent_classes': None, # (!) real value is "<attribute 'parent_classes' of 'panda3d.core.TypeHandle' objects>"
    }
    MCArray = 1
    MCDeletedChainActive = 2
    MCDeletedChainInactive = 3
    MCLimit = 4
    MCSingleton = 0
    MC_array = 1
    MC_deleted_chain_active = 2
    MC_deleted_chain_inactive = 3
    MC_limit = 4
    MC_singleton = 0


