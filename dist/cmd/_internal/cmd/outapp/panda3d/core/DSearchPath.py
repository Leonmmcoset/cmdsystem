# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class DSearchPath(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class stores a list of directories that can be searched, in order, to
     * locate a particular file.  It is normally constructed by passing it a
     * traditional searchpath-style string, e.g.  a list of directory names
     * delimited by spaces or colons, but it can also be built up explicitly.
     */
    """
    def appendDirectory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        append_directory(const DSearchPath self, const Filename directory)
        
        /**
         * Adds a new directory to the end of the search list.
         */
        """
        pass

    def appendPath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        append_path(const DSearchPath self, str path, str separator)
        
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

    def append_directory(self, const_DSearchPath_self, const_Filename_directory): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        append_directory(const DSearchPath self, const Filename directory)
        
        /**
         * Adds a new directory to the end of the search list.
         */
        """
        pass

    def append_path(self, const_DSearchPath_self, str_path, str_separator): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        append_path(const DSearchPath self, str path, str separator)
        
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

    def assign(self, const_DSearchPath_self, const_DSearchPath_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const DSearchPath self, const DSearchPath copy)
        """
        pass

    def clear(self, const_DSearchPath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const DSearchPath self)
        
        /**
         * Removes all the directories from the search list.
         */
        """
        pass

    def findAllFiles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_all_files(DSearchPath self, const Filename filename)
        find_all_files(DSearchPath self, const Filename filename, Results results)
        
        /**
         * This variant of find_all_files() returns the new Results object, instead of
         * filling on in on the parameter list.  This is a little more convenient to
         * call from Python.
         */
        
        /**
         * Searches all the directories in the search list for the indicated file, in
         * order.  Fills up the results list with *all* of the matching filenames
         * found, if any.  Returns the number of matches found.
         *
         * It is the responsibility of the the caller to clear the results list first;
         * otherwise, the newly-found files will be appended to the list.
         */
        """
        pass

    def findFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_file(DSearchPath self, const Filename filename)
        
        /**
         * Searches all the directories in the search list for the indicated file, in
         * order.  Returns the full matching pathname of the first match if found, or
         * the empty string if not found.
         */
        """
        pass

    def find_all_files(self, DSearchPath_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_all_files(DSearchPath self, const Filename filename)
        find_all_files(DSearchPath self, const Filename filename, Results results)
        
        /**
         * This variant of find_all_files() returns the new Results object, instead of
         * filling on in on the parameter list.  This is a little more convenient to
         * call from Python.
         */
        
        /**
         * Searches all the directories in the search list for the indicated file, in
         * order.  Fills up the results list with *all* of the matching filenames
         * found, if any.  Returns the number of matches found.
         *
         * It is the responsibility of the the caller to clear the results list first;
         * otherwise, the newly-found files will be appended to the list.
         */
        """
        pass

    def find_file(self, DSearchPath_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_file(DSearchPath self, const Filename filename)
        
        /**
         * Searches all the directories in the search list for the indicated file, in
         * order.  Returns the full matching pathname of the first match if found, or
         * the empty string if not found.
         */
        """
        pass

    def getDirectories(self, *args, **kwargs): # real signature unknown
        pass

    def getDirectory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_directory(DSearchPath self, int n)
        
        /**
         * Returns the nth directory on the search list.
         */
        """
        pass

    def getNumDirectories(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_directories(DSearchPath self)
        
        /**
         * Returns the number of directories on the search list.
         */
        """
        pass

    def get_directories(self, *args, **kwargs): # real signature unknown
        pass

    def get_directory(self, DSearchPath_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_directory(DSearchPath self, int n)
        
        /**
         * Returns the nth directory on the search list.
         */
        """
        pass

    def get_num_directories(self, DSearchPath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_directories(DSearchPath self)
        
        /**
         * Returns the number of directories on the search list.
         */
        """
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(DSearchPath self)
        
        /**
         * Returns true if the search list is empty, false otherwise.
         */
        """
        pass

    def is_empty(self, DSearchPath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(DSearchPath self)
        
        /**
         * Returns true if the search list is empty, false otherwise.
         */
        """
        pass

    def output(self, DSearchPath_self, ostream_out, str_separator): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(DSearchPath self, ostream out, str separator)
        
        /**
         *
         */
        """
        pass

    def prependDirectory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        prepend_directory(const DSearchPath self, const Filename directory)
        
        /**
         * Adds a new directory to the front of the search list.
         */
        """
        pass

    def prependPath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        prepend_path(const DSearchPath self, const DSearchPath path)
        
        /**
         * Adds all of the directories listed in the search path to the beginning of
         * the search list.
         */
        """
        pass

    def prepend_directory(self, const_DSearchPath_self, const_Filename_directory): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepend_directory(const DSearchPath self, const Filename directory)
        
        /**
         * Adds a new directory to the front of the search list.
         */
        """
        pass

    def prepend_path(self, const_DSearchPath_self, const_DSearchPath_path): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepend_path(const DSearchPath self, const DSearchPath path)
        
        /**
         * Adds all of the directories listed in the search path to the beginning of
         * the search list.
         */
        """
        pass

    def searchPath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        search_path(const Filename filename, str path, str separator)
        
        /**
         * A quick-and-easy way to search a searchpath for a file when you don't feel
         * like building or keeping around a DSearchPath object.  This simply
         * constructs a temporary DSearchPath based on the indicated path string, and
         * searches that.
         */
        """
        pass

    def search_path(self, const_Filename_filename, str_path, str_separator): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        search_path(const Filename filename, str path, str separator)
        
        /**
         * A quick-and-easy way to search a searchpath for a file when you don't feel
         * like building or keeping around a DSearchPath object.  This simply
         * constructs a temporary DSearchPath based on the indicated path string, and
         * searches that.
         */
        """
        pass

    def write(self, DSearchPath_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(DSearchPath self, ostream out, int indent_level)
        
        /**
         *
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    directories = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'Results': None, # (!) real value is "<class 'panda3d.core.Results'>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.DSearchPath' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.DSearchPath' objects>"
        '__doc__': '/**\n * This class stores a list of directories that can be searched, in order, to\n * locate a particular file.  It is normally constructed by passing it a\n * traditional searchpath-style string, e.g.  a list of directory names\n * delimited by spaces or colons, but it can also be built up explicitly.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DSearchPath' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE25BDC0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.DSearchPath' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.DSearchPath' objects>"
        'appendDirectory': None, # (!) real value is "<method 'appendDirectory' of 'panda3d.core.DSearchPath' objects>"
        'appendPath': None, # (!) real value is "<method 'appendPath' of 'panda3d.core.DSearchPath' objects>"
        'append_directory': None, # (!) real value is "<method 'append_directory' of 'panda3d.core.DSearchPath' objects>"
        'append_path': None, # (!) real value is "<method 'append_path' of 'panda3d.core.DSearchPath' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.DSearchPath' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.DSearchPath' objects>"
        'directories': None, # (!) real value is "<attribute 'directories' of 'panda3d.core.DSearchPath' objects>"
        'findAllFiles': None, # (!) real value is "<method 'findAllFiles' of 'panda3d.core.DSearchPath' objects>"
        'findFile': None, # (!) real value is "<method 'findFile' of 'panda3d.core.DSearchPath' objects>"
        'find_all_files': None, # (!) real value is "<method 'find_all_files' of 'panda3d.core.DSearchPath' objects>"
        'find_file': None, # (!) real value is "<method 'find_file' of 'panda3d.core.DSearchPath' objects>"
        'getDirectories': None, # (!) real value is "<method 'getDirectories' of 'panda3d.core.DSearchPath' objects>"
        'getDirectory': None, # (!) real value is "<method 'getDirectory' of 'panda3d.core.DSearchPath' objects>"
        'getNumDirectories': None, # (!) real value is "<method 'getNumDirectories' of 'panda3d.core.DSearchPath' objects>"
        'get_directories': None, # (!) real value is "<method 'get_directories' of 'panda3d.core.DSearchPath' objects>"
        'get_directory': None, # (!) real value is "<method 'get_directory' of 'panda3d.core.DSearchPath' objects>"
        'get_num_directories': None, # (!) real value is "<method 'get_num_directories' of 'panda3d.core.DSearchPath' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.core.DSearchPath' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.core.DSearchPath' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.DSearchPath' objects>"
        'prependDirectory': None, # (!) real value is "<method 'prependDirectory' of 'panda3d.core.DSearchPath' objects>"
        'prependPath': None, # (!) real value is "<method 'prependPath' of 'panda3d.core.DSearchPath' objects>"
        'prepend_directory': None, # (!) real value is "<method 'prepend_directory' of 'panda3d.core.DSearchPath' objects>"
        'prepend_path': None, # (!) real value is "<method 'prepend_path' of 'panda3d.core.DSearchPath' objects>"
        'searchPath': None, # (!) real value is '<staticmethod(<built-in method searchPath of type object at 0x00007FFCFE25BDC0>)>'
        'search_path': None, # (!) real value is '<staticmethod(<built-in method search_path of type object at 0x00007FFCFE25BDC0>)>'
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.DSearchPath' objects>"
    }
    Results = None # (!) real value is "<class 'panda3d.core.Results'>"


