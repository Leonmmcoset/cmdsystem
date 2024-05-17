# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class GraphicsPipeSelection(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This maintains a list of GraphicsPipes by type that are available for
     * creation.  Normally there is one default interactive GraphicsPipe, and
     * possibly other types available as well.
     */
    """
    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns a pointer to the one global GraphicsPipeSelection object.
         */
        """
        pass

    def getNumAuxModules(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_aux_modules(GraphicsPipeSelection self)
        
        /**
         * Returns the number of display modules that are still to be loaded.  If this
         * is nonzero, then calling load_aux_modules() will likely increase the number
         * of GraphicsPipes available.
         */
        """
        pass

    def getNumPipeTypes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_pipe_types(GraphicsPipeSelection self)
        
        /**
         * Returns the number of different types of GraphicsPipes that are available
         * to create through this interface.
         */
        """
        pass

    def getPipeType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pipe_type(GraphicsPipeSelection self, int n)
        
        /**
         * Returns the nth type of GraphicsPipe available through this interface.
         */
        """
        pass

    def getPipeTypes(self, *args, **kwargs): # real signature unknown
        pass

    def get_global_ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns a pointer to the one global GraphicsPipeSelection object.
         */
        """
        pass

    def get_num_aux_modules(self, GraphicsPipeSelection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_aux_modules(GraphicsPipeSelection self)
        
        /**
         * Returns the number of display modules that are still to be loaded.  If this
         * is nonzero, then calling load_aux_modules() will likely increase the number
         * of GraphicsPipes available.
         */
        """
        pass

    def get_num_pipe_types(self, GraphicsPipeSelection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_pipe_types(GraphicsPipeSelection self)
        
        /**
         * Returns the number of different types of GraphicsPipes that are available
         * to create through this interface.
         */
        """
        pass

    def get_pipe_type(self, GraphicsPipeSelection_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pipe_type(GraphicsPipeSelection self, int n)
        
        /**
         * Returns the nth type of GraphicsPipe available through this interface.
         */
        """
        pass

    def get_pipe_types(self, *args, **kwargs): # real signature unknown
        pass

    def loadAuxModules(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_aux_modules(const GraphicsPipeSelection self)
        
        /**
         * Loads all the modules named in the aux-display Configrc variable, making as
         * many graphics pipes as possible available.
         */
        """
        pass

    def load_aux_modules(self, const_GraphicsPipeSelection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_aux_modules(const GraphicsPipeSelection self)
        
        /**
         * Loads all the modules named in the aux-display Configrc variable, making as
         * many graphics pipes as possible available.
         */
        """
        pass

    def makeDefaultPipe(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_default_pipe(const GraphicsPipeSelection self)
        
        /**
         * Creates a new GraphicsPipe of some arbitrary type.  The user may specify a
         * preference using the Configrc file; otherwise, one will be chosen
         * arbitrarily.
         */
        """
        pass

    def makeModulePipe(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_module_pipe(const GraphicsPipeSelection self, str module_name)
        
        /**
         * Returns a new GraphicsPipe of a type defined by the indicated module.
         * Returns NULL if the module is not found or does not properly recommend a
         * GraphicsPipe.
         */
        """
        pass

    def makePipe(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_pipe(const GraphicsPipeSelection self, str type_name, str module_name)
        
        /**
         * Creates a new GraphicsPipe of the indicated type (or a type more specific
         * than the indicated type, if necessary) and returns it.  Returns NULL if the
         * type cannot be matched.
         *
         * If the type is not already defined, this will implicitly load the named
         * module, or if module_name is empty, it will call load_aux_modules().
         */
        
        /**
         * Creates a new GraphicsPipe of the indicated type (or a type more specific
         * than the indicated type, if necessary) and returns it.  Returns NULL if the
         * type cannot be matched.
         */
        """
        pass

    def make_default_pipe(self, const_GraphicsPipeSelection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_default_pipe(const GraphicsPipeSelection self)
        
        /**
         * Creates a new GraphicsPipe of some arbitrary type.  The user may specify a
         * preference using the Configrc file; otherwise, one will be chosen
         * arbitrarily.
         */
        """
        pass

    def make_module_pipe(self, const_GraphicsPipeSelection_self, str_module_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_module_pipe(const GraphicsPipeSelection self, str module_name)
        
        /**
         * Returns a new GraphicsPipe of a type defined by the indicated module.
         * Returns NULL if the module is not found or does not properly recommend a
         * GraphicsPipe.
         */
        """
        pass

    def make_pipe(self, const_GraphicsPipeSelection_self, str_type_name, str_module_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_pipe(const GraphicsPipeSelection self, str type_name, str module_name)
        
        /**
         * Creates a new GraphicsPipe of the indicated type (or a type more specific
         * than the indicated type, if necessary) and returns it.  Returns NULL if the
         * type cannot be matched.
         *
         * If the type is not already defined, this will implicitly load the named
         * module, or if module_name is empty, it will call load_aux_modules().
         */
        
        /**
         * Creates a new GraphicsPipe of the indicated type (or a type more specific
         * than the indicated type, if necessary) and returns it.  Returns NULL if the
         * type cannot be matched.
         */
        """
        pass

    def printPipeTypes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        print_pipe_types(GraphicsPipeSelection self)
        
        /**
         * Writes a list of the currently known GraphicsPipe types to nout, for the
         * user's information.
         */
        """
        pass

    def print_pipe_types(self, GraphicsPipeSelection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        print_pipe_types(GraphicsPipeSelection self)
        
        /**
         * Writes a list of the currently known GraphicsPipe types to nout, for the
         * user's information.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    pipe_types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This maintains a list of GraphicsPipes by type that are available for\n * creation.  Normally there is one default interactive GraphicsPipe, and\n * possibly other types available as well.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GraphicsPipeSelection' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DFB40>'
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFCFE2DFB40>)>'
        'getNumAuxModules': None, # (!) real value is "<method 'getNumAuxModules' of 'panda3d.core.GraphicsPipeSelection' objects>"
        'getNumPipeTypes': None, # (!) real value is "<method 'getNumPipeTypes' of 'panda3d.core.GraphicsPipeSelection' objects>"
        'getPipeType': None, # (!) real value is "<method 'getPipeType' of 'panda3d.core.GraphicsPipeSelection' objects>"
        'getPipeTypes': None, # (!) real value is "<method 'getPipeTypes' of 'panda3d.core.GraphicsPipeSelection' objects>"
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFCFE2DFB40>)>'
        'get_num_aux_modules': None, # (!) real value is "<method 'get_num_aux_modules' of 'panda3d.core.GraphicsPipeSelection' objects>"
        'get_num_pipe_types': None, # (!) real value is "<method 'get_num_pipe_types' of 'panda3d.core.GraphicsPipeSelection' objects>"
        'get_pipe_type': None, # (!) real value is "<method 'get_pipe_type' of 'panda3d.core.GraphicsPipeSelection' objects>"
        'get_pipe_types': None, # (!) real value is "<method 'get_pipe_types' of 'panda3d.core.GraphicsPipeSelection' objects>"
        'loadAuxModules': None, # (!) real value is "<method 'loadAuxModules' of 'panda3d.core.GraphicsPipeSelection' objects>"
        'load_aux_modules': None, # (!) real value is "<method 'load_aux_modules' of 'panda3d.core.GraphicsPipeSelection' objects>"
        'makeDefaultPipe': None, # (!) real value is "<method 'makeDefaultPipe' of 'panda3d.core.GraphicsPipeSelection' objects>"
        'makeModulePipe': None, # (!) real value is "<method 'makeModulePipe' of 'panda3d.core.GraphicsPipeSelection' objects>"
        'makePipe': None, # (!) real value is "<method 'makePipe' of 'panda3d.core.GraphicsPipeSelection' objects>"
        'make_default_pipe': None, # (!) real value is "<method 'make_default_pipe' of 'panda3d.core.GraphicsPipeSelection' objects>"
        'make_module_pipe': None, # (!) real value is "<method 'make_module_pipe' of 'panda3d.core.GraphicsPipeSelection' objects>"
        'make_pipe': None, # (!) real value is "<method 'make_pipe' of 'panda3d.core.GraphicsPipeSelection' objects>"
        'pipe_types': None, # (!) real value is "<attribute 'pipe_types' of 'panda3d.core.GraphicsPipeSelection' objects>"
        'printPipeTypes': None, # (!) real value is "<method 'printPipeTypes' of 'panda3d.core.GraphicsPipeSelection' objects>"
        'print_pipe_types': None, # (!) real value is "<method 'print_pipe_types' of 'panda3d.core.GraphicsPipeSelection' objects>"
    }


