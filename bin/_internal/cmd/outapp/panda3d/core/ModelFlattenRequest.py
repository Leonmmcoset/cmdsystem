# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .AsyncTask import AsyncTask

class ModelFlattenRequest(AsyncTask):
    """
    /**
     * This class object manages a single asynchronous request to flatten a model.
     * The model will be duplicated and flattened in a sub-thread (if threading is
     * available), without affecting the original model; and when the result is
     * done it may be retrieved from this object.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_model(ModelFlattenRequest self)
        
        /**
         * Returns the flattened copy of the model.  It is an error to call this
         * unless done() returns true.
         * @deprecated Use result() instead.
         */
        """
        pass

    def getOrig(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_orig(ModelFlattenRequest self)
        
        /**
         * Returns the original, unflattened node.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_model(self, ModelFlattenRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_model(ModelFlattenRequest self)
        
        /**
         * Returns the flattened copy of the model.  It is an error to call this
         * unless done() returns true.
         * @deprecated Use result() instead.
         */
        """
        pass

    def get_orig(self, ModelFlattenRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_orig(ModelFlattenRequest self)
        
        /**
         * Returns the original, unflattened node.
         */
        """
        pass

    def isReady(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_ready(ModelFlattenRequest self)
        
        /**
         * Returns true if this request has completed, false if it is still pending.
         * When this returns true, you may retrieve the model loaded by calling
         * result().
         * Equivalent to `req.done() and not req.cancelled()`.
         * @see done()
         */
        """
        pass

    def is_ready(self, ModelFlattenRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_ready(ModelFlattenRequest self)
        
        /**
         * Returns true if this request has completed, false if it is still pending.
         * When this returns true, you may retrieve the model loaded by calling
         * result().
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

    orig = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ModelFlattenRequest' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ModelFlattenRequest' objects>"
        '__doc__': '/**\n * This class object manages a single asynchronous request to flatten a model.\n * The model will be duplicated and flattened in a sub-thread (if threading is\n * available), without affecting the original model; and when the result is\n * done it may be retrieved from this object.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ModelFlattenRequest' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE298A30>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE298A30>)>'
        'getModel': None, # (!) real value is "<method 'getModel' of 'panda3d.core.ModelFlattenRequest' objects>"
        'getOrig': None, # (!) real value is "<method 'getOrig' of 'panda3d.core.ModelFlattenRequest' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE298A30>)>'
        'get_model': None, # (!) real value is "<method 'get_model' of 'panda3d.core.ModelFlattenRequest' objects>"
        'get_orig': None, # (!) real value is "<method 'get_orig' of 'panda3d.core.ModelFlattenRequest' objects>"
        'isReady': None, # (!) real value is "<method 'isReady' of 'panda3d.core.ModelFlattenRequest' objects>"
        'is_ready': None, # (!) real value is "<method 'is_ready' of 'panda3d.core.ModelFlattenRequest' objects>"
        'orig': None, # (!) real value is "<attribute 'orig' of 'panda3d.core.ModelFlattenRequest' objects>"
    }


