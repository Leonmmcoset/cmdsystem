# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ConfigVariableBase import ConfigVariableBase

class ConfigVariableSearchPath(ConfigVariableBase):
    """
    /**
     * This is similar to a ConfigVariableList, but it returns its list as a
     * DSearchPath, as a list of directories.
     *
     * You may locally append directories to the end of the search path with the
     * methods here, or prepend them to the beginning.  Use these methods to make
     * adjustments to the path; do not attempt to directly modify the const
     * DSearchPath object returned by get_value().
     *
     * Unlike other ConfigVariable types, local changes (made by calling
     * append_directory() and prepend_directory()) are specific to this particular
     * instance of the ConfigVariableSearchPath.  A separate instance of the same
     * variable, created by using the same name to the constructor, will not
     * reflect the local changes.
     */
    """
    def appendDirectory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        append_directory(const ConfigVariableSearchPath self, const Filename directory)
        
        /**
         * Adds a new directory to the end of the search list.
         */
        """
        pass

    def appendPath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        append_path(const ConfigVariableSearchPath self, str path, str separator)
        
        /**
         * Adds all of the directories listed in the search path to the end of the
         * search list.
         */
        
        /**
         * Adds all of the directories listed in the search path to the end of the
         * search list.
         */
        """
        pass

    def append_directory(self, const_ConfigVariableSearchPath_self, const_Filename_directory): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        append_directory(const ConfigVariableSearchPath self, const Filename directory)
        
        /**
         * Adds a new directory to the end of the search list.
         */
        """
        pass

    def append_path(self, const_ConfigVariableSearchPath_self, str_path, str_separator): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        append_path(const ConfigVariableSearchPath self, str path, str separator)
        
        /**
         * Adds all of the directories listed in the search path to the end of the
         * search list.
         */
        
        /**
         * Adds all of the directories listed in the search path to the end of the
         * search list.
         */
        """
        pass

    def clear(self, const_ConfigVariableSearchPath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const ConfigVariableSearchPath self)
        
        /**
         * Removes all the directories locally added to the search list, and restores
         * it to its original form.
         */
        """
        pass

    def clearLocalValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_local_value(const ConfigVariableSearchPath self)
        
        /**
         * Removes all the directories locally added to the search list, and restores
         * it to its original form.
         */
        """
        pass

    def clear_local_value(self, const_ConfigVariableSearchPath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_local_value(const ConfigVariableSearchPath self)
        
        /**
         * Removes all the directories locally added to the search list, and restores
         * it to its original form.
         */
        """
        pass

    def findAllFiles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_all_files(ConfigVariableSearchPath self, const Filename filename)
        find_all_files(ConfigVariableSearchPath self, const Filename filename, Results results)
        
        /**
         * Searches all the directories in the search list for the indicated file, in
         * order.  Fills up the results list with *all* of the matching filenames
         * found, if any.  Returns the number of matches found.
         *
         * It is the responsibility of the the caller to clear the results list first;
         * otherwise, the newly-found files will be appended to the list.
         */
        
        /**
         * This variant of find_all_files() returns the new Results object, instead of
         * filling on in on the parameter list.  This is a little more convenient to
         * call from Python.
         */
        """
        pass

    def findFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_file(ConfigVariableSearchPath self, const Filename filename)
        
        /**
         * Searches all the directories in the search list for the indicated file, in
         * order.  Returns the full matching pathname of the first match if found, or
         * the empty string if not found.
         */
        """
        pass

    def find_all_files(self, ConfigVariableSearchPath_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_all_files(ConfigVariableSearchPath self, const Filename filename)
        find_all_files(ConfigVariableSearchPath self, const Filename filename, Results results)
        
        /**
         * Searches all the directories in the search list for the indicated file, in
         * order.  Fills up the results list with *all* of the matching filenames
         * found, if any.  Returns the number of matches found.
         *
         * It is the responsibility of the the caller to clear the results list first;
         * otherwise, the newly-found files will be appended to the list.
         */
        
        /**
         * This variant of find_all_files() returns the new Results object, instead of
         * filling on in on the parameter list.  This is a little more convenient to
         * call from Python.
         */
        """
        pass

    def find_file(self, ConfigVariableSearchPath_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_file(ConfigVariableSearchPath self, const Filename filename)
        
        /**
         * Searches all the directories in the search list for the indicated file, in
         * order.  Returns the full matching pathname of the first match if found, or
         * the empty string if not found.
         */
        """
        pass

    def getDefaultValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_value(ConfigVariableSearchPath self)
        
        /**
         *
         */
        """
        pass

    def getDirectories(self, *args, **kwargs): # real signature unknown
        pass

    def getDirectory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_directory(ConfigVariableSearchPath self, int n)
        
        /**
         * Returns the nth directory on the search list.
         */
        """
        pass

    def getNumDirectories(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_directories(ConfigVariableSearchPath self)
        
        /**
         * Returns the number of directories on the search list.
         */
        """
        pass

    def getValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value(ConfigVariableSearchPath self)
        
        /**
         *
         */
        """
        pass

    def get_default_value(self, ConfigVariableSearchPath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_value(ConfigVariableSearchPath self)
        
        /**
         *
         */
        """
        pass

    def get_directories(self, *args, **kwargs): # real signature unknown
        pass

    def get_directory(self, ConfigVariableSearchPath_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_directory(ConfigVariableSearchPath self, int n)
        
        /**
         * Returns the nth directory on the search list.
         */
        """
        pass

    def get_num_directories(self, ConfigVariableSearchPath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_directories(ConfigVariableSearchPath self)
        
        /**
         * Returns the number of directories on the search list.
         */
        """
        pass

    def get_value(self, ConfigVariableSearchPath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value(ConfigVariableSearchPath self)
        
        /**
         *
         */
        """
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(ConfigVariableSearchPath self)
        
        /**
         * Returns true if the search list is empty, false otherwise.
         */
        """
        pass

    def is_empty(self, ConfigVariableSearchPath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(ConfigVariableSearchPath self)
        
        /**
         * Returns true if the search list is empty, false otherwise.
         */
        """
        pass

    def operatorTypecastDSearchPath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        operator_typecast_DSearchPath(ConfigVariableSearchPath self)
        """
        pass

    def operator_typecast_DSearchPath(self, ConfigVariableSearchPath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        operator_typecast_DSearchPath(ConfigVariableSearchPath self)
        """
        pass

    def output(self, ConfigVariableSearchPath_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(ConfigVariableSearchPath self, ostream out)
        
        /**
         *
         */
        """
        pass

    def prependDirectory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        prepend_directory(const ConfigVariableSearchPath self, const Filename directory)
        
        /**
         * Adds a new directory to the front of the search list.
         */
        """
        pass

    def prependPath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        prepend_path(const ConfigVariableSearchPath self, const DSearchPath path)
        
        /**
         * Adds all of the directories listed in the search path to the beginning of
         * the search list.
         */
        """
        pass

    def prepend_directory(self, const_ConfigVariableSearchPath_self, const_Filename_directory): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepend_directory(const ConfigVariableSearchPath self, const Filename directory)
        
        /**
         * Adds a new directory to the front of the search list.
         */
        """
        pass

    def prepend_path(self, const_ConfigVariableSearchPath_self, const_DSearchPath_path): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepend_path(const ConfigVariableSearchPath self, const DSearchPath path)
        
        /**
         * Adds all of the directories listed in the search path to the beginning of
         * the search list.
         */
        """
        pass

    def write(self, ConfigVariableSearchPath_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(ConfigVariableSearchPath self, ostream out)
        
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

    default_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    directories = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This is similar to a ConfigVariableList, but it returns its list as a\n * DSearchPath, as a list of directories.\n *\n * You may locally append directories to the end of the search path with the\n * methods here, or prepend them to the beginning.  Use these methods to make\n * adjustments to the path; do not attempt to directly modify the const\n * DSearchPath object returned by get_value().\n *\n * Unlike other ConfigVariable types, local changes (made by calling\n * append_directory() and prepend_directory()) are specific to this particular\n * instance of the ConfigVariableSearchPath.  A separate instance of the same\n * variable, created by using the same name to the constructor, will not\n * reflect the local changes.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE263BE0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'appendDirectory': None, # (!) real value is "<method 'appendDirectory' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'appendPath': None, # (!) real value is "<method 'appendPath' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'append_directory': None, # (!) real value is "<method 'append_directory' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'append_path': None, # (!) real value is "<method 'append_path' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'clearLocalValue': None, # (!) real value is "<method 'clearLocalValue' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'clear_local_value': None, # (!) real value is "<method 'clear_local_value' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'default_value': None, # (!) real value is "<attribute 'default_value' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'directories': None, # (!) real value is "<attribute 'directories' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'findAllFiles': None, # (!) real value is "<method 'findAllFiles' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'findFile': None, # (!) real value is "<method 'findFile' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'find_all_files': None, # (!) real value is "<method 'find_all_files' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'find_file': None, # (!) real value is "<method 'find_file' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'getDefaultValue': None, # (!) real value is "<method 'getDefaultValue' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'getDirectories': None, # (!) real value is "<method 'getDirectories' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'getDirectory': None, # (!) real value is "<method 'getDirectory' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'getNumDirectories': None, # (!) real value is "<method 'getNumDirectories' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'getValue': None, # (!) real value is "<method 'getValue' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'get_default_value': None, # (!) real value is "<method 'get_default_value' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'get_directories': None, # (!) real value is "<method 'get_directories' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'get_directory': None, # (!) real value is "<method 'get_directory' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'get_num_directories': None, # (!) real value is "<method 'get_num_directories' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'get_value': None, # (!) real value is "<method 'get_value' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'operatorTypecastDSearchPath': None, # (!) real value is "<method 'operatorTypecastDSearchPath' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'operator_typecast_DSearchPath': None, # (!) real value is "<method 'operator_typecast_DSearchPath' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'prependDirectory': None, # (!) real value is "<method 'prependDirectory' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'prependPath': None, # (!) real value is "<method 'prependPath' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'prepend_directory': None, # (!) real value is "<method 'prepend_directory' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'prepend_path': None, # (!) real value is "<method 'prepend_path' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'value': None, # (!) real value is "<attribute 'value' of 'panda3d.core.ConfigVariableSearchPath' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.ConfigVariableSearchPath' objects>"
    }


