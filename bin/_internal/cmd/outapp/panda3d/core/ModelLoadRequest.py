# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .AsyncTask import AsyncTask

class ModelLoadRequest(AsyncTask):
    """
    /**
     * A class object that manages a single asynchronous model load request.
     * Create a new ModelLoadRequest, and add it to the loader via load_async(),
     * to begin an asynchronous load.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_filename(ModelLoadRequest self)
        
        /**
         * Returns the filename associated with this asynchronous ModelLoadRequest.
         */
        """
        pass

    def getLoader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_loader(ModelLoadRequest self)
        
        /**
         * Returns the Loader object associated with this asynchronous
         * ModelLoadRequest.
         */
        """
        pass

    def getModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_model(ModelLoadRequest self)
        
        /**
         * Returns the model that was loaded asynchronously, if any, or null if there
         * was an error.  It is an error to call this unless done() returns true.
         * @deprecated Use result() instead.
         */
        """
        pass

    def getOptions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_options(ModelLoadRequest self)
        
        /**
         * Returns the LoaderOptions associated with this asynchronous
         * ModelLoadRequest.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_filename(self, ModelLoadRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_filename(ModelLoadRequest self)
        
        /**
         * Returns the filename associated with this asynchronous ModelLoadRequest.
         */
        """
        pass

    def get_loader(self, ModelLoadRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_loader(ModelLoadRequest self)
        
        /**
         * Returns the Loader object associated with this asynchronous
         * ModelLoadRequest.
         */
        """
        pass

    def get_model(self, ModelLoadRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_model(ModelLoadRequest self)
        
        /**
         * Returns the model that was loaded asynchronously, if any, or null if there
         * was an error.  It is an error to call this unless done() returns true.
         * @deprecated Use result() instead.
         */
        """
        pass

    def get_options(self, ModelLoadRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_options(ModelLoadRequest self)
        
        /**
         * Returns the LoaderOptions associated with this asynchronous
         * ModelLoadRequest.
         */
        """
        pass

    def isReady(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_ready(ModelLoadRequest self)
        
        /**
         * Returns true if this request has completed, false if it is still pending or
         * if it has been cancelled.  When this returns true, you may retrieve the
         * model loaded by calling get_model().
         * Equivalent to `req.done() and not req.cancelled()`.
         * @see done()
         */
        """
        pass

    def is_ready(self, ModelLoadRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_ready(ModelLoadRequest self)
        
        /**
         * Returns true if this request has completed, false if it is still pending or
         * if it has been cancelled.  When this returns true, you may retrieve the
         * model loaded by calling get_model().
         * Equivalent to `req.done() and not req.cancelled()`.
         * @see done()
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

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ModelLoadRequest' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ModelLoadRequest' objects>"
        '__doc__': '/**\n * A class object that manages a single asynchronous model load request.\n * Create a new ModelLoadRequest, and add it to the loader via load_async(),\n * to begin an asynchronous load.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ModelLoadRequest' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE298C00>'
        'filename': None, # (!) real value is "<attribute 'filename' of 'panda3d.core.ModelLoadRequest' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE298C00>)>'
        'getFilename': None, # (!) real value is "<method 'getFilename' of 'panda3d.core.ModelLoadRequest' objects>"
        'getLoader': None, # (!) real value is "<method 'getLoader' of 'panda3d.core.ModelLoadRequest' objects>"
        'getModel': None, # (!) real value is "<method 'getModel' of 'panda3d.core.ModelLoadRequest' objects>"
        'getOptions': None, # (!) real value is "<method 'getOptions' of 'panda3d.core.ModelLoadRequest' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE298C00>)>'
        'get_filename': None, # (!) real value is "<method 'get_filename' of 'panda3d.core.ModelLoadRequest' objects>"
        'get_loader': None, # (!) real value is "<method 'get_loader' of 'panda3d.core.ModelLoadRequest' objects>"
        'get_model': None, # (!) real value is "<method 'get_model' of 'panda3d.core.ModelLoadRequest' objects>"
        'get_options': None, # (!) real value is "<method 'get_options' of 'panda3d.core.ModelLoadRequest' objects>"
        'isReady': None, # (!) real value is "<method 'isReady' of 'panda3d.core.ModelLoadRequest' objects>"
        'is_ready': None, # (!) real value is "<method 'is_ready' of 'panda3d.core.ModelLoadRequest' objects>"
        'loader': None, # (!) real value is "<attribute 'loader' of 'panda3d.core.ModelLoadRequest' objects>"
        'options': None, # (!) real value is "<attribute 'options' of 'panda3d.core.ModelLoadRequest' objects>"
    }


