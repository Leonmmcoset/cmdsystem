# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class LoaderFileTypeRegistry(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class maintains the set of all known LoaderFileTypes in the universe.
     */
    """
    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns a pointer to the global LoaderFileTypeRegistry object.
         */
        """
        pass

    def getNumTypes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_types(LoaderFileTypeRegistry self)
        
        /**
         * Returns the total number of types registered.
         */
        """
        pass

    def getType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_type(LoaderFileTypeRegistry self, int n)
        
        /**
         * Returns the nth type registered.
         */
        """
        pass

    def getTypeFromExtension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_type_from_extension(const LoaderFileTypeRegistry self, str extension)
        
        /**
         * Determines the type of the file based on the indicated extension (without a
         * leading dot).  Returns NULL if the extension matches no known file types.
         */
        """
        pass

    def getTypes(self, *args, **kwargs): # real signature unknown
        pass

    def get_global_ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns a pointer to the global LoaderFileTypeRegistry object.
         */
        """
        pass

    def get_num_types(self, LoaderFileTypeRegistry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_types(LoaderFileTypeRegistry self)
        
        /**
         * Returns the total number of types registered.
         */
        """
        pass

    def get_type(self, LoaderFileTypeRegistry_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_type(LoaderFileTypeRegistry self, int n)
        
        /**
         * Returns the nth type registered.
         */
        """
        pass

    def get_types(self, *args, **kwargs): # real signature unknown
        pass

    def get_type_from_extension(self, const_LoaderFileTypeRegistry_self, str_extension): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_type_from_extension(const LoaderFileTypeRegistry self, str extension)
        
        /**
         * Determines the type of the file based on the indicated extension (without a
         * leading dot).  Returns NULL if the extension matches no known file types.
         */
        """
        pass

    def registerDeferredType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        register_deferred_type(const LoaderFileTypeRegistry self, object entry_point)
        
        /**
         * Records a type associated with a particular extension to be loaded in the
         * future.  The named library will be dynamically loaded the first time files
         * of this extension are loaded; presumably this library will call
         * register_type() when it initializes, thus making the extension loadable.
         */
        """
        pass

    def registerType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        register_type(const LoaderFileTypeRegistry self, object type)
        
        /**
         * Defines a new LoaderFileType in the universe.
         */
        """
        pass

    def register_deferred_type(self, const_LoaderFileTypeRegistry_self, object_entry_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        register_deferred_type(const LoaderFileTypeRegistry self, object entry_point)
        
        /**
         * Records a type associated with a particular extension to be loaded in the
         * future.  The named library will be dynamically loaded the first time files
         * of this extension are loaded; presumably this library will call
         * register_type() when it initializes, thus making the extension loadable.
         */
        """
        pass

    def register_type(self, const_LoaderFileTypeRegistry_self, object_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        register_type(const LoaderFileTypeRegistry self, object type)
        
        /**
         * Defines a new LoaderFileType in the universe.
         */
        """
        pass

    def unregisterType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unregister_type(const LoaderFileTypeRegistry self, object type)
        
        /**
         * Removes a type previously registered using register_type.
         */
        """
        pass

    def unregister_type(self, const_LoaderFileTypeRegistry_self, object_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unregister_type(const LoaderFileTypeRegistry self, object type)
        
        /**
         * Removes a type previously registered using register_type.
         */
        """
        pass

    def write(self, LoaderFileTypeRegistry_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(LoaderFileTypeRegistry self, ostream out, int indent_level)
        
        /**
         * Writes a list of supported file types to the indicated output stream, one
         * per line.
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

    def __reduce__(self, LoaderFileTypeRegistry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __reduce__(LoaderFileTypeRegistry self)
        """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
        '__doc__': '/**\n * This class maintains the set of all known LoaderFileTypes in the universe.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE298690>'
        '__reduce__': None, # (!) real value is "<method '__reduce__' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFCFE298690>)>'
        'getNumTypes': None, # (!) real value is "<method 'getNumTypes' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
        'getType': None, # (!) real value is "<method 'getType' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
        'getTypeFromExtension': None, # (!) real value is "<method 'getTypeFromExtension' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
        'getTypes': None, # (!) real value is "<method 'getTypes' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFCFE298690>)>'
        'get_num_types': None, # (!) real value is "<method 'get_num_types' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
        'get_type': None, # (!) real value is "<method 'get_type' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
        'get_type_from_extension': None, # (!) real value is "<method 'get_type_from_extension' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
        'get_types': None, # (!) real value is "<method 'get_types' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
        'registerDeferredType': None, # (!) real value is "<method 'registerDeferredType' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
        'registerType': None, # (!) real value is "<method 'registerType' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
        'register_deferred_type': None, # (!) real value is "<method 'register_deferred_type' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
        'register_type': None, # (!) real value is "<method 'register_type' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
        'types': None, # (!) real value is "<attribute 'types' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
        'unregisterType': None, # (!) real value is "<method 'unregisterType' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
        'unregister_type': None, # (!) real value is "<method 'unregister_type' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.LoaderFileTypeRegistry' objects>"
    }


