# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ConfigFlags import ConfigFlags

class ConfigDeclaration(ConfigFlags):
    """
    /**
     * A single declaration of a config variable, typically defined as one line in
     * a .prc file, e.g.  "show-frame-rate-meter 1".  This is really just a
     * pairing of a string name (actually, a ConfigVariableCore pointer) to a
     * string value.
     */
    """
    def getBoolWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bool_word(ConfigDeclaration self, int n)
        
        /**
         * Returns the boolean value of the nth word of the declaration's value, or
         * false if there is no nth value.  See also has_bool_word().
         */
        """
        pass

    def getDeclSeq(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_decl_seq(ConfigDeclaration self)
        
        /**
         * Returns the sequence number of the declaration within the page.  Sequence
         * numbers are assigned as each declaration is created; each declaration is
         * given a higher sequence number than all the declarations created in the
         * page before it.
         */
        """
        pass

    def getDoubleWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_double_word(ConfigDeclaration self, int n)
        
        /**
         * Returns the integer value of the nth word of the declaration's value, or 0
         * if there is no nth value.  See also has_double_word().
         */
        """
        pass

    def getFilenameValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_filename_value(ConfigDeclaration self)
        
        /**
         * Interprets the string value as a filename and returns it, with any
         * variables expanded.
         */
        """
        pass

    def getInt64Word(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_int64_word(ConfigDeclaration self, int n)
        
        /**
         * Returns the int64 value of the nth word of the declaration's value, or 0 if
         * there is no nth value.  See also has_int64_word().
         */
        """
        pass

    def getIntWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_int_word(ConfigDeclaration self, int n)
        
        /**
         * Returns the integer value of the nth word of the declaration's value, or 0
         * if there is no nth value.  See also has_int_word().
         */
        """
        pass

    def getNumWords(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_words(ConfigDeclaration self)
        
        /**
         * Returns the number of words in the declaration's value.  A word is defined
         * as a sequence of non-whitespace characters delimited by whitespace.
         */
        """
        pass

    def getPage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_page(ConfigDeclaration self)
        
        /**
         * Returns the page on which this declaration can be found.
         */
        """
        pass

    def getStringValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_string_value(ConfigDeclaration self)
        
        /**
         * Returns the value assigned to this variable.  This is the original one-line
         * text defined for the variable in the .prc file (or passed to
         * ConfigPage::make_declaration()).
         */
        """
        pass

    def getStringWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_string_word(ConfigDeclaration self, int n)
        
        /**
         * Returns the string value of the nth word of the declaration's value, or
         * empty string if there is no nth value.  See also has_string_word().
         */
        """
        pass

    def getVariable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_variable(ConfigDeclaration self)
        
        /**
         * Returns the variable that this declaration names.  This variable may or may
         * not have been defined by the time the declaration is read.
         */
        """
        pass

    def get_bool_word(self, ConfigDeclaration_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bool_word(ConfigDeclaration self, int n)
        
        /**
         * Returns the boolean value of the nth word of the declaration's value, or
         * false if there is no nth value.  See also has_bool_word().
         */
        """
        pass

    def get_decl_seq(self, ConfigDeclaration_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_decl_seq(ConfigDeclaration self)
        
        /**
         * Returns the sequence number of the declaration within the page.  Sequence
         * numbers are assigned as each declaration is created; each declaration is
         * given a higher sequence number than all the declarations created in the
         * page before it.
         */
        """
        pass

    def get_double_word(self, ConfigDeclaration_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_double_word(ConfigDeclaration self, int n)
        
        /**
         * Returns the integer value of the nth word of the declaration's value, or 0
         * if there is no nth value.  See also has_double_word().
         */
        """
        pass

    def get_filename_value(self, ConfigDeclaration_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_filename_value(ConfigDeclaration self)
        
        /**
         * Interprets the string value as a filename and returns it, with any
         * variables expanded.
         */
        """
        pass

    def get_int64_word(self, ConfigDeclaration_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_int64_word(ConfigDeclaration self, int n)
        
        /**
         * Returns the int64 value of the nth word of the declaration's value, or 0 if
         * there is no nth value.  See also has_int64_word().
         */
        """
        pass

    def get_int_word(self, ConfigDeclaration_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_int_word(ConfigDeclaration self, int n)
        
        /**
         * Returns the integer value of the nth word of the declaration's value, or 0
         * if there is no nth value.  See also has_int_word().
         */
        """
        pass

    def get_num_words(self, ConfigDeclaration_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_words(ConfigDeclaration self)
        
        /**
         * Returns the number of words in the declaration's value.  A word is defined
         * as a sequence of non-whitespace characters delimited by whitespace.
         */
        """
        pass

    def get_page(self, ConfigDeclaration_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_page(ConfigDeclaration self)
        
        /**
         * Returns the page on which this declaration can be found.
         */
        """
        pass

    def get_string_value(self, ConfigDeclaration_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_string_value(ConfigDeclaration self)
        
        /**
         * Returns the value assigned to this variable.  This is the original one-line
         * text defined for the variable in the .prc file (or passed to
         * ConfigPage::make_declaration()).
         */
        """
        pass

    def get_string_word(self, ConfigDeclaration_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_string_word(ConfigDeclaration self, int n)
        
        /**
         * Returns the string value of the nth word of the declaration's value, or
         * empty string if there is no nth value.  See also has_string_word().
         */
        """
        pass

    def get_variable(self, ConfigDeclaration_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_variable(ConfigDeclaration self)
        
        /**
         * Returns the variable that this declaration names.  This variable may or may
         * not have been defined by the time the declaration is read.
         */
        """
        pass

    def hasBoolWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_bool_word(ConfigDeclaration self, int n)
        
        /**
         * Returns true if the declaration's value has a valid boolean value for the
         * nth word.
         */
        """
        pass

    def hasDoubleWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_double_word(ConfigDeclaration self, int n)
        
        /**
         * Returns true if the declaration's value has a valid integer value for the
         * nth word.
         */
        """
        pass

    def hasInt64Word(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_int64_word(ConfigDeclaration self, int n)
        
        /**
         * Returns true if the declaration's value has a valid int64 value for the nth
         * word.
         */
        """
        pass

    def hasIntWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_int_word(ConfigDeclaration self, int n)
        
        /**
         * Returns true if the declaration's value has a valid integer value for the
         * nth word.
         */
        """
        pass

    def hasStringWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_string_word(ConfigDeclaration self, int n)
        
        /**
         * Returns true if the declaration's value has a valid string value for the
         * nth word.  This is really the same thing as asking if there are at least n
         * words in the value.
         */
        """
        pass

    def has_bool_word(self, ConfigDeclaration_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_bool_word(ConfigDeclaration self, int n)
        
        /**
         * Returns true if the declaration's value has a valid boolean value for the
         * nth word.
         */
        """
        pass

    def has_double_word(self, ConfigDeclaration_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_double_word(ConfigDeclaration self, int n)
        
        /**
         * Returns true if the declaration's value has a valid integer value for the
         * nth word.
         */
        """
        pass

    def has_int64_word(self, ConfigDeclaration_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_int64_word(ConfigDeclaration self, int n)
        
        /**
         * Returns true if the declaration's value has a valid int64 value for the nth
         * word.
         */
        """
        pass

    def has_int_word(self, ConfigDeclaration_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_int_word(ConfigDeclaration self, int n)
        
        /**
         * Returns true if the declaration's value has a valid integer value for the
         * nth word.
         */
        """
        pass

    def has_string_word(self, ConfigDeclaration_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_string_word(ConfigDeclaration self, int n)
        
        /**
         * Returns true if the declaration's value has a valid string value for the
         * nth word.  This is really the same thing as asking if there are at least n
         * words in the value.
         */
        """
        pass

    def output(self, ConfigDeclaration_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(ConfigDeclaration self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setBoolWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bool_word(const ConfigDeclaration self, int n, bool value)
        
        /**
         * Changes the nth word to the indicated value without affecting the other
         * words.
         */
        """
        pass

    def setDoubleWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_double_word(const ConfigDeclaration self, int n, double value)
        
        /**
         * Changes the nth word to the indicated value without affecting the other
         * words.
         */
        """
        pass

    def setInt64Word(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_int64_word(const ConfigDeclaration self, int n, long value)
        
        /**
         * Changes the nth word to the indicated value without affecting the other
         * words.
         */
        """
        pass

    def setIntWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_int_word(const ConfigDeclaration self, int n, int value)
        
        /**
         * Changes the nth word to the indicated value without affecting the other
         * words.
         */
        """
        pass

    def setStringValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_string_value(const ConfigDeclaration self, str value)
        
        /**
         * Changes the value assigned to this variable.
         */
        """
        pass

    def setStringWord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_string_word(const ConfigDeclaration self, int n, str value)
        
        /**
         * Changes the nth word to the indicated value without affecting the other
         * words.
         */
        """
        pass

    def set_bool_word(self, const_ConfigDeclaration_self, int_n, bool_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bool_word(const ConfigDeclaration self, int n, bool value)
        
        /**
         * Changes the nth word to the indicated value without affecting the other
         * words.
         */
        """
        pass

    def set_double_word(self, const_ConfigDeclaration_self, int_n, double_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_double_word(const ConfigDeclaration self, int n, double value)
        
        /**
         * Changes the nth word to the indicated value without affecting the other
         * words.
         */
        """
        pass

    def set_int64_word(self, const_ConfigDeclaration_self, int_n, long_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_int64_word(const ConfigDeclaration self, int n, long value)
        
        /**
         * Changes the nth word to the indicated value without affecting the other
         * words.
         */
        """
        pass

    def set_int_word(self, const_ConfigDeclaration_self, int_n, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_int_word(const ConfigDeclaration self, int n, int value)
        
        /**
         * Changes the nth word to the indicated value without affecting the other
         * words.
         */
        """
        pass

    def set_string_value(self, const_ConfigDeclaration_self, str_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_string_value(const ConfigDeclaration self, str value)
        
        /**
         * Changes the value assigned to this variable.
         */
        """
        pass

    def set_string_word(self, const_ConfigDeclaration_self, int_n, str_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_string_word(const ConfigDeclaration self, int n, str value)
        
        /**
         * Changes the nth word to the indicated value without affecting the other
         * words.
         */
        """
        pass

    def write(self, ConfigDeclaration_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(ConfigDeclaration self, ostream out)
        
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

    page = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    variable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A single declaration of a config variable, typically defined as one line in\n * a .prc file, e.g.  "show-frame-rate-meter 1".  This is really just a\n * pairing of a string name (actually, a ConfigVariableCore pointer) to a\n * string value.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ConfigDeclaration' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE262450>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.ConfigDeclaration' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.ConfigDeclaration' objects>"
        'getBoolWord': None, # (!) real value is "<method 'getBoolWord' of 'panda3d.core.ConfigDeclaration' objects>"
        'getDeclSeq': None, # (!) real value is "<method 'getDeclSeq' of 'panda3d.core.ConfigDeclaration' objects>"
        'getDoubleWord': None, # (!) real value is "<method 'getDoubleWord' of 'panda3d.core.ConfigDeclaration' objects>"
        'getFilenameValue': None, # (!) real value is "<method 'getFilenameValue' of 'panda3d.core.ConfigDeclaration' objects>"
        'getInt64Word': None, # (!) real value is "<method 'getInt64Word' of 'panda3d.core.ConfigDeclaration' objects>"
        'getIntWord': None, # (!) real value is "<method 'getIntWord' of 'panda3d.core.ConfigDeclaration' objects>"
        'getNumWords': None, # (!) real value is "<method 'getNumWords' of 'panda3d.core.ConfigDeclaration' objects>"
        'getPage': None, # (!) real value is "<method 'getPage' of 'panda3d.core.ConfigDeclaration' objects>"
        'getStringValue': None, # (!) real value is "<method 'getStringValue' of 'panda3d.core.ConfigDeclaration' objects>"
        'getStringWord': None, # (!) real value is "<method 'getStringWord' of 'panda3d.core.ConfigDeclaration' objects>"
        'getVariable': None, # (!) real value is "<method 'getVariable' of 'panda3d.core.ConfigDeclaration' objects>"
        'get_bool_word': None, # (!) real value is "<method 'get_bool_word' of 'panda3d.core.ConfigDeclaration' objects>"
        'get_decl_seq': None, # (!) real value is "<method 'get_decl_seq' of 'panda3d.core.ConfigDeclaration' objects>"
        'get_double_word': None, # (!) real value is "<method 'get_double_word' of 'panda3d.core.ConfigDeclaration' objects>"
        'get_filename_value': None, # (!) real value is "<method 'get_filename_value' of 'panda3d.core.ConfigDeclaration' objects>"
        'get_int64_word': None, # (!) real value is "<method 'get_int64_word' of 'panda3d.core.ConfigDeclaration' objects>"
        'get_int_word': None, # (!) real value is "<method 'get_int_word' of 'panda3d.core.ConfigDeclaration' objects>"
        'get_num_words': None, # (!) real value is "<method 'get_num_words' of 'panda3d.core.ConfigDeclaration' objects>"
        'get_page': None, # (!) real value is "<method 'get_page' of 'panda3d.core.ConfigDeclaration' objects>"
        'get_string_value': None, # (!) real value is "<method 'get_string_value' of 'panda3d.core.ConfigDeclaration' objects>"
        'get_string_word': None, # (!) real value is "<method 'get_string_word' of 'panda3d.core.ConfigDeclaration' objects>"
        'get_variable': None, # (!) real value is "<method 'get_variable' of 'panda3d.core.ConfigDeclaration' objects>"
        'hasBoolWord': None, # (!) real value is "<method 'hasBoolWord' of 'panda3d.core.ConfigDeclaration' objects>"
        'hasDoubleWord': None, # (!) real value is "<method 'hasDoubleWord' of 'panda3d.core.ConfigDeclaration' objects>"
        'hasInt64Word': None, # (!) real value is "<method 'hasInt64Word' of 'panda3d.core.ConfigDeclaration' objects>"
        'hasIntWord': None, # (!) real value is "<method 'hasIntWord' of 'panda3d.core.ConfigDeclaration' objects>"
        'hasStringWord': None, # (!) real value is "<method 'hasStringWord' of 'panda3d.core.ConfigDeclaration' objects>"
        'has_bool_word': None, # (!) real value is "<method 'has_bool_word' of 'panda3d.core.ConfigDeclaration' objects>"
        'has_double_word': None, # (!) real value is "<method 'has_double_word' of 'panda3d.core.ConfigDeclaration' objects>"
        'has_int64_word': None, # (!) real value is "<method 'has_int64_word' of 'panda3d.core.ConfigDeclaration' objects>"
        'has_int_word': None, # (!) real value is "<method 'has_int_word' of 'panda3d.core.ConfigDeclaration' objects>"
        'has_string_word': None, # (!) real value is "<method 'has_string_word' of 'panda3d.core.ConfigDeclaration' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.ConfigDeclaration' objects>"
        'page': None, # (!) real value is "<attribute 'page' of 'panda3d.core.ConfigDeclaration' objects>"
        'setBoolWord': None, # (!) real value is "<method 'setBoolWord' of 'panda3d.core.ConfigDeclaration' objects>"
        'setDoubleWord': None, # (!) real value is "<method 'setDoubleWord' of 'panda3d.core.ConfigDeclaration' objects>"
        'setInt64Word': None, # (!) real value is "<method 'setInt64Word' of 'panda3d.core.ConfigDeclaration' objects>"
        'setIntWord': None, # (!) real value is "<method 'setIntWord' of 'panda3d.core.ConfigDeclaration' objects>"
        'setStringValue': None, # (!) real value is "<method 'setStringValue' of 'panda3d.core.ConfigDeclaration' objects>"
        'setStringWord': None, # (!) real value is "<method 'setStringWord' of 'panda3d.core.ConfigDeclaration' objects>"
        'set_bool_word': None, # (!) real value is "<method 'set_bool_word' of 'panda3d.core.ConfigDeclaration' objects>"
        'set_double_word': None, # (!) real value is "<method 'set_double_word' of 'panda3d.core.ConfigDeclaration' objects>"
        'set_int64_word': None, # (!) real value is "<method 'set_int64_word' of 'panda3d.core.ConfigDeclaration' objects>"
        'set_int_word': None, # (!) real value is "<method 'set_int_word' of 'panda3d.core.ConfigDeclaration' objects>"
        'set_string_value': None, # (!) real value is "<method 'set_string_value' of 'panda3d.core.ConfigDeclaration' objects>"
        'set_string_word': None, # (!) real value is "<method 'set_string_word' of 'panda3d.core.ConfigDeclaration' objects>"
        'variable': None, # (!) real value is "<attribute 'variable' of 'panda3d.core.ConfigDeclaration' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.ConfigDeclaration' objects>"
    }


