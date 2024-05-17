# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

from .Namable import Namable

class Loader(TypedReferenceCount, Namable):
    """
    /**
     * A convenient class for loading models from disk, in bam or egg format (or
     * any of a number of other formats implemented by a LoaderFileType, such as
     * ptloader).
     *
     * This class supports synchronous as well as asynchronous loading.  In
     * asynchronous loading, the model is loaded in the background by a thread,
     * and an event will be generated when the model is available.  If threading
     * is not available, the asynchronous loading interface may be used, but it
     * loads synchronously.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns a pointer to the global Loader.  This is the Loader that most code
         * should use for loading models.
         */
        """
        pass

    def getTaskChain(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_task_chain(Loader self)
        
        /**
         * Returns the task chain that is used for asynchronous loads.
         */
        """
        pass

    def getTaskManager(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_task_manager(Loader self)
        
        /**
         * Returns the task manager that is used for asynchronous loads.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_global_ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns a pointer to the global Loader.  This is the Loader that most code
         * should use for loading models.
         */
        """
        pass

    def get_task_chain(self, Loader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_task_chain(Loader self)
        
        /**
         * Returns the task chain that is used for asynchronous loads.
         */
        """
        pass

    def get_task_manager(self, Loader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_task_manager(Loader self)
        
        /**
         * Returns the task manager that is used for asynchronous loads.
         */
        """
        pass

    def loadAsync(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_async(const Loader self, AsyncTask request)
        
        /**
         * Begins an asynchronous load request.  To use this call, first call
         * make_async_request() to create a new ModelLoadRequest object with the
         * filename you wish to load, and then add that object to the Loader with
         * load_async.  This function will return immediately, and the model will be
         * loaded in the background.
         *
         * To determine when the model has completely loaded, you may poll
         * request->is_ready() from time to time, or set the done_event on the request
         * object and listen for that event.  When the model is ready, you may
         * retrieve it via request->get_model().
         */
        """
        pass

    def loadBamStream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_bam_stream(const Loader self, istream in)
        
        /**
         * Attempts to read a bam file from the indicated stream and return the scene
         * graph defined there.
         */
        """
        pass

    def loadSync(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_sync(Loader self, const Filename filename, const LoaderOptions options)
        
        /**
         * Loads the file immediately, waiting for it to complete.
         *
         * If search is true, the file is searched for along the model path;
         * otherwise, only the exact filename is loaded.
         */
        """
        pass

    def load_async(self, const_Loader_self, AsyncTask_request): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_async(const Loader self, AsyncTask request)
        
        /**
         * Begins an asynchronous load request.  To use this call, first call
         * make_async_request() to create a new ModelLoadRequest object with the
         * filename you wish to load, and then add that object to the Loader with
         * load_async.  This function will return immediately, and the model will be
         * loaded in the background.
         *
         * To determine when the model has completely loaded, you may poll
         * request->is_ready() from time to time, or set the done_event on the request
         * object and listen for that event.  When the model is ready, you may
         * retrieve it via request->get_model().
         */
        """
        pass

    def load_bam_stream(self, const_Loader_self, istream_in): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_bam_stream(const Loader self, istream in)
        
        /**
         * Attempts to read a bam file from the indicated stream and return the scene
         * graph defined there.
         */
        """
        pass

    def load_sync(self, Loader_self, const_Filename_filename, const_LoaderOptions_options): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_sync(Loader self, const Filename filename, const LoaderOptions options)
        
        /**
         * Loads the file immediately, waiting for it to complete.
         *
         * If search is true, the file is searched for along the model path;
         * otherwise, only the exact filename is loaded.
         */
        """
        pass

    def makeAsyncRequest(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_async_request(const Loader self, const Filename filename, const LoaderOptions options)
        
        /**
         * Returns a new AsyncTask object suitable for adding to load_async() to start
         * an asynchronous model load.
         */
        """
        pass

    def makeAsyncSaveRequest(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_async_save_request(const Loader self, const Filename filename, const LoaderOptions options, PandaNode node)
        
        /**
         * Returns a new AsyncTask object suitable for adding to save_async() to start
         * an asynchronous model save.
         */
        """
        pass

    def make_async_request(self, const_Loader_self, const_Filename_filename, const_LoaderOptions_options): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_async_request(const Loader self, const Filename filename, const LoaderOptions options)
        
        /**
         * Returns a new AsyncTask object suitable for adding to load_async() to start
         * an asynchronous model load.
         */
        """
        pass

    def make_async_save_request(self, const_Loader_self, const_Filename_filename, const_LoaderOptions_options, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_async_save_request(const Loader self, const Filename filename, const LoaderOptions options, PandaNode node)
        
        /**
         * Returns a new AsyncTask object suitable for adding to save_async() to start
         * an asynchronous model save.
         */
        """
        pass

    def output(self, Loader_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(Loader self, ostream out)
        
        /**
         *
         */
        """
        pass

    def remove(self, const_Loader_self, AsyncTask_task): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove(const Loader self, AsyncTask task)
        
        /**
         * Removes a pending asynchronous load request.  Returns true if successful,
         * false otherwise.
         * @deprecated use task.cancel() to cancel the request instead.
         */
        """
        pass

    def saveAsync(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        save_async(const Loader self, AsyncTask request)
        
        /**
         * Begins an asynchronous save request.  To use this call, first call
         * make_async_save_request() to create a new ModelSaveRequest object with the
         * filename you wish to load, and then add that object to the Loader with
         * save_async.  This function will return immediately, and the model will be
         * loaded in the background.
         *
         * To determine when the model has completely loaded, you may poll
         * request->is_ready() from time to time, or set the done_event on the request
         * object and listen for that event.  When the request is ready, you may
         * retrieve the success or failure via request->get_success().
         */
        """
        pass

    def saveSync(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        save_sync(Loader self, const Filename filename, const LoaderOptions options, PandaNode node)
        
        /**
         * Saves the file immediately, waiting for it to complete.
         */
        """
        pass

    def save_async(self, const_Loader_self, AsyncTask_request): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        save_async(const Loader self, AsyncTask request)
        
        /**
         * Begins an asynchronous save request.  To use this call, first call
         * make_async_save_request() to create a new ModelSaveRequest object with the
         * filename you wish to load, and then add that object to the Loader with
         * save_async.  This function will return immediately, and the model will be
         * loaded in the background.
         *
         * To determine when the model has completely loaded, you may poll
         * request->is_ready() from time to time, or set the done_event on the request
         * object and listen for that event.  When the request is ready, you may
         * retrieve the success or failure via request->get_success().
         */
        """
        pass

    def save_sync(self, Loader_self, const_Filename_filename, const_LoaderOptions_options, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        save_sync(Loader self, const Filename filename, const LoaderOptions options, PandaNode node)
        
        /**
         * Saves the file immediately, waiting for it to complete.
         */
        """
        pass

    def setTaskChain(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_task_chain(const Loader self, str task_chain)
        
        /**
         * Specifies the task chain that is used for asynchronous loads.  The default
         * is the initial name of the Loader object.
         */
        """
        pass

    def setTaskManager(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_task_manager(const Loader self, AsyncTaskManager task_manager)
        
        /**
         * Specifies the task manager that is used for asynchronous loads.  The
         * default is the global task manager.
         */
        """
        pass

    def set_task_chain(self, const_Loader_self, str_task_chain): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_task_chain(const Loader self, str task_chain)
        
        /**
         * Specifies the task chain that is used for asynchronous loads.  The default
         * is the initial name of the Loader object.
         */
        """
        pass

    def set_task_manager(self, const_Loader_self, AsyncTaskManager_task_manager): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_task_manager(const Loader self, AsyncTaskManager task_manager)
        
        /**
         * Specifies the task manager that is used for asynchronous loads.  The
         * default is the global task manager.
         */
        """
        pass

    def stopThreads(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        stop_threads(const Loader self)
        
        /**
         * Stop any threads used for asynchronous loads.
         */
        """
        pass

    def stop_threads(self, const_Loader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        stop_threads(const Loader self)
        
        /**
         * Stop any threads used for asynchronous loads.
         */
        """
        pass

    def upcastToNamable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_Namable(const Loader self)
        
        upcast from Loader to Namable
        """
        pass

    def upcastToTypedReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedReferenceCount(const Loader self)
        
        upcast from Loader to TypedReferenceCount
        """
        pass

    def upcast_to_Namable(self, const_Loader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Namable(const Loader self)
        
        upcast from Loader to Namable
        """
        pass

    def upcast_to_TypedReferenceCount(self, const_Loader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedReferenceCount(const Loader self)
        
        upcast from Loader to TypedReferenceCount
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
        'Results': None, # (!) real value is "<class 'panda3d.core.Results'>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Loader' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Loader' objects>"
        '__doc__': '/**\n * A convenient class for loading models from disk, in bam or egg format (or\n * any of a number of other formats implemented by a LoaderFileType, such as\n * ptloader).\n *\n * This class supports synchronous as well as asynchronous loading.  In\n * asynchronous loading, the model is loaded in the background by a thread,\n * and an event will be generated when the model is available.  If threading\n * is not available, the asynchronous loading interface may be used, but it\n * loads synchronously.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Loader' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE298120>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.Loader' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.Loader' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE298120>)>'
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFCFE298120>)>'
        'getTaskChain': None, # (!) real value is "<method 'getTaskChain' of 'panda3d.core.Loader' objects>"
        'getTaskManager': None, # (!) real value is "<method 'getTaskManager' of 'panda3d.core.Loader' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE298120>)>'
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFCFE298120>)>'
        'get_task_chain': None, # (!) real value is "<method 'get_task_chain' of 'panda3d.core.Loader' objects>"
        'get_task_manager': None, # (!) real value is "<method 'get_task_manager' of 'panda3d.core.Loader' objects>"
        'loadAsync': None, # (!) real value is "<method 'loadAsync' of 'panda3d.core.Loader' objects>"
        'loadBamStream': None, # (!) real value is "<method 'loadBamStream' of 'panda3d.core.Loader' objects>"
        'loadSync': None, # (!) real value is "<method 'loadSync' of 'panda3d.core.Loader' objects>"
        'load_async': None, # (!) real value is "<method 'load_async' of 'panda3d.core.Loader' objects>"
        'load_bam_stream': None, # (!) real value is "<method 'load_bam_stream' of 'panda3d.core.Loader' objects>"
        'load_sync': None, # (!) real value is "<method 'load_sync' of 'panda3d.core.Loader' objects>"
        'makeAsyncRequest': None, # (!) real value is "<method 'makeAsyncRequest' of 'panda3d.core.Loader' objects>"
        'makeAsyncSaveRequest': None, # (!) real value is "<method 'makeAsyncSaveRequest' of 'panda3d.core.Loader' objects>"
        'make_async_request': None, # (!) real value is "<method 'make_async_request' of 'panda3d.core.Loader' objects>"
        'make_async_save_request': None, # (!) real value is "<method 'make_async_save_request' of 'panda3d.core.Loader' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.Loader' objects>"
        'remove': None, # (!) real value is "<method 'remove' of 'panda3d.core.Loader' objects>"
        'saveAsync': None, # (!) real value is "<method 'saveAsync' of 'panda3d.core.Loader' objects>"
        'saveSync': None, # (!) real value is "<method 'saveSync' of 'panda3d.core.Loader' objects>"
        'save_async': None, # (!) real value is "<method 'save_async' of 'panda3d.core.Loader' objects>"
        'save_sync': None, # (!) real value is "<method 'save_sync' of 'panda3d.core.Loader' objects>"
        'setTaskChain': None, # (!) real value is "<method 'setTaskChain' of 'panda3d.core.Loader' objects>"
        'setTaskManager': None, # (!) real value is "<method 'setTaskManager' of 'panda3d.core.Loader' objects>"
        'set_task_chain': None, # (!) real value is "<method 'set_task_chain' of 'panda3d.core.Loader' objects>"
        'set_task_manager': None, # (!) real value is "<method 'set_task_manager' of 'panda3d.core.Loader' objects>"
        'stopThreads': None, # (!) real value is "<method 'stopThreads' of 'panda3d.core.Loader' objects>"
        'stop_threads': None, # (!) real value is "<method 'stop_threads' of 'panda3d.core.Loader' objects>"
        'upcastToNamable': None, # (!) real value is "<method 'upcastToNamable' of 'panda3d.core.Loader' objects>"
        'upcastToTypedReferenceCount': None, # (!) real value is "<method 'upcastToTypedReferenceCount' of 'panda3d.core.Loader' objects>"
        'upcast_to_Namable': None, # (!) real value is "<method 'upcast_to_Namable' of 'panda3d.core.Loader' objects>"
        'upcast_to_TypedReferenceCount': None, # (!) real value is "<method 'upcast_to_TypedReferenceCount' of 'panda3d.core.Loader' objects>"
    }
    Results = None # (!) real value is "<class 'panda3d.core.Results'>"


