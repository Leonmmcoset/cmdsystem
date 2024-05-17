# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class ExecutionEnvironment(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * Encapsulates access to the environment variables and command-line arguments
     * at the time of execution.  This is encapsulated to support accessing these
     * things during static init time, which seems to be risky at best.
     */
    """
    def clearShadow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_shadow(str var)
        
        /**
         * Removes a value set by a previous call to shadow_environment_variable(),
         * and lets the actual value of the variable show again.
         */
        """
        pass

    def clear_shadow(self, str_var): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_shadow(str var)
        
        /**
         * Removes a value set by a previous call to shadow_environment_variable(),
         * and lets the actual value of the variable show again.
         */
        """
        pass

    def expandString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        expand_string(str str)
        
        /**
         * Reads the string, looking for environment variable names marked by a $.
         * Expands all such variable names.  A repeated dollar sign ($$) is mapped to
         * a single dollar sign.
         *
         * Returns the expanded string.
         */
        """
        pass

    def expand_string(self, str_str): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        expand_string(str str)
        
        /**
         * Reads the string, looking for environment variable names marked by a $.
         * Expands all such variable names.  A repeated dollar sign ($$) is mapped to
         * a single dollar sign.
         *
         * Returns the expanded string.
         */
        """
        pass

    def getArg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_arg(int n)
        
        /**
         * Returns the nth command-line argument.  The index n must be in the range [0
         * .. get_num_args()).  The first parameter, n == 0, is the first actual
         * parameter, not the binary name.
         */
        """
        pass

    def getBinaryName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_binary_name()
        
        /**
         * Returns the name of the binary executable that started this program, if it
         * can be determined.
         */
        """
        pass

    def getCwd(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cwd()
        
        /**
         * Returns the name of the current working directory.
         */
        """
        pass

    def getDtoolName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_dtool_name()
        
        /**
         * Returns the name of the libdtool DLL that is used in this program, if it
         * can be determined.
         */
        """
        pass

    def getEnvironmentVariable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_environment_variable(str var)
        
        /**
         * Returns the definition of the indicated environment variable, or the empty
         * string if the variable is undefined.
         */
        """
        pass

    def getNumArgs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_args()
        
        /**
         * Returns the number of command-line arguments available, not counting arg 0,
         * the binary name.
         */
        """
        pass

    def get_arg(self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_arg(int n)
        
        /**
         * Returns the nth command-line argument.  The index n must be in the range [0
         * .. get_num_args()).  The first parameter, n == 0, is the first actual
         * parameter, not the binary name.
         */
        """
        pass

    def get_binary_name(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_binary_name()
        
        /**
         * Returns the name of the binary executable that started this program, if it
         * can be determined.
         */
        """
        pass

    def get_cwd(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cwd()
        
        /**
         * Returns the name of the current working directory.
         */
        """
        pass

    def get_dtool_name(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_dtool_name()
        
        /**
         * Returns the name of the libdtool DLL that is used in this program, if it
         * can be determined.
         */
        """
        pass

    def get_environment_variable(self, str_var): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_environment_variable(str var)
        
        /**
         * Returns the definition of the indicated environment variable, or the empty
         * string if the variable is undefined.
         */
        """
        pass

    def get_num_args(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_args()
        
        /**
         * Returns the number of command-line arguments available, not counting arg 0,
         * the binary name.
         */
        """
        pass

    def hasEnvironmentVariable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_environment_variable(str var)
        
        /**
         * Returns true if the indicated environment variable is defined.
         */
        """
        pass

    def has_environment_variable(self, str_var): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_environment_variable(str var)
        
        /**
         * Returns true if the indicated environment variable is defined.
         */
        """
        pass

    def setBinaryName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_binary_name(str name)
        
        /**
         * Do not use.
         */
        """
        pass

    def setDtoolName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_dtool_name(str name)
        
        /**
         * Do not use.
         */
        """
        pass

    def setEnvironmentVariable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_environment_variable(str var, str value)
        
        /**
         * Changes the definition of the indicated environment variable.
         */
        """
        pass

    def set_binary_name(self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_binary_name(str name)
        
        /**
         * Do not use.
         */
        """
        pass

    def set_dtool_name(self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_dtool_name(str name)
        
        /**
         * Do not use.
         */
        """
        pass

    def set_environment_variable(self, str_var, str_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_environment_variable(str var, str value)
        
        /**
         * Changes the definition of the indicated environment variable.
         */
        """
        pass

    def shadowEnvironmentVariable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        shadow_environment_variable(str var, str value)
        
        /**
         * Changes the apparent definition of the indicated environment variable by
         * masking it within this class with a new value.  This does not change the
         * actual environment variable, but future calls to get_environment_variable()
         * will return this new value.
         */
        """
        pass

    def shadow_environment_variable(self, str_var, str_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        shadow_environment_variable(str var, str value)
        
        /**
         * Changes the apparent definition of the indicated environment variable by
         * masking it within this class with a new value.  This does not change the
         * actual environment variable, but future calls to get_environment_variable()
         * will return this new value.
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

    args = None # (!) real value is '<ExecutionEnvironment.args[4] of <NULL>>'
    binary_name = '/c/Users/leonm/AppData/Local/Programs/Python/Python311/python.exe'
    cwd = Filename('/c/Program Files/JetBrains/PyCharm 2023.2.1/jbr/bin')
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ExecutionEnvironment' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ExecutionEnvironment' objects>"
        '__doc__': '/**\n * Encapsulates access to the environment variables and command-line arguments\n * at the time of execution.  This is encapsulated to support accessing these\n * things during static init time, which seems to be risky at best.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ExecutionEnvironment' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE25C160>'
        'args': None, # (!) real value is "<attribute 'args' of 'panda3d.core.ExecutionEnvironment'>"
        'binary_name': None, # (!) real value is "<attribute 'binary_name' of 'panda3d.core.ExecutionEnvironment'>"
        'clearShadow': None, # (!) real value is '<staticmethod(<built-in method clearShadow of type object at 0x00007FFCFE25C160>)>'
        'clear_shadow': None, # (!) real value is '<staticmethod(<built-in method clear_shadow of type object at 0x00007FFCFE25C160>)>'
        'cwd': None, # (!) real value is "<attribute 'cwd' of 'panda3d.core.ExecutionEnvironment'>"
        'dtool_name': None, # (!) real value is "<attribute 'dtool_name' of 'panda3d.core.ExecutionEnvironment'>"
        'environment_variables': None, # (!) real value is "<attribute 'environment_variables' of 'panda3d.core.ExecutionEnvironment'>"
        'expandString': None, # (!) real value is '<staticmethod(<built-in method expandString of type object at 0x00007FFCFE25C160>)>'
        'expand_string': None, # (!) real value is '<staticmethod(<built-in method expand_string of type object at 0x00007FFCFE25C160>)>'
        'getArg': None, # (!) real value is '<staticmethod(<built-in method getArg of type object at 0x00007FFCFE25C160>)>'
        'getBinaryName': None, # (!) real value is '<staticmethod(<built-in method getBinaryName of type object at 0x00007FFCFE25C160>)>'
        'getCwd': None, # (!) real value is '<staticmethod(<built-in method getCwd of type object at 0x00007FFCFE25C160>)>'
        'getDtoolName': None, # (!) real value is '<staticmethod(<built-in method getDtoolName of type object at 0x00007FFCFE25C160>)>'
        'getEnvironmentVariable': None, # (!) real value is '<staticmethod(<built-in method getEnvironmentVariable of type object at 0x00007FFCFE25C160>)>'
        'getNumArgs': None, # (!) real value is '<staticmethod(<built-in method getNumArgs of type object at 0x00007FFCFE25C160>)>'
        'get_arg': None, # (!) real value is '<staticmethod(<built-in method get_arg of type object at 0x00007FFCFE25C160>)>'
        'get_binary_name': None, # (!) real value is '<staticmethod(<built-in method get_binary_name of type object at 0x00007FFCFE25C160>)>'
        'get_cwd': None, # (!) real value is '<staticmethod(<built-in method get_cwd of type object at 0x00007FFCFE25C160>)>'
        'get_dtool_name': None, # (!) real value is '<staticmethod(<built-in method get_dtool_name of type object at 0x00007FFCFE25C160>)>'
        'get_environment_variable': None, # (!) real value is '<staticmethod(<built-in method get_environment_variable of type object at 0x00007FFCFE25C160>)>'
        'get_num_args': None, # (!) real value is '<staticmethod(<built-in method get_num_args of type object at 0x00007FFCFE25C160>)>'
        'hasEnvironmentVariable': None, # (!) real value is '<staticmethod(<built-in method hasEnvironmentVariable of type object at 0x00007FFCFE25C160>)>'
        'has_environment_variable': None, # (!) real value is '<staticmethod(<built-in method has_environment_variable of type object at 0x00007FFCFE25C160>)>'
        'setBinaryName': None, # (!) real value is '<staticmethod(<built-in method setBinaryName of type object at 0x00007FFCFE25C160>)>'
        'setDtoolName': None, # (!) real value is '<staticmethod(<built-in method setDtoolName of type object at 0x00007FFCFE25C160>)>'
        'setEnvironmentVariable': None, # (!) real value is '<staticmethod(<built-in method setEnvironmentVariable of type object at 0x00007FFCFE25C160>)>'
        'set_binary_name': None, # (!) real value is '<staticmethod(<built-in method set_binary_name of type object at 0x00007FFCFE25C160>)>'
        'set_dtool_name': None, # (!) real value is '<staticmethod(<built-in method set_dtool_name of type object at 0x00007FFCFE25C160>)>'
        'set_environment_variable': None, # (!) real value is '<staticmethod(<built-in method set_environment_variable of type object at 0x00007FFCFE25C160>)>'
        'shadowEnvironmentVariable': None, # (!) real value is '<staticmethod(<built-in method shadowEnvironmentVariable of type object at 0x00007FFCFE25C160>)>'
        'shadow_environment_variable': None, # (!) real value is '<staticmethod(<built-in method shadow_environment_variable of type object at 0x00007FFCFE25C160>)>'
    }
    dtool_name = '/c/Users/leonm/PycharmProjects/LeonRandomPlus/venv/Lib/site-packages/panda3d/libp3dtool.dll'
    environment_variables = None # (!) real value is "<attribute 'environment_variables' of 'panda3d.core.ExecutionEnvironment'>"


