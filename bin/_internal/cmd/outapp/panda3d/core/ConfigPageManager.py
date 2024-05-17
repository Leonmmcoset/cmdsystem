# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ConfigFlags import ConfigFlags

class ConfigPageManager(ConfigFlags):
    """
    /**
     * A global object that maintains the set of ConfigPages everywhere in the
     * world, and keeps them in sorted order.
     */
    """
    def deleteExplicitPage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        delete_explicit_page(const ConfigPageManager self, ConfigPage page)
        
        /**
         * Removes a previously-constructed ConfigPage from the set of active pages,
         * and deletes it.  The ConfigPage object is no longer valid after this call.
         * Returns true if the page is successfully deleted, or false if it was
         * unknown (which should never happen if the page was legitimately
         * constructed).
         */
        """
        pass

    def delete_explicit_page(self, const_ConfigPageManager_self, ConfigPage_page): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        delete_explicit_page(const ConfigPageManager self, ConfigPage page)
        
        /**
         * Removes a previously-constructed ConfigPage from the set of active pages,
         * and deletes it.  The ConfigPage object is no longer valid after this call.
         * Returns true if the page is successfully deleted, or false if it was
         * unknown (which should never happen if the page was legitimately
         * constructed).
         */
        """
        pass

    def getExplicitPage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_explicit_page(ConfigPageManager self, int n)
        
        /**
         * Returns the nth explicit ConfigPage in the world.  See
         * get_num_explicit_pages().
         */
        """
        pass

    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         *
         */
        """
        pass

    def getImplicitPage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_implicit_page(ConfigPageManager self, int n)
        
        /**
         * Returns the nth implicit ConfigPage in the world.  See
         * get_num_implicit_pages().
         */
        """
        pass

    def getNumExplicitPages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_explicit_pages(ConfigPageManager self)
        
        /**
         * Returns the current number of explicitly-loaded ConfigPages in the world.
         * These represent pages that were loaded dynamically at runtime by explicit
         * calls to ConfigPageManager::make_explicit_page().
         */
        """
        pass

    def getNumImplicitPages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_implicit_pages(ConfigPageManager self)
        
        /**
         * Returns the current number of implicitly-loaded ConfigPages in the world.
         * These represent files that were automatically discovered on the disk as
         * .prc files.
         */
        """
        pass

    def getNumPrcEncryptedPatterns(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_prc_encrypted_patterns(ConfigPageManager self)
        
        /**
         * Returns the number of patterns, like `*.pre`, that are compiled in that
         * will be searched for as special config files that are understood to be
         * encrypted.
         */
        """
        pass

    def getNumPrcExecutablePatterns(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_prc_executable_patterns(ConfigPageManager self)
        
        /**
         * Returns the number of patterns, like `*.exe`, that are compiled in that
         * will be searched for as special config files that are to be executed as a
         * program, and their output taken to be input.  This is normally empty.
         */
        """
        pass

    def getNumPrcPatterns(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_prc_patterns(ConfigPageManager self)
        
        /**
         * Returns the number of patterns, like `*.prc`, that are compiled in that
         * will be searched for as default config filenames.  Normally there is only
         * one pattern, and it is `*.prc`, but others may be specified with the
         * PRC_FILENAME variable in Config.pp.
         */
        """
        pass

    def getPrcEncryptedPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_prc_encrypted_pattern(ConfigPageManager self, int n)
        
        /**
         * Returns the nth filename pattern that will be considered a match as a valid
         * encrypted config file.  See get_num_prc_encrypted_patterns().
         */
        """
        pass

    def getPrcExecutablePattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_prc_executable_pattern(ConfigPageManager self, int n)
        
        /**
         * Returns the nth filename pattern that will be considered a match as a valid
         * executable-style config file.  See get_num_prc_executable_patterns().
         */
        """
        pass

    def getPrcPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_prc_pattern(ConfigPageManager self, int n)
        
        /**
         * Returns the nth filename pattern that will be considered a match as a valid
         * config file.  See get_num_prc_patterns().
         */
        """
        pass

    def getSearchPath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_search_path(const ConfigPageManager self)
        
        /**
         * Returns the search path used to locate implicit .prc files.  This is
         * determined by the PRC_DIR and PRC_PATH environment variables.  The object
         * returned by this method may be modified to change the path at runtime, and
         * then reload_implicit_pages() called.
         */
        """
        pass

    def get_explicit_page(self, ConfigPageManager_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_explicit_page(ConfigPageManager self, int n)
        
        /**
         * Returns the nth explicit ConfigPage in the world.  See
         * get_num_explicit_pages().
         */
        """
        pass

    def get_global_ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         *
         */
        """
        pass

    def get_implicit_page(self, ConfigPageManager_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_implicit_page(ConfigPageManager self, int n)
        
        /**
         * Returns the nth implicit ConfigPage in the world.  See
         * get_num_implicit_pages().
         */
        """
        pass

    def get_num_explicit_pages(self, ConfigPageManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_explicit_pages(ConfigPageManager self)
        
        /**
         * Returns the current number of explicitly-loaded ConfigPages in the world.
         * These represent pages that were loaded dynamically at runtime by explicit
         * calls to ConfigPageManager::make_explicit_page().
         */
        """
        pass

    def get_num_implicit_pages(self, ConfigPageManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_implicit_pages(ConfigPageManager self)
        
        /**
         * Returns the current number of implicitly-loaded ConfigPages in the world.
         * These represent files that were automatically discovered on the disk as
         * .prc files.
         */
        """
        pass

    def get_num_prc_encrypted_patterns(self, ConfigPageManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_prc_encrypted_patterns(ConfigPageManager self)
        
        /**
         * Returns the number of patterns, like `*.pre`, that are compiled in that
         * will be searched for as special config files that are understood to be
         * encrypted.
         */
        """
        pass

    def get_num_prc_executable_patterns(self, ConfigPageManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_prc_executable_patterns(ConfigPageManager self)
        
        /**
         * Returns the number of patterns, like `*.exe`, that are compiled in that
         * will be searched for as special config files that are to be executed as a
         * program, and their output taken to be input.  This is normally empty.
         */
        """
        pass

    def get_num_prc_patterns(self, ConfigPageManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_prc_patterns(ConfigPageManager self)
        
        /**
         * Returns the number of patterns, like `*.prc`, that are compiled in that
         * will be searched for as default config filenames.  Normally there is only
         * one pattern, and it is `*.prc`, but others may be specified with the
         * PRC_FILENAME variable in Config.pp.
         */
        """
        pass

    def get_prc_encrypted_pattern(self, ConfigPageManager_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_prc_encrypted_pattern(ConfigPageManager self, int n)
        
        /**
         * Returns the nth filename pattern that will be considered a match as a valid
         * encrypted config file.  See get_num_prc_encrypted_patterns().
         */
        """
        pass

    def get_prc_executable_pattern(self, ConfigPageManager_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_prc_executable_pattern(ConfigPageManager self, int n)
        
        /**
         * Returns the nth filename pattern that will be considered a match as a valid
         * executable-style config file.  See get_num_prc_executable_patterns().
         */
        """
        pass

    def get_prc_pattern(self, ConfigPageManager_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_prc_pattern(ConfigPageManager self, int n)
        
        /**
         * Returns the nth filename pattern that will be considered a match as a valid
         * config file.  See get_num_prc_patterns().
         */
        """
        pass

    def get_search_path(self, const_ConfigPageManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_search_path(const ConfigPageManager self)
        
        /**
         * Returns the search path used to locate implicit .prc files.  This is
         * determined by the PRC_DIR and PRC_PATH environment variables.  The object
         * returned by this method may be modified to change the path at runtime, and
         * then reload_implicit_pages() called.
         */
        """
        pass

    def loadedImplicitPages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        loaded_implicit_pages(ConfigPageManager self)
        
        /**
         * Returns true if the implicit `*.prc` files have already been loaded, false
         * otherwise.  Normally this will only be false briefly before startup.
         */
        """
        pass

    def loaded_implicit_pages(self, ConfigPageManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        loaded_implicit_pages(ConfigPageManager self)
        
        /**
         * Returns true if the implicit `*.prc` files have already been loaded, false
         * otherwise.  Normally this will only be false briefly before startup.
         */
        """
        pass

    def loadImplicitPages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_implicit_pages(const ConfigPageManager self)
        
        /**
         * Searches the PRC_DIR and/or PRC_PATH directories for `*.prc` files and loads
         * them in as pages.  This is normally called automatically at startup time,
         * when the first variable's value is referenced.  See also
         * reload_implicit_pages().
         */
        """
        pass

    def load_implicit_pages(self, const_ConfigPageManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_implicit_pages(const ConfigPageManager self)
        
        /**
         * Searches the PRC_DIR and/or PRC_PATH directories for `*.prc` files and loads
         * them in as pages.  This is normally called automatically at startup time,
         * when the first variable's value is referenced.  See also
         * reload_implicit_pages().
         */
        """
        pass

    def makeExplicitPage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_explicit_page(const ConfigPageManager self, str name)
        
        /**
         * Creates and returns a new, empty ConfigPage.  This page will be stacked on
         * top of any pages that were created before; it may shadow variable
         * declarations that are defined in previous pages.
         */
        """
        pass

    def make_explicit_page(self, const_ConfigPageManager_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_explicit_page(const ConfigPageManager self, str name)
        
        /**
         * Creates and returns a new, empty ConfigPage.  This page will be stacked on
         * top of any pages that were created before; it may shadow variable
         * declarations that are defined in previous pages.
         */
        """
        pass

    def output(self, ConfigPageManager_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(ConfigPageManager self, ostream out)
        
        /**
         *
         */
        """
        pass

    def reloadImplicitPages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reload_implicit_pages(const ConfigPageManager self)
        
        /**
         * Searches the PRC_DIR and/or PRC_PATH directories for *.prc files and loads
         * them in as pages.
         *
         * This may be called after startup, to force the system to re-read all of the
         * implicit prc files.
         */
        """
        pass

    def reload_implicit_pages(self, const_ConfigPageManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reload_implicit_pages(const ConfigPageManager self)
        
        /**
         * Searches the PRC_DIR and/or PRC_PATH directories for *.prc files and loads
         * them in as pages.
         *
         * This may be called after startup, to force the system to re-read all of the
         * implicit prc files.
         */
        """
        pass

    def write(self, ConfigPageManager_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(ConfigPageManager self, ostream out)
        
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

    explicit_pages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    implicit_pages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prc_encrypted_patterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prc_executable_patterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prc_patterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    search_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A global object that maintains the set of ConfigPages everywhere in the\n * world, and keeps them in sorted order.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ConfigPageManager' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2629C0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.ConfigPageManager' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.ConfigPageManager' objects>"
        'deleteExplicitPage': None, # (!) real value is "<method 'deleteExplicitPage' of 'panda3d.core.ConfigPageManager' objects>"
        'delete_explicit_page': None, # (!) real value is "<method 'delete_explicit_page' of 'panda3d.core.ConfigPageManager' objects>"
        'explicit_pages': None, # (!) real value is "<attribute 'explicit_pages' of 'panda3d.core.ConfigPageManager' objects>"
        'getExplicitPage': None, # (!) real value is "<method 'getExplicitPage' of 'panda3d.core.ConfigPageManager' objects>"
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFCFE2629C0>)>'
        'getImplicitPage': None, # (!) real value is "<method 'getImplicitPage' of 'panda3d.core.ConfigPageManager' objects>"
        'getNumExplicitPages': None, # (!) real value is "<method 'getNumExplicitPages' of 'panda3d.core.ConfigPageManager' objects>"
        'getNumImplicitPages': None, # (!) real value is "<method 'getNumImplicitPages' of 'panda3d.core.ConfigPageManager' objects>"
        'getNumPrcEncryptedPatterns': None, # (!) real value is "<method 'getNumPrcEncryptedPatterns' of 'panda3d.core.ConfigPageManager' objects>"
        'getNumPrcExecutablePatterns': None, # (!) real value is "<method 'getNumPrcExecutablePatterns' of 'panda3d.core.ConfigPageManager' objects>"
        'getNumPrcPatterns': None, # (!) real value is "<method 'getNumPrcPatterns' of 'panda3d.core.ConfigPageManager' objects>"
        'getPrcEncryptedPattern': None, # (!) real value is "<method 'getPrcEncryptedPattern' of 'panda3d.core.ConfigPageManager' objects>"
        'getPrcExecutablePattern': None, # (!) real value is "<method 'getPrcExecutablePattern' of 'panda3d.core.ConfigPageManager' objects>"
        'getPrcPattern': None, # (!) real value is "<method 'getPrcPattern' of 'panda3d.core.ConfigPageManager' objects>"
        'getSearchPath': None, # (!) real value is "<method 'getSearchPath' of 'panda3d.core.ConfigPageManager' objects>"
        'get_explicit_page': None, # (!) real value is "<method 'get_explicit_page' of 'panda3d.core.ConfigPageManager' objects>"
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFCFE2629C0>)>'
        'get_implicit_page': None, # (!) real value is "<method 'get_implicit_page' of 'panda3d.core.ConfigPageManager' objects>"
        'get_num_explicit_pages': None, # (!) real value is "<method 'get_num_explicit_pages' of 'panda3d.core.ConfigPageManager' objects>"
        'get_num_implicit_pages': None, # (!) real value is "<method 'get_num_implicit_pages' of 'panda3d.core.ConfigPageManager' objects>"
        'get_num_prc_encrypted_patterns': None, # (!) real value is "<method 'get_num_prc_encrypted_patterns' of 'panda3d.core.ConfigPageManager' objects>"
        'get_num_prc_executable_patterns': None, # (!) real value is "<method 'get_num_prc_executable_patterns' of 'panda3d.core.ConfigPageManager' objects>"
        'get_num_prc_patterns': None, # (!) real value is "<method 'get_num_prc_patterns' of 'panda3d.core.ConfigPageManager' objects>"
        'get_prc_encrypted_pattern': None, # (!) real value is "<method 'get_prc_encrypted_pattern' of 'panda3d.core.ConfigPageManager' objects>"
        'get_prc_executable_pattern': None, # (!) real value is "<method 'get_prc_executable_pattern' of 'panda3d.core.ConfigPageManager' objects>"
        'get_prc_pattern': None, # (!) real value is "<method 'get_prc_pattern' of 'panda3d.core.ConfigPageManager' objects>"
        'get_search_path': None, # (!) real value is "<method 'get_search_path' of 'panda3d.core.ConfigPageManager' objects>"
        'implicit_pages': None, # (!) real value is "<attribute 'implicit_pages' of 'panda3d.core.ConfigPageManager' objects>"
        'loadImplicitPages': None, # (!) real value is "<method 'loadImplicitPages' of 'panda3d.core.ConfigPageManager' objects>"
        'load_implicit_pages': None, # (!) real value is "<method 'load_implicit_pages' of 'panda3d.core.ConfigPageManager' objects>"
        'loadedImplicitPages': None, # (!) real value is "<method 'loadedImplicitPages' of 'panda3d.core.ConfigPageManager' objects>"
        'loaded_implicit_pages': None, # (!) real value is "<method 'loaded_implicit_pages' of 'panda3d.core.ConfigPageManager' objects>"
        'makeExplicitPage': None, # (!) real value is "<method 'makeExplicitPage' of 'panda3d.core.ConfigPageManager' objects>"
        'make_explicit_page': None, # (!) real value is "<method 'make_explicit_page' of 'panda3d.core.ConfigPageManager' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.ConfigPageManager' objects>"
        'prc_encrypted_patterns': None, # (!) real value is "<attribute 'prc_encrypted_patterns' of 'panda3d.core.ConfigPageManager' objects>"
        'prc_executable_patterns': None, # (!) real value is "<attribute 'prc_executable_patterns' of 'panda3d.core.ConfigPageManager' objects>"
        'prc_patterns': None, # (!) real value is "<attribute 'prc_patterns' of 'panda3d.core.ConfigPageManager' objects>"
        'reloadImplicitPages': None, # (!) real value is "<method 'reloadImplicitPages' of 'panda3d.core.ConfigPageManager' objects>"
        'reload_implicit_pages': None, # (!) real value is "<method 'reload_implicit_pages' of 'panda3d.core.ConfigPageManager' objects>"
        'search_path': None, # (!) real value is "<attribute 'search_path' of 'panda3d.core.ConfigPageManager' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.ConfigPageManager' objects>"
    }


