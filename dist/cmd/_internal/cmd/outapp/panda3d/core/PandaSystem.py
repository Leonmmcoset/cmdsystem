# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class PandaSystem(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class is used as a namespace to group several global properties of
     * Panda.  Application developers can use this class to query the runtime
     * version or capabilities of the current Panda environment.
     */
    """
    def addSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_system(const PandaSystem self, str system)
        
        /**
         * Intended for use by each subsystem to register itself at startup.
         */
        """
        pass

    def add_system(self, const_PandaSystem_self, str_system): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_system(const PandaSystem self, str system)
        
        /**
         * Intended for use by each subsystem to register itself at startup.
         */
        """
        pass

    def getBuildDate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_build_date()
        
        /**
         * Returns a string representing the date and time at which this version of
         * Panda (or at least dtool) was compiled, if available.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCompiler(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_compiler()
        
        /**
         * Returns a string representing the compiler that was used to generate this
         * version of Panda, if it is available, or "unknown" if it is not.
         */
        """
        pass

    def getDistributor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_distributor()
        
        /**
         * Returns the string defined by the distributor of this version of Panda, or
         * "homebuilt" if this version was built directly from the sources by the end-
         * user.  This is a completely arbitrary string.
         */
        """
        pass

    def getGitCommit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_git_commit()
        
        /**
         * Returns a string representing the git commit hash that this source tree is
         * based on, or the empty string if it has not been specified at build time.
         */
        """
        pass

    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns the global PandaSystem object.
         */
        """
        pass

    def getMajorVersion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_major_version()
        
        /**
         * Returns the major version number of the current version of Panda.  This is
         * the first number of the dotted triple returned by get_version_string().  It
         * changes very rarely.
         */
        """
        pass

    def getMemoryAlignment(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_memory_alignment()
        
        /**
         * Returns the memory alignment that Panda's allocators are using.
         */
        """
        pass

    def getMinorVersion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_minor_version()
        
        /**
         * Returns the minor version number of the current version of Panda.  This is
         * the second number of the dotted triple returned by get_version_string().
         * It changes with each release that introduces new features.
         */
        """
        pass

    def getNumSystems(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_systems(PandaSystem self)
        
        /**
         * Returns the number of Panda subsystems that have registered themselves.
         * This can be used with get_system() to iterate through the entire list of
         * available Panda subsystems.
         */
        """
        pass

    def getP3dCoreapiVersionString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_p3d_coreapi_version_string()
        
        /**
         * Returns the current version of Panda's Core API, expressed as a string of
         * dot-delimited integers.  There are usually four integers in this version,
         * but this is not guaranteed.
         *
         * The Core API is used during the runtime (plugin) environment only.  This
         * may be the empty string if the current version of Panda is not built to
         * provide a particular Core API, which will be the normal case in a
         * development SDK.  However, you should not use this method to determine
         * whether you are running in a runtime environment or not.
         */
        """
        pass

    def getPackageHostUrl(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_package_host_url()
        
        /**
         * Returns the URL of the download server that provides the Panda3D
         * distributable package currently running.  This can be used, along with the
         * get_package_version_string(), to uniquely identify the running version of
         * Panda among distributable Panda versions.
         *
         * See get_package_version_string() for more information.
         *
         * This string is set explicitly at compilation time.  Normally, it should be
         * set to a nonempty string only when building a Panda3D package for
         * distribution.
         */
        """
        pass

    def getPackageVersionString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_package_version_string()
        
        /**
         * Returns the version of the Panda3D distributable package that provides this
         * build of Panda.
         *
         * When the currently-executing version of Panda was loaded from a
         * distributable package, such as via the browser plugin, then this string
         * will be nonempty and will contain the corresponding version string.  You
         * can build applications that use this particular version of Panda by
         * requesting it in the pdef file, using "panda3d", this version string, and
         * the download host provided by get_package_host_url().
         *
         * If this string is empty, then the currently-executing Panda was built
         * independently, and is not part of a distributable package.
         *
         * This string is set explicitly at compilation time.  Normally, it should be
         * set to a nonempty string only when building a Panda3D package for
         * distribution.
         */
        """
        pass

    def getPlatform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_platform()
        
        /**
         * Returns a string representing the runtime platform that we are currently
         * running on.  This will be something like "win32" or "osx_i386" or
         * "linux_amd64".
         */
        """
        pass

    def getSequenceVersion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sequence_version()
        
        /**
         * Returns the sequence version number of the current version of Panda.  This
         * is the third number of the dotted triple returned by get_version_string().
         * It changes with bugfix updates and very minor feature updates.
         */
        """
        pass

    def getSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_system(PandaSystem self, int n)
        
        /**
         * Returns the nth Panda subsystem that has registered itself.  This list will
         * be sorted in alphabetical order.
         */
        """
        pass

    def getSystems(self, *args, **kwargs): # real signature unknown
        pass

    def getSystemTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_system_tag(PandaSystem self, str system, str tag)
        
        /**
         * Returns the value associated with the indicated tag for the given system.
         * This provides a standard way to query each subsystem's advertised
         * capabilities.  The set of tags and values are per-system and
         * implementation-defined.
         *
         * The return value is the empty string if the indicated system is undefined
         * or if does not define the indicated tag.
         */
        """
        pass

    def getVersionString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_version_string()
        
        /**
         * Returns the current version of Panda, expressed as a string, e.g.  "1.0.0".
         * The string will end in the letter "c" if this build does not represent an
         * official version.
         */
        """
        pass

    def get_build_date(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_build_date()
        
        /**
         * Returns a string representing the date and time at which this version of
         * Panda (or at least dtool) was compiled, if available.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_compiler(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_compiler()
        
        /**
         * Returns a string representing the compiler that was used to generate this
         * version of Panda, if it is available, or "unknown" if it is not.
         */
        """
        pass

    def get_distributor(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_distributor()
        
        /**
         * Returns the string defined by the distributor of this version of Panda, or
         * "homebuilt" if this version was built directly from the sources by the end-
         * user.  This is a completely arbitrary string.
         */
        """
        pass

    def get_git_commit(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_git_commit()
        
        /**
         * Returns a string representing the git commit hash that this source tree is
         * based on, or the empty string if it has not been specified at build time.
         */
        """
        pass

    def get_global_ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns the global PandaSystem object.
         */
        """
        pass

    def get_major_version(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_major_version()
        
        /**
         * Returns the major version number of the current version of Panda.  This is
         * the first number of the dotted triple returned by get_version_string().  It
         * changes very rarely.
         */
        """
        pass

    def get_memory_alignment(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_memory_alignment()
        
        /**
         * Returns the memory alignment that Panda's allocators are using.
         */
        """
        pass

    def get_minor_version(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_minor_version()
        
        /**
         * Returns the minor version number of the current version of Panda.  This is
         * the second number of the dotted triple returned by get_version_string().
         * It changes with each release that introduces new features.
         */
        """
        pass

    def get_num_systems(self, PandaSystem_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_systems(PandaSystem self)
        
        /**
         * Returns the number of Panda subsystems that have registered themselves.
         * This can be used with get_system() to iterate through the entire list of
         * available Panda subsystems.
         */
        """
        pass

    def get_p3d_coreapi_version_string(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_p3d_coreapi_version_string()
        
        /**
         * Returns the current version of Panda's Core API, expressed as a string of
         * dot-delimited integers.  There are usually four integers in this version,
         * but this is not guaranteed.
         *
         * The Core API is used during the runtime (plugin) environment only.  This
         * may be the empty string if the current version of Panda is not built to
         * provide a particular Core API, which will be the normal case in a
         * development SDK.  However, you should not use this method to determine
         * whether you are running in a runtime environment or not.
         */
        """
        pass

    def get_package_host_url(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_package_host_url()
        
        /**
         * Returns the URL of the download server that provides the Panda3D
         * distributable package currently running.  This can be used, along with the
         * get_package_version_string(), to uniquely identify the running version of
         * Panda among distributable Panda versions.
         *
         * See get_package_version_string() for more information.
         *
         * This string is set explicitly at compilation time.  Normally, it should be
         * set to a nonempty string only when building a Panda3D package for
         * distribution.
         */
        """
        pass

    def get_package_version_string(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_package_version_string()
        
        /**
         * Returns the version of the Panda3D distributable package that provides this
         * build of Panda.
         *
         * When the currently-executing version of Panda was loaded from a
         * distributable package, such as via the browser plugin, then this string
         * will be nonempty and will contain the corresponding version string.  You
         * can build applications that use this particular version of Panda by
         * requesting it in the pdef file, using "panda3d", this version string, and
         * the download host provided by get_package_host_url().
         *
         * If this string is empty, then the currently-executing Panda was built
         * independently, and is not part of a distributable package.
         *
         * This string is set explicitly at compilation time.  Normally, it should be
         * set to a nonempty string only when building a Panda3D package for
         * distribution.
         */
        """
        pass

    def get_platform(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_platform()
        
        /**
         * Returns a string representing the runtime platform that we are currently
         * running on.  This will be something like "win32" or "osx_i386" or
         * "linux_amd64".
         */
        """
        pass

    def get_sequence_version(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sequence_version()
        
        /**
         * Returns the sequence version number of the current version of Panda.  This
         * is the third number of the dotted triple returned by get_version_string().
         * It changes with bugfix updates and very minor feature updates.
         */
        """
        pass

    def get_system(self, PandaSystem_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_system(PandaSystem self, int n)
        
        /**
         * Returns the nth Panda subsystem that has registered itself.  This list will
         * be sorted in alphabetical order.
         */
        """
        pass

    def get_systems(self, *args, **kwargs): # real signature unknown
        pass

    def get_system_tag(self, PandaSystem_self, str_system, str_tag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_system_tag(PandaSystem self, str system, str tag)
        
        /**
         * Returns the value associated with the indicated tag for the given system.
         * This provides a standard way to query each subsystem's advertised
         * capabilities.  The set of tags and values are per-system and
         * implementation-defined.
         *
         * The return value is the empty string if the indicated system is undefined
         * or if does not define the indicated tag.
         */
        """
        pass

    def get_version_string(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_version_string()
        
        /**
         * Returns the current version of Panda, expressed as a string, e.g.  "1.0.0".
         * The string will end in the letter "c" if this build does not represent an
         * official version.
         */
        """
        pass

    def hasSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_system(PandaSystem self, str system)
        
        /**
         * Returns true if the current version of Panda claims to have the indicated
         * subsystem installed, false otherwise.  The set of available subsystems is
         * implementation defined.
         */
        """
        pass

    def has_system(self, PandaSystem_self, str_system): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_system(PandaSystem self, str system)
        
        /**
         * Returns true if the current version of Panda claims to have the indicated
         * subsystem installed, false otherwise.  The set of available subsystems is
         * implementation defined.
         */
        """
        pass

    def heapTrim(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        heap_trim(const PandaSystem self, int pad)
        
        /**
         * Attempts to release memory back to the system, if possible.  The pad
         * argument is the minimum amount of unused memory to keep in the heap
         * (against future allocations).  Any memory above that may be released to the
         * system, reducing the memory size of this process.  There is no guarantee
         * that any memory may be released.
         *
         * Returns true if any memory was actually released, false otherwise.
         */
        """
        pass

    def heap_trim(self, const_PandaSystem_self, int_pad): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        heap_trim(const PandaSystem self, int pad)
        
        /**
         * Attempts to release memory back to the system, if possible.  The pad
         * argument is the minimum amount of unused memory to keep in the heap
         * (against future allocations).  Any memory above that may be released to the
         * system, reducing the memory size of this process.  There is no guarantee
         * that any memory may be released.
         *
         * Returns true if any memory was actually released, false otherwise.
         */
        """
        pass

    def isOfficialVersion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_official_version()
        
        /**
         * Returns true if current version of Panda claims to be an "official"
         * version, that is, one that was compiled by an official distributor of Panda
         * using a specific version of the panda source tree.  If this is true, there
         * will not be a "c" at the end of the version string returned by
         * get_version_string().
         *
         * Note that we must take the distributor's word for it here.
         */
        """
        pass

    def is_official_version(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_official_version()
        
        /**
         * Returns true if current version of Panda claims to be an "official"
         * version, that is, one that was compiled by an official distributor of Panda
         * using a specific version of the panda source tree.  If this is true, there
         * will not be a "c" at the end of the version string returned by
         * get_version_string().
         *
         * Note that we must take the distributor's word for it here.
         */
        """
        pass

    def output(self, PandaSystem_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(PandaSystem self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setSystemTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_system_tag(const PandaSystem self, str system, str tag, str value)
        
        /**
         * Intended for use by each subsystem to register its set of capabilities at
         * startup.
         */
        """
        pass

    def set_system_tag(self, const_PandaSystem_self, str_system, str_tag, str_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_system_tag(const PandaSystem self, str system, str tag, str value)
        
        /**
         * Intended for use by each subsystem to register its set of capabilities at
         * startup.
         */
        """
        pass

    def write(self, PandaSystem_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(PandaSystem self, ostream out)
        
        /**
         *
         */
        """
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

    systems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    build_date = 'Jan  8 2024 13:54:48'
    compiler = 'MSC v.1900 64 bit (AMD64)'
    distributor = 'cmu'
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This class is used as a namespace to group several global properties of\n * Panda.  Application developers can use this class to query the runtime\n * version or capabilities of the current Panda environment.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PandaSystem' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE25BBF0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.PandaSystem' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.PandaSystem' objects>"
        'addSystem': None, # (!) real value is "<method 'addSystem' of 'panda3d.core.PandaSystem' objects>"
        'add_system': None, # (!) real value is "<method 'add_system' of 'panda3d.core.PandaSystem' objects>"
        'build_date': None, # (!) real value is "<attribute 'build_date' of 'panda3d.core.PandaSystem'>"
        'compiler': None, # (!) real value is "<attribute 'compiler' of 'panda3d.core.PandaSystem'>"
        'distributor': None, # (!) real value is "<attribute 'distributor' of 'panda3d.core.PandaSystem'>"
        'getBuildDate': None, # (!) real value is '<staticmethod(<built-in method getBuildDate of type object at 0x00007FFCFE25BBF0>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE25BBF0>)>'
        'getCompiler': None, # (!) real value is '<staticmethod(<built-in method getCompiler of type object at 0x00007FFCFE25BBF0>)>'
        'getDistributor': None, # (!) real value is '<staticmethod(<built-in method getDistributor of type object at 0x00007FFCFE25BBF0>)>'
        'getGitCommit': None, # (!) real value is '<staticmethod(<built-in method getGitCommit of type object at 0x00007FFCFE25BBF0>)>'
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFCFE25BBF0>)>'
        'getMajorVersion': None, # (!) real value is '<staticmethod(<built-in method getMajorVersion of type object at 0x00007FFCFE25BBF0>)>'
        'getMemoryAlignment': None, # (!) real value is '<staticmethod(<built-in method getMemoryAlignment of type object at 0x00007FFCFE25BBF0>)>'
        'getMinorVersion': None, # (!) real value is '<staticmethod(<built-in method getMinorVersion of type object at 0x00007FFCFE25BBF0>)>'
        'getNumSystems': None, # (!) real value is "<method 'getNumSystems' of 'panda3d.core.PandaSystem' objects>"
        'getP3dCoreapiVersionString': None, # (!) real value is '<staticmethod(<built-in method getP3dCoreapiVersionString of type object at 0x00007FFCFE25BBF0>)>'
        'getPackageHostUrl': None, # (!) real value is '<staticmethod(<built-in method getPackageHostUrl of type object at 0x00007FFCFE25BBF0>)>'
        'getPackageVersionString': None, # (!) real value is '<staticmethod(<built-in method getPackageVersionString of type object at 0x00007FFCFE25BBF0>)>'
        'getPlatform': None, # (!) real value is '<staticmethod(<built-in method getPlatform of type object at 0x00007FFCFE25BBF0>)>'
        'getSequenceVersion': None, # (!) real value is '<staticmethod(<built-in method getSequenceVersion of type object at 0x00007FFCFE25BBF0>)>'
        'getSystem': None, # (!) real value is "<method 'getSystem' of 'panda3d.core.PandaSystem' objects>"
        'getSystemTag': None, # (!) real value is "<method 'getSystemTag' of 'panda3d.core.PandaSystem' objects>"
        'getSystems': None, # (!) real value is "<method 'getSystems' of 'panda3d.core.PandaSystem' objects>"
        'getVersionString': None, # (!) real value is '<staticmethod(<built-in method getVersionString of type object at 0x00007FFCFE25BBF0>)>'
        'get_build_date': None, # (!) real value is '<staticmethod(<built-in method get_build_date of type object at 0x00007FFCFE25BBF0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE25BBF0>)>'
        'get_compiler': None, # (!) real value is '<staticmethod(<built-in method get_compiler of type object at 0x00007FFCFE25BBF0>)>'
        'get_distributor': None, # (!) real value is '<staticmethod(<built-in method get_distributor of type object at 0x00007FFCFE25BBF0>)>'
        'get_git_commit': None, # (!) real value is '<staticmethod(<built-in method get_git_commit of type object at 0x00007FFCFE25BBF0>)>'
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFCFE25BBF0>)>'
        'get_major_version': None, # (!) real value is '<staticmethod(<built-in method get_major_version of type object at 0x00007FFCFE25BBF0>)>'
        'get_memory_alignment': None, # (!) real value is '<staticmethod(<built-in method get_memory_alignment of type object at 0x00007FFCFE25BBF0>)>'
        'get_minor_version': None, # (!) real value is '<staticmethod(<built-in method get_minor_version of type object at 0x00007FFCFE25BBF0>)>'
        'get_num_systems': None, # (!) real value is "<method 'get_num_systems' of 'panda3d.core.PandaSystem' objects>"
        'get_p3d_coreapi_version_string': None, # (!) real value is '<staticmethod(<built-in method get_p3d_coreapi_version_string of type object at 0x00007FFCFE25BBF0>)>'
        'get_package_host_url': None, # (!) real value is '<staticmethod(<built-in method get_package_host_url of type object at 0x00007FFCFE25BBF0>)>'
        'get_package_version_string': None, # (!) real value is '<staticmethod(<built-in method get_package_version_string of type object at 0x00007FFCFE25BBF0>)>'
        'get_platform': None, # (!) real value is '<staticmethod(<built-in method get_platform of type object at 0x00007FFCFE25BBF0>)>'
        'get_sequence_version': None, # (!) real value is '<staticmethod(<built-in method get_sequence_version of type object at 0x00007FFCFE25BBF0>)>'
        'get_system': None, # (!) real value is "<method 'get_system' of 'panda3d.core.PandaSystem' objects>"
        'get_system_tag': None, # (!) real value is "<method 'get_system_tag' of 'panda3d.core.PandaSystem' objects>"
        'get_systems': None, # (!) real value is "<method 'get_systems' of 'panda3d.core.PandaSystem' objects>"
        'get_version_string': None, # (!) real value is '<staticmethod(<built-in method get_version_string of type object at 0x00007FFCFE25BBF0>)>'
        'git_commit': None, # (!) real value is "<attribute 'git_commit' of 'panda3d.core.PandaSystem'>"
        'hasSystem': None, # (!) real value is "<method 'hasSystem' of 'panda3d.core.PandaSystem' objects>"
        'has_system': None, # (!) real value is "<method 'has_system' of 'panda3d.core.PandaSystem' objects>"
        'heapTrim': None, # (!) real value is "<method 'heapTrim' of 'panda3d.core.PandaSystem' objects>"
        'heap_trim': None, # (!) real value is "<method 'heap_trim' of 'panda3d.core.PandaSystem' objects>"
        'isOfficialVersion': None, # (!) real value is '<staticmethod(<built-in method isOfficialVersion of type object at 0x00007FFCFE25BBF0>)>'
        'is_official_version': None, # (!) real value is '<staticmethod(<built-in method is_official_version of type object at 0x00007FFCFE25BBF0>)>'
        'major_version': None, # (!) real value is "<attribute 'major_version' of 'panda3d.core.PandaSystem'>"
        'memory_alignment': None, # (!) real value is "<attribute 'memory_alignment' of 'panda3d.core.PandaSystem'>"
        'minor_version': None, # (!) real value is "<attribute 'minor_version' of 'panda3d.core.PandaSystem'>"
        'official_version': None, # (!) real value is "<attribute 'official_version' of 'panda3d.core.PandaSystem'>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.PandaSystem' objects>"
        'platform': None, # (!) real value is "<attribute 'platform' of 'panda3d.core.PandaSystem'>"
        'sequence_version': None, # (!) real value is "<attribute 'sequence_version' of 'panda3d.core.PandaSystem'>"
        'setSystemTag': None, # (!) real value is "<method 'setSystemTag' of 'panda3d.core.PandaSystem' objects>"
        'set_system_tag': None, # (!) real value is "<method 'set_system_tag' of 'panda3d.core.PandaSystem' objects>"
        'systems': None, # (!) real value is "<attribute 'systems' of 'panda3d.core.PandaSystem' objects>"
        'version_string': None, # (!) real value is "<attribute 'version_string' of 'panda3d.core.PandaSystem'>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.PandaSystem' objects>"
    }
    git_commit = '8e539bd99840da261853c08bc426e0ea43bddd24'
    major_version = 1
    memory_alignment = 16
    minor_version = 10
    official_version = True
    platform = 'win_amd64'
    sequence_version = 14
    version_string = '1.10.14'


