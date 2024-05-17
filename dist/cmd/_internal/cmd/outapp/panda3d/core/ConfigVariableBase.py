# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ConfigFlags import ConfigFlags

class ConfigVariableBase(ConfigFlags):
    """
    /**
     * This class is the base class for both ConfigVariableList and ConfigVariable
     * (and hence for all of the ConfigVariableBool, ConfigVaribleString, etc.
     * classes).  It collects together the common interface for all generic
     * ConfigVariables.
     *
     * Mostly, this class serves as a thin wrapper around ConfigVariableCore
     * and/or ConfigDeclaration, more or less duplicating the interface presented
     * there.
     */
    """
    def clearLocalValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_local_value(const ConfigVariableBase self)
        
        /**
         * Removes the local value defined for this variable, and allows its value to
         * be once again retrieved from the .prc files.
         *
         * Returns true if the value was successfully removed, false if it did not
         * exist in the first place.
         */
        """
        pass

    def clear_local_value(self, const_ConfigVariableBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_local_value(const ConfigVariableBase self)
        
        /**
         * Removes the local value defined for this variable, and allows its value to
         * be once again retrieved from the .prc files.
         *
         * Returns true if the value was successfully removed, false if it did not
         * exist in the first place.
         */
        """
        pass

    def getDescription(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_description(ConfigVariableBase self)
        
        /**
         * Returns the brief description of this variable, if it has been defined.
         */
        """
        pass

    def getFlags(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_flags(ConfigVariableBase self)
        
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
        get_name(ConfigVariableBase self)
        
        /**
         * Returns the name of the variable.
         */
        """
        pass

    def getTrustLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_trust_level(ConfigVariableBase self)
        
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

    def getValueType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value_type(ConfigVariableBase self)
        
        /**
         * Returns the stated type of this variable.  This should be VT_list, unless a
         * later variable declaration has changed it.
         */
        """
        pass

    def get_description(self, ConfigVariableBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_description(ConfigVariableBase self)
        
        /**
         * Returns the brief description of this variable, if it has been defined.
         */
        """
        pass

    def get_flags(self, ConfigVariableBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_flags(ConfigVariableBase self)
        
        /**
         * Returns the flags value as set by set_flags().  This includes the trust
         * level and some other settings.  See the individual methods is_closed(),
         * get_trust_level(), etc.  to pull out the semantic meaning of these flags
         * individually.
         */
        """
        pass

    def get_name(self, ConfigVariableBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(ConfigVariableBase self)
        
        /**
         * Returns the name of the variable.
         */
        """
        pass

    def get_trust_level(self, ConfigVariableBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_trust_level(ConfigVariableBase self)
        
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

    def get_value_type(self, ConfigVariableBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value_type(ConfigVariableBase self)
        
        /**
         * Returns the stated type of this variable.  This should be VT_list, unless a
         * later variable declaration has changed it.
         */
        """
        pass

    def hasLocalValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_local_value(ConfigVariableBase self)
        
        /**
         * Returns true if this variable's value has been shadowed by a local
         * assignment (as created via make_local_value()), or false otherwise.
         */
        """
        pass

    def hasValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_value(ConfigVariableBase self)
        
        /**
         * Returns true if this variable has an explicit value, either from a prc file
         * or locally set, or false if variable has its default value.
         */
        """
        pass

    def has_local_value(self, ConfigVariableBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_local_value(ConfigVariableBase self)
        
        /**
         * Returns true if this variable's value has been shadowed by a local
         * assignment (as created via make_local_value()), or false otherwise.
         */
        """
        pass

    def has_value(self, ConfigVariableBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_value(ConfigVariableBase self)
        
        /**
         * Returns true if this variable has an explicit value, either from a prc file
         * or locally set, or false if variable has its default value.
         */
        """
        pass

    def isClosed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_closed(ConfigVariableBase self)
        
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
        is_dynamic(ConfigVariableBase self)
        
        /**
         * Returns true if the variable was indicated as "dynamic" by its constructor,
         * indicating that its name was dynamically generated, possibly from a large
         * pool, and it should not be listed along with the other variables.
         */
        """
        pass

    def is_closed(self, ConfigVariableBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_closed(ConfigVariableBase self)
        
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

    def is_dynamic(self, ConfigVariableBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_dynamic(ConfigVariableBase self)
        
        /**
         * Returns true if the variable was indicated as "dynamic" by its constructor,
         * indicating that its name was dynamically generated, possibly from a large
         * pool, and it should not be listed along with the other variables.
         */
        """
        pass

    def output(self, ConfigVariableBase_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(ConfigVariableBase self, ostream out)
        
        /**
         *
         */
        """
        pass

    def write(self, ConfigVariableBase_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(ConfigVariableBase self, ostream out)
        
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

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dynamic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    trust_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This class is the base class for both ConfigVariableList and ConfigVariable\n * (and hence for all of the ConfigVariableBool, ConfigVaribleString, etc.\n * classes).  It collects together the common interface for all generic\n * ConfigVariables.\n *\n * Mostly, this class serves as a thin wrapper around ConfigVariableCore\n * and/or ConfigDeclaration, more or less duplicating the interface presented\n * there.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ConfigVariableBase' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE262D60>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.ConfigVariableBase' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.ConfigVariableBase' objects>"
        'clearLocalValue': None, # (!) real value is "<method 'clearLocalValue' of 'panda3d.core.ConfigVariableBase' objects>"
        'clear_local_value': None, # (!) real value is "<method 'clear_local_value' of 'panda3d.core.ConfigVariableBase' objects>"
        'closed': None, # (!) real value is "<attribute 'closed' of 'panda3d.core.ConfigVariableBase' objects>"
        'description': None, # (!) real value is "<attribute 'description' of 'panda3d.core.ConfigVariableBase' objects>"
        'dynamic': None, # (!) real value is "<attribute 'dynamic' of 'panda3d.core.ConfigVariableBase' objects>"
        'getDescription': None, # (!) real value is "<method 'getDescription' of 'panda3d.core.ConfigVariableBase' objects>"
        'getFlags': None, # (!) real value is "<method 'getFlags' of 'panda3d.core.ConfigVariableBase' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.ConfigVariableBase' objects>"
        'getTrustLevel': None, # (!) real value is "<method 'getTrustLevel' of 'panda3d.core.ConfigVariableBase' objects>"
        'getValueType': None, # (!) real value is "<method 'getValueType' of 'panda3d.core.ConfigVariableBase' objects>"
        'get_description': None, # (!) real value is "<method 'get_description' of 'panda3d.core.ConfigVariableBase' objects>"
        'get_flags': None, # (!) real value is "<method 'get_flags' of 'panda3d.core.ConfigVariableBase' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.ConfigVariableBase' objects>"
        'get_trust_level': None, # (!) real value is "<method 'get_trust_level' of 'panda3d.core.ConfigVariableBase' objects>"
        'get_value_type': None, # (!) real value is "<method 'get_value_type' of 'panda3d.core.ConfigVariableBase' objects>"
        'hasLocalValue': None, # (!) real value is "<method 'hasLocalValue' of 'panda3d.core.ConfigVariableBase' objects>"
        'hasValue': None, # (!) real value is "<method 'hasValue' of 'panda3d.core.ConfigVariableBase' objects>"
        'has_local_value': None, # (!) real value is "<method 'has_local_value' of 'panda3d.core.ConfigVariableBase' objects>"
        'has_value': None, # (!) real value is "<method 'has_value' of 'panda3d.core.ConfigVariableBase' objects>"
        'isClosed': None, # (!) real value is "<method 'isClosed' of 'panda3d.core.ConfigVariableBase' objects>"
        'isDynamic': None, # (!) real value is "<method 'isDynamic' of 'panda3d.core.ConfigVariableBase' objects>"
        'is_closed': None, # (!) real value is "<method 'is_closed' of 'panda3d.core.ConfigVariableBase' objects>"
        'is_dynamic': None, # (!) real value is "<method 'is_dynamic' of 'panda3d.core.ConfigVariableBase' objects>"
        'name': None, # (!) real value is "<attribute 'name' of 'panda3d.core.ConfigVariableBase' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.ConfigVariableBase' objects>"
        'trust_level': None, # (!) real value is "<attribute 'trust_level' of 'panda3d.core.ConfigVariableBase' objects>"
        'value_type': None, # (!) real value is "<attribute 'value_type' of 'panda3d.core.ConfigVariableBase' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.ConfigVariableBase' objects>"
    }


