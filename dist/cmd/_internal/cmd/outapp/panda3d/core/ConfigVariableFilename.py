# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ConfigVariable import ConfigVariable

class ConfigVariableFilename(ConfigVariable):
    """
    /**
     * This is a convenience class to specialize ConfigVariable as a Filename
     * type.  It is almost the same thing as ConfigVariableString, except it
     * handles an implicit Filename::expand_from() operation so that the user may
     * put OS-specific filenames, or filenames based on environment variables, in
     * the prc file.
     */
    """
    def assign(self, const_ConfigVariableFilename_self, const_Filename_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const ConfigVariableFilename self, const Filename value)
        """
        pass

    def cStr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        c_str(ConfigVariableFilename self)
        
        // These methods help the ConfigVariableFilename act like a Filename object.
        
        /**
         *
         */
        """
        pass

    def c_str(self, ConfigVariableFilename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        c_str(ConfigVariableFilename self)
        
        // These methods help the ConfigVariableFilename act like a Filename object.
        
        /**
         *
         */
        """
        pass

    def empty(self, ConfigVariableFilename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        empty(ConfigVariableFilename self)
        
        /**
         *
         */
        """
        pass

    def Fspath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        __fspath__(ConfigVariableFilename self)
        
        /**
         * Allows a ConfigVariableFilename object to be passed to any Python function
         * that accepts an os.PathLike object.
         *
         * @since 1.10.13
         */
        """
        pass

    def getBasename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_basename(ConfigVariableFilename self)
        
        /**
         * Returns the basename part of the filename.  This is everything in the
         * filename after the rightmost slash, including any extensions.
         */
        """
        pass

    def getBasenameWoExtension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_basename_wo_extension(ConfigVariableFilename self)
        
        /**
         * Returns the basename part of the filename, without the file extension.
         */
        """
        pass

    def getDefaultValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_value(ConfigVariableFilename self)
        
        /**
         * Returns the variable's default value.
         */
        """
        pass

    def getDirname(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_dirname(ConfigVariableFilename self)
        
        /**
         * Returns the directory part of the filename.  This is everything in the
         * filename up to, but not including the rightmost slash.
         */
        """
        pass

    def getExtension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_extension(ConfigVariableFilename self)
        
        /**
         * Returns the file extension.  This is everything after the rightmost dot, if
         * there is one, or the empty string if there is not.
         */
        """
        pass

    def getFullpath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fullpath(ConfigVariableFilename self)
        
        /**
         * Returns the entire filename: directory, basename, extension.  This is the
         * same thing returned by the string typecast operator, so this function is a
         * little redundant.
         */
        """
        pass

    def getFullpathWoExtension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fullpath_wo_extension(ConfigVariableFilename self)
        
        /**
         * Returns the full filename--directory and basename parts--except for the
         * extension.
         */
        """
        pass

    def getValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value(ConfigVariableFilename self)
        
        /**
         * Returns the variable's value.
         */
        """
        pass

    def getWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_word(ConfigVariableFilename self, int n)
        
        /**
         * Returns the variable's nth value.
         */
        """
        pass

    def get_basename(self, ConfigVariableFilename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_basename(ConfigVariableFilename self)
        
        /**
         * Returns the basename part of the filename.  This is everything in the
         * filename after the rightmost slash, including any extensions.
         */
        """
        pass

    def get_basename_wo_extension(self, ConfigVariableFilename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_basename_wo_extension(ConfigVariableFilename self)
        
        /**
         * Returns the basename part of the filename, without the file extension.
         */
        """
        pass

    def get_default_value(self, ConfigVariableFilename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_value(ConfigVariableFilename self)
        
        /**
         * Returns the variable's default value.
         */
        """
        pass

    def get_dirname(self, ConfigVariableFilename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_dirname(ConfigVariableFilename self)
        
        /**
         * Returns the directory part of the filename.  This is everything in the
         * filename up to, but not including the rightmost slash.
         */
        """
        pass

    def get_extension(self, ConfigVariableFilename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_extension(ConfigVariableFilename self)
        
        /**
         * Returns the file extension.  This is everything after the rightmost dot, if
         * there is one, or the empty string if there is not.
         */
        """
        pass

    def get_fullpath(self, ConfigVariableFilename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fullpath(ConfigVariableFilename self)
        
        /**
         * Returns the entire filename: directory, basename, extension.  This is the
         * same thing returned by the string typecast operator, so this function is a
         * little redundant.
         */
        """
        pass

    def get_fullpath_wo_extension(self, ConfigVariableFilename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fullpath_wo_extension(ConfigVariableFilename self)
        
        /**
         * Returns the full filename--directory and basename parts--except for the
         * extension.
         */
        """
        pass

    def get_value(self, ConfigVariableFilename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value(ConfigVariableFilename self)
        
        /**
         * Returns the variable's value.
         */
        """
        pass

    def get_word(self, ConfigVariableFilename_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_word(ConfigVariableFilename self, int n)
        
        /**
         * Returns the variable's nth value.
         */
        """
        pass

    def length(self, ConfigVariableFilename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        length(ConfigVariableFilename self)
        
        /**
         *
         */
        """
        pass

    def operatorTypecast(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        operator_typecast(ConfigVariableFilename self)
        """
        pass

    def operator_typecast(self, ConfigVariableFilename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        operator_typecast(ConfigVariableFilename self)
        """
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_value(const ConfigVariableFilename self, const Filename value)
        
        /**
         * Reassigns the variable's local value.
         */
        """
        pass

    def setWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_word(const ConfigVariableFilename self, int n, const Filename value)
        
        /**
         * Reassigns the variable's nth value.  This makes a local copy of the
         * variable's overall value.
         */
        """
        pass

    def set_value(self, const_ConfigVariableFilename_self, const_Filename_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_value(const ConfigVariableFilename self, const Filename value)
        
        /**
         * Reassigns the variable's local value.
         */
        """
        pass

    def set_word(self, const_ConfigVariableFilename_self, int_n, const_Filename_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_word(const ConfigVariableFilename self, int n, const Filename value)
        
        /**
         * Reassigns the variable's nth value.  This makes a local copy of the
         * variable's overall value.
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

    def __fspath__(self, ConfigVariableFilename_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __fspath__(ConfigVariableFilename self)
        
        /**
         * Allows a ConfigVariableFilename object to be passed to any Python function
         * that accepts an os.PathLike object.
         *
         * @since 1.10.13
         */
        """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
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

    default_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'Fspath': None, # (!) real value is "<method 'Fspath' of 'panda3d.core.ConfigVariableFilename' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ConfigVariableFilename' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ConfigVariableFilename' objects>"
        '__doc__': '/**\n * This is a convenience class to specialize ConfigVariable as a Filename\n * type.  It is almost the same thing as ConfigVariableString, except it\n * handles an implicit Filename::expand_from() operation so that the user may\n * put OS-specific filenames, or filenames based on environment variables, in\n * the prc file.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.ConfigVariableFilename' objects>"
        '__fspath__': None, # (!) real value is "<method '__fspath__' of 'panda3d.core.ConfigVariableFilename' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.ConfigVariableFilename' objects>"
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.core.ConfigVariableFilename' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.ConfigVariableFilename' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.ConfigVariableFilename' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ConfigVariableFilename' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.ConfigVariableFilename' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.ConfigVariableFilename' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.ConfigVariableFilename' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2634A0>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.ConfigVariableFilename' objects>"
        'cStr': None, # (!) real value is "<method 'cStr' of 'panda3d.core.ConfigVariableFilename' objects>"
        'c_str': None, # (!) real value is "<method 'c_str' of 'panda3d.core.ConfigVariableFilename' objects>"
        'default_value': None, # (!) real value is "<attribute 'default_value' of 'panda3d.core.ConfigVariableFilename' objects>"
        'empty': None, # (!) real value is "<method 'empty' of 'panda3d.core.ConfigVariableFilename' objects>"
        'getBasename': None, # (!) real value is "<method 'getBasename' of 'panda3d.core.ConfigVariableFilename' objects>"
        'getBasenameWoExtension': None, # (!) real value is "<method 'getBasenameWoExtension' of 'panda3d.core.ConfigVariableFilename' objects>"
        'getDefaultValue': None, # (!) real value is "<method 'getDefaultValue' of 'panda3d.core.ConfigVariableFilename' objects>"
        'getDirname': None, # (!) real value is "<method 'getDirname' of 'panda3d.core.ConfigVariableFilename' objects>"
        'getExtension': None, # (!) real value is "<method 'getExtension' of 'panda3d.core.ConfigVariableFilename' objects>"
        'getFullpath': None, # (!) real value is "<method 'getFullpath' of 'panda3d.core.ConfigVariableFilename' objects>"
        'getFullpathWoExtension': None, # (!) real value is "<method 'getFullpathWoExtension' of 'panda3d.core.ConfigVariableFilename' objects>"
        'getValue': None, # (!) real value is "<method 'getValue' of 'panda3d.core.ConfigVariableFilename' objects>"
        'getWord': None, # (!) real value is "<method 'getWord' of 'panda3d.core.ConfigVariableFilename' objects>"
        'get_basename': None, # (!) real value is "<method 'get_basename' of 'panda3d.core.ConfigVariableFilename' objects>"
        'get_basename_wo_extension': None, # (!) real value is "<method 'get_basename_wo_extension' of 'panda3d.core.ConfigVariableFilename' objects>"
        'get_default_value': None, # (!) real value is "<method 'get_default_value' of 'panda3d.core.ConfigVariableFilename' objects>"
        'get_dirname': None, # (!) real value is "<method 'get_dirname' of 'panda3d.core.ConfigVariableFilename' objects>"
        'get_extension': None, # (!) real value is "<method 'get_extension' of 'panda3d.core.ConfigVariableFilename' objects>"
        'get_fullpath': None, # (!) real value is "<method 'get_fullpath' of 'panda3d.core.ConfigVariableFilename' objects>"
        'get_fullpath_wo_extension': None, # (!) real value is "<method 'get_fullpath_wo_extension' of 'panda3d.core.ConfigVariableFilename' objects>"
        'get_value': None, # (!) real value is "<method 'get_value' of 'panda3d.core.ConfigVariableFilename' objects>"
        'get_word': None, # (!) real value is "<method 'get_word' of 'panda3d.core.ConfigVariableFilename' objects>"
        'length': None, # (!) real value is "<method 'length' of 'panda3d.core.ConfigVariableFilename' objects>"
        'operatorTypecast': None, # (!) real value is "<method 'operatorTypecast' of 'panda3d.core.ConfigVariableFilename' objects>"
        'operator_typecast': None, # (!) real value is "<method 'operator_typecast' of 'panda3d.core.ConfigVariableFilename' objects>"
        'setValue': None, # (!) real value is "<method 'setValue' of 'panda3d.core.ConfigVariableFilename' objects>"
        'setWord': None, # (!) real value is "<method 'setWord' of 'panda3d.core.ConfigVariableFilename' objects>"
        'set_value': None, # (!) real value is "<method 'set_value' of 'panda3d.core.ConfigVariableFilename' objects>"
        'set_word': None, # (!) real value is "<method 'set_word' of 'panda3d.core.ConfigVariableFilename' objects>"
        'value': None, # (!) real value is "<attribute 'value' of 'panda3d.core.ConfigVariableFilename' objects>"
    }


