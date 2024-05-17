# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class ConfigVariableManager(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A global object that maintains the set of ConfigVariables (actually,
     * ConfigVariableCores) everywhere in the world, and keeps them in sorted
     * order.
     */
    """
    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         *
         */
        """
        pass

    def getNumVariables(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_variables(ConfigVariableManager self)
        
        /**
         * Returns the current number of active ConfigVariableCores in the world.
         */
        """
        pass

    def getVariable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_variable(ConfigVariableManager self, int n)
        
        /**
         * Returns the nth active ConfigVariableCore in the world.
         */
        """
        pass

    def getVariableName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_variable_name(ConfigVariableManager self, int n)
        
        /**
         * Returns the name of the nth active ConfigVariable in the list.
         */
        """
        pass

    def getVariables(self, *args, **kwargs): # real signature unknown
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

    def get_num_variables(self, ConfigVariableManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_variables(ConfigVariableManager self)
        
        /**
         * Returns the current number of active ConfigVariableCores in the world.
         */
        """
        pass

    def get_variable(self, ConfigVariableManager_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_variable(ConfigVariableManager self, int n)
        
        /**
         * Returns the nth active ConfigVariableCore in the world.
         */
        """
        pass

    def get_variables(self, *args, **kwargs): # real signature unknown
        pass

    def get_variable_name(self, ConfigVariableManager_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_variable_name(ConfigVariableManager self, int n)
        
        /**
         * Returns the name of the nth active ConfigVariable in the list.
         */
        """
        pass

    def isVariableUsed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_variable_used(ConfigVariableManager self, int n)
        
        /**
         * Returns true if the nth active ConfigVariable in the list has been used by
         * code, false otherwise.
         */
        """
        pass

    def is_variable_used(self, ConfigVariableManager_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_variable_used(ConfigVariableManager self, int n)
        
        /**
         * Returns true if the nth active ConfigVariable in the list has been used by
         * code, false otherwise.
         */
        """
        pass

    def listDynamicVariables(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        list_dynamic_variables(ConfigVariableManager self)
        
        /**
         * Writes a list of all the "dynamic" variables that have been declared
         * somewhere in code, along with a brief description.  This is a (usually
         * large) list of config variables that are declared with a generated variable
         * name.
         */
        """
        pass

    def listUnusedVariables(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        list_unused_variables(ConfigVariableManager self)
        
        /**
         * Writes a list of all the variables that have been defined in a prc file
         * without having been declared somewhere in code.
         */
        """
        pass

    def listVariables(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        list_variables(ConfigVariableManager self)
        
        /**
         * Writes a list of all the variables that have been declared somewhere in
         * code, along with a brief description.
         */
        """
        pass

    def list_dynamic_variables(self, ConfigVariableManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        list_dynamic_variables(ConfigVariableManager self)
        
        /**
         * Writes a list of all the "dynamic" variables that have been declared
         * somewhere in code, along with a brief description.  This is a (usually
         * large) list of config variables that are declared with a generated variable
         * name.
         */
        """
        pass

    def list_unused_variables(self, ConfigVariableManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        list_unused_variables(ConfigVariableManager self)
        
        /**
         * Writes a list of all the variables that have been defined in a prc file
         * without having been declared somewhere in code.
         */
        """
        pass

    def list_variables(self, ConfigVariableManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        list_variables(ConfigVariableManager self)
        
        /**
         * Writes a list of all the variables that have been declared somewhere in
         * code, along with a brief description.
         */
        """
        pass

    def makeVariable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_variable(const ConfigVariableManager self, str name)
        
        /**
         * Creates and returns a new, undefined ConfigVariableCore with the indicated
         * name; or if a variable with this name has already been created, returns
         * that one instead.
         */
        """
        pass

    def makeVariableTemplate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_variable_template(const ConfigVariableManager self, str pattern, int type, str default_value, str description, int flags)
        
        /**
         * Defines a variable "template" to match against dynamically-defined
         * variables that may or may not be created in the future.
         *
         * The template consists of a glob pattern, e.g.  `notify-level-*`, which will
         * be tested against any config variable passed to a future call to
         * make_variable().  If the pattern matches, the returned ConfigVariableCore
         * is copied to define the new variable, instead of creating a default, empty
         * one.
         *
         * This is useful to pre-specify default values for a family of variables that
         * all have similar properties, and all may not be created at the same time.
         * It is especially useful to avoid cluttering up the list of available
         * variables with user-declared variables that have not been defined yet by
         * the application (e.g. `egg-object-type-*`).
         *
         * This method basically pre-defines all variables that match the specified
         * glob pattern.
         */
        """
        pass

    def make_variable(self, const_ConfigVariableManager_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_variable(const ConfigVariableManager self, str name)
        
        /**
         * Creates and returns a new, undefined ConfigVariableCore with the indicated
         * name; or if a variable with this name has already been created, returns
         * that one instead.
         */
        """
        pass

    def make_variable_template(self, const_ConfigVariableManager_self, str_pattern, int_type, str_default_value, str_description, int_flags): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_variable_template(const ConfigVariableManager self, str pattern, int type, str default_value, str description, int flags)
        
        /**
         * Defines a variable "template" to match against dynamically-defined
         * variables that may or may not be created in the future.
         *
         * The template consists of a glob pattern, e.g.  `notify-level-*`, which will
         * be tested against any config variable passed to a future call to
         * make_variable().  If the pattern matches, the returned ConfigVariableCore
         * is copied to define the new variable, instead of creating a default, empty
         * one.
         *
         * This is useful to pre-specify default values for a family of variables that
         * all have similar properties, and all may not be created at the same time.
         * It is especially useful to avoid cluttering up the list of available
         * variables with user-declared variables that have not been defined yet by
         * the application (e.g. `egg-object-type-*`).
         *
         * This method basically pre-defines all variables that match the specified
         * glob pattern.
         */
        """
        pass

    def output(self, ConfigVariableManager_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(ConfigVariableManager self, ostream out)
        
        /**
         *
         */
        """
        pass

    def write(self, ConfigVariableManager_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(ConfigVariableManager self, ostream out)
        
        /**
         *
         */
        """
        pass

    def writePrcVariables(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_prc_variables(ConfigVariableManager self, ostream out)
        
        /**
         * Writes all of the prc-set config variables, as they appear in a prc file
         * somewhere, one per line, very concisely.  This lists the dominant value in
         * the prc file; it does not list shadowed values, and it does not list
         * locally-set values.
         *
         * This is mainly intended for generating a hash of the input config file
         * state.
         */
        """
        pass

    def write_prc_variables(self, ConfigVariableManager_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_prc_variables(ConfigVariableManager self, ostream out)
        
        /**
         * Writes all of the prc-set config variables, as they appear in a prc file
         * somewhere, one per line, very concisely.  This lists the dominant value in
         * the prc file; it does not list shadowed values, and it does not list
         * locally-set values.
         *
         * This is mainly intended for generating a hash of the input config file
         * state.
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

    variables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A global object that maintains the set of ConfigVariables (actually,\n * ConfigVariableCores) everywhere in the world, and keeps them in sorted\n * order.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ConfigVariableManager' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE262B90>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.ConfigVariableManager' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.ConfigVariableManager' objects>"
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFCFE262B90>)>'
        'getNumVariables': None, # (!) real value is "<method 'getNumVariables' of 'panda3d.core.ConfigVariableManager' objects>"
        'getVariable': None, # (!) real value is "<method 'getVariable' of 'panda3d.core.ConfigVariableManager' objects>"
        'getVariableName': None, # (!) real value is "<method 'getVariableName' of 'panda3d.core.ConfigVariableManager' objects>"
        'getVariables': None, # (!) real value is "<method 'getVariables' of 'panda3d.core.ConfigVariableManager' objects>"
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFCFE262B90>)>'
        'get_num_variables': None, # (!) real value is "<method 'get_num_variables' of 'panda3d.core.ConfigVariableManager' objects>"
        'get_variable': None, # (!) real value is "<method 'get_variable' of 'panda3d.core.ConfigVariableManager' objects>"
        'get_variable_name': None, # (!) real value is "<method 'get_variable_name' of 'panda3d.core.ConfigVariableManager' objects>"
        'get_variables': None, # (!) real value is "<method 'get_variables' of 'panda3d.core.ConfigVariableManager' objects>"
        'isVariableUsed': None, # (!) real value is "<method 'isVariableUsed' of 'panda3d.core.ConfigVariableManager' objects>"
        'is_variable_used': None, # (!) real value is "<method 'is_variable_used' of 'panda3d.core.ConfigVariableManager' objects>"
        'listDynamicVariables': None, # (!) real value is "<method 'listDynamicVariables' of 'panda3d.core.ConfigVariableManager' objects>"
        'listUnusedVariables': None, # (!) real value is "<method 'listUnusedVariables' of 'panda3d.core.ConfigVariableManager' objects>"
        'listVariables': None, # (!) real value is "<method 'listVariables' of 'panda3d.core.ConfigVariableManager' objects>"
        'list_dynamic_variables': None, # (!) real value is "<method 'list_dynamic_variables' of 'panda3d.core.ConfigVariableManager' objects>"
        'list_unused_variables': None, # (!) real value is "<method 'list_unused_variables' of 'panda3d.core.ConfigVariableManager' objects>"
        'list_variables': None, # (!) real value is "<method 'list_variables' of 'panda3d.core.ConfigVariableManager' objects>"
        'makeVariable': None, # (!) real value is "<method 'makeVariable' of 'panda3d.core.ConfigVariableManager' objects>"
        'makeVariableTemplate': None, # (!) real value is "<method 'makeVariableTemplate' of 'panda3d.core.ConfigVariableManager' objects>"
        'make_variable': None, # (!) real value is "<method 'make_variable' of 'panda3d.core.ConfigVariableManager' objects>"
        'make_variable_template': None, # (!) real value is "<method 'make_variable_template' of 'panda3d.core.ConfigVariableManager' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.ConfigVariableManager' objects>"
        'variables': None, # (!) real value is "<attribute 'variables' of 'panda3d.core.ConfigVariableManager' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.ConfigVariableManager' objects>"
        'writePrcVariables': None, # (!) real value is "<method 'writePrcVariables' of 'panda3d.core.ConfigVariableManager' objects>"
        'write_prc_variables': None, # (!) real value is "<method 'write_prc_variables' of 'panda3d.core.ConfigVariableManager' objects>"
    }


