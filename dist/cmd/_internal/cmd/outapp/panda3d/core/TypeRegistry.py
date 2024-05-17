# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class TypeRegistry(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * The TypeRegistry class maintains all the assigned TypeHandles in a given
     * system.  There should be only one TypeRegistry class during the lifetime of
     * the application.  It will be created on the local heap initially, and it
     * should be migrated to shared memory as soon as shared memory becomes
     * available.
     */
    """
    def findType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_type(TypeRegistry self, str name)
        
        /**
         * Looks for a previously-registered type of the given name.  Returns its
         * TypeHandle if it exists, or TypeHandle::none() if there is no such type.
         */
        """
        pass

    def findTypeById(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_type_by_id(TypeRegistry self, int id)
        
        /**
         * Looks for a previously-registered type with the given id number (as
         * returned by TypeHandle::get_index()). Returns its TypeHandle if it exists,
         * or TypeHandle::none() if there is no such type.
         */
        """
        pass

    def find_type(self, TypeRegistry_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_type(TypeRegistry self, str name)
        
        /**
         * Looks for a previously-registered type of the given name.  Returns its
         * TypeHandle if it exists, or TypeHandle::none() if there is no such type.
         */
        """
        pass

    def find_type_by_id(self, TypeRegistry_self, int_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_type_by_id(TypeRegistry self, int id)
        
        /**
         * Looks for a previously-registered type with the given id number (as
         * returned by TypeHandle::get_index()). Returns its TypeHandle if it exists,
         * or TypeHandle::none() if there is no such type.
         */
        """
        pass

    def getChildClass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_child_class(TypeRegistry self, TypeHandle child, int index)
        
        /**
         * Returns the nth child class of this type.  The index should be in the range
         * 0 <= index < get_num_child_classes().
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(TypeRegistry self, TypeHandle type, TypedObject object)
        
        /**
         * Returns the name of the indicated type.
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
        get_num_child_classes(TypeRegistry self, TypeHandle child, TypedObject child_object)
        
        /**
         * Returns the number of child classes that the indicated type is known to
         * have.  This may then be used to index into get_child_class().
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
        get_num_parent_classes(TypeRegistry self, TypeHandle child, TypedObject child_object)
        
        /**
         * Returns the number of parent classes that the indicated type is known to
         * have.  This may then be used to index into get_parent_class().  The result
         * will be 0 if this class does not inherit from any other classes, 1 if
         * normal, single inheritance is in effect, or greater than one if multiple
         * inheritance is in effect.
         *
         * The "object" pointer is an optional pointer to the TypedObject class that
         * owns this TypeHandle.  It is only used in case the TypeHandle is
         * inadvertantly undefined.
         */
        """
        pass

    def getNumRootClasses(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_root_classes(const TypeRegistry self)
        
        /**
         * Returns the number of root classes--that is, classes that do not inherit
         * from any other classes--known in the system.
         */
        """
        pass

    def getNumTypehandles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_typehandles(const TypeRegistry self)
        
        /**
         * Returns the total number of unique TypeHandles in the system.
         */
        """
        pass

    def getParentClass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_parent_class(TypeRegistry self, TypeHandle child, int index)
        
        /**
         * Returns the nth parent class of this type.  The index should be in the
         * range 0 <= index < get_num_parent_classes().
         */
        """
        pass

    def getParentTowards(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_parent_towards(const TypeRegistry self, TypeHandle child, TypeHandle base, TypedObject child_object)
        
        /**
         * Returns the parent of the indicated child class that is in a direct line of
         * inheritance to the indicated ancestor class.  This is useful in the
         * presence of multiple inheritance to try to determine what properties an
         * unknown type may have.
         *
         * The "object" pointer is an optional pointer to the TypedObject class that
         * owns this TypeHandle.  It is only used in case the TypeHandle is
         * inadvertantly undefined.
         */
        """
        pass

    def getRootClass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_root_class(const TypeRegistry self, int n)
        
        /**
         * Returns the nth root class in the system.  See get_num_root_classes().
         */
        """
        pass

    def getRootClasses(self, *args, **kwargs): # real signature unknown
        pass

    def getTypehandle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_typehandle(const TypeRegistry self, int n)
        
        /**
         * Returns the nth TypeHandle in the system.  See get_num_typehandles().
         */
        """
        pass

    def getTypehandles(self, *args, **kwargs): # real signature unknown
        pass

    def get_child_class(self, TypeRegistry_self, TypeHandle_child, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_child_class(TypeRegistry self, TypeHandle child, int index)
        
        /**
         * Returns the nth child class of this type.  The index should be in the range
         * 0 <= index < get_num_child_classes().
         */
        """
        pass

    def get_name(self, TypeRegistry_self, TypeHandle_type, TypedObject_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(TypeRegistry self, TypeHandle type, TypedObject object)
        
        /**
         * Returns the name of the indicated type.
         *
         * The "object" pointer is an optional pointer to the TypedObject class that
         * owns this TypeHandle.  It is only used in case the TypeHandle is
         * inadvertantly undefined.
         */
        """
        pass

    def get_num_child_classes(self, TypeRegistry_self, TypeHandle_child, TypedObject_child_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_child_classes(TypeRegistry self, TypeHandle child, TypedObject child_object)
        
        /**
         * Returns the number of child classes that the indicated type is known to
         * have.  This may then be used to index into get_child_class().
         *
         * The "object" pointer is an optional pointer to the TypedObject class that
         * owns this TypeHandle.  It is only used in case the TypeHandle is
         * inadvertantly undefined.
         */
        """
        pass

    def get_num_parent_classes(self, TypeRegistry_self, TypeHandle_child, TypedObject_child_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_parent_classes(TypeRegistry self, TypeHandle child, TypedObject child_object)
        
        /**
         * Returns the number of parent classes that the indicated type is known to
         * have.  This may then be used to index into get_parent_class().  The result
         * will be 0 if this class does not inherit from any other classes, 1 if
         * normal, single inheritance is in effect, or greater than one if multiple
         * inheritance is in effect.
         *
         * The "object" pointer is an optional pointer to the TypedObject class that
         * owns this TypeHandle.  It is only used in case the TypeHandle is
         * inadvertantly undefined.
         */
        """
        pass

    def get_num_root_classes(self, const_TypeRegistry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_root_classes(const TypeRegistry self)
        
        /**
         * Returns the number of root classes--that is, classes that do not inherit
         * from any other classes--known in the system.
         */
        """
        pass

    def get_num_typehandles(self, const_TypeRegistry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_typehandles(const TypeRegistry self)
        
        /**
         * Returns the total number of unique TypeHandles in the system.
         */
        """
        pass

    def get_parent_class(self, TypeRegistry_self, TypeHandle_child, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_parent_class(TypeRegistry self, TypeHandle child, int index)
        
        /**
         * Returns the nth parent class of this type.  The index should be in the
         * range 0 <= index < get_num_parent_classes().
         */
        """
        pass

    def get_parent_towards(self, const_TypeRegistry_self, TypeHandle_child, TypeHandle_base, TypedObject_child_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_parent_towards(const TypeRegistry self, TypeHandle child, TypeHandle base, TypedObject child_object)
        
        /**
         * Returns the parent of the indicated child class that is in a direct line of
         * inheritance to the indicated ancestor class.  This is useful in the
         * presence of multiple inheritance to try to determine what properties an
         * unknown type may have.
         *
         * The "object" pointer is an optional pointer to the TypedObject class that
         * owns this TypeHandle.  It is only used in case the TypeHandle is
         * inadvertantly undefined.
         */
        """
        pass

    def get_root_class(self, const_TypeRegistry_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_root_class(const TypeRegistry self, int n)
        
        /**
         * Returns the nth root class in the system.  See get_num_root_classes().
         */
        """
        pass

    def get_root_classes(self, *args, **kwargs): # real signature unknown
        pass

    def get_typehandle(self, const_TypeRegistry_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_typehandle(const TypeRegistry self, int n)
        
        /**
         * Returns the nth TypeHandle in the system.  See get_num_typehandles().
         */
        """
        pass

    def get_typehandles(self, *args, **kwargs): # real signature unknown
        pass

    def isDerivedFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_derived_from(const TypeRegistry self, TypeHandle child, TypeHandle base, TypedObject child_object)
        
        /**
         * Returns true if the first type is derived from the second type, false
         * otherwise.
         *
         * The "child_object" pointer is an optional pointer to the TypedObject class
         * that owns the child TypeHandle.  It is only used in case the TypeHandle is
         * inadvertently undefined.
         *
         * This function definition follows the definitions for look_up() and
         * freshen_derivations() just to maximize the chance the the compiler will be
         * able to inline the above functions.  Yeah, a compiler shouldn't care, but
         * there's a big different between "shouldn't" and "doesn't".
         */
        """
        pass

    def is_derived_from(self, const_TypeRegistry_self, TypeHandle_child, TypeHandle_base, TypedObject_child_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_derived_from(const TypeRegistry self, TypeHandle child, TypeHandle base, TypedObject child_object)
        
        /**
         * Returns true if the first type is derived from the second type, false
         * otherwise.
         *
         * The "child_object" pointer is an optional pointer to the TypedObject class
         * that owns the child TypeHandle.  It is only used in case the TypeHandle is
         * inadvertently undefined.
         *
         * This function definition follows the definitions for look_up() and
         * freshen_derivations() just to maximize the chance the the compiler will be
         * able to inline the above functions.  Yeah, a compiler shouldn't care, but
         * there's a big different between "shouldn't" and "doesn't".
         */
        """
        pass

    def ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ptr()
        
        // ptr() returns the pointer to the global TypeRegistry object.
        
        /**
         * Returns the pointer to the global TypeRegistry object.
         */
        """
        pass

    def recordAlternateName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        record_alternate_name(const TypeRegistry self, TypeHandle type, str name)
        
        /**
         * Indicates an alternate name for the same type.  This is particularly useful
         * when a type has changed names, since the type is stored in a Bam file by
         * name; setting the original name as the alternate will allow the type to be
         * correctly read from old Bam files.
         */
        """
        pass

    def recordDerivation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        record_derivation(const TypeRegistry self, TypeHandle child, TypeHandle parent)
        
        /**
         * Records that the type referenced by child inherits directly from the type
         * referenced by parent.  In the event of multiple inheritance, this should be
         * called once for each parent class.
         */
        """
        pass

    def recordPythonType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        record_python_type(const TypeRegistry self, TypeHandle type, object python_type)
        
        /**
         * Records the given Python type pointer in the type registry for the benefit
         * of interrogate, which expects this to contain a Dtool_PyTypedObject.
         */
        """
        pass

    def record_alternate_name(self, const_TypeRegistry_self, TypeHandle_type, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        record_alternate_name(const TypeRegistry self, TypeHandle type, str name)
        
        /**
         * Indicates an alternate name for the same type.  This is particularly useful
         * when a type has changed names, since the type is stored in a Bam file by
         * name; setting the original name as the alternate will allow the type to be
         * correctly read from old Bam files.
         */
        """
        pass

    def record_derivation(self, const_TypeRegistry_self, TypeHandle_child, TypeHandle_parent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        record_derivation(const TypeRegistry self, TypeHandle child, TypeHandle parent)
        
        /**
         * Records that the type referenced by child inherits directly from the type
         * referenced by parent.  In the event of multiple inheritance, this should be
         * called once for each parent class.
         */
        """
        pass

    def record_python_type(self, const_TypeRegistry_self, TypeHandle_type, object_python_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        record_python_type(const TypeRegistry self, TypeHandle type, object python_type)
        
        /**
         * Records the given Python type pointer in the type registry for the benefit
         * of interrogate, which expects this to contain a Dtool_PyTypedObject.
         */
        """
        pass

    def registerDynamicType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        register_dynamic_type(const TypeRegistry self, str name)
        
        /**
         * Registers a new type on-the-fly, presumably at runtime.  A new TypeHandle
         * is returned if the typename was not seen before; otherwise the same
         * TypeHandle that was last used for this typename is returned.
         */
        """
        pass

    def register_dynamic_type(self, const_TypeRegistry_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        register_dynamic_type(const TypeRegistry self, str name)
        
        /**
         * Registers a new type on-the-fly, presumably at runtime.  A new TypeHandle
         * is returned if the typename was not seen before; otherwise the same
         * TypeHandle that was last used for this typename is returned.
         */
        """
        pass

    def reregisterTypes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reregister_types()
        
        /**
         * Walks through the TypeRegistry tree and makes sure that each type that was
         * previously registered is *still* registered.  This seems to get broken in
         * certain circumstances when compiled against libc5--it is as if the static
         * initializer stomps on the _type_handle values of each class after they've
         * been registered.
         */
        """
        pass

    def reregister_types(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reregister_types()
        
        /**
         * Walks through the TypeRegistry tree and makes sure that each type that was
         * previously registered is *still* registered.  This seems to get broken in
         * certain circumstances when compiled against libc5--it is as if the static
         * initializer stomps on the _type_handle values of each class after they've
         * been registered.
         */
        """
        pass

    def write(self, TypeRegistry_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(TypeRegistry self, ostream out)
        
        /**
         * Makes an attempt to format the entire TypeRegistry in a nice way that shows
         * the derivation tree as intelligently as possible.
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    root_classes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typehandles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TypeRegistry' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TypeRegistry' objects>"
        '__doc__': '/**\n * The TypeRegistry class maintains all the assigned TypeHandles in a given\n * system.  There should be only one TypeRegistry class during the lifetime of\n * the application.  It will be created on the local heap initially, and it\n * should be migrated to shared memory as soon as shared memory becomes\n * available.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TypeRegistry' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE258850>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.TypeRegistry' objects>"
        'findType': None, # (!) real value is "<method 'findType' of 'panda3d.core.TypeRegistry' objects>"
        'findTypeById': None, # (!) real value is "<method 'findTypeById' of 'panda3d.core.TypeRegistry' objects>"
        'find_type': None, # (!) real value is "<method 'find_type' of 'panda3d.core.TypeRegistry' objects>"
        'find_type_by_id': None, # (!) real value is "<method 'find_type_by_id' of 'panda3d.core.TypeRegistry' objects>"
        'getChildClass': None, # (!) real value is "<method 'getChildClass' of 'panda3d.core.TypeRegistry' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.TypeRegistry' objects>"
        'getNumChildClasses': None, # (!) real value is "<method 'getNumChildClasses' of 'panda3d.core.TypeRegistry' objects>"
        'getNumParentClasses': None, # (!) real value is "<method 'getNumParentClasses' of 'panda3d.core.TypeRegistry' objects>"
        'getNumRootClasses': None, # (!) real value is "<method 'getNumRootClasses' of 'panda3d.core.TypeRegistry' objects>"
        'getNumTypehandles': None, # (!) real value is "<method 'getNumTypehandles' of 'panda3d.core.TypeRegistry' objects>"
        'getParentClass': None, # (!) real value is "<method 'getParentClass' of 'panda3d.core.TypeRegistry' objects>"
        'getParentTowards': None, # (!) real value is "<method 'getParentTowards' of 'panda3d.core.TypeRegistry' objects>"
        'getRootClass': None, # (!) real value is "<method 'getRootClass' of 'panda3d.core.TypeRegistry' objects>"
        'getRootClasses': None, # (!) real value is "<method 'getRootClasses' of 'panda3d.core.TypeRegistry' objects>"
        'getTypehandle': None, # (!) real value is "<method 'getTypehandle' of 'panda3d.core.TypeRegistry' objects>"
        'getTypehandles': None, # (!) real value is "<method 'getTypehandles' of 'panda3d.core.TypeRegistry' objects>"
        'get_child_class': None, # (!) real value is "<method 'get_child_class' of 'panda3d.core.TypeRegistry' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.TypeRegistry' objects>"
        'get_num_child_classes': None, # (!) real value is "<method 'get_num_child_classes' of 'panda3d.core.TypeRegistry' objects>"
        'get_num_parent_classes': None, # (!) real value is "<method 'get_num_parent_classes' of 'panda3d.core.TypeRegistry' objects>"
        'get_num_root_classes': None, # (!) real value is "<method 'get_num_root_classes' of 'panda3d.core.TypeRegistry' objects>"
        'get_num_typehandles': None, # (!) real value is "<method 'get_num_typehandles' of 'panda3d.core.TypeRegistry' objects>"
        'get_parent_class': None, # (!) real value is "<method 'get_parent_class' of 'panda3d.core.TypeRegistry' objects>"
        'get_parent_towards': None, # (!) real value is "<method 'get_parent_towards' of 'panda3d.core.TypeRegistry' objects>"
        'get_root_class': None, # (!) real value is "<method 'get_root_class' of 'panda3d.core.TypeRegistry' objects>"
        'get_root_classes': None, # (!) real value is "<method 'get_root_classes' of 'panda3d.core.TypeRegistry' objects>"
        'get_typehandle': None, # (!) real value is "<method 'get_typehandle' of 'panda3d.core.TypeRegistry' objects>"
        'get_typehandles': None, # (!) real value is "<method 'get_typehandles' of 'panda3d.core.TypeRegistry' objects>"
        'isDerivedFrom': None, # (!) real value is "<method 'isDerivedFrom' of 'panda3d.core.TypeRegistry' objects>"
        'is_derived_from': None, # (!) real value is "<method 'is_derived_from' of 'panda3d.core.TypeRegistry' objects>"
        'ptr': None, # (!) real value is '<staticmethod(<built-in method ptr of type object at 0x00007FFCFE258850>)>'
        'recordAlternateName': None, # (!) real value is "<method 'recordAlternateName' of 'panda3d.core.TypeRegistry' objects>"
        'recordDerivation': None, # (!) real value is "<method 'recordDerivation' of 'panda3d.core.TypeRegistry' objects>"
        'recordPythonType': None, # (!) real value is "<method 'recordPythonType' of 'panda3d.core.TypeRegistry' objects>"
        'record_alternate_name': None, # (!) real value is "<method 'record_alternate_name' of 'panda3d.core.TypeRegistry' objects>"
        'record_derivation': None, # (!) real value is "<method 'record_derivation' of 'panda3d.core.TypeRegistry' objects>"
        'record_python_type': None, # (!) real value is "<method 'record_python_type' of 'panda3d.core.TypeRegistry' objects>"
        'registerDynamicType': None, # (!) real value is "<method 'registerDynamicType' of 'panda3d.core.TypeRegistry' objects>"
        'register_dynamic_type': None, # (!) real value is "<method 'register_dynamic_type' of 'panda3d.core.TypeRegistry' objects>"
        'reregisterTypes': None, # (!) real value is '<staticmethod(<built-in method reregisterTypes of type object at 0x00007FFCFE258850>)>'
        'reregister_types': None, # (!) real value is '<staticmethod(<built-in method reregister_types of type object at 0x00007FFCFE258850>)>'
        'root_classes': None, # (!) real value is "<attribute 'root_classes' of 'panda3d.core.TypeRegistry' objects>"
        'typehandles': None, # (!) real value is "<attribute 'typehandles' of 'panda3d.core.TypeRegistry' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.TypeRegistry' objects>"
    }


