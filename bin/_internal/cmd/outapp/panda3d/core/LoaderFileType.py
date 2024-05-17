# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedObject import TypedObject

class LoaderFileType(TypedObject):
    """
    /**
     * This is the base class for a family of scene-graph file types that the
     * Loader supports.  Each kind of loader that's available should define a
     * corresponding LoaderFileType object and register itself.
     */
    """
    def getAdditionalExtensions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_additional_extensions(LoaderFileType self)
        
        /**
         * Returns a space-separated list of extension, in addition to the one
         * returned by get_extension(), that are recognized by this loader.
         */
        """
        pass

    def getAllowDiskCache(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_allow_disk_cache(LoaderFileType self, const LoaderOptions options)
        
        /**
         * Returns true if the loader flags allow retrieving the model from the on-
         * disk bam cache (if it is enabled), false otherwise.
         */
        """
        pass

    def getAllowRamCache(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_allow_ram_cache(LoaderFileType self, const LoaderOptions options)
        
        /**
         * Returns true if the loader flags allow retrieving the model from the in-
         * memory ModelPool cache, false otherwise.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getExtension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_extension(LoaderFileType self)
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(LoaderFileType self)
        """
        pass

    def get_additional_extensions(self, LoaderFileType_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_additional_extensions(LoaderFileType self)
        
        /**
         * Returns a space-separated list of extension, in addition to the one
         * returned by get_extension(), that are recognized by this loader.
         */
        """
        pass

    def get_allow_disk_cache(self, LoaderFileType_self, const_LoaderOptions_options): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_allow_disk_cache(LoaderFileType self, const LoaderOptions options)
        
        /**
         * Returns true if the loader flags allow retrieving the model from the on-
         * disk bam cache (if it is enabled), false otherwise.
         */
        """
        pass

    def get_allow_ram_cache(self, LoaderFileType_self, const_LoaderOptions_options): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_allow_ram_cache(LoaderFileType self, const LoaderOptions options)
        
        /**
         * Returns true if the loader flags allow retrieving the model from the in-
         * memory ModelPool cache, false otherwise.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_extension(self, LoaderFileType_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_extension(LoaderFileType self)
        """
        pass

    def get_name(self, LoaderFileType_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(LoaderFileType self)
        """
        pass

    def supportsCompressed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        supports_compressed(LoaderFileType self)
        
        /**
         * Returns true if this file type can transparently load compressed files
         * (with a .pz or .gz extension), false otherwise.
         */
        """
        pass

    def supportsLoad(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        supports_load(LoaderFileType self)
        
        /**
         * Returns true if the file type can be used to load files, and load_file() is
         * supported.  Returns false if load_file() is unimplemented and will always
         * fail.
         */
        """
        pass

    def supportsSave(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        supports_save(LoaderFileType self)
        
        /**
         * Returns true if the file type can be used to save files, and save_file() is
         * supported.  Returns false if save_file() is unimplemented and will always
         * fail.
         */
        """
        pass

    def supports_compressed(self, LoaderFileType_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        supports_compressed(LoaderFileType self)
        
        /**
         * Returns true if this file type can transparently load compressed files
         * (with a .pz or .gz extension), false otherwise.
         */
        """
        pass

    def supports_load(self, LoaderFileType_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        supports_load(LoaderFileType self)
        
        /**
         * Returns true if the file type can be used to load files, and load_file() is
         * supported.  Returns false if load_file() is unimplemented and will always
         * fail.
         */
        """
        pass

    def supports_save(self, LoaderFileType_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        supports_save(LoaderFileType self)
        
        /**
         * Returns true if the file type can be used to save files, and save_file() is
         * supported.  Returns false if save_file() is unimplemented and will always
         * fail.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * This is the base class for a family of scene-graph file types that the\n * Loader supports.  Each kind of loader that's available should define a\n * corresponding LoaderFileType object and register itself.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LoaderFileType' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2984C0>'
        'getAdditionalExtensions': None, # (!) real value is "<method 'getAdditionalExtensions' of 'panda3d.core.LoaderFileType' objects>"
        'getAllowDiskCache': None, # (!) real value is "<method 'getAllowDiskCache' of 'panda3d.core.LoaderFileType' objects>"
        'getAllowRamCache': None, # (!) real value is "<method 'getAllowRamCache' of 'panda3d.core.LoaderFileType' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2984C0>)>'
        'getExtension': None, # (!) real value is "<method 'getExtension' of 'panda3d.core.LoaderFileType' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.LoaderFileType' objects>"
        'get_additional_extensions': None, # (!) real value is "<method 'get_additional_extensions' of 'panda3d.core.LoaderFileType' objects>"
        'get_allow_disk_cache': None, # (!) real value is "<method 'get_allow_disk_cache' of 'panda3d.core.LoaderFileType' objects>"
        'get_allow_ram_cache': None, # (!) real value is "<method 'get_allow_ram_cache' of 'panda3d.core.LoaderFileType' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2984C0>)>'
        'get_extension': None, # (!) real value is "<method 'get_extension' of 'panda3d.core.LoaderFileType' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.LoaderFileType' objects>"
        'supportsCompressed': None, # (!) real value is "<method 'supportsCompressed' of 'panda3d.core.LoaderFileType' objects>"
        'supportsLoad': None, # (!) real value is "<method 'supportsLoad' of 'panda3d.core.LoaderFileType' objects>"
        'supportsSave': None, # (!) real value is "<method 'supportsSave' of 'panda3d.core.LoaderFileType' objects>"
        'supports_compressed': None, # (!) real value is "<method 'supports_compressed' of 'panda3d.core.LoaderFileType' objects>"
        'supports_load': None, # (!) real value is "<method 'supports_load' of 'panda3d.core.LoaderFileType' objects>"
        'supports_save': None, # (!) real value is "<method 'supports_save' of 'panda3d.core.LoaderFileType' objects>"
    }


