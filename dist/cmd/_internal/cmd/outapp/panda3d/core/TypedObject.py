# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class TypedObject(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is an abstract class that all classes which use TypeHandle, and also
     * provide virtual functions to support polymorphism, should inherit from.
     * Each derived class should define get_type(), which should return the
     * specific type of the derived class.  Inheriting from this automatically
     * provides support for is_of_type() and is_exact_type().
     *
     * All classes that inherit directly or indirectly from TypedObject should
     * redefine get_type() and force_init_type(), as shown below.  Some classes
     * that do not inherit from TypedObject may still declare TypeHandles for
     * themselves by defining methods called get_class_type() and init_type().
     * Classes such as these may serve as base classes, but the dynamic type
     * identification system will be limited.  Classes that do not inherit from
     * TypedObject need not define the virtual functions get_type() and
     * force_init_type() (or any other virtual functions).
     *
     * There is a specific layout for defining the overrides from this class.
     * Keeping the definitions formatted just like these examples will allow
     * someone in the future to use a sed (or similar) script to make global
     * changes, if necessary.  Avoid rearranging the braces or the order of the
     * functions unless you're ready to change them in every file all at once.
     *
     * What follows are some examples that can be used in new classes that you
     * create.
     *
     * @par In the class definition (.h file):
     * @code
     * public:
     *   static TypeHandle get_class_type() {
     *     return _type_handle;
     *   }
     *   static void init_type() {
     *     <<<BaseClassOne>>>::init_type();
     *     <<<BaseClassTwo>>>::init_type();
     *     <<<BaseClassN>>>::init_type();
     *     register_type(_type_handle, "<<<ThisClassStringName>>>",
     *                   <<<BaseClassOne>>>::get_class_type(),
     *                   <<<BaseClassTwo>>>::get_class_type(),
     *                   <<<BaseClassN>>>::get_class_type());
     *   }
     *   virtual TypeHandle get_type() const {
     *     return get_class_type();
     *   }
     *   virtual TypeHandle force_init_type() {init_type(); return get_class_type();}
     *
     * private:
     *   static TypeHandle _type_handle;
     * @endcode
     *
     * @par In the class .cxx file:
     * @code
     * TypeHandle <<<ThisClassStringName>>>::_type_handle;
     * @endcode
     *
     * @par In the class config_<<<PackageName>>>.cxx file:
     * @code
     * ConfigureFn(config_<<<PackageName>>>) {
     *   <<<ClassOne>>>::init_type();
     *   <<<ClassTwo>>>::init_type();
     *   <<<ClassN>>>::init_type();
     * }
     * @endcode
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_type(TypedObject self)
        
        // Derived classes should override this function to return get_class_type().
        
        // Derived classes should override this function to return get_class_type().
        
        /**
         *
         */
        """
        pass

    def getTypeIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_type_index(TypedObject self)
        
        /**
         * Returns the internal index number associated with this object's TypeHandle,
         * a unique number for each different type.  This is equivalent to
         * get_type().get_index().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_type(self, TypedObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_type(TypedObject self)
        
        // Derived classes should override this function to return get_class_type().
        
        // Derived classes should override this function to return get_class_type().
        
        /**
         *
         */
        """
        pass

    def get_type_index(self, TypedObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_type_index(TypedObject self)
        
        /**
         * Returns the internal index number associated with this object's TypeHandle,
         * a unique number for each different type.  This is equivalent to
         * get_type().get_index().
         */
        """
        pass

    def isExactType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_exact_type(TypedObject self, TypeHandle handle)
        
        /**
         * Returns true if the current object is the indicated type exactly.
         */
        """
        pass

    def isOfType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_of_type(TypedObject self, TypeHandle handle)
        
        /**
         * Returns true if the current object is or derives from the indicated type.
         */
        """
        pass

    def is_exact_type(self, TypedObject_self, TypeHandle_handle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_exact_type(TypedObject self, TypeHandle handle)
        
        /**
         * Returns true if the current object is the indicated type exactly.
         */
        """
        pass

    def is_of_type(self, TypedObject_self, TypeHandle_handle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_of_type(TypedObject self, TypeHandle handle)
        
        /**
         * Returns true if the current object is or derives from the indicated type.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// Returns the TypeHandle representing this object's type."""


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This is an abstract class that all classes which use TypeHandle, and also\n * provide virtual functions to support polymorphism, should inherit from.\n * Each derived class should define get_type(), which should return the\n * specific type of the derived class.  Inheriting from this automatically\n * provides support for is_of_type() and is_exact_type().\n *\n * All classes that inherit directly or indirectly from TypedObject should\n * redefine get_type() and force_init_type(), as shown below.  Some classes\n * that do not inherit from TypedObject may still declare TypeHandles for\n * themselves by defining methods called get_class_type() and init_type().\n * Classes such as these may serve as base classes, but the dynamic type\n * identification system will be limited.  Classes that do not inherit from\n * TypedObject need not define the virtual functions get_type() and\n * force_init_type() (or any other virtual functions).\n *\n * There is a specific layout for defining the overrides from this class.\n * Keeping the definitions formatted just like these examples will allow\n * someone in the future to use a sed (or similar) script to make global\n * changes, if necessary.  Avoid rearranging the braces or the order of the\n * functions unless you\'re ready to change them in every file all at once.\n *\n * What follows are some examples that can be used in new classes that you\n * create.\n *\n * @par In the class definition (.h file):\n * @code\n * public:\n *   static TypeHandle get_class_type() {\n *     return _type_handle;\n *   }\n *   static void init_type() {\n *     <<<BaseClassOne>>>::init_type();\n *     <<<BaseClassTwo>>>::init_type();\n *     <<<BaseClassN>>>::init_type();\n *     register_type(_type_handle, "<<<ThisClassStringName>>>",\n *                   <<<BaseClassOne>>>::get_class_type(),\n *                   <<<BaseClassTwo>>>::get_class_type(),\n *                   <<<BaseClassN>>>::get_class_type());\n *   }\n *   virtual TypeHandle get_type() const {\n *     return get_class_type();\n *   }\n *   virtual TypeHandle force_init_type() {init_type(); return get_class_type();}\n *\n * private:\n *   static TypeHandle _type_handle;\n * @endcode\n *\n * @par In the class .cxx file:\n * @code\n * TypeHandle <<<ThisClassStringName>>>::_type_handle;\n * @endcode\n *\n * @par In the class config_<<<PackageName>>>.cxx file:\n * @code\n * ConfigureFn(config_<<<PackageName>>>) {\n *   <<<ClassOne>>>::init_type();\n *   <<<ClassTwo>>>::init_type();\n *   <<<ClassN>>>::init_type();\n * }\n * @endcode\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TypedObject' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE258A20>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE258A20>)>'
        'getType': None, # (!) real value is "<method 'getType' of 'panda3d.core.TypedObject' objects>"
        'getTypeIndex': None, # (!) real value is "<method 'getTypeIndex' of 'panda3d.core.TypedObject' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE258A20>)>'
        'get_type': None, # (!) real value is "<method 'get_type' of 'panda3d.core.TypedObject' objects>"
        'get_type_index': None, # (!) real value is "<method 'get_type_index' of 'panda3d.core.TypedObject' objects>"
        'isExactType': None, # (!) real value is "<method 'isExactType' of 'panda3d.core.TypedObject' objects>"
        'isOfType': None, # (!) real value is "<method 'isOfType' of 'panda3d.core.TypedObject' objects>"
        'is_exact_type': None, # (!) real value is "<method 'is_exact_type' of 'panda3d.core.TypedObject' objects>"
        'is_of_type': None, # (!) real value is "<method 'is_of_type' of 'panda3d.core.TypedObject' objects>"
        'type': None, # (!) real value is "<attribute 'type' of 'panda3d.core.TypedObject' objects>"
    }


