# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class PNMFileTypeRegistry(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class maintains the set of all known PNMFileTypes in the universe.
     */
    """
    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns a pointer to the global PNMFileTypeRegistry object.
         */
        """
        pass

    def getNumTypes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_types(PNMFileTypeRegistry self)
        
        /**
         * Returns the total number of types registered.
         */
        """
        pass

    def getType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_type(PNMFileTypeRegistry self, int n)
        
        /**
         * Returns the nth type registered.
         */
        """
        pass

    def getTypeByHandle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_type_by_handle(PNMFileTypeRegistry self, TypeHandle handle)
        
        /**
         * Returns the PNMFileType instance stored in the registry for the given
         * TypeHandle, e.g.  as retrieved by a previous call to get_type() on the type
         * instance.
         */
        """
        pass

    def getTypeFromExtension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_type_from_extension(PNMFileTypeRegistry self, str filename)
        
        /**
         * Tries to determine what the PNMFileType is likely to be for a particular
         * image file based on its extension.  Returns a suitable PNMFileType pointer,
         * or NULL if no type can be determined.
         */
        """
        pass

    def getTypeFromMagicNumber(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_type_from_magic_number(PNMFileTypeRegistry self, str magic_number)
        
        /**
         * Tries to determine what the PNMFileType is likely to be for a particular
         * image file based on its magic number, the first two bytes read from the
         * file.  Returns a suitable PNMFileType pointer, or NULL if no type can be
         * determined.
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
         * Returns a pointer to the global PNMFileTypeRegistry object.
         */
        """
        pass

    def get_num_types(self, PNMFileTypeRegistry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_types(PNMFileTypeRegistry self)
        
        /**
         * Returns the total number of types registered.
         */
        """
        pass

    def get_type(self, PNMFileTypeRegistry_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_type(PNMFileTypeRegistry self, int n)
        
        /**
         * Returns the nth type registered.
         */
        """
        pass

    def get_types(self, *args, **kwargs): # real signature unknown
        pass

    def get_type_by_handle(self, PNMFileTypeRegistry_self, TypeHandle_handle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_type_by_handle(PNMFileTypeRegistry self, TypeHandle handle)
        
        /**
         * Returns the PNMFileType instance stored in the registry for the given
         * TypeHandle, e.g.  as retrieved by a previous call to get_type() on the type
         * instance.
         */
        """
        pass

    def get_type_from_extension(self, PNMFileTypeRegistry_self, str_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_type_from_extension(PNMFileTypeRegistry self, str filename)
        
        /**
         * Tries to determine what the PNMFileType is likely to be for a particular
         * image file based on its extension.  Returns a suitable PNMFileType pointer,
         * or NULL if no type can be determined.
         */
        """
        pass

    def get_type_from_magic_number(self, PNMFileTypeRegistry_self, str_magic_number): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_type_from_magic_number(PNMFileTypeRegistry self, str magic_number)
        
        /**
         * Tries to determine what the PNMFileType is likely to be for a particular
         * image file based on its magic number, the first two bytes read from the
         * file.  Returns a suitable PNMFileType pointer, or NULL if no type can be
         * determined.
         */
        """
        pass

    def write(self, PNMFileTypeRegistry_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(PNMFileTypeRegistry self, ostream out, int indent_level)
        
        /**
         * Writes a list of supported image file types to the indicated output stream,
         * one per line.
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

    types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.PNMFileTypeRegistry' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.PNMFileTypeRegistry' objects>"
        '__doc__': '/**\n * This class maintains the set of all known PNMFileTypes in the universe.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PNMFileTypeRegistry' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE355780>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.PNMFileTypeRegistry' objects>"
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFCFE355780>)>'
        'getNumTypes': None, # (!) real value is "<method 'getNumTypes' of 'panda3d.core.PNMFileTypeRegistry' objects>"
        'getType': None, # (!) real value is "<method 'getType' of 'panda3d.core.PNMFileTypeRegistry' objects>"
        'getTypeByHandle': None, # (!) real value is "<method 'getTypeByHandle' of 'panda3d.core.PNMFileTypeRegistry' objects>"
        'getTypeFromExtension': None, # (!) real value is "<method 'getTypeFromExtension' of 'panda3d.core.PNMFileTypeRegistry' objects>"
        'getTypeFromMagicNumber': None, # (!) real value is "<method 'getTypeFromMagicNumber' of 'panda3d.core.PNMFileTypeRegistry' objects>"
        'getTypes': None, # (!) real value is "<method 'getTypes' of 'panda3d.core.PNMFileTypeRegistry' objects>"
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFCFE355780>)>'
        'get_num_types': None, # (!) real value is "<method 'get_num_types' of 'panda3d.core.PNMFileTypeRegistry' objects>"
        'get_type': None, # (!) real value is "<method 'get_type' of 'panda3d.core.PNMFileTypeRegistry' objects>"
        'get_type_by_handle': None, # (!) real value is "<method 'get_type_by_handle' of 'panda3d.core.PNMFileTypeRegistry' objects>"
        'get_type_from_extension': None, # (!) real value is "<method 'get_type_from_extension' of 'panda3d.core.PNMFileTypeRegistry' objects>"
        'get_type_from_magic_number': None, # (!) real value is "<method 'get_type_from_magic_number' of 'panda3d.core.PNMFileTypeRegistry' objects>"
        'get_types': None, # (!) real value is "<method 'get_types' of 'panda3d.core.PNMFileTypeRegistry' objects>"
        'types': None, # (!) real value is "<attribute 'types' of 'panda3d.core.PNMFileTypeRegistry' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.PNMFileTypeRegistry' objects>"
    }


