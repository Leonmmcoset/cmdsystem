# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class GraphicsThreadingModel(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This represents the user's specification of how a particular frame is
     * handled by the various threads.
     */
    """
    def assign(self, const_GraphicsThreadingModel_self, const_GraphicsThreadingModel_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const GraphicsThreadingModel self, const GraphicsThreadingModel copy)
        """
        pass

    def getCullName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cull_name(GraphicsThreadingModel self)
        
        /**
         * Returns the name of the thread that will handle culling in this model.
         */
        """
        pass

    def getCullSorting(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cull_sorting(GraphicsThreadingModel self)
        
        /**
         * Returns true if the model involves a separate cull pass, or false if
         * culling happens implicitly, at the same time as draw.
         */
        """
        pass

    def getCullStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cull_stage(GraphicsThreadingModel self)
        
        /**
         * Returns the pipeline stage from which the cull thread should access data.
         * This will be 0 if the cull is run in the same thread as app, or 1 if it is
         * its own thread.
         */
        """
        pass

    def getDrawName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_draw_name(GraphicsThreadingModel self)
        
        /**
         * Returns the name of the thread that will handle sending the actual graphics
         * primitives to the graphics API in this model.
         */
        """
        pass

    def getDrawStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_draw_stage(GraphicsThreadingModel self)
        
        /**
         * Returns the pipeline stage from which the draw thread should access data.
         * This will be the same value as get_cull_stage() if cull and draw are run in
         * the same thread, or one more than that value if draw should be in its own
         * thread.
         */
        """
        pass

    def getModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_model(GraphicsThreadingModel self)
        
        /**
         * Returns the string that describes the threading model.  See the
         * constructor.
         */
        """
        pass

    def get_cull_name(self, GraphicsThreadingModel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cull_name(GraphicsThreadingModel self)
        
        /**
         * Returns the name of the thread that will handle culling in this model.
         */
        """
        pass

    def get_cull_sorting(self, GraphicsThreadingModel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cull_sorting(GraphicsThreadingModel self)
        
        /**
         * Returns true if the model involves a separate cull pass, or false if
         * culling happens implicitly, at the same time as draw.
         */
        """
        pass

    def get_cull_stage(self, GraphicsThreadingModel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cull_stage(GraphicsThreadingModel self)
        
        /**
         * Returns the pipeline stage from which the cull thread should access data.
         * This will be 0 if the cull is run in the same thread as app, or 1 if it is
         * its own thread.
         */
        """
        pass

    def get_draw_name(self, GraphicsThreadingModel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_draw_name(GraphicsThreadingModel self)
        
        /**
         * Returns the name of the thread that will handle sending the actual graphics
         * primitives to the graphics API in this model.
         */
        """
        pass

    def get_draw_stage(self, GraphicsThreadingModel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_draw_stage(GraphicsThreadingModel self)
        
        /**
         * Returns the pipeline stage from which the draw thread should access data.
         * This will be the same value as get_cull_stage() if cull and draw are run in
         * the same thread, or one more than that value if draw should be in its own
         * thread.
         */
        """
        pass

    def get_model(self, GraphicsThreadingModel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_model(GraphicsThreadingModel self)
        
        /**
         * Returns the string that describes the threading model.  See the
         * constructor.
         */
        """
        pass

    def isDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_default(GraphicsThreadingModel self)
        
        /**
         * Returns true if the threading model is the default, cull-then-draw single-
         * threaded model, or false otherwise.
         */
        """
        pass

    def isSingleThreaded(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_single_threaded(GraphicsThreadingModel self)
        
        /**
         * Returns true if the threading model is a single-threaded model, or false if
         * it involves threads.
         */
        """
        pass

    def is_default(self, GraphicsThreadingModel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_default(GraphicsThreadingModel self)
        
        /**
         * Returns true if the threading model is the default, cull-then-draw single-
         * threaded model, or false otherwise.
         */
        """
        pass

    def is_single_threaded(self, GraphicsThreadingModel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_single_threaded(GraphicsThreadingModel self)
        
        /**
         * Returns true if the threading model is a single-threaded model, or false if
         * it involves threads.
         */
        """
        pass

    def output(self, GraphicsThreadingModel_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(GraphicsThreadingModel self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setCullName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cull_name(const GraphicsThreadingModel self, str cull_name)
        
        /**
         * Changes the name of the thread that will handle culling in this model.
         * This won't change any windows that were already created with this model;
         * this only has an effect on newly-opened windows.
         */
        """
        pass

    def setCullSorting(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cull_sorting(const GraphicsThreadingModel self, bool cull_sorting)
        
        /**
         * Changes the flag that indicates whether the threading model involves a
         * separate cull pass.  This won't change any windows that were already
         * created with this model; this only has an effect on newly-opened windows.
         */
        """
        pass

    def setDrawName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_draw_name(const GraphicsThreadingModel self, str cull_name)
        
        /**
         * Changes the name of the thread that will handle drawing in this model.
         * This won't change any windows that were already created with this model;
         * this only has an effect on newly-opened windows.
         */
        """
        pass

    def set_cull_name(self, const_GraphicsThreadingModel_self, str_cull_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cull_name(const GraphicsThreadingModel self, str cull_name)
        
        /**
         * Changes the name of the thread that will handle culling in this model.
         * This won't change any windows that were already created with this model;
         * this only has an effect on newly-opened windows.
         */
        """
        pass

    def set_cull_sorting(self, const_GraphicsThreadingModel_self, bool_cull_sorting): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cull_sorting(const GraphicsThreadingModel self, bool cull_sorting)
        
        /**
         * Changes the flag that indicates whether the threading model involves a
         * separate cull pass.  This won't change any windows that were already
         * created with this model; this only has an effect on newly-opened windows.
         */
        """
        pass

    def set_draw_name(self, const_GraphicsThreadingModel_self, str_cull_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_draw_name(const GraphicsThreadingModel self, str cull_name)
        
        /**
         * Changes the name of the thread that will handle drawing in this model.
         * This won't change any windows that were already created with this model;
         * this only has an effect on newly-opened windows.
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.GraphicsThreadingModel' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.GraphicsThreadingModel' objects>"
        '__doc__': "/**\n * This represents the user's specification of how a particular frame is\n * handled by the various threads.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GraphicsThreadingModel' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DDC70>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.GraphicsThreadingModel' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'getCullName': None, # (!) real value is "<method 'getCullName' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'getCullSorting': None, # (!) real value is "<method 'getCullSorting' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'getCullStage': None, # (!) real value is "<method 'getCullStage' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'getDrawName': None, # (!) real value is "<method 'getDrawName' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'getDrawStage': None, # (!) real value is "<method 'getDrawStage' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'getModel': None, # (!) real value is "<method 'getModel' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'get_cull_name': None, # (!) real value is "<method 'get_cull_name' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'get_cull_sorting': None, # (!) real value is "<method 'get_cull_sorting' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'get_cull_stage': None, # (!) real value is "<method 'get_cull_stage' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'get_draw_name': None, # (!) real value is "<method 'get_draw_name' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'get_draw_stage': None, # (!) real value is "<method 'get_draw_stage' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'get_model': None, # (!) real value is "<method 'get_model' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'isDefault': None, # (!) real value is "<method 'isDefault' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'isSingleThreaded': None, # (!) real value is "<method 'isSingleThreaded' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'is_default': None, # (!) real value is "<method 'is_default' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'is_single_threaded': None, # (!) real value is "<method 'is_single_threaded' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'setCullName': None, # (!) real value is "<method 'setCullName' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'setCullSorting': None, # (!) real value is "<method 'setCullSorting' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'setDrawName': None, # (!) real value is "<method 'setDrawName' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'set_cull_name': None, # (!) real value is "<method 'set_cull_name' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'set_cull_sorting': None, # (!) real value is "<method 'set_cull_sorting' of 'panda3d.core.GraphicsThreadingModel' objects>"
        'set_draw_name': None, # (!) real value is "<method 'set_draw_name' of 'panda3d.core.GraphicsThreadingModel' objects>"
    }


