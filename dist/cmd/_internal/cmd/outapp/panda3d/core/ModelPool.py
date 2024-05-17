# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class ModelPool(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class unifies all references to the same filename, so that multiple
     * attempts to load the same model will return the same pointer.  Note that
     * the default behavior is thus to make instances: use with caution.  Use the
     * copy_subgraph() method on Node (or use NodePath::copy_to) to make
     * modifiable copies of the node.
     *
     * Unlike TexturePool, this class does not automatically resolve the model
     * filenames before loading, so a relative path and an absolute path to the
     * same model will appear to be different filenames.
     *
     * However, see the Loader class, which is now the preferred interface for
     * loading models.  The Loader class can resolve filenames, supports threaded
     * loading, and can automatically consult the ModelPool, according to the
     * supplied LoaderOptions.
     */
    """
    def addModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_model(ModelRoot model)
        add_model(const Filename filename, ModelRoot model)
        
        /**
         * Adds the indicated already-loaded model to the pool.  The model will
         * replace any previously-loaded model in the pool that had the same filename.
         *
         * @deprecated Use the one-parameter add_model(model) instead.
         */
        
        /**
         * Adds the indicated already-loaded model to the pool.  The model will
         * replace any previously-loaded model in the pool that had the same filename.
         */
        """
        pass

    def add_model(self, ModelRoot_model): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_model(ModelRoot model)
        add_model(const Filename filename, ModelRoot model)
        
        /**
         * Adds the indicated already-loaded model to the pool.  The model will
         * replace any previously-loaded model in the pool that had the same filename.
         *
         * @deprecated Use the one-parameter add_model(model) instead.
         */
        
        /**
         * Adds the indicated already-loaded model to the pool.  The model will
         * replace any previously-loaded model in the pool that had the same filename.
         */
        """
        pass

    def garbageCollect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        garbage_collect()
        
        /**
         * Releases only those models in the pool that have a reference count of
         * exactly 1; i.e.  only those models that are not being used outside of the
         * pool.  Returns the number of models released.
         */
        """
        pass

    def garbage_collect(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        garbage_collect()
        
        /**
         * Releases only those models in the pool that have a reference count of
         * exactly 1; i.e.  only those models that are not being used outside of the
         * pool.  Returns the number of models released.
         */
        """
        pass

    def getModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_model(const Filename filename, bool verify)
        
        /**
         * Returns the model that has already been previously loaded, or NULL
         * otherwise.  If verify is true, it will check if the file is still up-to-
         * date (and hasn't been modified in the meantime), and if not, will still
         * return NULL.
         */
        """
        pass

    def get_model(self, const_Filename_filename, bool_verify): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_model(const Filename filename, bool verify)
        
        /**
         * Returns the model that has already been previously loaded, or NULL
         * otherwise.  If verify is true, it will check if the file is still up-to-
         * date (and hasn't been modified in the meantime), and if not, will still
         * return NULL.
         */
        """
        pass

    def hasModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_model(const Filename filename)
        
        /**
         * Returns true if the model has ever been loaded, false otherwise.  Note that
         * this does not guarantee that the model is still up-to-date.
         */
        """
        pass

    def has_model(self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_model(const Filename filename)
        
        /**
         * Returns true if the model has ever been loaded, false otherwise.  Note that
         * this does not guarantee that the model is still up-to-date.
         */
        """
        pass

    def listContents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        list_contents()
        list_contents(ostream out)
        
        /**
         * Lists the contents of the model pool to the indicated output stream.
         */
        
        /**
         * Lists the contents of the model pool to cout.
         */
        """
        pass

    def list_contents(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        list_contents()
        list_contents(ostream out)
        
        /**
         * Lists the contents of the model pool to the indicated output stream.
         */
        
        /**
         * Lists the contents of the model pool to cout.
         */
        """
        pass

    def loadModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_model(const Filename filename, const LoaderOptions options)
        
        /**
         * Loads the given filename up as a model, if it has not already been loaded,
         * and returns the new model.  If a model with the same filename was
         * previously loaded, returns that one instead (unless cache-check-timestamps
         * is true and the file has recently changed).  If the model file cannot be
         * found, or cannot be loaded for some reason, returns NULL.
         */
        """
        pass

    def load_model(self, const_Filename_filename, const_LoaderOptions_options): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_model(const Filename filename, const LoaderOptions options)
        
        /**
         * Loads the given filename up as a model, if it has not already been loaded,
         * and returns the new model.  If a model with the same filename was
         * previously loaded, returns that one instead (unless cache-check-timestamps
         * is true and the file has recently changed).  If the model file cannot be
         * found, or cannot be loaded for some reason, returns NULL.
         */
        """
        pass

    def releaseAllModels(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all_models()
        
        /**
         * Releases all models in the pool and restores the pool to the empty state.
         */
        """
        pass

    def releaseModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_model(ModelRoot model)
        
        /**
         * Removes the indicated model from the pool, indicating it will never be
         * loaded again; the model may then be freed.  If this function is never
         * called, a reference count will be maintained on every model every loaded,
         * and models will never be freed.
         *
         * @deprecated Use release_model(model) instead.
         */
        
        /**
         * Removes the indicated model from the pool, indicating it will never be
         * loaded again; the model may then be freed.  If this function (and
         * garbage_collect()) is never called, a reference count will be maintained on
         * every model every loaded, and models will never be freed.
         *
         * The model's get_fullpath() value should not have been changed during its
         * lifetime, or this function may fail to locate it in the pool.
         */
        """
        pass

    def release_all_models(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all_models()
        
        /**
         * Releases all models in the pool and restores the pool to the empty state.
         */
        """
        pass

    def release_model(self, ModelRoot_model): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_model(ModelRoot model)
        
        /**
         * Removes the indicated model from the pool, indicating it will never be
         * loaded again; the model may then be freed.  If this function is never
         * called, a reference count will be maintained on every model every loaded,
         * and models will never be freed.
         *
         * @deprecated Use release_model(model) instead.
         */
        
        /**
         * Removes the indicated model from the pool, indicating it will never be
         * loaded again; the model may then be freed.  If this function (and
         * garbage_collect()) is never called, a reference count will be maintained on
         * every model every loaded, and models will never be freed.
         *
         * The model's get_fullpath() value should not have been changed during its
         * lifetime, or this function may fail to locate it in the pool.
         */
        """
        pass

    def verifyModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        verify_model(const Filename filename)
        
        /**
         * Loads the given filename up as a model, if it has not already been loaded,
         * and returns true to indicate success, or false to indicate failure.  If
         * this returns true, it is probable that a subsequent call to load_model()
         * with the same model name will return a valid PandaNode.
         *
         * However, even if this returns true, it is still possible for a subsequent
         * call to load_model() to fail.  This can happen if cache-check-timestamps is
         * true, and the on-disk file is subsequently modified to replace it with an
         * invalid model.
         */
        """
        pass

    def verify_model(self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        verify_model(const Filename filename)
        
        /**
         * Loads the given filename up as a model, if it has not already been loaded,
         * and returns true to indicate success, or false to indicate failure.  If
         * this returns true, it is probable that a subsequent call to load_model()
         * with the same model name will return a valid PandaNode.
         *
         * However, even if this returns true, it is still possible for a subsequent
         * call to load_model() to fail.  This can happen if cache-check-timestamps is
         * true, and the on-disk file is subsequently modified to replace it with an
         * invalid model.
         */
        """
        pass

    def write(self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(ostream out)
        
        /**
         * Lists the contents of the model pool to the indicated output stream.  Helps
         * with debugging.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This class unifies all references to the same filename, so that multiple\n * attempts to load the same model will return the same pointer.  Note that\n * the default behavior is thus to make instances: use with caution.  Use the\n * copy_subgraph() method on Node (or use NodePath::copy_to) to make\n * modifiable copies of the node.\n *\n * Unlike TexturePool, this class does not automatically resolve the model\n * filenames before loading, so a relative path and an absolute path to the\n * same model will appear to be different filenames.\n *\n * However, see the Loader class, which is now the preferred interface for\n * loading models.  The Loader class can resolve filenames, supports threaded\n * loading, and can automatically consult the ModelPool, according to the\n * supplied LoaderOptions.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ModelPool' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE299340>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.ModelPool' objects>"
        'addModel': None, # (!) real value is '<staticmethod(<built-in method addModel of type object at 0x00007FFCFE299340>)>'
        'add_model': None, # (!) real value is '<staticmethod(<built-in method add_model of type object at 0x00007FFCFE299340>)>'
        'garbageCollect': None, # (!) real value is '<staticmethod(<built-in method garbageCollect of type object at 0x00007FFCFE299340>)>'
        'garbage_collect': None, # (!) real value is '<staticmethod(<built-in method garbage_collect of type object at 0x00007FFCFE299340>)>'
        'getModel': None, # (!) real value is '<staticmethod(<built-in method getModel of type object at 0x00007FFCFE299340>)>'
        'get_model': None, # (!) real value is '<staticmethod(<built-in method get_model of type object at 0x00007FFCFE299340>)>'
        'hasModel': None, # (!) real value is '<staticmethod(<built-in method hasModel of type object at 0x00007FFCFE299340>)>'
        'has_model': None, # (!) real value is '<staticmethod(<built-in method has_model of type object at 0x00007FFCFE299340>)>'
        'listContents': None, # (!) real value is '<staticmethod(<built-in method listContents of type object at 0x00007FFCFE299340>)>'
        'list_contents': None, # (!) real value is '<staticmethod(<built-in method list_contents of type object at 0x00007FFCFE299340>)>'
        'loadModel': None, # (!) real value is '<staticmethod(<built-in method loadModel of type object at 0x00007FFCFE299340>)>'
        'load_model': None, # (!) real value is '<staticmethod(<built-in method load_model of type object at 0x00007FFCFE299340>)>'
        'releaseAllModels': None, # (!) real value is '<staticmethod(<built-in method releaseAllModels of type object at 0x00007FFCFE299340>)>'
        'releaseModel': None, # (!) real value is '<staticmethod(<built-in method releaseModel of type object at 0x00007FFCFE299340>)>'
        'release_all_models': None, # (!) real value is '<staticmethod(<built-in method release_all_models of type object at 0x00007FFCFE299340>)>'
        'release_model': None, # (!) real value is '<staticmethod(<built-in method release_model of type object at 0x00007FFCFE299340>)>'
        'verifyModel': None, # (!) real value is '<staticmethod(<built-in method verifyModel of type object at 0x00007FFCFE299340>)>'
        'verify_model': None, # (!) real value is '<staticmethod(<built-in method verify_model of type object at 0x00007FFCFE299340>)>'
        'write': None, # (!) real value is '<staticmethod(<built-in method write of type object at 0x00007FFCFE299340>)>'
    }


