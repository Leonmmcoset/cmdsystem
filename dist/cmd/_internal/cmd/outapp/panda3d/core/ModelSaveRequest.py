# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .AsyncTask import AsyncTask

class ModelSaveRequest(AsyncTask):
    """
    /**
     * A class object that manages a single asynchronous model save request.
     * Create a new ModelSaveRequest, and add it to the loader via save_async(),
     * to begin an asynchronous save.
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
        get_filename(ModelSaveRequest self)
        
        /**
         * Returns the filename associated with this asynchronous ModelSaveRequest.
         */
        """
        pass

    def getLoader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_loader(ModelSaveRequest self)
        
        /**
         * Returns the Loader object associated with this asynchronous
         * ModelSaveRequest.
         */
        """
        pass

    def getNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node(ModelSaveRequest self)
        
        /**
         * Returns the node that was passed to the constructor.
         */
        """
        pass

    def getOptions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_options(ModelSaveRequest self)
        
        /**
         * Returns the LoaderOptions associated with this asynchronous
         * ModelSaveRequest.
         */
        """
        pass

    def getSuccess(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_success(ModelSaveRequest self)
        
        /**
         * Returns the true if the model was saved successfully, false otherwise.  It
         * is an error to call this unless done() returns true.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_filename(self, ModelSaveRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_filename(ModelSaveRequest self)
        
        /**
         * Returns the filename associated with this asynchronous ModelSaveRequest.
         */
        """
        pass

    def get_loader(self, ModelSaveRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_loader(ModelSaveRequest self)
        
        /**
         * Returns the Loader object associated with this asynchronous
         * ModelSaveRequest.
         */
        """
        pass

    def get_node(self, ModelSaveRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node(ModelSaveRequest self)
        
        /**
         * Returns the node that was passed to the constructor.
         */
        """
        pass

    def get_options(self, ModelSaveRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_options(ModelSaveRequest self)
        
        /**
         * Returns the LoaderOptions associated with this asynchronous
         * ModelSaveRequest.
         */
        """
        pass

    def get_success(self, ModelSaveRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_success(ModelSaveRequest self)
        
        /**
         * Returns the true if the model was saved successfully, false otherwise.  It
         * is an error to call this unless done() returns true.
         */
        """
        pass

    def isReady(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_ready(ModelSaveRequest self)
        
        /**
         * Returns true if this request has completed, false if it is still pending.
         * When this returns true, you may retrieve the success flag with
         * get_success().
         * Equivalent to `req.done() and not req.cancelled()`.
         * @see done()
         */
        """
        pass

    def is_ready(self, ModelSaveRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_ready(ModelSaveRequest self)
        
        /**
         * Returns true if this request has completed, false if it is still pending.
         * When this returns true, you may retrieve the success flag with
         * get_success().
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

    node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ModelSaveRequest' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ModelSaveRequest' objects>"
        '__doc__': '/**\n * A class object that manages a single asynchronous model save request.\n * Create a new ModelSaveRequest, and add it to the loader via save_async(),\n * to begin an asynchronous save.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ModelSaveRequest' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE299510>'
        'filename': None, # (!) real value is "<attribute 'filename' of 'panda3d.core.ModelSaveRequest' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE299510>)>'
        'getFilename': None, # (!) real value is "<method 'getFilename' of 'panda3d.core.ModelSaveRequest' objects>"
        'getLoader': None, # (!) real value is "<method 'getLoader' of 'panda3d.core.ModelSaveRequest' objects>"
        'getNode': None, # (!) real value is "<method 'getNode' of 'panda3d.core.ModelSaveRequest' objects>"
        'getOptions': None, # (!) real value is "<method 'getOptions' of 'panda3d.core.ModelSaveRequest' objects>"
        'getSuccess': None, # (!) real value is "<method 'getSuccess' of 'panda3d.core.ModelSaveRequest' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE299510>)>'
        'get_filename': None, # (!) real value is "<method 'get_filename' of 'panda3d.core.ModelSaveRequest' objects>"
        'get_loader': None, # (!) real value is "<method 'get_loader' of 'panda3d.core.ModelSaveRequest' objects>"
        'get_node': None, # (!) real value is "<method 'get_node' of 'panda3d.core.ModelSaveRequest' objects>"
        'get_options': None, # (!) real value is "<method 'get_options' of 'panda3d.core.ModelSaveRequest' objects>"
        'get_success': None, # (!) real value is "<method 'get_success' of 'panda3d.core.ModelSaveRequest' objects>"
        'isReady': None, # (!) real value is "<method 'isReady' of 'panda3d.core.ModelSaveRequest' objects>"
        'is_ready': None, # (!) real value is "<method 'is_ready' of 'panda3d.core.ModelSaveRequest' objects>"
        'loader': None, # (!) real value is "<attribute 'loader' of 'panda3d.core.ModelSaveRequest' objects>"
        'node': None, # (!) real value is "<attribute 'node' of 'panda3d.core.ModelSaveRequest' objects>"
        'options': None, # (!) real value is "<attribute 'options' of 'panda3d.core.ModelSaveRequest' objects>"
    }


