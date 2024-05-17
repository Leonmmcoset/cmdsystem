# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class GlobPattern(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class can be used to test for string matches against standard Unix-
     * shell filename globbing conventions.  It serves as a portable standin for
     * the Posix fnmatch() call.
     *
     * A GlobPattern is given a pattern string, which can contain operators like
     * *, ?, and [].  Then it can be tested against any number of candidate
     * strings; for each candidate, it will indicate whether the string matches
     * the pattern or not.  It can be used, for example, to scan a directory for
     * all files matching a particular pattern.
     */
    """
    def assign(self, const_GlobPattern_self, const_GlobPattern_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const GlobPattern self, const GlobPattern copy)
        """
        pass

    def getCaseSensitive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_case_sensitive(GlobPattern self)
        
        /**
         * Returns whether the match is case sensitive (true) or case insensitive
         * (false).  The default is case sensitive.
         */
        """
        pass

    def getConstPrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_const_prefix(GlobPattern self)
        
        /**
         * Returns the initial part of the pattern before the first glob character.
         * Since many glob patterns begin with a sequence of static characters and end
         * with one or more glob characters, this can be used to optimized searches
         * through sorted indices.
         */
        """
        pass

    def getNomatchChars(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_nomatch_chars(GlobPattern self)
        
        /**
         * Returns the set of characters that are not matched by * or ?.
         */
        """
        pass

    def getPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pattern(GlobPattern self)
        
        /**
         * Returns the pattern string that the GlobPattern object matches.
         */
        """
        pass

    def get_case_sensitive(self, GlobPattern_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_case_sensitive(GlobPattern self)
        
        /**
         * Returns whether the match is case sensitive (true) or case insensitive
         * (false).  The default is case sensitive.
         */
        """
        pass

    def get_const_prefix(self, GlobPattern_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_const_prefix(GlobPattern self)
        
        /**
         * Returns the initial part of the pattern before the first glob character.
         * Since many glob patterns begin with a sequence of static characters and end
         * with one or more glob characters, this can be used to optimized searches
         * through sorted indices.
         */
        """
        pass

    def get_nomatch_chars(self, GlobPattern_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_nomatch_chars(GlobPattern self)
        
        /**
         * Returns the set of characters that are not matched by * or ?.
         */
        """
        pass

    def get_pattern(self, GlobPattern_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pattern(GlobPattern self)
        
        /**
         * Returns the pattern string that the GlobPattern object matches.
         */
        """
        pass

    def hasGlobCharacters(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_glob_characters(GlobPattern self)
        
        /**
         * Returns true if the pattern includes any special globbing characters, or
         * false if it is just a literal string.
         */
        """
        pass

    def has_glob_characters(self, GlobPattern_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_glob_characters(GlobPattern self)
        
        /**
         * Returns true if the pattern includes any special globbing characters, or
         * false if it is just a literal string.
         */
        """
        pass

    def matches(self, GlobPattern_self, str_candidate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        matches(GlobPattern self, str candidate)
        
        /**
         * Returns true if the candidate string matches the pattern, false otherwise.
         */
        """
        pass

    def matchesFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        matches_file(GlobPattern self, Filename candidate)
        
        /**
         * Treats the GlobPattern as a filename pattern, and returns true if the given
         * filename matches the pattern.  Unlike matches(), this will not match slash
         * characters for single asterisk characters, and it will ignore path
         * components that only contain a dot.
         */
        """
        pass

    def matches_file(self, GlobPattern_self, Filename_candidate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        matches_file(GlobPattern self, Filename candidate)
        
        /**
         * Treats the GlobPattern as a filename pattern, and returns true if the given
         * filename matches the pattern.  Unlike matches(), this will not match slash
         * characters for single asterisk characters, and it will ignore path
         * components that only contain a dot.
         */
        """
        pass

    def matchFiles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        match_files(GlobPattern self, const Filename cwd)
        
        /**
         * Treats the GlobPattern as a filename pattern, and returns a list of any
         * actual files that match the pattern.  This is the behavior of the standard
         * Posix glob() function.  Any part of the filename may contain glob
         * characters, including intermediate directory names.
         *
         * If cwd is specified, it is the directory that relative filenames are taken
         * to be relative to; otherwise, the actual current working directory is
         * assumed.
         *
         * The return value is the number of files matched, which are added to the
         * results vector.
         */
        """
        pass

    def match_files(self, GlobPattern_self, const_Filename_cwd): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        match_files(GlobPattern self, const Filename cwd)
        
        /**
         * Treats the GlobPattern as a filename pattern, and returns a list of any
         * actual files that match the pattern.  This is the behavior of the standard
         * Posix glob() function.  Any part of the filename may contain glob
         * characters, including intermediate directory names.
         *
         * If cwd is specified, it is the directory that relative filenames are taken
         * to be relative to; otherwise, the actual current working directory is
         * assumed.
         *
         * The return value is the number of files matched, which are added to the
         * results vector.
         */
        """
        pass

    def output(self, GlobPattern_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(GlobPattern self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setCaseSensitive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_case_sensitive(const GlobPattern self, bool case_sensitive)
        
        /**
         * Sets whether the match is case sensitive (true) or case insensitive
         * (false).  The default is case sensitive.
         */
        """
        pass

    def setNomatchChars(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_nomatch_chars(const GlobPattern self, str nomatch_chars)
        
        /**
         * Specifies a set of characters that are not matched by * or ?.
         */
        """
        pass

    def setPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pattern(const GlobPattern self, str pattern)
        
        /**
         * Changes the pattern string that the GlobPattern object matches.
         */
        """
        pass

    def set_case_sensitive(self, const_GlobPattern_self, bool_case_sensitive): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_case_sensitive(const GlobPattern self, bool case_sensitive)
        
        /**
         * Sets whether the match is case sensitive (true) or case insensitive
         * (false).  The default is case sensitive.
         */
        """
        pass

    def set_nomatch_chars(self, const_GlobPattern_self, str_nomatch_chars): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_nomatch_chars(const GlobPattern self, str nomatch_chars)
        
        /**
         * Specifies a set of characters that are not matched by * or ?.
         */
        """
        pass

    def set_pattern(self, const_GlobPattern_self, str_pattern): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pattern(const GlobPattern self, str pattern)
        
        /**
         * Changes the pattern string that the GlobPattern object matches.
         */
        """
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

    case_sensitive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nomatch_chars = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pattern = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.GlobPattern' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.GlobPattern' objects>"
        '__doc__': '/**\n * This class can be used to test for string matches against standard Unix-\n * shell filename globbing conventions.  It serves as a portable standin for\n * the Posix fnmatch() call.\n *\n * A GlobPattern is given a pattern string, which can contain operators like\n * *, ?, and [].  Then it can be tested against any number of candidate\n * strings; for each candidate, it will indicate whether the string matches\n * the pattern or not.  It can be used, for example, to scan a directory for\n * all files matching a particular pattern.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.GlobPattern' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.GlobPattern' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.GlobPattern' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.GlobPattern' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GlobPattern' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.GlobPattern' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.GlobPattern' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.GlobPattern' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE25C330>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.GlobPattern' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.GlobPattern' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.GlobPattern' objects>"
        'case_sensitive': None, # (!) real value is "<attribute 'case_sensitive' of 'panda3d.core.GlobPattern' objects>"
        'getCaseSensitive': None, # (!) real value is "<method 'getCaseSensitive' of 'panda3d.core.GlobPattern' objects>"
        'getConstPrefix': None, # (!) real value is "<method 'getConstPrefix' of 'panda3d.core.GlobPattern' objects>"
        'getNomatchChars': None, # (!) real value is "<method 'getNomatchChars' of 'panda3d.core.GlobPattern' objects>"
        'getPattern': None, # (!) real value is "<method 'getPattern' of 'panda3d.core.GlobPattern' objects>"
        'get_case_sensitive': None, # (!) real value is "<method 'get_case_sensitive' of 'panda3d.core.GlobPattern' objects>"
        'get_const_prefix': None, # (!) real value is "<method 'get_const_prefix' of 'panda3d.core.GlobPattern' objects>"
        'get_nomatch_chars': None, # (!) real value is "<method 'get_nomatch_chars' of 'panda3d.core.GlobPattern' objects>"
        'get_pattern': None, # (!) real value is "<method 'get_pattern' of 'panda3d.core.GlobPattern' objects>"
        'hasGlobCharacters': None, # (!) real value is "<method 'hasGlobCharacters' of 'panda3d.core.GlobPattern' objects>"
        'has_glob_characters': None, # (!) real value is "<method 'has_glob_characters' of 'panda3d.core.GlobPattern' objects>"
        'matchFiles': None, # (!) real value is "<method 'matchFiles' of 'panda3d.core.GlobPattern' objects>"
        'match_files': None, # (!) real value is "<method 'match_files' of 'panda3d.core.GlobPattern' objects>"
        'matches': None, # (!) real value is "<method 'matches' of 'panda3d.core.GlobPattern' objects>"
        'matchesFile': None, # (!) real value is "<method 'matchesFile' of 'panda3d.core.GlobPattern' objects>"
        'matches_file': None, # (!) real value is "<method 'matches_file' of 'panda3d.core.GlobPattern' objects>"
        'nomatch_chars': None, # (!) real value is "<attribute 'nomatch_chars' of 'panda3d.core.GlobPattern' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.GlobPattern' objects>"
        'pattern': None, # (!) real value is "<attribute 'pattern' of 'panda3d.core.GlobPattern' objects>"
        'setCaseSensitive': None, # (!) real value is "<method 'setCaseSensitive' of 'panda3d.core.GlobPattern' objects>"
        'setNomatchChars': None, # (!) real value is "<method 'setNomatchChars' of 'panda3d.core.GlobPattern' objects>"
        'setPattern': None, # (!) real value is "<method 'setPattern' of 'panda3d.core.GlobPattern' objects>"
        'set_case_sensitive': None, # (!) real value is "<method 'set_case_sensitive' of 'panda3d.core.GlobPattern' objects>"
        'set_nomatch_chars': None, # (!) real value is "<method 'set_nomatch_chars' of 'panda3d.core.GlobPattern' objects>"
        'set_pattern': None, # (!) real value is "<method 'set_pattern' of 'panda3d.core.GlobPattern' objects>"
    }


