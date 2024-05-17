# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ConfigFlags import ConfigFlags

class ConfigVariableCore(ConfigFlags):
    """
    /**
     * The internal definition of a ConfigVariable.  This object is shared between
     * all instances of a ConfigVariable that use the same variable name.
     *
     * You cannot create a ConfigVariableCore instance directly; instead, use the
     * make() method, which may return a shared instance.  Once created, these
     * objects are never destructed.
     */
    """
    def clearLocalValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_local_value(const ConfigVariableCore self)
        
        /**
         * Removes the local value defined for this variable, and allows its value to
         * be once again retrieved from the .prc files.
         *
         * Returns true if the value was successfully removed, false if it did not
         * exist in the first place.
         */
        """
        pass

    def clear_local_value(self, const_ConfigVariableCore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_local_value(const ConfigVariableCore self)
        
        /**
         * Removes the local value defined for this variable, and allows its value to
         * be once again retrieved from the .prc files.
         *
         * Returns true if the value was successfully removed, false if it did not
         * exist in the first place.
         */
        """
        pass

    def getDeclaration(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_declaration(ConfigVariableCore self, int n)
        
        /**
         * Returns the nth declarations that contributes to this variable's value.
         * The declarations are arranged in order such that earlier declarations
         * shadow later declarations; thus, get_declaration(0) is always defined and
         * always returns the current value of the variable.
         */
        """
        pass

    def getDeclarations(self, *args, **kwargs): # real signature unknown
        pass

    def getDefaultValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_value(ConfigVariableCore self)
        
        /**
         * Returns the default variable specified for this variable.  If the variable
         * has not yet been defined, this will return NULL.
         */
        """
        pass

    def getDescription(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_description(ConfigVariableCore self)
        
        /**
         * Returns the brief description of this variable, if it has been defined.
         */
        """
        pass

    def getFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_flags(ConfigVariableCore self)
        
        /**
         * Returns the flags value as set by set_flags().  This includes the trust
         * level and some other settings.  See the individual methods is_closed(),
         * get_trust_level(), etc.  to pull out the semantic meaning of these flags
         * individually.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(ConfigVariableCore self)
        
        /**
         * Returns the name of the variable.
         */
        """
        pass

    def getNumDeclarations(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_declarations(ConfigVariableCore self)
        
        /**
         * Returns the number of declarations that contribute to this variable's
         * value.  If the variable has been defined, this will always be at least 1
         * (for the default value, at least).
         */
        """
        pass

    def getNumReferences(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_references(ConfigVariableCore self)
        
        /**
         * Returns the number of prc files that reference this variable.  This is not
         * exactly the same as the number of declarations; see get_reference().
         */
        """
        pass

    def getNumTrustedReferences(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_trusted_references(ConfigVariableCore self)
        
        /**
         * Returns the number of trusted prc files that reference this variable.  See
         * also get_num_references().
         */
        """
        pass

    def getNumUniqueReferences(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_unique_references(ConfigVariableCore self)
        
        /**
         * Returns the number of trusted, unique (by string value) values there exist
         * for this variable.
         */
        """
        pass

    def getReference(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_reference(ConfigVariableCore self, int n)
        
        /**
         * Returns the nth declaration in a prc file that references this variable.
         * This is similar, but not identical to, get_declaration().  The difference
         * is that this will list *only* true references in a prc file, and will not
         * list default values or locally-assigned values; it also will list even the
         * untrusted files.
         */
        """
        pass

    def getReferences(self, *args, **kwargs): # real signature unknown
        pass

    def getTrustedReference(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_trusted_reference(ConfigVariableCore self, int n)
        
        /**
         * Returns the nth declaration in a trusted prc file that references this
         * variable.  This is similar, but not identical to, get_declaration().  The
         * difference is that this will list *only* true references in a prc file, and
         * will not list default values or locally-assigned values.
         *
         * This is also similar to get_reference(), except that it only lists the
         * trusted declarations, omitting the untrusted ones.
         */
        """
        pass

    def getTrustedReferences(self, *args, **kwargs): # real signature unknown
        pass

    def getTrustLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_trust_level(ConfigVariableCore self)
        
        /**
         * Returns the minimum trust_level a prc file must demonstrate in order to
         * redefine the value for this variable.  Arguably, this should be called the
         * "mistrust level", since the larger the value, the more suspicious we are of
         * prc files.  This value is not used if is_closed() returns true, which
         * indicates no file may be trusted.
         *
         * This value only has effect in a release build (specifically, when
         * PRC_RESPECT_TRUST_LEVEL is defined true in Config.pp).
         */
        """
        pass

    def getUniqueReference(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_unique_reference(ConfigVariableCore self, int n)
        
        /**
         * Returns the nth trusted, unique value for this variable.  This is similar
         * to get_trusted_reference(), except that duplicate values are removed.
         */
        """
        pass

    def getUniqueReferences(self, *args, **kwargs): # real signature unknown
        pass

    def getValueType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value_type(ConfigVariableCore self)
        
        /**
         * Returns the stated type of this variable.  If the variable has not yet been
         * defined, this will be VT_undefined.
         */
        """
        pass

    def get_declaration(self, ConfigVariableCore_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_declaration(ConfigVariableCore self, int n)
        
        /**
         * Returns the nth declarations that contributes to this variable's value.
         * The declarations are arranged in order such that earlier declarations
         * shadow later declarations; thus, get_declaration(0) is always defined and
         * always returns the current value of the variable.
         */
        """
        pass

    def get_declarations(self, *args, **kwargs): # real signature unknown
        pass

    def get_default_value(self, ConfigVariableCore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_value(ConfigVariableCore self)
        
        /**
         * Returns the default variable specified for this variable.  If the variable
         * has not yet been defined, this will return NULL.
         */
        """
        pass

    def get_description(self, ConfigVariableCore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_description(ConfigVariableCore self)
        
        /**
         * Returns the brief description of this variable, if it has been defined.
         */
        """
        pass

    def get_flags(self, ConfigVariableCore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_flags(ConfigVariableCore self)
        
        /**
         * Returns the flags value as set by set_flags().  This includes the trust
         * level and some other settings.  See the individual methods is_closed(),
         * get_trust_level(), etc.  to pull out the semantic meaning of these flags
         * individually.
         */
        """
        pass

    def get_name(self, ConfigVariableCore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(ConfigVariableCore self)
        
        /**
         * Returns the name of the variable.
         */
        """
        pass

    def get_num_declarations(self, ConfigVariableCore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_declarations(ConfigVariableCore self)
        
        /**
         * Returns the number of declarations that contribute to this variable's
         * value.  If the variable has been defined, this will always be at least 1
         * (for the default value, at least).
         */
        """
        pass

    def get_num_references(self, ConfigVariableCore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_references(ConfigVariableCore self)
        
        /**
         * Returns the number of prc files that reference this variable.  This is not
         * exactly the same as the number of declarations; see get_reference().
         */
        """
        pass

    def get_num_trusted_references(self, ConfigVariableCore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_trusted_references(ConfigVariableCore self)
        
        /**
         * Returns the number of trusted prc files that reference this variable.  See
         * also get_num_references().
         */
        """
        pass

    def get_num_unique_references(self, ConfigVariableCore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_unique_references(ConfigVariableCore self)
        
        /**
         * Returns the number of trusted, unique (by string value) values there exist
         * for this variable.
         */
        """
        pass

    def get_reference(self, ConfigVariableCore_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_reference(ConfigVariableCore self, int n)
        
        /**
         * Returns the nth declaration in a prc file that references this variable.
         * This is similar, but not identical to, get_declaration().  The difference
         * is that this will list *only* true references in a prc file, and will not
         * list default values or locally-assigned values; it also will list even the
         * untrusted files.
         */
        """
        pass

    def get_references(self, *args, **kwargs): # real signature unknown
        pass

    def get_trusted_reference(self, ConfigVariableCore_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_trusted_reference(ConfigVariableCore self, int n)
        
        /**
         * Returns the nth declaration in a trusted prc file that references this
         * variable.  This is similar, but not identical to, get_declaration().  The
         * difference is that this will list *only* true references in a prc file, and
         * will not list default values or locally-assigned values.
         *
         * This is also similar to get_reference(), except that it only lists the
         * trusted declarations, omitting the untrusted ones.
         */
        """
        pass

    def get_trusted_references(self, *args, **kwargs): # real signature unknown
        pass

    def get_trust_level(self, ConfigVariableCore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_trust_level(ConfigVariableCore self)
        
        /**
         * Returns the minimum trust_level a prc file must demonstrate in order to
         * redefine the value for this variable.  Arguably, this should be called the
         * "mistrust level", since the larger the value, the more suspicious we are of
         * prc files.  This value is not used if is_closed() returns true, which
         * indicates no file may be trusted.
         *
         * This value only has effect in a release build (specifically, when
         * PRC_RESPECT_TRUST_LEVEL is defined true in Config.pp).
         */
        """
        pass

    def get_unique_reference(self, ConfigVariableCore_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_unique_reference(ConfigVariableCore self, int n)
        
        /**
         * Returns the nth trusted, unique value for this variable.  This is similar
         * to get_trusted_reference(), except that duplicate values are removed.
         */
        """
        pass

    def get_unique_references(self, *args, **kwargs): # real signature unknown
        pass

    def get_value_type(self, ConfigVariableCore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value_type(ConfigVariableCore self)
        
        /**
         * Returns the stated type of this variable.  If the variable has not yet been
         * defined, this will be VT_undefined.
         */
        """
        pass

    def hasLocalValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_local_value(ConfigVariableCore self)
        
        /**
         * Returns true if this variable's value has been shadowed by a local
         * assignment (as created via make_local_value()), or false otherwise.
         */
        """
        pass

    def hasValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_value(ConfigVariableCore self)
        
        /**
         * Returns true if this variable has an explicit value, either from a prc file
         * or locally set, or false if variable has its default value.
         */
        """
        pass

    def has_local_value(self, ConfigVariableCore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_local_value(ConfigVariableCore self)
        
        /**
         * Returns true if this variable's value has been shadowed by a local
         * assignment (as created via make_local_value()), or false otherwise.
         */
        """
        pass

    def has_value(self, ConfigVariableCore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_value(ConfigVariableCore self)
        
        /**
         * Returns true if this variable has an explicit value, either from a prc file
         * or locally set, or false if variable has its default value.
         */
        """
        pass

    def isClosed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_closed(ConfigVariableCore self)
        
        /**
         * Returns true if the variable is not trusted by any prc file (and hence
         * cannot be modified from its compiled-in default value), or false for the
         * normal case, in which the variable can be modified by any prc file at or
         * above its trust level (see get_trust_level()).
         *
         * This value only has effect in a release build (specifically, when
         * PRC_RESPECT_TRUST_LEVEL is defined true in Config.pp).
         */
        """
        pass

    def isDynamic(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_dynamic(ConfigVariableCore self)
        
        /**
         * Returns true if the variable was indicated as "dynamic" by its constructor,
         * indicating that its name was dynamically generated, possibly from a large
         * pool, and it should not be listed along with the other variables.
         */
        """
        pass

    def isUsed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_used(ConfigVariableCore self)
        
        /**
         * Returns true if the variable has been referenced by a ConfigVariable
         * somewhere in code, false otherwise.
         */
        """
        pass

    def is_closed(self, ConfigVariableCore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_closed(ConfigVariableCore self)
        
        /**
         * Returns true if the variable is not trusted by any prc file (and hence
         * cannot be modified from its compiled-in default value), or false for the
         * normal case, in which the variable can be modified by any prc file at or
         * above its trust level (see get_trust_level()).
         *
         * This value only has effect in a release build (specifically, when
         * PRC_RESPECT_TRUST_LEVEL is defined true in Config.pp).
         */
        """
        pass

    def is_dynamic(self, ConfigVariableCore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_dynamic(ConfigVariableCore self)
        
        /**
         * Returns true if the variable was indicated as "dynamic" by its constructor,
         * indicating that its name was dynamically generated, possibly from a large
         * pool, and it should not be listed along with the other variables.
         */
        """
        pass

    def is_used(self, ConfigVariableCore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_used(ConfigVariableCore self)
        
        /**
         * Returns true if the variable has been referenced by a ConfigVariable
         * somewhere in code, false otherwise.
         */
        """
        pass

    def makeLocalValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_local_value(const ConfigVariableCore self)
        
        /**
         * Creates a new local value for this variable, if there is not already one
         * specified.  This will shadow any values defined in the various .prc files.
         *
         * If there is already a local value defined for this variable, simply returns
         * that one.
         *
         * Use clear_local_value() to remove the local value definition.
         */
        """
        pass

    def make_local_value(self, const_ConfigVariableCore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_local_value(const ConfigVariableCore self)
        
        /**
         * Creates a new local value for this variable, if there is not already one
         * specified.  This will shadow any values defined in the various .prc files.
         *
         * If there is already a local value defined for this variable, simply returns
         * that one.
         *
         * Use clear_local_value() to remove the local value definition.
         */
        """
        pass

    def output(self, ConfigVariableCore_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(ConfigVariableCore self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setDefaultValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_default_value(const ConfigVariableCore self, str default_value)
        
        /**
         * Specifies the default value for this variable if it is not defined in any
         * prc file.
         */
        """
        pass

    def setDescription(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_description(const ConfigVariableCore self, str description)
        
        /**
         * Specifies the one-line description of this variable.  See
         * get_description().  It is not an error to call this multiple times, but if
         * the value changes once get_declaration() has been called, a warning is
         * printed.
         */
        """
        pass

    def setFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_flags(const ConfigVariableCore self, int flags)
        
        /**
         * Specifies the trust level of this variable.  See get_flags().  It is not an
         * error to call this multiple times, but if the value changes once
         * get_declaration() has been called, a warning is printed.
         */
        """
        pass

    def setUsed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_used(const ConfigVariableCore self)
        
        /**
         * Marks that the variable has been "declared" by a ConfigVariable.
         */
        """
        pass

    def setValueType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_value_type(const ConfigVariableCore self, int value_type)
        
        /**
         * Specifies the type of this variable.  See get_value_type().  It is not an
         * error to call this multiple times, but if the value changes once
         * get_declaration() has been called, a warning is printed.
         */
        """
        pass

    def set_default_value(self, const_ConfigVariableCore_self, str_default_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_default_value(const ConfigVariableCore self, str default_value)
        
        /**
         * Specifies the default value for this variable if it is not defined in any
         * prc file.
         */
        """
        pass

    def set_description(self, const_ConfigVariableCore_self, str_description): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_description(const ConfigVariableCore self, str description)
        
        /**
         * Specifies the one-line description of this variable.  See
         * get_description().  It is not an error to call this multiple times, but if
         * the value changes once get_declaration() has been called, a warning is
         * printed.
         */
        """
        pass

    def set_flags(self, const_ConfigVariableCore_self, int_flags): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_flags(const ConfigVariableCore self, int flags)
        
        /**
         * Specifies the trust level of this variable.  See get_flags().  It is not an
         * error to call this multiple times, but if the value changes once
         * get_declaration() has been called, a warning is printed.
         */
        """
        pass

    def set_used(self, const_ConfigVariableCore_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_used(const ConfigVariableCore self)
        
        /**
         * Marks that the variable has been "declared" by a ConfigVariable.
         */
        """
        pass

    def set_value_type(self, const_ConfigVariableCore_self, int_value_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_value_type(const ConfigVariableCore self, int value_type)
        
        /**
         * Specifies the type of this variable.  See get_value_type().  It is not an
         * error to call this multiple times, but if the value changes once
         * get_declaration() has been called, a warning is printed.
         */
        """
        pass

    def write(self, ConfigVariableCore_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(ConfigVariableCore self, ostream out)
        
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

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    declarations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    default_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dynamic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    references = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    trusted_references = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    trust_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unique_references = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    used = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * The internal definition of a ConfigVariable.  This object is shared between\n * all instances of a ConfigVariable that use the same variable name.\n *\n * You cannot create a ConfigVariableCore instance directly; instead, use the\n * make() method, which may return a shared instance.  Once created, these\n * objects are never destructed.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ConfigVariableCore' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE262620>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.ConfigVariableCore' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.ConfigVariableCore' objects>"
        'clearLocalValue': None, # (!) real value is "<method 'clearLocalValue' of 'panda3d.core.ConfigVariableCore' objects>"
        'clear_local_value': None, # (!) real value is "<method 'clear_local_value' of 'panda3d.core.ConfigVariableCore' objects>"
        'closed': None, # (!) real value is "<attribute 'closed' of 'panda3d.core.ConfigVariableCore' objects>"
        'declarations': None, # (!) real value is "<attribute 'declarations' of 'panda3d.core.ConfigVariableCore' objects>"
        'default_value': None, # (!) real value is "<attribute 'default_value' of 'panda3d.core.ConfigVariableCore' objects>"
        'description': None, # (!) real value is "<attribute 'description' of 'panda3d.core.ConfigVariableCore' objects>"
        'dynamic': None, # (!) real value is "<attribute 'dynamic' of 'panda3d.core.ConfigVariableCore' objects>"
        'getDeclaration': None, # (!) real value is "<method 'getDeclaration' of 'panda3d.core.ConfigVariableCore' objects>"
        'getDeclarations': None, # (!) real value is "<method 'getDeclarations' of 'panda3d.core.ConfigVariableCore' objects>"
        'getDefaultValue': None, # (!) real value is "<method 'getDefaultValue' of 'panda3d.core.ConfigVariableCore' objects>"
        'getDescription': None, # (!) real value is "<method 'getDescription' of 'panda3d.core.ConfigVariableCore' objects>"
        'getFlags': None, # (!) real value is "<method 'getFlags' of 'panda3d.core.ConfigVariableCore' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.ConfigVariableCore' objects>"
        'getNumDeclarations': None, # (!) real value is "<method 'getNumDeclarations' of 'panda3d.core.ConfigVariableCore' objects>"
        'getNumReferences': None, # (!) real value is "<method 'getNumReferences' of 'panda3d.core.ConfigVariableCore' objects>"
        'getNumTrustedReferences': None, # (!) real value is "<method 'getNumTrustedReferences' of 'panda3d.core.ConfigVariableCore' objects>"
        'getNumUniqueReferences': None, # (!) real value is "<method 'getNumUniqueReferences' of 'panda3d.core.ConfigVariableCore' objects>"
        'getReference': None, # (!) real value is "<method 'getReference' of 'panda3d.core.ConfigVariableCore' objects>"
        'getReferences': None, # (!) real value is "<method 'getReferences' of 'panda3d.core.ConfigVariableCore' objects>"
        'getTrustLevel': None, # (!) real value is "<method 'getTrustLevel' of 'panda3d.core.ConfigVariableCore' objects>"
        'getTrustedReference': None, # (!) real value is "<method 'getTrustedReference' of 'panda3d.core.ConfigVariableCore' objects>"
        'getTrustedReferences': None, # (!) real value is "<method 'getTrustedReferences' of 'panda3d.core.ConfigVariableCore' objects>"
        'getUniqueReference': None, # (!) real value is "<method 'getUniqueReference' of 'panda3d.core.ConfigVariableCore' objects>"
        'getUniqueReferences': None, # (!) real value is "<method 'getUniqueReferences' of 'panda3d.core.ConfigVariableCore' objects>"
        'getValueType': None, # (!) real value is "<method 'getValueType' of 'panda3d.core.ConfigVariableCore' objects>"
        'get_declaration': None, # (!) real value is "<method 'get_declaration' of 'panda3d.core.ConfigVariableCore' objects>"
        'get_declarations': None, # (!) real value is "<method 'get_declarations' of 'panda3d.core.ConfigVariableCore' objects>"
        'get_default_value': None, # (!) real value is "<method 'get_default_value' of 'panda3d.core.ConfigVariableCore' objects>"
        'get_description': None, # (!) real value is "<method 'get_description' of 'panda3d.core.ConfigVariableCore' objects>"
        'get_flags': None, # (!) real value is "<method 'get_flags' of 'panda3d.core.ConfigVariableCore' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.ConfigVariableCore' objects>"
        'get_num_declarations': None, # (!) real value is "<method 'get_num_declarations' of 'panda3d.core.ConfigVariableCore' objects>"
        'get_num_references': None, # (!) real value is "<method 'get_num_references' of 'panda3d.core.ConfigVariableCore' objects>"
        'get_num_trusted_references': None, # (!) real value is "<method 'get_num_trusted_references' of 'panda3d.core.ConfigVariableCore' objects>"
        'get_num_unique_references': None, # (!) real value is "<method 'get_num_unique_references' of 'panda3d.core.ConfigVariableCore' objects>"
        'get_reference': None, # (!) real value is "<method 'get_reference' of 'panda3d.core.ConfigVariableCore' objects>"
        'get_references': None, # (!) real value is "<method 'get_references' of 'panda3d.core.ConfigVariableCore' objects>"
        'get_trust_level': None, # (!) real value is "<method 'get_trust_level' of 'panda3d.core.ConfigVariableCore' objects>"
        'get_trusted_reference': None, # (!) real value is "<method 'get_trusted_reference' of 'panda3d.core.ConfigVariableCore' objects>"
        'get_trusted_references': None, # (!) real value is "<method 'get_trusted_references' of 'panda3d.core.ConfigVariableCore' objects>"
        'get_unique_reference': None, # (!) real value is "<method 'get_unique_reference' of 'panda3d.core.ConfigVariableCore' objects>"
        'get_unique_references': None, # (!) real value is "<method 'get_unique_references' of 'panda3d.core.ConfigVariableCore' objects>"
        'get_value_type': None, # (!) real value is "<method 'get_value_type' of 'panda3d.core.ConfigVariableCore' objects>"
        'hasLocalValue': None, # (!) real value is "<method 'hasLocalValue' of 'panda3d.core.ConfigVariableCore' objects>"
        'hasValue': None, # (!) real value is "<method 'hasValue' of 'panda3d.core.ConfigVariableCore' objects>"
        'has_local_value': None, # (!) real value is "<method 'has_local_value' of 'panda3d.core.ConfigVariableCore' objects>"
        'has_value': None, # (!) real value is "<method 'has_value' of 'panda3d.core.ConfigVariableCore' objects>"
        'isClosed': None, # (!) real value is "<method 'isClosed' of 'panda3d.core.ConfigVariableCore' objects>"
        'isDynamic': None, # (!) real value is "<method 'isDynamic' of 'panda3d.core.ConfigVariableCore' objects>"
        'isUsed': None, # (!) real value is "<method 'isUsed' of 'panda3d.core.ConfigVariableCore' objects>"
        'is_closed': None, # (!) real value is "<method 'is_closed' of 'panda3d.core.ConfigVariableCore' objects>"
        'is_dynamic': None, # (!) real value is "<method 'is_dynamic' of 'panda3d.core.ConfigVariableCore' objects>"
        'is_used': None, # (!) real value is "<method 'is_used' of 'panda3d.core.ConfigVariableCore' objects>"
        'makeLocalValue': None, # (!) real value is "<method 'makeLocalValue' of 'panda3d.core.ConfigVariableCore' objects>"
        'make_local_value': None, # (!) real value is "<method 'make_local_value' of 'panda3d.core.ConfigVariableCore' objects>"
        'name': None, # (!) real value is "<attribute 'name' of 'panda3d.core.ConfigVariableCore' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.ConfigVariableCore' objects>"
        'references': None, # (!) real value is "<attribute 'references' of 'panda3d.core.ConfigVariableCore' objects>"
        'setDefaultValue': None, # (!) real value is "<method 'setDefaultValue' of 'panda3d.core.ConfigVariableCore' objects>"
        'setDescription': None, # (!) real value is "<method 'setDescription' of 'panda3d.core.ConfigVariableCore' objects>"
        'setFlags': None, # (!) real value is "<method 'setFlags' of 'panda3d.core.ConfigVariableCore' objects>"
        'setUsed': None, # (!) real value is "<method 'setUsed' of 'panda3d.core.ConfigVariableCore' objects>"
        'setValueType': None, # (!) real value is "<method 'setValueType' of 'panda3d.core.ConfigVariableCore' objects>"
        'set_default_value': None, # (!) real value is "<method 'set_default_value' of 'panda3d.core.ConfigVariableCore' objects>"
        'set_description': None, # (!) real value is "<method 'set_description' of 'panda3d.core.ConfigVariableCore' objects>"
        'set_flags': None, # (!) real value is "<method 'set_flags' of 'panda3d.core.ConfigVariableCore' objects>"
        'set_used': None, # (!) real value is "<method 'set_used' of 'panda3d.core.ConfigVariableCore' objects>"
        'set_value_type': None, # (!) real value is "<method 'set_value_type' of 'panda3d.core.ConfigVariableCore' objects>"
        'trust_level': None, # (!) real value is "<attribute 'trust_level' of 'panda3d.core.ConfigVariableCore' objects>"
        'trusted_references': None, # (!) real value is "<attribute 'trusted_references' of 'panda3d.core.ConfigVariableCore' objects>"
        'unique_references': None, # (!) real value is "<attribute 'unique_references' of 'panda3d.core.ConfigVariableCore' objects>"
        'used': None, # (!) real value is "<attribute 'used' of 'panda3d.core.ConfigVariableCore' objects>"
        'value_type': None, # (!) real value is "<attribute 'value_type' of 'panda3d.core.ConfigVariableCore' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.ConfigVariableCore' objects>"
    }


